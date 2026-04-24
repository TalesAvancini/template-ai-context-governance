---
version: 2.5.2
type: GOVERNANCE
---

# 🗺️ SSOT_MAP: Roteador do Oráculo & Hierarquia da Verdade

> **💡 TEMPLATE CLONE - INSTRUÇÃO OBRIGATÓRIA (Para Humanos & IAs)**
> Como este é um template (`template_inicío_de_projeto`), o ID do Oráculo abaixo aponta para a base de conhecimento estrutural do próprio template (sobre como usar o H.O.K). **Logo após clonar este repositório para iniciar um novo negócio, o humano DEVE criar um novo Notebook no NotebookLM e a IA DEVE vir aqui atualizar o ID abaixo.**

## 🔮 Oracle Baseline (Memória Externa)
O NotebookLM armazena o "Contexto Massivo" contínuo (PDFs, pesquisas, históricos detalhados) que saturaria nosso limite local de tokens. Agentes como `@vision-architect` e `@spec-enricher` o utilizam como extensão cerebral primária.

- **`oracle_mcp_id`:** `8979de2f-a111-4856-8a71-197d6b9ec876` *(ID do Oráculo - Altere no pós-clone!)*
- **Comportamento da IA:** Consulte usando ferramentas do MCP (`mcp_notebooklm_chat_with_notebook`) sempre que a informação transcender a raiz do código.

## 🏗️ Hierarquia da Verdade Local (SSOT)
Ordem de precedência (o nível superior sempre anula o inferior):

1. `🔮 Oráculo Externo (NotebookLM)`: Literatura de mercado, manuais extensos e macro-histórico.
2. `market/WIKI/concepts/`: Conhecimento destilado e regras de engenharia (Harness, TDD).
3. `market/compliance/*.md`: Regras imutáveis de negócio locais (Leis, Controles).
4. `brain/INCEPTION.md`: Visão estratégica, regras comportamentais (NUNCA/SEMPRE).
5. `brain/PRD.md`: Regras do produto e fluxo transacional atual.
6. `maintenance/schema.sql`: O contrato final implementado tecnicamente.

⚠️ **Conflito Nuvem vs Local:** Em caso de divergência entre o Oráculo (Mercado/Visão) e os arquivos locais, a IA deve disparar um alerta e o Humano deve arbitrar quem detém a verdade correta no momento (Paradigma da Lei 3 - Hok Governor).

