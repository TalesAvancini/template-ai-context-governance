# 🤖 Plano de Implementação: Arquitetura Multi-Agent

Este plano detalha a especialização do template com foco em **Especialização de Papéis**, **Isolamento de Contexto** e **Protocolos de Handoff**. O objetivo é transformar o agente em um sistema de engenharia cognitiva coordenado.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Roles, Context Isolation & Token Efficiency
- **Status:** Aguardando Aprovação (Em Separado)

---

## 🧩 1. Novos Componentes de Estrutura

### [REFINED] `AGENT_REGISTRY.md`
- **Conceito:** DNS cognitivo e Manifesto de Especialidades.
- **Regra de Ouro:** "Não registrado = Não executado".
- **Conteúdo Robusto:** Tabela com Roles (`@db-architect`, `@frontend-specialist`, `@backend-engineer`, `@qa-validator`, `@devops-guardian`, `@context-keeper`, `@fullstack-generalist`), permissões granulares de escrita e gatilhos de ativação.
- **Human Insights:** Blocos de contexto explicando o "porquê" das decisões técnicas para futuras IAs.

### [NEW] `PROMPT_LIBRARY.md`
- **Função:** Catálogo de templates de prompts de alta performance.
- **Conteúdo:** Instruções estruturadas para tarefas repetitivas (ex: "Criação de Componente", "Análise de Bug Crítico", "Escrita de Documentação").

---

## 📑 2. Protocolos de Handoff & Isolamento

### 🛡️ Camadas de Isolamento (Context Layering)
Implementação de carregamento por camadas no `RULES.md`:
1.  **🌍 Global (Sempre):** `RULES.md`, `MASTER_FLOW.md`, `ROADMAP.md`.
2.  **🎯 Role-Specific:** Definido no registry (ex: `@db` lê `schema.sql`).
3.  **📦 Task-Ephemeral:** `PRD.md` ativo e últimas 30-50 linhas do `JOURNAL.md`.
4.  **🗃️ Deep Archive:** Acesso apenas sob demanda explícita.

### 🤝 Protocolo de Handoff Estruturado
Tarefas cross-domain exigem registro de estado no `JOURNAL.md` antes da troca:
- **Formato:** `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [Checkpoint Técnico] | Próximo: [Ação]`

---

## 🛠️ 3. Integração com o Workflow Atual

### [MODIFY] `RULES.md`
- Adicionar a seção **3.1 Protocolo Multi-Agent**.
- Definir a obrigatoriedade da declaração de ativação: `🤖 Ativando @[role] | Tarefa: [X]`.

### [MODIFY] `MASTER_FLOW.md`
- Incluir `AGENT_REGISTRY.md` e `PROMPT_LIBRARY.md` no diagrama de árvore.
- Adicionar o ciclo de vida da sessão Multi-Agent.

---

## 🚦 Próximos Passos

1.  **Revisão do Plano** em paralelo com o plano de Automação (v2.0).
2.  **Criação dos arquivos MD** com os templates pré-definidos.
3.  **Simulação de Handoff** para testagem da lógica de semente (`Seed Context`).

---

> [!TIP]
> Esta arquitetura permite que o projeto escale para milhares de linhas de código sem que a IA perca o foco ou alucine por excesso de arquivos irrelevantes na janela de contexto.
