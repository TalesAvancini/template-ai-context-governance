#!/usr/bin/env python3
"""
🛡️ ingest_wiki_guard.py — Guardião de Ingestão Wiki (H.O.K v2.5)
Valida conformidade Karpathy antes de permitir a entrada de novos artigos.
"""
import re, sys, os
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
WIKI_DIR = CONTEXT_DIR / "market/WIKI"

def validate_article(path):
    content = path.read_text(encoding="utf-8")
    errors = []

    # 1. Validação de Frontmatter
    frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not frontmatter_match:
        errors.append("Frontmatter (---) ausente ou mal formado.")
    else:
        fields = frontmatter_match.group(1)
        required = ['id:', 'entity:', 'concept:', 'tags:', 'source:', 'last_updated:']
        for r in required:
            if r not in fields:
                errors.append(f"Campo obrigatório '{r}' ausente no frontmatter.")

    # 2. Validação de Fonte (Karpathy Rule)
    if not re.search(r'^>\s*Fonte:\s*(market/)?RAW/.+\.md', content, re.MULTILINE):
        errors.append("Citação de fonte '> Fonte: RAW/...' ausente ou inválida.")

    # 3. Estrutura Mínima
    if "## Key Takeaways" not in content:
        errors.append("Seção '## Key Takeaways' ausente.")
    
    if "## Related" not in content and "[[" not in content:
        errors.append("Conectividade ausente (Seção '## Related' ou '[[wikilinks]]' necessários).")

    return errors

def main():
    if not WIKI_DIR.exists():
        print("[OK] Diretório WIKI não encontrado. Ignorando.")
        sys.exit(0)

    # Coleta arquivos para validar (excluindo templates e indices)
    articles = [p for p in WIKI_DIR.rglob("*.md") if not p.name.startswith("_")]
    
    if not articles:
        print("[OK] Nenhum artigo novo para validar.")
        sys.exit(0)

    all_errors = {}
    for art in articles:
        rel_path = art.relative_to(CONTEXT_DIR).as_posix()
        errs = validate_article(art)
        if errs:
            all_errors[rel_path] = errs

    if all_errors:
        print("❌ FALHA NA INGESTÃO WIKI:")
        for path, errs in all_errors.items():
            print(f"\n📄 {path}:")
            for e in errs:
                print(f"  - {e}")
        sys.exit(1)

    print(f"✅ Todos os {len(articles)} artigos WIKI estão em conformidade.")
    sys.exit(0)

if __name__ == "__main__":
    # Garante UTF-8 no Windows
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
