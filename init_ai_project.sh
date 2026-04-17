#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.4.1 Hardened)
# -----------------------------------------------------------------------------
# Versão Suprema: Fusão Antigravity + TLC Spec-Driven.
# Com detecção automática de gerenciador e motores de manutenção completos.
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
  if command -v python3 >/dev/null 2>&1; then PYTHON="python3"
  elif command -v python >/dev/null 2>&1; then PYTHON="python"
  else error "python3 ou python e obrigatorio."
  fi
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
log "Inicializando Antigravity AI-Ready Framework v2.4.1 Hardened..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop TLC..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança e integração TLC..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit + TLC Fusion)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT). O workshop \`.specs\` e o espaco de execucao efemera.

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo e handoffs.
- .specs/: Workbench atômico (Regra de 48h/Max 3).

🔄 4. Gatilhos Operacionais
- "Inicie a fase de SPECIFY para o PRD #[ID]": IA cria spec atômica no .specs/.
- "Atualize contexto": Sincronizacao proativa via sync_project.py.
EOF

cat > .context/brain/TLC_INTEGRATION.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 🔗 TLC_INTEGRATION.md
Ponte entre Governança (.context/) e Execução Atômica (.specs/).

## 🔄 Ciclo de Vida Híbrido
1. INTENT -> PRD.md ativo define escopo.
2. SPECIFY -> IA cria .specs/features/[nome]/spec.md.
3. IMPLEMENT -> Geração de código baseada na spec.
4. VERIFY -> STATE.md marcado como ✅ PASSED.
5. SYNC -> Lições para o JOURNAL.md e limpeza da spec.
EOF

# Os Motores Reais v2.4.1 Hardened já residem na pasta .context/_scripts do template.
# Diferente de versões anteriores, este bootstrapper NÃO sobrescreve os motores Python nativos com cat.

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
Object.assign(pkg.scripts, {
  'context:validate': 'python run_context.py validate',
  'context:cleanup': 'python run_context.py cleanup',
  'context:purge': 'python run_context.py purge',
  'context:sync': 'python run_context.py sync',
  'context:oracle': 'python run_context.py oracle',
  'context:lint': 'python run_context.py lint',
  'context:harness': 'python run_context.py harness',
  'context:all': 'python run_context.py all',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:all" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."
