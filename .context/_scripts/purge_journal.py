#!/usr/bin/env python3
import os
import shutil
from datetime import datetime

JOURNAL_PATH = ".context/maintenance/JOURNAL.md"
ARCHIVE_DIR = ".context/maintenance/_archive_context/journals"

def purge_journal():
    if not os.path.exists(JOURNAL_PATH):
        print("[ERROR] Journal não encontrado.")
        return

    with open(JOURNAL_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if len(lines) < 100:
        print("[INFO] Journal ainda pequeno. Purge não necessário.")
        return

    # Lógica: 70% arquivado, 30% mantido
    split_index = int(len(lines) * 0.7)
    archived_content = lines[:split_index]
    kept_content = lines[split_index:]

    # Salva no arquivo de arquivo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    archive_filename = f"journal_purge_{timestamp}.md"
    archive_path = os.path.join(ARCHIVE_DIR, archive_filename)

    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    with open(archive_path, 'w', encoding='utf-8') as f:
        f.writelines(archived_content)

    # Sobrescreve o original com a semente
    seed_header = f"---\nPurge realizado em: {timestamp}\nSeed Context: Mantido os últimos 30%\n---\n\n"
    with open(JOURNAL_PATH, 'w', encoding='utf-8') as f:
        f.write(seed_header)
        f.writelines(kept_content)

    print(f"[OK] Purge concluído! {len(archived_content)} linhas movidas para {archive_path}")

if __name__ == "__main__":
    purge_journal()
