#!/usr/bin/env python3
"""
📊 health_sync.py — Atualizador Dinâmico do Dashboard (Fase 2)
Gera a tabela de métricas em CONTEXT_HEALTH.md baseada na realidade física do repositório.
"""
import re, sys, os
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(fmt)
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
HEALTH_PATH = CONTEXT_DIR / "monitoring" / "CONTEXT_HEALTH.md"
JOURNAL_PATH = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SCHEMA_PATH = CONTEXT_DIR / "maintenance" / "schema.sql"

def count_journal_metrics():
    if not JOURNAL_PATH.exists(): return 0, 0, "No Data"
    text = JOURNAL_PATH.read_text(encoding="utf-8")
    lines = len(text.splitlines())
    chars = len(text)
    
    # Busca a última entrada do Harness
    harness_matches = re.findall(r'\[HARNESS-(FAIL|PASS)\]', text)
    last_harness = harness_matches[-1] if harness_matches else "N/A"
    
    return lines, chars, last_harness

def count_schema_tables():
    if not SCHEMA_PATH.exists(): return 0
    text = SCHEMA_PATH.read_text(encoding="utf-8")
    tables = re.findall(r'CREATE\s+TABLE', text, re.I)
    return len(tables)

def estimate_tokens():
    total_chars = 0
    # Vasculha todos os arquivos do contexto
    for root, _, files in os.walk(CONTEXT_DIR):
        for file in files:
            p = Path(root) / file
            if p.suffix in {'.md', '.py', '.sql', '.sh'}:
                try:
                    total_chars += len(p.read_text(encoding="utf-8"))
                except: pass
    return total_chars // 4

def update_dashboard():
    j_lines, j_chars, harness = count_journal_metrics()
    tables = count_schema_tables()
    tokens = estimate_tokens()
    
    now = format_ts()
    
    # Determinar status heurísticos
    lines_status = "[OK]" if j_lines < 550 else "[WARN] Limpar!"
    chars_status = "[OK]" if j_chars < 45000 else "[WARN] Pesado"
    tokens_status = "[OK]" if tokens < 100000 else "[WARN] Context Bloat"
    harness_status = f"[{harness}]" if harness != "N/A" else "N/A"
    
    table_content = f"""<!-- HEALTH_TABLE_START -->
| Metrica | Valor Atual | Limite Ideal | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Manutencao** | | | | |
| Linhas do Journal | {j_lines} | 600 | Tracker | {lines_status} |
| Carga do Journal | {j_chars // 1000}k chars | 50k chars | Tracker | {chars_status} |
| **Cognitivo** | | | | |
| Estimativa Tokens | ~{tokens // 1000}k | 128k (Max) | Eficiencia | {tokens_status} |
| **Consistencia** | | | | |
| Tabelas no Schema | {tables} | N/A | DB-First | [OK] |
| Ultimo Harness | Role Check | Pass/Fail | Integridade | {harness_status} |
| Ultima Sincronia | {now} | Real-Time | Automacao | [OK] |
<!-- HEALTH_TABLE_END -->"""

    # Ler o arquivo atual e substituir a tabela usando regex
    if not HEALTH_PATH.exists():
        print(f"[ERROR] {HEALTH_PATH.name} não encontrado.")
        return
        
    content = HEALTH_PATH.read_text(encoding="utf-8")
    new_content = re.sub(
        r'<!-- HEALTH_TABLE_START -->.*?<!-- HEALTH_TABLE_END -->',
        table_content,
        content,
        flags=re.DOTALL
    )
    
    # Atualizar metadado de update se existir
    new_content = re.sub(
        r'(Última Atualização:|Ultima Atualizacao:).*',
        f'Ultima Atualizacao: {now}',
        new_content
    )
    
    HEALTH_PATH.write_text(new_content, encoding="utf-8")
    print(f"[OK] {HEALTH_PATH.name} atualizado (Tokens: ~{tokens//1000}k, Linhas: {j_lines}).")

if __name__ == "__main__":
    update_dashboard()
