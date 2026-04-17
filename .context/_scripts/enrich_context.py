#!/usr/bin/env python3
"""
🕵️‍♂️ enrich_context.py — Valida gaps de mercado e prepara scaffolding.
Exit: 0 (PRD ready) | 2 (Research needed) | 1 (Structural error)
"""
import re, sys
# Forçar UTF-8 em Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from datetime import date
from pathlib import Path

# Configuração de caminhos relativos ao script
CONTEXT_DIR = Path(__file__).resolve().parents[1]
INCEPTION = CONTEXT_DIR / "brain" / "INCEPTION.md"
MARKET = CONTEXT_DIR / "market"
INBOX = MARKET / "MARKET_INBOX.md"

def scan_entities():
    if not INCEPTION.exists(): return [], "INCEPTION.md ausente"
    text = INCEPTION.read_text(encoding="utf-8")
    # Captura entidades conhecidas (case-insensitive)
    entities = re.findall(r'(META|Stripe|Supabase|Firebase|AWS|LGPD|PCI|HIPAA|Oracle|MongoDB|PostgreSQL|React|Node|Python)\b', text, re.I)
    return list(set(entities)), "OK"

def check_market_coverage(entities):
    """Verifica se entidades críticas possuem lastro REAL em compliance/ ou research/."""
    missing = []
    # 🔒 Restringe busca APENAS às pastas de fonte (ignora inbox, ssot, economics)
    search_paths = [MARKET / "compliance", MARKET / "research"]
    
    for e in entities:
        found = False
        for search_dir in search_paths:
            if not search_dir.exists(): continue
            for p in search_dir.rglob("*.md"):
                # 1. Check por nome/arquivo (rápido)
                if e.lower() in p.stem.lower() or e.lower() in p.name.lower():
                    found = True; break
                # 2. Check por conteúdo (primeiros 1000 chars para performance)
                try:
                    text = p.read_text(encoding="utf-8", errors="ignore")[:1000].lower()
                    if e.lower() in text:
                        found = True; break
                except: continue
            if found: break
        if not found:
            missing.append(e)
    return missing

def update_inbox(missing):
    """Registra gaps detectados no MARKET_INBOX.md (uma linha por entidade)."""
    if not missing: return
    today = date.today().isoformat()
    
    new_entries = ""
    for e in missing:
        new_entries += f"| Integração {e} | `> Fonte: raw/docs_oficiais.md` | Crítica | 🔍 Pesquisa | {today}\n"
    
    if INBOX.exists():
        text = INBOX.read_text(encoding="utf-8")
        # Filtra entradas que já existem para evitar duplicatas
        final_entries = ""
        for line in new_entries.strip().split("\n"):
            if line.split("|")[1].strip() not in text:
                final_entries += line + "\n"
        
        if final_entries:
            INBOX.write_text(text.rstrip() + "\n" + final_entries, encoding="utf-8")
    else:
        header = "# MARKET INBOX\n| Gap | Fonte | Prioridade | Status | Data |\n|-----|-------|------------|--------|------|\n"
        INBOX.write_text(header + new_entries, encoding="utf-8")

def get_inception_status():
    """Lê o status do Inception mestre."""
    if not INCEPTION.exists(): return "MISSING"
    try:
        content = INCEPTION.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("status:"):
                # Captura o valor antes de qualquer comentário #
                return line.split(":")[1].strip().split("#")[0].strip()
    except:
        return "ERROR"
    return "UNKNOWN"

def main():
    print("[RUN] Spec Enricher (Gap Check & Strategy Sync)...")
    
    # Nova lógica de Onboarding Híbrido
    status = get_inception_status()
    vision_exists = (CONTEXT_DIR / "brain" / "VISION.md").exists()
    
    if status == "DRAFT":
        if vision_exists:
            print("[TRANSLATION_PENDING] Visão detectada. Solicite à IA: \"@spec-enricher proponha o INCEPTION.md\".")
            sys.exit(2)
        else:
            print("[ONBOARDING_MODE] Inception em DRAFT e sem VISION.md. Consulte START_HERE.md.")
            sys.exit(0)
            
    if status == "TRANSLATION_LOCK":
        print("[TRANSLATION_LOCK] INCEPTION.proposed.md gerado. Revise, renomeie e mude status para ACTIVE.")
        sys.exit(2)

    entities, scan_status = scan_entities()
    if scan_status != "OK":
        print(f"[ERROR] {scan_status}")
        sys.exit(1)

    missing = check_market_coverage(entities)
    if missing:
        update_inbox(missing)
        print(f"[ACTION] Gaps detectados: {', '.join(missing)}")
        print("[EXIT 2] Popule market/ e rode 'npm run context:enrich' novamente.")
        sys.exit(2)

    print("[OK] Market coverage validada. Pronto para cristalização do PRD.")
    sys.exit(0)

if __name__ == "__main__":
    main()
