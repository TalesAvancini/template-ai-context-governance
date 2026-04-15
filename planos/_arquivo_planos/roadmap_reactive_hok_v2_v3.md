# 🗺️ Roadmap de Governança Reativa (Fases 2 e 3) - Antigravity Kit v2.2
**Data de Criação:** 2026-04-11
**Status:** Planejamento Aprovado / Pronto para Execução

Este plano estratégico detalha a transformação do Antigravity Kit de um sistema de validação passivo para um **Sistema Nervoso Autônomo**, focado em dashboards dinâmicos e inteligência proativa.

---

## 📊 Fase 2: Health Sync & Dashboard Vivo
*Transformação do CONTEXT_HEALTH.md em um monitor de "pulso" em tempo real.*

### Objetivos:
1. **Dinamização do Health Check:** Scripts Python atualizarão automaticamente as métricas de saúde (linhas do log, status do harness, token estimation).
2. **Tratamento de Exit 2 (Oracle):** O orquestrador `run_context.py` interceptará baixas confianças do Oráculo para forçar intervenção humana via `[oracle:uncertain]`.

### Entregáveis:
- [ ] Integração de marcadores HTML/RegEx no `CONTEXT_HEALTH.md`.
- [ ] Patch no `run_context.py` para sincronização de métricas pós-validação.
- [ ] Refinamento da lógica de fallback no Orquestrador.

---

## 🔍 Fase 3: Oracle Routing & Karpathy Strict Mode
*Evolução da inteligência semântica e fiscalização rigorosa de fontes.*

### Objetivos:
1. **Auto-Sugestão Karpathy:** Se um claim técnico falhar no lint, o motor buscará automaticamente em `raw_inbox/` uma fonte provável e sugerirá a citação.
2. **Strict Mode:** Bloqueio total de commits se houver claims sem lastro (pós-período de carência de Fase 1).

### Entregáveis:
- [ ] Refactor no `lint_wiki.py` para inclusão do parâmetro `--strict`.
- [ ] Ponte entre `context_oracle.py` e `lint_wiki.py` para busca de fontes sugeridas.

---

## 📈 Critérios de Sucesso
- `npm run context:all` gera atualização visual imediata no Dash de saúde.
- Redução de zero alucinações técnicas em specs através de pausas obrigatórias (Exit 2).
- Bibliografia do projeto 100% rastreável até a pasta `raw/`.

---
> [!IMPORTANT]
> **Governança:** "O contexto não é lido, ele é respirado pela automação."
