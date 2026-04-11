#!/usr/bin/env python3
"""
📖 lint_wiki.py — Validação de conhecimento (Karpathy Layer)
Verifica citações obrigatórias para claims técnicos.
Atualmente em modo WARN-ONLY (Fase 1).
"""
import re, sys
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
WIKI_DIRS = [CONTEXT_DIR / "brain", CONTEXT_DIR / "maintenance"]

# Regex refinado para claims técnicos em PT-BR
CLAIM_REGEX = r'(?:implementa|utiliza|segue|depende de|conforme)\s+[A-Z][a-zA-Z0-9\s\.,\-]{10,}'

def check_citations():
    issues = []
    for d in WIKI_DIRS:
        for f in d.rglob("*.md"):
            if "_archive" in str(f) or f.name in {"RULES.md", "README.md", "MASTER_FLOW.md"}:
                continue
                
            text = f.read_text(encoding="utf-8")
            claims = re.findall(CLAIM_REGEX, text, re.MULTILINE)
            for c in claims:
                if "> Fonte:" not in text and "SSOT" not in text and "raw/" not in text:
                    issues.append(f"[WARN] {f.name}: Claim sem citacao -> `{c[:40]}...`")
    return issues

def check_raw_dir():
    raw = CONTEXT_DIR / "maintenance" / "_archive_context" / "raw"
    if not raw.exists():
        return ["[WARN] Crie `.context/maintenance/_archive_context/raw/` (inbox imutavel)"]
    return []

if __name__ == "__main__":
    issues = check_raw_dir() + check_citations()
    if issues:
        print("[LINT] Wiki Report (WARN-ONLY):")
        for i in issues: print(i)
        
        # Como estamos na Fase 1, não daremos exit 1. 
        # O Pipeline deve prosseguir, apenas logando os avisos.
        sys.exit(0)
        
    print("[OK] Wiki clean: Citacoes e estrutura OK.")
    sys.exit(0)
