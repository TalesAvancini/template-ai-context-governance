---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
type: standard
executor_context_id: "CTX_TESTE_EXE_0428"
validator_context_id: "CTX_TESTE_VAL_0428"
impact_control:
  max_impact_radius: 2
  pre_flight_grep_terms: ["teste.py"]
definition_of_done:
  - [x] Criar arquivo `scripts/teste.py`.
  - [x] O script deve imprimir exatamente `1+1=2`.
qa_signoff: true
signed_by: "@qa-validator"
---

# 📄 Spec: Teste de Handoff Multi-Agent

## 🎯 Objetivo
Provar que o handoff mecânico entre o Hub (Planner) e os subagentes isolados em `.agent/subagents/` funciona via trigger do Host, sem misturar memória de contexto.

## ⚠️ Pre-Flight Gate
1. Verifique se existe algo que quebre (não deve existir).
2. O `max_impact_radius` é 2 (seguro).

## 🔨 Escopo de Execução
- Crie a pasta `scripts/` se não existir.
- Crie o arquivo `scripts/teste.py`.
- Escreva a lógica: `print("1+1=2")`.
