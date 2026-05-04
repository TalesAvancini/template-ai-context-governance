#!/usr/bin/env python3
"""
🧠 learnings_aggregator.py (Memória Estratégica - Lobo Temporal)
Varre o SSD_ERRORS_LEDGER.md (Tático) e o HARNESS_LOG.md (Técnico)
para gerar o LEARNINGS.md (Estratégico).
"""
import sys
import re
from pathlib import Path
from datetime import datetime

# Configurações de Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONTEXT_DIR = PROJECT_ROOT / ".context"
BRAIN_DIR = CONTEXT_DIR / "brain"
MAINTENANCE_DIR = CONTEXT_DIR / "maintenance"
SPECS_DIR = PROJECT_ROOT / ".specs" / "features"

LEDGER_FILE = SPECS_DIR / "SSD_ERRORS_LEDGER.md"
HARNESS_LOG_FILE = MAINTENANCE_DIR / "HARNESS_LOG.md"
LEARNINGS_FILE = BRAIN_DIR / "LEARNINGS.md"

# Output encoding
stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
if callable(stdout_reconfigure):
    stdout_reconfigure(encoding="utf-8", errors="replace")

def safe_parse_ledger():
    """Lê o Ledger focado no Formato B (Scars)."""
    scars = []
    if not LEDGER_FILE.exists():
        print(f"[WARN] Ledger não encontrado em {LEDGER_FILE}")
        return scars

    content = LEDGER_FILE.read_text(encoding="utf-8", errors="replace")
    
    # Regex para capturar ### Scar #NNN — Título
    scar_blocks = re.split(r'(?m)^###\s*Scar\s*#\d+\s*[—\-]\s*', content)
    
    if len(scar_blocks) <= 1:
        return scars
        
    for block in scar_blocks[1:]:
        lines = block.strip().split('\n')
        title = lines[0].strip()
        
        scar_data = {
            "title": title,
            "data": "",
            "feature": "",
            "erro": "",
            "sintoma": "",
            "causa_raiz": "",
            "correcao": "",
            "regra": ""
        }
        
        for line in lines[1:]:
            line = line.strip()
            if not line: continue
            if line == "---": break
            
            if line.startswith("- **Data:**"): scar_data["data"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Feature:**"): scar_data["feature"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Erro:**"): scar_data["erro"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Sintoma observado:**"): scar_data["sintoma"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Causa raiz:**"): scar_data["causa_raiz"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Correcao aplicada:**"): scar_data["correcao"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Regra adicionada/ajustada:**"): scar_data["regra"] = line.split(":**", 1)[1].strip()

        scars.append(scar_data)
        
    return scars

def safe_parse_harness_log():
    """Analisa o HARNESS_LOG.md em busca de falhas recorrentes."""
    failures = {}
    if not HARNESS_LOG_FILE.exists():
        return failures
    
    content = HARNESS_LOG_FILE.read_text(encoding="utf-8", errors="replace")
    
    # Busca por: ## [HARNESS-FAIL] Report | spec:name
    matches = re.findall(r'## \[HARNESS-FAIL\] Report \| spec:(.*)', content)
    for spec in matches:
        spec = spec.strip()
        failures[spec] = failures.get(spec, 0) + 1
        
    return failures

def calculate_score(scar, harness_failures):
    """Calcula a relevância da Scar com Decaimento e Frequência."""
    score = 100 # Base
    
    # Bônus por reincidência no Harness
    feat_name = scar.get("feature", "")
    if feat_name in harness_failures:
        # Cada falha no log soma 10 pontos
        score += (harness_failures[feat_name] * 10)
        
    # Decaimento Temporal (Decay)
    try:
        data_str = scar.get("data", "").split(" ")[0]
        data_scar = datetime.strptime(data_str, "%Y-%m-%d")
        dias = (datetime.now() - data_scar).days
        
        if dias > 30:
            score *= 0.5 # Perde metade do peso após 1 mês
        elif dias > 7:
            score *= 0.9 # Perde 10% após 1 semana
    except:
        pass # Data malformada mantém score base
        
    return int(score)

def generate_learnings_md(scars, harness_failures):
    """Gera o arquivo LEARNINGS.md estruturado."""
    
    # Mapeia scores
    scored_scars = []
    for s in scars:
        s["_score"] = calculate_score(s, harness_failures)
        scored_scars.append(s)
        
    # Ordena por score decrescente
    scored_scars = sorted(scored_scars, key=lambda x: x["_score"], reverse=True)
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    md = f"""---
Criado em: 2026-05-04
Ultima Atualizacao: {now}
Status: Ativo
---

# 🧠 LEARNINGS.md (Memória Estratégica MiMo)

> "Aquele que não lembra o passado está condenado a repeti-lo."
> Gerado automaticamente por `learnings_aggregator.py`.

## 🚨 Top Cicatrizes Ativas (Scars)
*(Erros que custaram caro e NÃO devem ser repetidos)*

"""
    for i, scar in enumerate(scored_scars[:10], 1):
        md += f"### [SCAR-{i:03d}] {scar['title']} (Score: {scar['_score']})\n"
        md += f"- **Última vez:** {scar['feature']} ({scar['data']})\n"
        md += f"- **O que aconteceu:** {scar['erro']} -> {scar['causa_raiz']}\n"
        md += f"- **A Regra:** {scar['regra']}\n\n"
        
    # Auto-Scars (Falhas no Harness sem registro no Ledger)
    md += "---\n\n## ⚠️ Alertas Automáticos (Harness Log)\n"
    found_auto = False
    for spec, count in harness_failures.items():
        if count >= 3: # Threshold
            # Verifica se já não existe no Ledger (busca simples por nome)
            if not any(spec.lower() in s.get("feature", "").lower() for s in scars):
                md += f"- **[LOOP DETECTADO]** Spec `{spec}` falhou {count} vezes recentemente. Requer análise estratégica.\n"
                found_auto = True
    
    if not found_auto:
        md += "*(Nenhum loop de erro crítico detectado fora do Ledger)*\n"
        
    return md

def main():
    triage_mode = "--triage" in sys.argv
    
    print("🧠 [LEARNINGS] Iniciando agregação de memória (MiMo v2.1 - Pro)...")
    
    scars = safe_parse_ledger()
    harness_failures = safe_parse_harness_log()
    
    print(f"[INFO] {len(scars)} Scars lidas do Ledger.")
    print(f"[INFO] {len(harness_failures)} Features com falhas no log.")
    
    if triage_mode:
        print("\n--- TRIAGE MODE ---")
        for s in scars:
            score = calculate_score(s, harness_failures)
            print(f"[{score} pts] {s['title']} | Feat: {s['feature']}")
        print("-------------------\n")
        sys.exit(0)
        
    content = generate_learnings_md(scars, harness_failures)
    
    LEARNINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    LEARNINGS_FILE.write_text(content, encoding="utf-8")
    
    print(f"✅ [SUCCESS] LEARNINGS.md atualizado com heurísticas e auto-scars.")

if __name__ == "__main__":
    main()
