#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto v2.4 (Hardened Pipeline)
Sequencia otimizada: validate → scan-secrets → sync → migrations → harness → lint(strict) → health
"""
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"

def run_script(name, args=None):
    if args is None: args = []
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} nao encontrado em {SCRIPTS_DIR}")
        sys.exit(1)
    
    print(f"[RUN] Executando {name}...")
    try:
        subprocess.run([sys.executable, str(script_path)] + args, check=True)
        print(f"[OK] Concluido: {name}\n")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Falha em {name}. Pipeline abortado.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("[USAGE] python run_context.py [validate|purge|sync|cleanup|harness|lint|oracle|health|scan-secrets|check-migrations|all|help]")
        sys.exit(1)

    cmd = sys.argv[1]
    extra_args = sys.argv[2:]

    if cmd == "validate": run_script("validate_context.py", extra_args)
    elif cmd == "purge":  run_script("purge_journal.py", extra_args)
    elif cmd == "sync":   run_script("sync_project.py", extra_args)
    elif cmd == "cleanup": run_script("cleanup_specs.py", extra_args)
    elif cmd == "harness": run_script("harness_runner.py", extra_args)
    elif cmd == "lint":    run_script("lint_wiki.py", extra_args)
    elif cmd == "lint-strict": run_script("lint_wiki.py", ["--strict"] + extra_args)
    elif cmd == "oracle":  run_script("context_oracle.py", extra_args)
    elif cmd == "health":  run_script("health_sync.py", extra_args)
    elif cmd == "scan-secrets": run_script("secrets_scanner.py", extra_args)
    elif cmd == "check-migrations": run_script("migration_registry.py", extra_args)
    
    elif cmd == "all":
        # Fail-Fast Pipeline (CRÍTICO APENAS)
        run_script("validate_context.py")
        run_script("secrets_scanner.py")
        run_script("sync_project.py")
        run_script("migration_registry.py")
        run_script("harness_runner.py")
        print("[RUN] Executando lint_wiki.py (Strict)...")
        run_script("lint_wiki.py", ["--strict"])
        print("[RUN] Sincronizando Health Dashboard...")
        run_script("health_sync.py")
        print("[DONE] Pipeline H.O.K. + Security + Migrations + Health concluido com sucesso.")
        
    elif cmd in ["help", "--help", "-h"]:
        print("Comandos: validate | purge | sync | cleanup | harness | lint | oracle | health | scan-secrets | check-migrations | all")
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
