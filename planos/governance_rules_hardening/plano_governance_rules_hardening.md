---
version: V5
status: READY_FOR_SPEC_BOOTSTRAP
topic: Governance Rules Hardening
date: 2026-04-30
owner: @spec-driver
auditor: @qa-validator + Codex
source:
  - _flash_report/_flash_report.md
  - .context/brain/RULES.md
  - .context/brain/MASTER_FLOW.md
  - .context/monitoring/PROJECT_INDEX.md
---

# Plano: Governance Rules Hardening (v5 - Arquiteto Rigoroso)

## 1) Objetivo e Diagnóstico

Transformar aprendizados do pós-missão em governança executável end-to-end, eliminando reincidência de:
- falso fechamento de onda com working tree suja;
- regressão estrutural em `STATE.md`;
- divergência narrativa/real (`spec`/`tasks`/`STATE`/Git);
- fraude narrativa no SAM;
- desalinhamento entre regra documental e enforcement automatizado.

**Lacunas Críticas:** ausência de regra hardened nos papéis, falta de `start_hash` atômico, telemetria sem taxonomia de fricção.

---

## 2) Protocolo de Ignição: Rito de Início (Obrigatório)

Este rito deve ser executado **antes** de qualquer alteração de conteúdo. O descumprimento bloqueia a Sprint 01.

### 2.1 Baseline de Arranque (Ponto Zero)
- registrar `start_hash`, `captured_at`, `captured_by` no `STATE.md`;
- validar `git status --short` vazio;
- se houver sujeira, o status da missão é `BLOCKED`.

### 2.2 Escopo Travado (Anti-Blowout)
- Sprint 01 toca apenas: `RULES.md`, `MASTER_FLOW.md` e diretório da feature `.specs/features/governance_rules_hardening/`.

### 2.3 Rito de Re-sincronização (Ralph Wiggum Check)
- leitura forçada de `RULES`, `MASTER_FLOW`, `spec`, `tasks`, `STATE` em caso de deriva.
- registro do re-sync no `JOURNAL.md`.

---

## 3) Bootstrap da Feature Spec

Criar estrutura em `.specs/features/governance_rules_hardening/`:
- `spec.md` (contract_mode: sprint_based)
- `tasks.md`
- `STATE.md`

---

## 4) Sprints de Implementação (A Esteira)

### Sprint 01 — Regras Canônicas & Self-Audit
- inserir `CLOSE_WAVE` + `ANTI_FALSE_PASS` em `RULES.md`;
- inserir `Pre-Close Audit` em `MASTER_FLOW.md`;
- **Inovação:** adicionar passo **Pre-close Self-Audit** no workflow do `spec-driver`.
- **Exemplos PASS/FAIL:** incluir no `RULES.md` cenários binários para evitar interpretação.

### Sprint 02 — Integridade SSOT & Scripts Críticos
- formalizar `MIMO_STATE_INTEGRITY` e `CRITICAL_SCRIPT_SANITY` no `RULES.md`.
- política de edição cirúrgica obrigatória.

### Sprint 03 — Runbook & Métricas Operacionais
- inserir checklist anti-reincidência no `MASTER_FLOW.md`.
- definir métricas mínimas por onda (HG/SG/hotfix).

### Sprint 04 — Sincronização Institucional
- atualizar `HARNESS_REGISTRY.md`, `SCRIPT_GLOSSARY.md`, `FILE_GLOSSARY.md`, `PROMPT_LIBRARY.md`.

### Sprint 05 — Enforcement Automático (Músculos)
- implementar validação automática em `validate_context.py` ou `test_context.py`.
- foco em detectar árvore suja e estado incoerente.

### Sprint 06 — Hardening de Agenciamento (Nervos)
- atualizar papéis `spec-driver` e `qa-validator` com protocolo de `Hardened Closing`.
- transição atômica para `IN_PROGRESS` via código.

### Sprint 07 — Hardening SAM & Telemetria
- detecção de fraude narrativa no `workflow_journal_auditor.py`.
- implantação do schema de telemetria `[GOVERNANCE-FRICTION]`.
- atualização do `AGENT_REGISTRY.md`.

### Sprint 08 — Visão: RX Communications
- criar `.context/maintenance/rx-communications.md` (SSOT de conectividade).
- referenciar explicitamente no `MASTER_FLOW.md` e `FILE_GLOSSARY.md`.

---

## 5) Definition of Done (Feature)

A feature só sela quando:
- Todas as 5 regras novas estão no `RULES.md`.
- Rito `Pre-Close Audit` está no `MASTER_FLOW.md`.
- `rx-communications.md` está ativo e referenciado.
- SAM bloqueia fraude narrativa (Journal concluído + Signoff false).
- Telemetria `[GOVERNANCE-FRICTION]` é emitida em bloqueios.
- `STATE.md` em `PASSED` com evidência quantitativa.
- Árvore Git limpa no fechamento.

---

## 6) Plano de Testes (Validação Binária)

1. fechar onda com árvore suja -> FAIL.
2. transição `IN_PROGRESS` sem `start_hash` -> FAIL.
3. claim de conclusão sem `qa_signoff` no SAM -> FAIL.
4. editar `STATE.md` preservando campos MiMo -> PASS.
5. RX Communications ausente ou sem ref-cruzada -> FAIL.

---

## 7) Veredito do Arquiteto

Plano consolidado com ordem lógica de execução, ritos de entrada blindados e prevenção explícita de deriva cognitiva. Pronto para execução assistida.

---
*Atualizado em: 2026-04-30 20:30 (BRT)*
rio de aceite do Rito de Início:
- PASS: os quatro itens acima registrados com evidência.
- FAIL: ausência de qualquer item bloqueia início de implementação.

---

## 14) Veredito

Plano pronto para abrir a feature spec `governance_rules_hardening` com cobertura completa de norma, agenciamento hardened, enforcement automático, telemetria de fricção e prevenção ativa de fraude narrativa.

---
*Atualizado em: 2026-04-30 20:22 (BRT)*
