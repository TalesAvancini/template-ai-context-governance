#!/usr/bin/env python3
"""
📖 lint_wiki.py — Validacao Epistemologica (Karpathy Layer v2.5)
Enforce de rastreabilidade mandatória para a Wiki de Mercado.
"""
import sys
import re
import argparse
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
# RAW centralizado na nova estrutura Fase 3
RAW_DIR = CONTEXT_DIR / "market" / "RAW"
# Diretórios de Wiki (Adicionada a nova market/WIKI)
WIKI_DIRS = [CONTEXT_DIR / "brain", CONTEXT_DIR / "maintenance", CONTEXT_DIR / "market" / "WIKI"]

# Regex para capturar claims técnicos
CLAIM_REGEX = re.compile(
    r'^(?![\s\-\*#>])'
    r'([A-ZÁÉÍÓÚÂÊÎÔÛÃÕÇ][a-záéíóúâêîôûãõç\s,]{15,}'
    r'(?:utiliza|implementa|segue|requer|garante|valida|integra|usa|e|é)\s'
    r'.+?\.)',
    re.MULTILINE
)

def find_raw_sources():
    """Lista arquivos na inbox RAW para sugestão."""
    if not RAW_DIR.exists(): return []
    return [f.name for f in RAW_DIR.iterdir() if f.suffix == '.md']

def suggest_source(claim_text, raw_files):
    """Heurística simples: busca palavras-chave do claim nos nomes dos arquivos RAW."""
    words = set(re.findall(r'\b\w{5,}\b', claim_text.lower()))
    ignore = {'deve', 'como', 'para', 'sistema', 'projeto', 'este', 'esta', 'ser', 'com', 'sobre'}
    words -= ignore
    if not words: return None
    
    matches = []
    for raw_file in raw_files:
        if any(w in raw_file.lower() for w in words):
            matches.append(f"RAW/{raw_file}")
    return matches[0] if matches else None

def check_wiki(strict=False):
    """Varre a wiki em busca de claims sem citação."""
    raw_files = find_raw_sources()
    issues = []
    
    for d in WIKI_DIRS:
        if not d.exists(): continue
        for f in d.rglob("*.md"):
            if "_archive" in str(f) or "lint_report" in str(f) or f.name.startswith("_"): continue
            
            text = f.read_text(encoding="utf-8")
            if f.name in ["README.md", "MASTER_FLOW.md", "RULES.md", "CONTEXT_HEALTH.md", "rebuild_guide.md"]: continue

            # 🛠️ REGRA MANDATÓRIA KARPATHY (v2.5)
            # Se o arquivo está em market/WIKI, ele DEVE seguir o schema Nível 2
            if "market" in str(f) and "WIKI" in str(f):
                if "> Fonte: RAW/" not in text and "> Fonte: market/RAW/" not in text:
                    issues.append(f"[FATAL] [{f.name}] Wiki de Mercado sem citação RAW obrigatória.")
                
                if strict:
                    # Check de Frontmatter Básico
                    if not re.search(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL):
                        issues.append(f"[FATAL] [{f.name}] Frontmatter ausente ou inválido.")
                    
                    # Check de Estrutura
                    if "## Key Takeaways" not in text:
                        issues.append(f"[FATAL] [{f.name}] Seção '## Key Takeaways' ausente.")
                    
                    if "## Related" not in text and "[[" not in text:
                        issues.append(f"[FATAL] [{f.name}] Conectividade ausente (Related ou [[links]]).")

            # Checagem de claims (Geral)
            for match in CLAIM_REGEX.finditer(text):
                claim = match.group(0)
                context_window = text[max(0, match.start() - 150):min(len(text), match.start() + 250)]
                if "> Fonte:" not in context_window and "> Fonte:" not in text and "SSOT" not in text:
                    suggestion = suggest_source(claim, raw_files)
                    error_msg = f"[WARN] [{f.name}] Claim sem fonte: '{claim[:50]}...'"
                    if suggestion: error_msg += f"\n   [DICA] Sugestao: Adicione '> Fonte: {suggestion}'"
                    issues.append(error_msg)

    if issues:
        print("\n[LINT] Wiki Report:")
        print("\n".join(issues))
        # Se houver erro FATAL na WIKI, trava independente do strict-mode
        has_fatal = any("[FATAL]" in i for i in issues)
        if strict or has_fatal:
            print("\n[FATAL] Pipeline bloqueado por integridade epistemológica.")
            sys.exit(1)
        else:
            print("\n[WARN] Verifique as citacoes pendentes.")
            sys.exit(0)
    else:
        print("[OK] Wiki limpa: Epistemologia em dia.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint de Karpathy Layer")
    parser.add_argument("--strict", action="store_true", help="Bloqueia o pipeline")
    args = parser.parse_args()
    check_wiki(strict=args.strict)
