#!/usr/bin/env python3
"""
🔍 context_oracle.py — Oráculo de consulta local (H.O.K v2.5 Optimized)
Busca determinística na camada WIKI/Compliance com retorno integral de arquivos.
"""
import re, sys, json, os
from pathlib import Path
from collections import Counter

CONTEXT_DIR = Path(__file__).resolve().parents[1]

# Import utilitário de log
sys.path.append(str(CONTEXT_DIR / "_scripts"))
try:
    from _wiki_log_utils import append_to_wiki_log
except ImportError:
    def append_to_wiki_log(*args): pass

def load_index_file():
    """Lê o índice mestre WIKI para roteamento determinístico."""
    index_file = CONTEXT_DIR / "market/WIKI/_index.md"
    mapping = {}
    if index_file.exists():
        content = index_file.read_text(encoding="utf-8")
        # Encontra padrões como: - [[link]] | tags: t1, t2
        matches = re.finditer(r'- \[\[(.+?)\]\]\s*\|\s*tags:\s*(.+)', content)
        for m in matches:
            path_stub = m.group(1).strip()
            tags = [t.strip().lower() for t in m.group(2).split(",")]
            for tag in tags:
                # Peso 1.0 para tags explícitas no índice
                mapping.setdefault(tag, []).append({"path": f"market/WIKI/{path_stub}.md", "weight": 1.0})
    return mapping

def build_index():
    index = {}
    # 🔒 Restringe busca APENAS a WIKI e compliance (Princípio do Menor Privilégio)
    search_paths = [
        CONTEXT_DIR / "market/WIKI",
        CONTEXT_DIR / "market/compliance"
    ]
    
    for search_dir in search_paths:
        if not search_dir.exists(): continue
        # rglob para varredura recursiva
        for p in search_dir.rglob("*.md"):
            try:
                rel = p.relative_to(CONTEXT_DIR).as_posix()
                text = p.read_text(encoding="utf-8")
                
                # Heurística de Matching 1: Palavras-chave no corpo
                words = re.findall(r'\b\w{3,}\b', text.lower())
                for w in set(words):
                    index.setdefault(w, []).append({"path": rel, "weight": 0.2})
                
                # Heurística de Matching 2: Nome do arquivo (stem)
                stem = p.stem.lower()
                index.setdefault(stem, []).append({"path": rel, "weight": 0.5})
                
                # Heurística de Matching 3: Título / Keywords no Título
                title_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip().lower()
                    # Match exato do título (0.8)
                    index.setdefault(title, []).append({"path": rel, "weight": 0.8})
                    # Keywords dentro do título (0.6 por palavra do título)
                    title_words = re.findall(r'\b\w{3,}\b', title)
                    for tw in set(title_words):
                        index.setdefault(tw, []).append({"path": rel, "weight": 0.6})
            except Exception:
                continue
    return index

def query_oracle(question, role="unknown"):
    idx = build_index()
    det_idx = load_index_file()
    keywords = set(re.findall(r'\b\w{3,}\b', question.lower()))
    hits = Counter()
    
    # 1. Busca Determinística (Peso 1.0 - Vindo do _index.md)
    for kw in keywords:
        for match in det_idx.get(kw, []):
            hits[match["path"]] += match["weight"]
            
    # 2. Busca Léxica (Pesos variados - Vindo do build_index dinâmico)
    for kw in keywords:
        for match in idx.get(kw, []):
            # Se já houver um hit determinístico, somamos apenas se for o mesmo arquivo
            hits[match["path"]] += match["weight"]
    
    if not hits:
        return {
            "answer": "[INFO] Termo não encontrado na WIKI de Mercado. Para lógica interna (schema, PRD), consulte o bundle do projeto.",
            "confidence": 0.0, 
            "sources": []
        }
    
    # Seleciona apenas o match mais relevante (1 arquivo atômico por vez)
    top_file, score = hits.most_common(1)[0]
    
    # Retorno Integral (Anti-Bloat)
    if score >= 0.6:
        content = (CONTEXT_DIR / top_file).read_text(encoding="utf-8")
        return {
            "answer": f"📄 ARQUIVO COMPLETO ({top_file}):\n\n{content}",
            "confidence": min(1.0, score),
            "sources": [top_file]
        }
    
    return {
        "answer": "[WARN] Referência encontrada, mas com baixa confiança. Refine a pesquisa.",
        "confidence": score,
        "sources": [top_file]
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python context_oracle.py \"sua pergunta aqui\"")
        sys.exit(1)
    res = query_oracle(sys.argv[1], os.environ.get("AGENT_ROLE", "manual"))
    
    # Log de Query (Resumido)
    q_stub = sys.argv[1][:30] + "..." if len(sys.argv[1]) > 30 else sys.argv[1]
    status = "OK" if res["confidence"] >= 0.5 else "FAIL"
    source = res["sources"][0] if res["sources"] else "-"
    append_to_wiki_log("QUERY", f"Busca: {q_stub} (conf: {res['confidence']:.2f})", source, status)

    try:
        print(json.dumps(res, indent=2, ensure_ascii=True))
    except Exception as e:
        print(f"[ERROR] Fail encoding json: {e}")
        
    sys.exit(0 if res["confidence"] >= 0.5 else 2)
