---
id: SPRINT_CONTRACTS_RESEARCH
type: literature
domain: market/research
---

# 🧠 Pesquisa: Contratos de Sprint e Leniency Bias em Sessões de LLM

## 1. Resumo Tático: A Filosofia dos Contratos de Sprint

**O Problema (Leniency Bias):** 
Em sistemas de múltiplos agentes ou loops contínuos, agentes de IA sofrem de "viés de autoavaliação" (*self-evaluation bias* ou *leniency bias*). Eles tendem a elogiar e aprovar o próprio código de forma confiante, mesmo quando a qualidade é medíocre. Além disso, se o agente que testa (QA) não tiver um limite estrito, ele começará a sugerir adições fora do escopo original, gerando loops infinitos de refatoração para o gerador.

**A Solução (O Contrato e o Backpressure):** 
A solução estrutural é forçar a aprovação prévia do "Definition of Done". O agente Gerador propõe a lista de tarefas (*o que será feito e como verificar*), e o agente Avaliador revisa a lista para confirmar conformidade plena e exclusiva em relação à Spec original. 
Só após o "Handshake", ocorre a **Execução Isolada** e depois o **QA Mecânico** baseado nestes critérios firmados.

## 2. Excertos Brutos e Evidências da Literatura (Citação Obrigatória)

**Sobre o Viés de Leniência (Leniency Bias):**
> "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work—even when, to a human observer, the quality is obviously mediocre."
> "Agents are structurally poor at grading their own work, reliably praising mediocre outputs on subjective tasks. The evaluation landscape is warped by the generation process itself."

**Sobre Contratos de Sprint e Workflow Generativo:**
> "Before each sprint, the generator and evaluator negotiated a sprint contract: agreeing on what "done" looked like for that chunk of work before any code was written."
> "The generator proposed what it would build and how success would be verified, and the evaluator reviewed that proposal to make sure the generator was building the right thing. The two iterated until they agreed."
> "...é um contrato entre o agente que desenvolve e o agente que testa [...] no momento de planejamento quando um sprint vai começar o agente que vai desenvolver cria uma lista de coisas que ele vai fazer o agente que vai avaliar ele olha para essa lista e diz: "Essa lista tá batendo com a spec""

**Sobre Backpressure Mecânico Binário:**
> "Backpressure is the mechanical verification that rejects bad work. Name the actual commands— bun test , npm run typecheck , eslint . —and instruct the agent to run them after every change."
> "The agent needs *something* that can tell it “no, that's wrong” without requiring human judgment."
