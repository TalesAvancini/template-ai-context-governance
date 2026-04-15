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

# (Injeção dos Motores Reais v2.4.1 Hardened)
cat > .context/_scripts/validate_context.py << 'EOF'
#!/usr/bin/env python3
import os, sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQUIRED = ["brain/RULES.md", "brain/PRD.md", "maintenance/JOURNAL.md"]
def check_specs():
    specs = CONTEXT_DIR.parent / ".specs/features"
    if not specs.exists(): return True
    return all((d / "STATE.md").exists() for d in specs.iterdir() if d.is_dir())
def validate():
    print("--- Validacao v2.4.1 Hardened ---")
    missing = [f for f in REQUIRED if not (CONTEXT_DIR / f).exists()]
    if missing or not check_specs(): sys.exit(1)
    print("✅ Contexto e Workshop integros.")
if __name__ == "__main__": validate()
EOF

cat > .context/_scripts/cleanup_specs.py << 'EOF'
#!/usr/bin/env python3
import os, shutil, time
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
SPECS_DIR = SCRIPT_DIR.parent.parent / ".specs" / "features"
ARCHIVE_DIR = SCRIPT_DIR.parent / "maintenance" / "_archive_context" / "specs"
def cleanup():
    if not SPECS_DIR.exists(): return
    specs = sorted([d for d in SPECS_DIR.iterdir() if d.is_dir()], key=os.path.getmtime)
    while len(specs) > 3:
        shutil.move(str(specs.pop(0)), str(ARCHIVE_DIR))
    print("[OK] Manutencao de specs concluida.")
if __name__ == "__main__": cleanup()
EOF

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
const runner = '$PKG_MGR' === 'npm' ? 'npm run' : '$PKG_MGR';
Object.assign(pkg.scripts, {
  'context:validate': 'bash run_context.sh validate',
  'context:cleanup': 'bash run_context.sh cleanup',
  'context:all': runner + ' context:validate && ' + runner + ' context:cleanup',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:validate" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."
