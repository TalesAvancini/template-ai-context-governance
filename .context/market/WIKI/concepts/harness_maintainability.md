---
id: HARNESS_MAINTAINABILITY
type: concept
tags: [harness-engineering, governanca, qualidade-de-codigo]
aliases: [Maintainability Harness, Harness de Manutenibilidade]
concept: Prevenção de Dívida Técnica e AI Slop
entity: Antigravity Framework
source: market/RAW/harness_engineering_manifesto.md
last_updated: 2026-04-23
---

# Maintainability Harness (Harness de Manutenibilidade)

> Fonte: market/RAW/harness_engineering_manifesto.md

O **Maintainability Harness** (Harness de Manutenibilidade) é a categoria de controle cibernético focada em regular a qualidade interna do código para evitar que a base do software "apodreça" rapidamente. Como as inteligências artificiais tendem a escrever o código mais fácil para resolver o problema imediato, elas frequentemente duplicam lógicas e ignoram padrões de projeto se não forem estritamente supervisionadas. Este harness atua como um inspetor implacável, utilizando ferramentas para impedir a degradação contínua da arquitetura.

## Key Takeaways
*   **Foco Principal:** Prevenção de dívida técnica, código duplicado, violações de estilo e complexidade ciclomática elevada.
*   **Sensores Computacionais (Obrigatórios):** Linters, formatadores e *type checkers* que rodam localmente para fornecer resultados determinísticos e bloquear commits ruins.
*   **Sensores Inferenciais (Complementares):** Agentes de IA atuando em *background* para avaliar semanticamente o código, identificar redundâncias e sugerir refatorações.
*   **Regulação Passiva e Ativa:** O sistema não apenas aponta o erro, mas injeta a solução no prompt da IA para que ela se autocorrija sem intervenção humana.

### 🏢 Exemplos de Implementação (Padrões Globais)

*   **Garbage Collection de IA:** Processo recorrente onde agentes em background varrem o repositório em busca de padrões subótimos introduzidos por gerações anteriores, abrindo PRs de refatoração automática.
*   **Regras Determinísticas de AST:** Conversão de Code Reviews humanos em regras sintáticas (via *tree-sitter*) que impedem mecanicamente que a IA repita o mesmo erro arquitetural.
*   **Loop de Autocorreção (Iterate-PR):** Ciclo onde o agente detecta falhas nos logs do CI/Linter, aplica correções autonomamente e reenvia a verificação.

### ⚙️ Integração no Antigravity Kit (H.O.K. v2.5.2)

No framework v2.5.2, o **Maintainability Harness** opera através das seguintes camadas:

1.  **Linter Epistemológico:** O script `lint_wiki.py` garante a sanidade da documentação, exigindo fontes (`> Fonte: RAW/...`) para cada afirmação técnica.
2.  **Hardening de Captura:** O script `captura_projeto.py` (v2.5.2) atua como um harness de manutenibilidade de contexto, filtrando ruídos, arquivos mortos e dossiers pesados da janela de tokens da IA.
3.  **Harness de Contratos:** O `harness_runner.py` valida o estado das specs antes do commit, impedindo que tarefas "atropeladas" ou mal documentadas entrem na base de código.

## Related
*   [[harness_architecture]] (Architecture Fitness Harness)
*   [[ralph_wiggum_loop]]
*   [[karpathy_protocol]] (Governança Epistemológica)
