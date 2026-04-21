---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-21
Status: Ativo
---

# 🗺️ ROADMAP: Fases do Autobuilder
> 🤖 [SYSTEM HOOK] Siga esta ordem. Não pule fases.

| Fase | Nome | Gatilho de Início | Critério de Saída |
|------|------|-------------------|-------------------|
| **1** | Discovery | `INCEPTION.md` ativo + `npm run context:enrich` | `PRD.md` lastreado + `market/` ok |
| **2** | Contratos/DB | `schema.sql` criado + `qa_signoff` | Harness passa + Migrations 001 applied |
| **3** | Features/WIKI | `.specs/` criadas + `lint_wiki.py --strict` | `STATE.md: ✅ PASSED` em todas specs |
| **4** | Scale/Deploy | CI/CD green + `npm run context:cleanup` | `VERSION.md` bumped + Tag release |
