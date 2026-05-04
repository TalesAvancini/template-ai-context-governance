# 🤖 Inteligência Autônoma (.agent/)

> **Conceito Chave:** No H.O.K Forge, não trabalhamos com "IAs genéricas". Trabalhamos com **Personas (Roles)** e **Motores de Execução (Sub-Agents/Firmwares)**.

Este diretório contém os moldes mentais e protocolos que transformam um LLM comum em um componente especializado do sistema.

---

## 🎭 1. Roles (Personas) vs. Sub-Agents (Firmwares)

É vital entender a diferença entre esses dois níveis de atuação para não causar "Token Bloat" ou alucinações arquiteturais:

### A. Roles Lógicas (Personas)
**O que são:** "Chapéus cognitivos" assumidos pelo Agente Hub durante a conversa.
**Exemplos:** `@spec-enricher`, `@backend-engineer`, `@vision-architect`.
**Onde moram:** São definidas no `AGENT_REGISTRY.md` e ativadas via instrução de contexto.
**Quando usar:** Para brainstorm, planejamento, desenho de PRD e discussões estratégicas onde a fluidez e a visão macro são essenciais.

### B. Sub-Agents (Firmwares de Execução)
**O que são:** Arquivos físicos `.md` que servem para **reprogramar** o cérebro da IA local (Cursor, Cline, etc).
**Exemplos:** `spec-driver.md`, `qa-validator.md`.
**Onde moram:** `./subagents/`.
**Quando usar:** Para execução de código, auditoria técnica e tarefas de "mão na massa" (Fase de Implementação).
**Por que existem:** Eles atuam como um **Firmware rígido**. Ao carregar um subagente, a IA perde o livre-arbítrio e passa a seguir uma máquina de estados (ex: as 9 Skills do spec-driver), garantindo que o código seja escrito de forma atômica, testada e sem desvios criativos perigosos.

---

## 📁 Estrutura do Diretório

- **`/subagents/`**: Contém os protocolos de firmware que isolam o contexto e forçam a disciplina técnica (Zero-Trust).
- **`/templates/`**: Moldes para novos artefatos (Specs, Scratchpads, etc).
- **`/skills/`**: Definições de permissões e ferramentas (JSON) que limitam o poder de escrita das IAs.

---

## 🛡️ Regra de Ouro (Anti-Alucinação)
> **"Planeje como um Arquiteto (@spec-enricher), execute como um Robô (@spec-driver)."**

Nunca tente codificar uma feature complexa usando apenas a Role lógica. Sempre instancie o Firmware do `spec-driver` para garantir que as leis da física do projeto (RULES.md) sejam respeitadas mecanicamente.
