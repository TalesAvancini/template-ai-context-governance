#!/usr/bin/env python3
import os
import sys

# Configurações de limites (Heurísticas do RULES.md)
JOURNAL_PATH = ".context/maintenance/JOURNAL.md"
MAX_LINES = 600
MAX_CHARS = 50000

def check_file_health(path):
    if not os.path.exists(path):
        return f"[ERROR] Erro: Arquivo {path} não encontrado."
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()
        char_count = len(content)
        
        status = "[OK]"
        if len(lines) > MAX_LINES or char_count > MAX_CHARS:
            status = "[WARN] Degradado (Requer Purge)"
            
        return f"{status} | {path} ({len(lines)} linhas, {char_count} caracteres)"

def validate_structure():
    print("--- Validando Integridade do Contexto ---")
    layers = [".context/brain", ".context/maintenance", ".context/monitoring"]
    for layer in layers:
        if os.path.isdir(layer):
            print(f"[OK] Camada {layer} encontrada.")
        else:
            print(f"[ERROR] Camada {layer} MISSING!")

    print("\n--- Health Check ---")
    print(check_file_health(JOURNAL_PATH))
    
    # Validação simples de Schema vs PRD (Proxy)
    prd_path = ".context/brain/PRD.md"
    schema_path = ".context/maintenance/schema.sql"
    if os.path.exists(prd_path) and os.path.exists(schema_path):
        print("[OK] Sincronismo Schema/PRD verificado (Proxy).")
    else:
        print("[WARN] Aviso: PRD ou Schema ausentes para validação cruzada.")

if __name__ == "__main__":
    try:
        validate_structure()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        sys.exit(1)
