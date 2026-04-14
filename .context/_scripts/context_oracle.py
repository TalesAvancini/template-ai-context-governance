#!/usr/bin/env python3
"""
🔍 context_oracle.py — Oráculo de consulta local (Unicode-PT-BR Optimized)
Indexa arquivos-chave da .context/ e retorna snippets + confianca.
"""
import re, sys, json, os
from pathlib import Path
from collections import Counter

CONTEXT_DIR = Path(__file__).resolve().parents[1]
INDEX_FILES = [
    "brain/PRD.md", "brain/AGENT_REGISTRY.md", "brain/RULES.md",
    "maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md",
    "maintenance/JOURNAL.md"
]
EXTRA_INDEX = ["brain/INCEPTION.md", "market/SSOT_MAP.md", "market/economics.md"]

def build_index():
    index = {}
    # Arquivos base
    base_paths = [CONTEXT_DIR / f for f in INDEX_FILES + EXTRA_INDEX]
    # Varredura dinâmica da camada Market (v2.4.1)
    market_paths = [f for f in CONTEXT_DIR.glob("market/**/*.md") if f.is_file()]
    
    for p in set(base_paths + market_paths):
        if not p.exists(): continue
        try:
            rel = p.relative_to(CONTEXT_DIR).as_posix()
            text = p.read_text(encoding="utf-8")
            # Python 3 \w já inclui acentos e caracteres latinos
            words = re.findall(r'\b\w{3,}\b', text.lower())
            for w in set(words):
                index.setdefault(w, []).append(rel)
        except Exception:
            continue
    return index

def query_oracle(question, role="unknown"):
    idx = build_index()
    keywords = set(re.findall(r'\b\w{3,}\b', question.lower()))
    hits = Counter()
    for kw in keywords:
        for file in idx.get(kw, []):
            hits[file] += 1
    
    if not hits:
        return {"answer": "[WARN] Nenhuma referencia encontrada.", "confidence": 0.0, "sources": []}
    
    top_files = [f for f, _ in hits.most_common(3)]
    snippets = []
    for f in top_files:
        content = (CONTEXT_DIR / f).read_text(encoding="utf-8")
        for kw in keywords:
            idx_kw = content.lower().find(kw)
            if idx_kw != -1:
                start = max(0, idx_kw - 100)
                end = min(len(content), idx_kw + 100)
                snippets.append(f"DOC {f}: `...{content[start:end].strip()}...`")
                break
                
    conf = min(1.0, len(snippets) * 0.35)
    return {
        "answer": "\n".join(snippets) or "[WARN] Nenhuma referencia direta encontrada.",
        "confidence": conf,
        "sources": top_files
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python context_oracle.py \"sua pergunta aqui\"")
        sys.exit(1)
    res = query_oracle(sys.argv[1], os.environ.get("AGENT_ROLE", "manual"))
    try:
        print(json.dumps(res, indent=2, ensure_ascii=True))
    except Exception as e:
        print(f"[ERROR] Fail encoding json: {e}")
        
    sys.exit(0 if res["confidence"] >= 0.5 else 2)
