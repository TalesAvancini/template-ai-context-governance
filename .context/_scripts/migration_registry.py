#!/usr/bin/env python3
"""
🗂️ migration_registry.py — Registro e Auditoria de Esquemas DB-First
Força os agentes a respeitar a ordem incremental de manipulação estrutural de banco.
"""
import re, sys
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
MIG_DIR = CONTEXT_DIR / "maintenance" / "migrations"
SCHEMA = CONTEXT_DIR / "maintenance" / "schema.sql"

def validate():
    print("[RUN] Executando Registro de Migrations...")
    
    if not MIG_DIR.exists():
        print("[WARN] migrations/ ausente. Ignorando (modo snapshot).")
        return
    
    files = sorted(MIG_DIR.glob("*.sql"))
    if not files:
        print("[OK] Nenhuma migration pendente.")
        return

    # 1. Convenção estrita (001_*.sql)
    for i, f in enumerate(files, 1):
        if not re.match(rf"^{i:03d}_.*\.sql$", f.name):
            print(f"[FATAL] Migration fora de ordem ou padrao invalido: {f.name}")
            print(f"💡 Esperado: {i:03d}_nome_da_migration.sql")
            sys.exit(1)

    # 2. Integridade Heurística vs Schema
    if SCHEMA.exists():
        last_mig = files[-1]
        schema_content = SCHEMA.read_text(encoding="utf-8")
        if last_mig.name not in schema_content and "-- Last migration:" not in schema_content:
            print(f"[WARN] schema.sql pode estar desatualizado! Ultima migration: {last_mig.name}")
            print("[DICA] Apos rodar o SQL, rode 'npm run context:sync' com a string da ultima migration no topo do schema.")
            # Nao aborta o pipe, apenas educa a I.A e o Dev.
    
    print(f"[OK] Migrations validas: {len(files)} detectadas. Arquitetura DB-First OK.")

if __name__ == "__main__":
    validate()
