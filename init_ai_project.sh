#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.2 Premium)
# -----------------------------------------------------------------------------
# Versão com Detecção Automática de Gerenciador (NPM, YARN, PNPM)
# Injeta automaticamente motores de automação v2.2 e blindagem Husky.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  command -v python3 >/dev/null 2>&1 || PYTHON="python3"
  command -v python >/dev/null 2>&1 || PYTHON="python"
  [ -z "${PYTHON:-}" ] && error "python3 ou python e obrigatorio."
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity AI-Ready Framework v2.2 Premium..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals}
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança v2.2..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT).

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo para decisoes criticas.
- TECHNICAL_REQUIREMENTS.md: Inventario tecnico auto-sincronizado.

🤖 2. Comportamento do Agente
- Identificacao: \`🤖 Ativando @role para...\`
- Context Gate: Valide Schema, Journal e Libs antes de codar.
- Handoff: Registro obrigatorio no \`JOURNAL.md\` ao trocar de dominio.
EOF

# (Injeção do motor real v2.2 - Purge/Sync/Validate)
log "Injetando motor de automacao Python v2.2 Reais..."

cat > .context/_scripts/validate_context.py << 'EOF'
#!/usr/bin/env python3
import os, sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQUIRED = ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md", "maintenance/JOURNAL.md", "maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md"]
def validate():
    print("--- Validacao v2.2 ---")
    missing = [f for f in REQUIRED if not (CONTEXT_DIR / f).exists()]
    if missing: 
        print(f"❌ Ausentes: {missing}")
        sys.exit(1)
    print("✅ Contexto integro.")
if __name__ == "__main__": validate()
EOF

cat > .context/_scripts/purge_journal.py << 'EOF'
#!/usr/bin/env python3
import re, os
from pathlib import Path
from datetime import datetime
SCRIPT_DIR = Path(__file__).parent
JOURNAL = SCRIPT_DIR.parent / "maintenance/JOURNAL.md"
ARCHIVE = SCRIPT_DIR.parent / "maintenance/_archive_context/journals"
def purge():
    if not JOURNAL.exists(): return
    content = JOURNAL.read_text(encoding="utf-8")
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    entries = [p.strip() for p in parts if p.strip()]
    if len(entries) <= 1: return
    keep = max(1, int(len(entries) * 0.3))
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    (ARCHIVE / f"journal_{ts}.md").write_text("\n\n".join(entries[:-keep]), encoding="utf-8")
    JOURNAL.write_text("\n\n".join(entries[-keep:]), encoding="utf-8")
    print(f"[OK] Purge concluido.")
if __name__ == "__main__": purge()
EOF

# Orquestradores
cat > run_context.sh << 'EOF'
#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"
PYTHON="${PYTHON:-python3}"
[ -z "$1" ] && exit 1
$PYTHON "$SCRIPT_DIR/${1}_context.py"
EOF

# 📦 Inicializa package.json se não existir
if [ ! -f package.json ]; then
  case $PKG_MGR in
    npm)  npm init -y > /dev/null 2>&1 ;;
    yarn) yarn init -y > /dev/null 2>&1 ;;
    pnpm) pnpm init > /dev/null 2>&1 ;;
  esac
fi

log "Instalando Husky via $PKG_MGR..."
case $PKG_MGR in
  npm)  npm install -D husky > /dev/null 2>&1 ;;
  yarn) yarn add -D husky > /dev/null 2>&1 ;;
  pnpm) pnpm add -D husky > /dev/null 2>&1 ;;
esac

log "Injetando scripts no package.json..."
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
const runner = '$PKG_MGR' === 'npm' ? 'npm run' : '$PKG_MGR';
Object.assign(pkg.scripts, {
  'context:validate': 'bash run_context.sh validate',
  'context:test': 'python tests/test_context.py',
  'context:all': runner + ' context:validate && ' + runner + ' context:sync && ' + runner + ' context:purge',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:test" > .husky/pre-commit

chmod +x run_context.sh .context/_scripts/*.py .husky/pre-commit

success "Antigravity Kit v2.2 Premium inicializado com $PKG_MGR!"
warn "Execute '$PKG_MGR run context:validate' para confirmar."
