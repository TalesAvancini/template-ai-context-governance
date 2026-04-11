#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto (v2.2.1 Premium)
Orquestrador multiplataforma para validacao, sincronia e limpeza.
"""
import sys
import subprocess
from pathlib import Path

# Configurações
BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"

def run_script(name):
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} nao encontrado em {SCRIPTS_DIR}")
        sys.exit(1)
    
    print(f"[RUN] Executando {name}...")
    try:
        # Usa o mesmo interpretador atual para garantir consistência
        subprocess.run([sys.executable, str(script_path)], check=True)
        print(f"[OK] Concluido: {name}\n")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Falha em {name}. Pipeline abortado.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("[USAGE] python run_context.py [validate|purge|sync|cleanup|all|help]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "validate": run_script("validate_context.py")
    elif cmd == "purge":  run_script("purge_journal.py")
    elif cmd == "sync":   run_script("sync_project.py")
    elif cmd == "cleanup": run_script("cleanup_specs.py")
    elif cmd == "all":
        run_script("validate_context.py")
        run_script("sync_project.py")
        run_script("cleanup_specs.py")
        print("[DONE] Pipeline completo finalizado (Validate -> Sync -> Cleanup).")
    elif cmd in ["help", "--help", "-h"]:
        print("Comandos: validate | purge | sync | cleanup | all")
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
