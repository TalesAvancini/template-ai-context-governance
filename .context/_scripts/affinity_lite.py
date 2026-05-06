import os
import subprocess
import re
import json
import uuid
import sys
import argparse
from datetime import datetime

# --- CONFIGURAÇÕES PADRÃO ---
DEFAULT_THRESHOLD_TEMPORAL = 0.3
DEFAULT_THRESHOLD_REFERENCIAL = 0.1
DEFAULT_MIN_COMMITS = 3
OUTPUT_MD = ".context/maintenance/rx-affinity-lite.md"
OUTPUT_JSON = ".context/maintenance/rx-affinity-lite.json"

class AffinityLite:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.run_id = str(uuid.uuid4())[:8]
        self.file_commits = {}  # {filepath: set(hashes)}
        self.file_content = {}  # {filepath: content}
        self.drift_results = []
        self.stats = {"processed": 0, "ghosts": 0, "dead_refs": 0, "healthy": 0}

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [RUN:{self.run_id}] {message}")

    def get_git_history(self):
        self.log("Coletando histórico temporal do Git...")
        try:
            # Coleta hashes e arquivos impactados de uma vez
            # --name-only lista os arquivos, %H o hash curto
            cmd = ["git", "log", "--pretty=format:%h", "--name-only"]
            output = subprocess.check_output(cmd, encoding="utf-8")
            
            current_hash = None
            for line in output.splitlines():
                line = line.strip()
                if not line: continue
                
                if len(line) == 7 and re.match(r'^[0-9a-f]+$', line):
                    current_hash = line
                else:
                    filepath = line.replace("\\", "/")
                    if filepath not in self.file_commits:
                        self.file_commits[filepath] = set()
                    if current_hash:
                        self.file_commits[filepath].add(current_hash)
        except Exception as e:
            self.log(f"ERRO ao ler Git: {e}")

    def load_files(self):
        self.log("Carregando conteúdo dos arquivos para análise referencial...")
        # Filtramos arquivos de interesse (MD e PY contextuais)
        for root, _, files in os.walk("."):
            if "node_modules" in root or ".git" in root or "scratch" in root:
                continue
            
            for file in files:
                if file.endswith((".md", ".py")):
                    path = os.path.join(root, file).replace("\\", "/")
                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            self.file_content[path] = f.read()
                        self.stats["processed"] += 1
                    except:
                        continue

    def calculate_jaccard(self, set1, set2):
        if not set1 or not set2: return 0.0
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union

    def find_references(self, target_path):
        # O stem é o nome do arquivo sem extensão (ex: RULES.md -> RULES)
        stem = os.path.splitext(os.path.basename(target_path))[0]
        if len(stem) < 3: return 0  # Evitar matches curtos demais (ex: a.py)
        
        total_mentions = 0
        pattern = rf'\b{re.escape(stem)}\b'
        
        for path, content in self.file_content.items():
            if path == target_path: continue # Não contar auto-referência
            matches = re.findall(pattern, content, re.IGNORECASE)
            total_mentions += len(matches)
        
        return total_mentions

    def run_analysis(self):
        self.get_git_history()
        self.load_files()
        
        files = list(self.file_commits.keys())
        self.log(f"Analisando afinidade entre {len(files)} arquivos...")
        
        # Iteramos apenas sobre arquivos que existem fisicamente agora
        active_files = [f for f in files if os.path.exists(f)]
        
        for i, f1 in enumerate(active_files):
            # 1. Score Referencial (quantas vezes f1 é citado no projeto todo)
            ref_count = self.find_references(f1)
            # Normalização logarítmica simples: log(1+count)/log(10) capado em 1.0
            import math
            ref_score = min(1.0, math.log1p(ref_count) / 2.3) # 2.3 ~ ln(10)
            
            for j in range(i + 1, len(active_files)):
                f2 = active_files[j]
                
                # 2. Score Temporal (Jaccard)
                commits1 = self.file_commits[f1]
                commits2 = self.file_commits[f2]
                
                if len(commits1) < DEFAULT_MIN_COMMITS or len(commits2) < DEFAULT_MIN_COMMITS:
                    continue
                    
                temp_score = self.calculate_jaccard(commits1, commits2)
                
                if temp_score < 0.05: continue # Ruído baixo demais
                
                # 3. Classificação de Drift
                drift_type = "Healthy"
                if temp_score > DEFAULT_THRESHOLD_TEMPORAL and ref_score < DEFAULT_THRESHOLD_REFERENCIAL:
                    drift_type = "Ghost Coupling"
                    self.stats["ghosts"] += 1
                elif ref_score > 0.3 and temp_score < 0.05:
                    drift_type = "Dead Reference"
                    self.stats["dead_refs"] += 1
                elif temp_score > 0.1:
                    self.stats["healthy"] += 1
                
                self.drift_results.append({
                    "pair": [f1, f2],
                    "temporal": round(temp_score, 3),
                    "referential_f1": round(ref_score, 3),
                    "type": drift_type
                })

    def generate_reports(self):
        if self.dry_run:
            self.log("MODO DRY-RUN: Relatórios não serão escritos.")
            return

        # Gerar JSON
        data = {
            "run_id": self.run_id,
            "timestamp": datetime.now().isoformat(),
            "stats": self.stats,
            "results": self.drift_results
        }
        
        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        # Gerar MD (Lista de Adjacência)
        with open(OUTPUT_MD, "w", encoding="utf-8") as f:
            f.write(f"# 📊 Relatório de Afinidade e Drift (Affinity Lite)\n")
            f.write(f"> Gerado em: {data['timestamp']} | ID: {self.run_id}\n\n")
            
            f.write("## 📈 Resumo Executivo\n")
            f.write(f"- 📁 Arquivos Processados: {self.stats['processed']}\n")
            f.write(f"- 👻 Acoplamentos Fantasma: {self.stats['ghosts']}\n")
            f.write(f"- 💀 Referências Mortas: {self.stats['dead_refs']}\n")
            f.write(f"- ✅ Conexões Saudáveis: {self.stats['healthy']}\n\n")
            
            f.write("## 🕸️ Matriz de Drift (Lista de Adjacência)\n")
            f.write("Abaixo estão listados os pares com desvio operacional detectado.\n\n")
            
            # Agrupar por tipo para legibilidade
            for d_type in ["Ghost Coupling", "Dead Reference", "Healthy"]:
                relevant = [r for r in self.drift_results if r['type'] == d_type]
                if not relevant: continue
                
                f.write(f"### 📍 {d_type}\n")
                for item in relevant:
                    f1, f2 = item['pair']
                    f.write(f"- **{os.path.basename(f1)}** ↔️ **{os.path.basename(f2)}**\n")
                    f.write(f"  - Temporal: `{item['temporal']}` | Referencial: `{item['referential_f1']}`\n")
                f.write("\n")

        self.log(f"Relatórios gerados em {OUTPUT_MD}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Affinity Lite - Drift Detector")
    parser.add_argument("--dry-run", action="store_true", help="Executa sem salvar arquivos")
    args = parser.parse_args()
    
    app = AffinityLite(dry_run=args.dry_run)
    app.run_analysis()
    app.generate_reports()
    app.log("Processo concluído com sucesso.")
