# 🏛️ MASTER PLAN: Context Governance Framework (v2.0 + Multi-Agent)

Este plano consolida as estratégias de **Automação de Manutenção** e **Especialização Cognitiva (Multi-Agent)** em um único framework modular, pronto para escalar de pequenos MVPs a grandes sistemas.

## 🕒 Metadados
- **Versão:** 2.0 (Consolidada)
- **Foco:** Eficiência de Tokens, Governança Rígida e Automação Python
- **Status:** Aguardando Aprovação Final

---

## 🧩 1. Estrutura de Arquivos em Camadas (`.context/`)

A pasta será organizada em quatro camadas lógicas para isolamento operacional:

### 🧠 Camada Cognitiva (The Brain)
- **`MASTER_FLOW.md`**: Diretriz mestre de navegação.
- **`RULES.md`**: Protocolos de conduta ("A Lei").
- **`AGENT_REGISTRY.md`**: DNS de papéis, permissões e isolamento.
- **`PROMPT_LIBRARY.md`**: Biblioteca de templates de prompts.
- **`PRD.md`**: Requisito em execução (O "Norte").
- **`ROADMAP.md`**: Metas e fases (O Planejamento).

### 🛠️ Camada de Manutenção (The Housekeeper)
- **`JOURNAL.md`**: Log vivo (limite heurístico de tokens).
- **`TECHNICAL_REQUIREMENTS.md`**: Inventário técnico consolidado.
- **`rebuild_guide.md`**: Manual de setup e infra.
- **`schema.sql`**: Snapshot do banco de dados.
- **`ARCHITECTURE.md`**, `TESTS.md`, `rx-anatomy.md`, `rx-biology.md`.
- **`_archive_context/`**: Memória de longo prazo.

### 📊 Camada de Monitoramento (The Dashboard)
- **`CONTEXT_HEALTH.md`**: Status dashboard técnico e cognitivo.

### ⚙️ Camada de Automação (The Arms)
- **`_scripts/`**: Scripts Python com `#!/usr/bin/env python3`.

---

## 📜 2. Protocolos Integrados em `RULES.md`

1.  **🛡️ Checklist de Carga (Obrigatório):** Antes de codificar, validar carga de:
    - [ ] Global (Rules, MasterFlow, Roadmap)
    - [ ] Role (Registry-defined)
    - [ ] Ephemeral (PRD ativo + Journal tail 30-50 lines)
2.  **🔒 Context Gate:** Verificação de integridade Schema vs PRD.
3.  **🤖 Active Role Declaration:** Início de tarefa com `🤖 Ativando @[role]`.
4.  **🔢 Heurística de Token (Session Budget):** Disparar alerta de reset/purge ao detectar:
    - `~15-20 trocas densas` OU `~50k caracteres no prompt`.
5.  **🤝 Handoff Protocol:** Registro estruturado no `JOURNAL.md` em trocas de domínio.

---

## 🐍 3. Automação Python (`.context/_scripts/`)

Scripts unificados que entendem a hierarquia de agentes:

- **`validate_context.py`**: Checa integridade de arquivos, conformidade de roles e saúde geral.
- **`purge_journal.py`**: Arquiva 70% do log e gera uma semente de contexto no topo do arquivo atual.
- **`sync_project.py`**: Atualiza `TECHNICAL_REQUIREMENTS.md` lendo o `package.json` e `schema.sql`.

---

## 📈 4. Dashboard de Saúde (`CONTEXT_HEALTH.md`)

```markdown
# 📊 Context Health Check
| Métrica | Status | Pilar |
| :--- | :--- | :--- |
| Journal Line Count | [ 412 / 600 ] | Manutenção |
| Active Role | @frontend-specialist | Cognitivo |
| Schema Consistency | ✅ Synchronized | DB-First |
| Token Window | ⚠️ 78k (80%) | Sessão |
```

---

## 🚦 Roadmap de Execução

1.  **Fase 1: Estrutura MD** (Criar Registry, Prompt Library e Health).
2.  **Fase 2: As Leis** (Atualizar Master Flow e Rules com a lógica Multi-Agent).
3.  **Fase 3: Os Braços** (Implementar scripts Python em `_scripts/`).
4.  **Fase 4: Finalização** (Git Commit + Walkthrough).

---

> [!IMPORTANT]
> Este plano prioriza a **independência**. O projeto pode ser operado em "Modo Solo" (Single Agent) usando a role `@fullstack-generalist`, ou em "Modo Escala" (Multi-Agent) conforme a necessidade.
