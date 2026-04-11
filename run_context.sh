#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - Orquestrador Universal de Contexto v2.2
# ---------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"

# 🔍 Detecção robusta de Python
if command -v python3 &>/dev/null; then PYTHON="python3"
elif command -v python &>/dev/null; then PYTHON="python"
else echo "❌ Erro: Python não encontrado no PATH."; exit 1; fi

run_script() {
  local script_name="$1"
  echo "▶️ Executando $script_name..."
  if ! $PYTHON "$SCRIPT_DIR/$script_name"; then
    echo "❌ Falha em $script_name. Pipeline abortado."; exit 1;
  fi
  echo -e "✅ Concluído: $script_name\n"
}

[[ $# -eq 0 ]] && { echo "🛠️ Uso: $0 [validate|purge|sync|cleanup|all|help]"; exit 1; }

case "$1" in
  validate) run_script "validate_context.py" ;;
  purge)    run_script "purge_journal.py" ;;
  sync)     run_script "sync_project.py" ;;
  cleanup)  run_script "cleanup_specs.py" ;;
  all)
    run_script "validate_context.py"
    run_script "sync_project.py"
    run_script "cleanup_specs.py"
    echo "🎉 Pipeline completo finalizado (Validate → Sync → Cleanup)."
    ;;
  help|--help|-h) echo "Comandos: validate | purge | sync | cleanup | all" ;;
  *) echo "❌ Comando desconhecido: $1"; exit 1 ;;
esac
