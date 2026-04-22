#!/usr/bin/env python3
"""
🛠️ _wiki_log_utils.py — Utilitário de Rastreabilidade Wiki (H.O.K v2.5.1)
Centraliza a escrita atômica e segura no wiki_log.md.
"""
import os
import sys
from datetime import datetime
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = CONTEXT_DIR / "market/wiki_log.md"

def append_to_wiki_log(mode, description, files, status):
    """
    Adiciona uma entrada ao log da Wiki de forma robusta.
    mode: INGEST | LINT | QUERY | SKIP
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Escape de pipes para não quebrar a tabela Markdown
    safe_desc = str(description).replace("|", "\\|")
    safe_files = str(files).replace("|", "\\|")
    
    line = f"| [{timestamp}] | {mode} | {safe_desc} | {safe_files} | {status} |\n"
    
    try:
        # Garante a existência do arquivo e do cabeçalho
        if not LOG_FILE.exists():
            headers = [
                "# Wiki Log (Append-only)\n\n",
                "| Timestamp | Mode | Description | Files | Status |\n",
                "|-----------|------|-------------|-------|--------|\n"
            ]
            LOG_FILE.write_text("".join(headers), encoding="utf-8")
        
        # Escrita Append (Atômica simples via append mode)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)
            
    except Exception as e:
        # Não trava o pipeline se o log falhar, mas avisa
        print(f"[WARN] Falha ao gravar no wiki_log.md: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Teste rápido se chamado diretamente
    test_mode = sys.argv[1] if len(sys.argv) > 1 else "TEST"
    append_to_wiki_log(test_mode, "Teste de utilitário", "test.py", "OK")
    print(f"[OK] Entrada de teste '{test_mode}' gravada.")
