---
id: HARNESS_BEHAVIOR
type: concept
tags: [harness-engineering, governanca, testes, qa, leniency-bias]
aliases: [Behaviour Harness, Harness de Comportamento, Contratos de Sprint]
concept: Validação de Intenção e Cura do Viés de Leniência
entity: Antigravity Framework
source: market/RAW/harness_engineering_manifesto.md
last_updated: 2026-04-23
---

# Behaviour Harness (Harness de Comportamento)

> Fonte: market/RAW/harness_engineering_manifesto.md

O **Behaviour Harness** (Harness de Comportamento) é o pilar mais complexo e desafiador da *Harness Engineering*. Como define Martin Fowler, ele é o "elefante na sala": o foco aqui é garantir e sentir se a aplicação funcionalmente se comporta da maneira que precisa ser feita sob a perspectiva do negócio e do usuário. 

Enquanto linters de código garantem a sintaxe (Manutenibilidade) e validadores de banco garantem as fronteiras (Arquitetura), o Harness de Comportamento lida com a **intenção**. Ele existe para curar uma patologia estrutural profunda nas IAs chamada **Viés de Leniência** (*Leniency Bias*): a incapacidade crônica que agentes de IA possuem de avaliar rigorosamente o próprio trabalho, tendendo a aprovar e elogiar saídas medíocres com extrema confiança.

## Key Takeaways
*   **A Cura para o Leniency Bias:** A única forma de garantir o comportamento funcional autônomo é **separar o agente que constrói do agente que julga**.
*   **Controles Preventivos (Feedforward):** Especificações funcionais rigorosas e Contratos de Sprint definidos *antes* da execução.
*   **Controles Reativos (Feedback):** Testes E2E (End-to-End) automatizados, verificações binárias e agentes de QA agindo como usuários reais.

### 🏢 Exemplos Práticos na Indústria (Como as Big Techs fazem)

*   **O "Avaliador Implacável" da Anthropic:** Arquitetura de três agentes (*Planner*, *Generator*, *Evaluator*). O Avaliador usa ferramentas como Playwright para testar a aplicação como um humano, injetando erros mecânicos de volta no contexto do Gerador.
*   **Negociação de Contratos (Handshake):** Antes da escrita do código, os agentes negociam o que significa estar "pronto". O sucesso é verificado contra uma lista determinística, eliminando julgamentos subjetivos.

### ⚙️ Integração no Antigravity Kit (H.O.K. v2.5.2)

No framework v2.5.2, o **Behaviour Harness** é ativado pela mecânica imutável da pasta `.specs/` e fiscalizado pelo seu pipeline de segurança:

1. **A Regra de Papéis (`RULES.md` v2.5.2):** O sistema exige a separação entre o `Maker` (Executor) e o `Checker` (Validator). Se os IDs de contexto forem iguais em uma spec `standard`, o harness bloqueia o avanço.
2. **O Aperto de Mão Determinístico:** A intenção vira um documento obrigatório na spec. O gerador deve listar deterministicamente como o sucesso será verificado e o avaliador deve assinar isso via `qa_signoff: true`.
3. **Backpressure via `harness_runner.py`:** O script validador bloqueia qualquer tentativa de merge no `STATE.md` se o contrato não estiver formalmente assinado e as evidências (logs/testes) não estiverem presentes.

## Related
* [[harness_maintainability]] (Maintainability Harness)
* [[harness_architecture]] (Architecture Fitness Harness)
* [[sprint_contracts]] (A mecânica do Acordo de Qualidade)
* [[leniency_bias]] (A Patologia do Auto-Adulador)
