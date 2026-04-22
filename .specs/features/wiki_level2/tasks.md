# Tasks: Wiki Level 2

Rifa de tarefas atômicas para implementação do paradigma Karpathy Wiki.

---

## [Phase 1] Foundation & Logs
- [x] **TASK-01**: Criar arquivos base da Wiki.
  - Criar `.context/market/WIKI/_index.md` (root index).
  - Criar `.context/market/wiki_log.md` (append-only log).
  - *Verify*: `ls .context/market/WIKI/_index.md`
- [x] **TASK-02**: Atualizar documentação de governança.
  - Injetar fluxo INGEST -> LINT -> LOG em `RULES.md` e `MASTER_FLOW.md`.
  - *Verify*: Check manual dos arquivos.

## [Phase 2] Oracle Cascade
- [x] **TASK-03**: Patch cirúrgico em `context_oracle.py`.
  - Injetar lógica de busca SSOT -> Index -> Lexical.
  - *Verify*: `python .context/_scripts/context_oracle.py "test"` deve retornar fallback (exit 2).

## [Phase 3] Guard & Lint
- [ ] **TASK-04**: Implementar `ingest_wiki_guard.py`.
  - Validação de schema (Frontmatter, Fonte, Takeaways).
  - *Verify*: Rodar contra um mock inválido e esperar falha.
- [ ] **TASK-05**: Atualizar `lint_wiki.py` para modo `--strict`.
  - Bloqueio de artigos sem meta-dados Karpathy.
  - *Verify*: `python .context/_scripts/lint_wiki.py --strict`
- [ ] **TASK-06**: Integrar no pipeline Central.
  - Atualizar `run_context.py` e `package.json` com novos comandos.
  - *Verify*: `npm run context:all` verde.

## [Phase 4] Health Check
- [ ] **TASK-07**: Patch em `validate_context.py`.
  - Injetar `check_wiki_integrity()`.
  - *Verify*: `npm run context:wiki-health`
