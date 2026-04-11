# 🏛️ AI-Ready Engineering Kit (v2.2)
> **Governance, Context & Multi-Agent Orchestration for Next-Gen Development.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação (GitHub Copilot, Cursor, Antigravity). Ele estabelece uma infraestrutura de **Governança de Contexto** rígida para evitar alucinações, garantir escalabilidade e manter a saúde técnica do projeto a longo prazo.

---

## 🧠 A Filosofia: "Se não está no Contexto, não existe."

Neste framework, a pasta `.context/` é a **Single Source of Truth (SSOT)**. O código é apenas o reflexo físico da inteligência e das decisões documentadas aqui.

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada Cognitiva
- **`brain/`**: Onde mora a inteligência. Contém as regras (`RULES.md`), o fluxo mestre (`MASTER_FLOW.md`), o registro de agentes (`AGENT_REGISTRY.md`) e os prompts padronizados (`PROMPT_LIBRARY.md`).
- **`maintenance/`**: Onde mora a "verdade real". Contém o log vivo (`JOURNAL.md`), o esquema do banco (`schema.sql`), arquitetura e requisitos técnicos.
- **`monitoring/`**: Dashboard de saúde do contexto (`CONTEXT_HEALTH.md`).
- **`_scripts/`**: O motor de automação (Python).

### 2. Automação & Orquestração
O projeto vem "blindado" com ferramentas de orquestração:
- **`Makefile`**: Padrão industrial para automação Unix.
- **`run_context.sh`**: Script bash universal.
- **`package.json`**: Atalhos NPM para fácil acesso.

---

## 🚀 Como Começar (Getting Started)

### Requisitos de Sistema:
- **Python ≥ 3.8**
- **Node.js**
- **Git**

### Instalação:
```bash
# Instale as dependências (Husky, etc.)
npm install
```

### Comandos Essenciais:
| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Verifica a integridade dos arquivos e saúde dos tokens. |
| `npm run context:sync` | Sincroniza `TECHNICAL_REQUIREMENTS.md` com `package.json` e `schema.sql`. |
| `npm run context:purge` | Limpa o `JOURNAL.md` mantendo 30% como semente e arquivando o resto. |
| `npm run context:all` | Executa o pipeline completo (Valida -> Sync -> Purge). |
| `npm run context:test` | Roda a suíte de testes de infraestrutura (Python). |

---

## 🤝 Protocolo Multi-Agent

Este template foi desenhado para fluxo de múltiplos agentes. Sempre declare sua role ao iniciar uma tarefa:
1. Consulte `brain/AGENT_REGISTRY.md`.
2. Use um template de `brain/PROMPT_LIBRARY.md`.
3. Registre decisões críticas no `maintenance/JOURNAL.md`.

---

## 🛡️ Camadas de Blindagem
- **Local:** Husky impede commits se os testes de contexto falharem.
- **Remoto:** GitHub Actions valida a estrutura em cada Push/Pull Request.

---

## 🛠️ Personalização
Ao clonar este template, siga estes passos:
1. Edite o `brain/ROADMAP.md` com as metas do seu novo projeto.
2. Atualize o `maintenance/TECHNICAL_REQUIREMENTS.md` com a sua Stack.
3. Defina o seu `maintenance/schema.sql` inicial.

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*
