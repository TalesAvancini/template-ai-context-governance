### 🔍 Por que um único arquivo não basta?
A IA não lê apenas um arquivo para definir comportamento. Ela avalia:
- 📁 Estrutura de pastas (`brain/`, `maintenance/`, `monitoring/`, `.specs/`)
- 🤖 `AGENT_REGISTRY.md` (ainda carregará 7 roles se existir)
- 🐍 Scripts Python e hooks do Husky (continuam ativos)
- 📜 Regras de carregamento (`Checklist de Carga` ainda exige camadas)
- 🧠 Memória de sessão (a IA tentará carregar tudo o que encontrar)

Se você só trocar o `RULES.md`, a IA ficará em **estado híbrido confuso**: regras dizem "modo leve", mas a estrutura exige validações pesadas, registry complexo e scripts de automação. Isso gera `token bloat`, alucinação e falhas de contexto gate.

---
### 🛠️ 3 Caminhos Técnicos Viáveis

| Abordagem | Como funciona | Prós | Contras |
|-----------|--------------|------|---------|
| `MODE.md` (Flag) | Arquivo simples: `MODE: LIGHT`. A IA lê primeiro e ajusta comportamento. | Zero destruição, reversível, explícito. | Exige atualização no `RULES_LIGHT.md` para ler a flag. |
| `init_ai_project_light.sh` | Bootstrap que cria estrutura mínima do zero (sem camadas, sem scripts, sem Husky). | Limpo, seguro, ideal para novos MVPs. | Não converte projetos robustos existentes. |
| `downgrade_to_light.sh` | Remove camadas, desativa Husky, arquiva scripts, substitui `RULES.md`. | Converte projeto existente sem perder histórico. | Irreversível sem backup manual. |

---
### ✅ Recomendação: `MODE.md` + `init_ai_project_light.sh`
É a combinação mais segura. Você mantém o robusto como padrão, mas pode ativar o modo leve em qualquer repositório novo ou existente com **um arquivo de flag** ou **um comando de init**.

---
### 📄 1. `MODE.md` (A Chave de Conversão)
Coloque na raiz de `.context/`. A IA **DEVE** ler este arquivo antes de qualquer checklist.

```markdown
---
Criado em: YYYY-MM-DD HH:MM
Última Atualização: YYYY-MM-DD HH:MM
Status: Ativo
---

# 🪶 MODE.md
> Define o perfil operacional do framework. A IA ajusta carregamento, roles e automação conforme este valor.

**MODE:** LIGHT  
**Reason:** MVP < 2 semanas | Time 1-2 devs | Velocidade > Governança  

💡 *Insight IA: Se MODE = LIGHT, ignore camadas, scripts, registry multi-agent e .specs/. Carregue apenas: RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql. Use @fullstack-generalist por padrão.*
```

---
### 📜 2. Patch Obrigatório no `RULES_LIGHT.md`
Adicione este bloco no **topo** do arquivo, antes de qualquer regra:

```markdown
📜 RULES_LIGHT.md — Modo Minimalista (MVP/POC)
Projeto: [NOME DO PROJETO] | Arquitetura: Single-Agent + Database-First
> 🪶 **MODO ATIVO:** Leia `MODE.md`. Se `MODE: LIGHT`, siga estritamente este protocolo enxuto. Ignore `.specs/`, scripts Python, Husky e `AGENT_REGISTRY.md`.

🛡️ Checklist de Carga (Light)
1. [ ] RULES_LIGHT.md (este arquivo)
2. [ ] PRD.md ativo
3. [ ] schema.sql atualizado
4. [ ] JOURNAL.md < 300 linhas
⚠️ Se faltar 1 item → pare e solicite correção.

🔄 Comportamento do Agente (Light)
- Role padrão: `@fullstack-generalist` (única ativa)
- Sem handoff obrigatório. Registre decisões críticas direto no JOURNAL.md
- Database-First mantido. Nunca assuma schema.
- Sem automação. Validação manual: `grep -q "schema.sql" PRD.md && echo "✅ OK"`
- Fim de sessão: `"Contexto atualizado? [S/N]"`
```

---
### 🐚 3. `init_ai_project_light.sh` (Bootstrap Seguro)
Cria uma estrutura flat, sem camadas, sem scripts, sem Husky. Ideal para `git init` de MVPs.

```bash
#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
NC='\033[0m'

[ -d ".context" ] && { echo "❌ .context/ já existe. Abortando."; exit 1; }

echo -e "\n${GREEN}🪶 Inicializando Modo LIGHT...${NC}"
mkdir -p .context

NOW=$(date +%Y-%m-%d\ %H:%M)

# MODE Flag
cat > .context/MODE.md << EOF
---
Criado em: $NOW
Status: Ativo
---
MODE: LIGHT
Reason: MVP rápido | Velocidade > Governança
💡 IA: Ignore camadas, scripts, registry e .specs/. Use apenas RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql.
EOF

# RULES_LIGHT (minimalista)
cat > .context/RULES_LIGHT.md << 'EOF'
📜 RULES_LIGHT.md — Modo Minimalista
> 🪶 MODE: LIGHT ativo. Role única: @fullstack-generalist. Sem scripts, sem Husky, sem handoff complexo.
🛡️ Carga: [ ] RULES_LIGHT.md [ ] PRD.md [ ] schema.sql [ ] JOURNAL.md <300lin
🗄️ DB-First: Valide schema antes de UI. Se faltar campo → pare e avise.
🔄 Fim de sessão: Pergunte "Atualizo contexto?" e registre no JOURNAL.md apenas mudanças de lógica/bug.
⚠️ Sem automação. Sem registry. Sem .specs/. Mantenha enxuto.
EOF

# Arquivos base
for f in PRD.md JOURNAL.md schema.sql; do
  cat > ".context/$f" << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📄 $f
EOF
done

echo -e "${GREEN}✅ Modo LIGHT pronto. Estrutura plana, sem overhead.${NC}"
echo "📖 Próximo: Preencha PRD.md e comece. A IA usará @fullstack por padrão."
```

---
### 🧠 Como a IA Interpreta Isso na Prática
1. **Início de sessão:** A IA lê `MODE.md` primeiro.
2. **Se `MODE: LIGHT`:** 
   - Ignora `brain/`, `maintenance/`, `monitoring/`, `_scripts/`, `.specs/`
   - Carrega apenas os 4 arquivos essenciais
   - Ativa `@fullstack-generalist` implicitamente
   - Desativa validações Python/Husky automaticamente
   - Usa heurística simplificada de tokens (limite ~20k chars)
3. **Se quiser voltar ao robusto:** Troque `MODE: ROBUST` e rode `npm run context:all` para restaurar camadas/scripts.

---
### 🚀 Próximo Passo
Quer que eu:
1. **Gere o `downgrade_to_light.sh`** para converter um projeto robusto existente sem perder histórico?
2. **Ajuste o `init_ai_project.sh` principal** para incluir uma flag `--light` que alterna entre os dois modos automaticamente?
3. **Entregue o `RULES_LIGHT.md` completo** (versão pronta para copiar/colar, com todos os protocolos simplificados)?

Escolha o fechamento. O framework agora tem conversão explícita, segura e reversível. 🏁