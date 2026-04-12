#!/usr/bin/env python3
"""
🔐 secrets_scanner.py — Scanner Nativo de Segredos
Motor de varredura pré-commit. Usa git ls-files para performance O(N) e 
ignora chaves seguras através da lista .secrets-allowlist.
"""
import re, sys, subprocess, os
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = CONTEXT_DIR.parent
ALLOWLIST_FILE = ROOT_DIR / ".secrets-allowlist"
ALLOWLIST = ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines() if ALLOWLIST_FILE.exists() else []

SECRET_PATTERNS = [
    re.compile(r"(sk|pk|rk)_(live|test)_[a-zA-Z0-9]{20,}", re.I),
    re.compile(r"whsec_[a-zA-Z0-9]{24,}", re.I),
    re.compile(r"supabase_(key|url)\s*[:=]\s*[\"']?\S{10,}[\"']?", re.I),
    re.compile(r"(AIzaSy|AKIAIOSFODNN7EXAMPLE)\w*", re.I),
    re.compile(r"(NEXT_PUBLIC_|VITE_|REACT_APP_)\w*\s*=\s*[\"']?\S{8,}[\"']?", re.I),
]

def get_files_to_scan():
    try:
        # Apenas arquivos rastreados pelo Git (instantâneo, seguro)
        res = subprocess.run(["git", "ls-files"], cwd=ROOT_DIR, capture_output=True, text=True, check=True)
        return [ROOT_DIR / f for f in res.stdout.splitlines()]
    except Exception:
        # Fallback seguro: escopo explícito, ignora node_modules/venv/dist
        safe_dirs = ["src", "api", "config", ".context"]
        files = []
        for d in safe_dirs:
            p = ROOT_DIR / d
            if p.exists():
                files.extend(p.rglob("*.*"))
        return files

def scan():
    hits = []
    print("[RUN] Executando Scanner de Segredos...")
    for f in get_files_to_scan():
        if not f.is_file() or f.suffix in {".lock", ".png", ".jpg", ".md", ".json"}: continue
        content = f.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            for m in pat.finditer(content):
                val = m.group(0)
                # Filtros anti falso-positivo genéricos
                if any(aw.lower() in val.lower() for aw in ALLOWLIST): continue
                if re.search(r'EXAMPLE|YOUR_|CHANGE_ME|test_', val, re.I): continue
                hits.append(f"🔒 [{f.relative_to(ROOT_DIR)}]: '{val[:15]}...'")
    
    if hits:
        print("\n[FATAL] SECRET SCAN FAILED:")
        print("\n".join(hits))
        print("\n💡 Dica: Use .env e .gitignore. Adicione excecoes legitimas em .secrets-allowlist")
        sys.exit(1)
        
    print("[OK] Secret scan clean.")

if __name__ == "__main__":
    scan()
