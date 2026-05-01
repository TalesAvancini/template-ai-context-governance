# CHECKLIST Sprint-Based (Execucao)

## A. Bootstrap
- [ ] Pasta da feature criada em `.specs/features/[feature_id]/`
- [ ] `spec.md`, `tasks.md`, `STATE.md`, `design.md` criados
- [ ] `contract_mode: sprint_based` definido
- [ ] `current_sprint: sprint_01` definido
- [ ] Bloco `sprints.sprint_01` presente
- [ ] `type: standard` ausente

## B. Rito de Inicio
- [ ] `git status --short` sem saida
- [ ] `start_hash` registrado no `STATE.md`
- [ ] `captured_at` e `captured_by` preenchidos
- [ ] baseline registrado no `JOURNAL.md`

## C. Escopo
- [ ] `scope_allow` da sprint atual definido
- [ ] `scope_deny` definido quando necessario
- [ ] sem alteracoes fora do escopo

## D. Pre-close Self-Audit
- [ ] `spec.md`, `tasks.md`, `STATE.md` coerentes
- [ ] criterios de aceite atualizados
- [ ] se tasks da sprint atual estao concluidas, `acceptance` no `spec.md` esta marcado (`[x]`)
- [ ] evidencia no `JOURNAL.md` ou `HARNESS_LOG.md`
- [ ] validacao executada (`context:validate` ou equivalente)

## E. Fechamento
- [ ] `qa_signoff: true` na sprint atual
- [ ] harness PASS
- [ ] arvore Git limpa
- [ ] nenhum conflito entre narrativa e estado
- [ ] metadados de `RULES.md` e `MASTER_FLOW.md` atualizados

Se qualquer item falhar, manter status `IN_PROGRESS`.
