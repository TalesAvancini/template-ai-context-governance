#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - Orquestrador Universal de Contexto
# ---------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"

# Detecção inteligente de Python (Windows vs Unix)
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "❌ Erro: Python não encontrado no PATH."
    exit 1
fi

usage() {
    echo "🛠️ Context Management Runner"
    echo "Usage: ./run_context.sh [command]"
    echo ""
    echo "Commands:"
    echo "  validate  - Check .context integrity & estimate tokens"
    echo "  purge     - Archive 70% of oldest journal entries"
    echo "  sync      - Sync TECH_REQUIREMENTS.md with package.json & schema.sql"
    echo "  all       - Run full pipeline (validate -> sync -> purge)"
    echo "  help      - Show this message"
    exit 1
}

run_script() {
    local script_name="$1"
    echo "▶️ Running $script_name..."
    if ! $PYTHON "$SCRIPT_DIR/$script_name"; then
        echo "❌ Failed: $script_name"
        exit 1
    fi
    echo "✅ Completed: $script_name"
    echo ""
}

[[ $# -eq 0 ]] && usage

case "$1" in
    validate) run_script "validate_context.py" ;;
    purge)    run_script "purge_journal.py" ;;
    sync)     run_script "sync_project.py" ;;
    all)
        run_script "validate_context.py"
        run_script "sync_project.py"
        run_script "purge_journal.py"
        echo "🎉 Full pipeline completed successfully."
        ;;
    help|--help|-h) usage ;;
    *) echo "❌ Unknown command: $1"; usage ;;
esac
