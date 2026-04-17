#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - [DEPRECATED] Módulo Retido por Compatibilidade (v2.4.1)
# ---------------------------------------------------------
set -euo pipefail

echo -e "\033[1;33m[DEPRECATED]\033[0m O uso de 'run_context.sh' e desencorajado na v2.4.1+. Redirecionando para 'run_context.py'..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 🔍 Detecção robusta de Python na máquina host (para Linux/macOS)
if command -v python3 &>/dev/null; then PYTHON="python3"
elif command -v python &>/dev/null; then PYTHON="python"
else echo "❌ Erro: Python não encontrado no PATH."; exit 1; fi

# Delega argumentos diretamente para a engine unificada Python
exec $PYTHON "$SCRIPT_DIR/run_context.py" "$@"
