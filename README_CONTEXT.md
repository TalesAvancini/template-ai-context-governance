---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria viva, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.sh`, `Makefile` | Validacao, purge, sync e orquestracao. |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `tests/test_context.py` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija antes de forcar.

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rapidos (Cheat Sheet)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Sincronizar deps e schema com TECH_REQUIREMENTS.md
npm run context:sync

# Arquivar 70% do journal (mantem 30% como semente)
npm run context:purge

# Pipeline completo (validate -> sync -> purge)
npm run context:all

# Rodar testes do framework manualmente (Universal Python)
npm run context:test
```
> 💡 *Fallbacks:* `make all` ou `bash run_context.sh all`

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se `validate_context.py` ou `test_context.py` falharem.
- **CI/CD:** O GitHub Actions roda o pipeline em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Clone
- [ ] `.context/` existe com estrutura de camadas ok.
- [ ] `brain/RULES.md` e `brain/MASTER_FLOW.md` alinhados a stack.
- [ ] `brain/AGENT_REGISTRY.md` possui roles registradas.
- [ ] `npm run context:all` executa sem erros.

### 🚀 Inicio de Feature / PRD
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---

> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.
