# 🏛️ Plano de Expansão: Context Governance Framework (v2.0)

Este plano detalha a transição do template de um sistema de documentação estática para um framework de governança ativa, focado em **escala**, **automação** e **prevenção de drift**.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Automação em Python e Escala de Contexto
- **Status:** Aguardando Aprovação

---

## 🧩 1. Estrutura de Arquivos Ampliada

Vamos expandir a pasta `.context/` para incluir novas camadas de inteligência:

### [NEW] Novos Documentos de Governança
- **`PROMPT_LIBRARY.md`**: Catálogo de personas e templates de prompts específicos para garantir consistência entre sessões.
- **`SESSION_MANAGER.md`**: Regras de gerenciamento de janela de tokens, limites de sessão e snapshots de resumo.
- **`CONTEXT_HEALTH.md`**: Dashboard de saúde do contexto (métricas de linhas, divergências e obsolescência).
- **`AGENT_REGISTRY.md`**: Definição de papéis (Expertises) e permissões de escrita/leitura nos arquivos do contexto.

---

## 📜 2. Atualização dos Protocolos (`RULES.md`)

Injetaremos novos protocolos de segurança e eficiência no arquivo de leis do agente:

### 🔹 Context Gate (Validação Pré-Voo)
O Agente deve realizar um "Checklist de Integridade" antes de gerar código, validando se o PRD e o Schema estão sincronizados.

### 🔹 Session Budget (Gestão de Tokens)
Definição de limites claros: ao atingir 80% da janela de contexto (estimada), o agente **deve** realizar um purge do `JOURNAL.md` (via script) e gerar um resumo semente.

---

## 🛠️ 3. Automação com Python (`.context/_scripts/`)

Criaremos scripts em Python para tornar a governança ativa e independente do ambiente da IDE.

### #### [NEW] `validate_context.py`
- Verifica se o `schema.sql` contém os campos referenciados no PRD atual.
- Valida o limite de linhas do `JOURNAL.md`.
- Gera um alerta visual se o status em qualquer arquivo for `Stale` ou `Deprecated`.

### #### [NEW] `purge_journal.py`
- Executa a lógica de arquivamento: move os primeiros 70% do log para `_archive_context/journals/`.
- Mantém os 30% finais e insere um resumo gerado pela IA no topo como conexão lógica.

### #### [NEW] `init_context.py`
- Script de bootstrap que inicializa a estrutura em novos projetos, gera os metadados de tempo reais e cria o `schema.sql` inicial.

---

## 📈 4. Monitoramento (`CONTEXT_HEALTH.md`)

Criação do dashboard dinâmico que será atualizado periodicamente pelos scripts ou manualmente pela IA.

| Métrica | Limite | Ação em caso de Falha |
| :--- | :--- | :--- |
| JOURNAL size | 600 linhas | Trigger `purge_journal.py` |
| PRD sync | 100% | Bloqueio de geração de UI |
| Token Window | 128k (80%) | Trigger Snapshot de Sessão |

---

## 🚦 Próximos Passos (Workflow)

1.  **Aprovação do Plano** (Você).
2.  **Criação dos Arquivos MD** com os templates propostos.
3.  **Geração do Código Python** para cada script de automação.
4.  **Atualização do `MASTER_FLOW.md` e `RULES.md`** para refletir a nova arquitetura.
5.  **Validação Final** da estrutura completa.

---

> [!IMPORTANT]
> A implementação será feita de forma **não invasiva** e **não executável** conforme solicitado, apenas preparando o repositório para ser exportado para o GitHub.
