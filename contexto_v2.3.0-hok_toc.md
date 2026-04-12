# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-12T03:21:39.890203+00:00
root: template_inicío_de_projeto
mode: full | TOC
profile: ai-default
file_count: 54
byte_count: 164505
ignored_dirs:
  - .cache
  - .cursor
  - .git
  - .idea
  - .mypy_cache
  - .netlify
  - .next
  - .nuxt
  - .pytest_cache
  - .ruff_cache
  - .tox
  - .venv
  - .vercel
  - .vite
  - .vscode
  - __pycache__
  - bin
  - build
  - captura_projeto
  - coverage
  - dist
  - node_modules
  - obj
  - out
  - target
  - venv
sensitive_rules:
  - *.cert
  - *.key
  - *.p12
  - *.pem
  - *.pfx
  - .env*
  - credentials*.json
  - id_rsa*
  - secrets.*
---

## INDEX_BY_DOMAIN
- `config`:
  - `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
  - `package-lock.json` -> [file_fa288d1472d2](#file_fa288d1472d2)
  - `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `db`:
  - `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `docs`:
  - `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
  - `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
  - `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
  - `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
  - `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
  - `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
  - `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
  - `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
  - `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
  - `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
  - `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
  - `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
  - `.context/maintenance/_archive_context/raw/stripe_docs.md` -> [file_eaebfc593089](#file_eaebfc593089)
  - `.context/maintenance/_archive_context/raw/template_inbox.md` -> [file_618e9f7de1e8](#file_618e9f7de1e8)
  - `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
  - `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
  - `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
  - `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
  - `.specs/features/hok-advanced-modules/STATE.md` -> [file_3c39185314df](#file_3c39185314df)
  - `.specs/features/hok-advanced-modules/spec.md` -> [file_8746e653f22c](#file_8746e653f22c)
  - `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
  - `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
  - `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
  - `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
  - `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
  - `contexto.md` -> [file_aa78525fb574](#file_aa78525fb574)
  - `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
  - `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
  - `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
  - `planos/plan_hok_advanced_security_and_db.md` -> [file_7bd2d6af54a4](#file_7bd2d6af54a4)
  - `planos/roadmap_reactive_hok_v2_v3.md` -> [file_44c34e6237da](#file_44c34e6237da)
  - `planos/walkthrough_hok_triad.md` -> [file_6a4bd0586b20](#file_6a4bd0586b20)
- `source`:
  - `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
  - `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
  - `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
  - `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
  - `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
  - `.context/_scripts/lint_wiki.py` -> [file_ab41b07fb3fb](#file_ab41b07fb3fb)
  - `.context/_scripts/migration_registry.py` -> [file_d65b48a9d56c](#file_d65b48a9d56c)
  - `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
  - `.context/_scripts/secrets_scanner.py` -> [file_e98b95e5fb6d](#file_e98b95e5fb6d)
  - `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
  - `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
  - `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
  - `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
  - `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
  - `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
  - `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
  - `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
  - `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

## INDEX_BY_PATH
- `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
- `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
- `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
- `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
- `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
- `.context/_scripts/lint_wiki.py` -> [file_ab41b07fb3fb](#file_ab41b07fb3fb)
- `.context/_scripts/migration_registry.py` -> [file_d65b48a9d56c](#file_d65b48a9d56c)
- `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
- `.context/_scripts/secrets_scanner.py` -> [file_e98b95e5fb6d](#file_e98b95e5fb6d)
- `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
- `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
- `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
- `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
- `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
- `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
- `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
- `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
- `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
- `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
- `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
- `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
- `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
- `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
- `.context/maintenance/_archive_context/raw/stripe_docs.md` -> [file_eaebfc593089](#file_eaebfc593089)
- `.context/maintenance/_archive_context/raw/template_inbox.md` -> [file_618e9f7de1e8](#file_618e9f7de1e8)
- `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
- `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
- `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
- `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
- `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
- `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
- `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
- `.specs/features/hok-advanced-modules/STATE.md` -> [file_3c39185314df](#file_3c39185314df)
- `.specs/features/hok-advanced-modules/spec.md` -> [file_8746e653f22c](#file_8746e653f22c)
- `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
- `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
- `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
- `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
- `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
- `contexto.md` -> [file_aa78525fb574](#file_aa78525fb574)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package-lock.json` -> [file_fa288d1472d2](#file_fa288d1472d2)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
- `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
- `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
- `planos/plan_hok_advanced_security_and_db.md` -> [file_7bd2d6af54a4](#file_7bd2d6af54a4)
- `planos/roadmap_reactive_hok_v2_v3.md` -> [file_44c34e6237da](#file_44c34e6237da)
- `planos/walkthrough_hok_triad.md` -> [file_6a4bd0586b20](#file_6a4bd0586b20)
- `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

---
<a id="file_dbef1acce0d4"></a>
FILE_START id=file_dbef1acce0d4 path=.context/_scripts/_tz_utils.py domain=source lang=python lines=37 bytes=1257 mtime=2026-04-12T02:47:25.198957+00:00 sha1=a49568f45d4b962ab01f0ed4b359ee4c09f65741
CONTENT_OMITTED toc_only=true
FILE_END id=file_dbef1acce0d4

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CONTENT_OMITTED toc_only=true
FILE_END id=file_82cd6bde54ff

---
<a id="file_10081abf87e1"></a>
FILE_START id=file_10081abf87e1 path=.context/_scripts/context_oracle.py domain=source lang=python lines=69 bytes=2393 mtime=2026-04-11T23:58:41.287250+00:00 sha1=461ad9521982d5934769db35c938e5956f50a552
CONTENT_OMITTED toc_only=true
FILE_END id=file_10081abf87e1

---
<a id="file_1edef35c2f56"></a>
FILE_START id=file_1edef35c2f56 path=.context/_scripts/harness_runner.py domain=source lang=python lines=105 bytes=4438 mtime=2026-04-12T02:49:38.135700+00:00 sha1=4017d9da1bb2ca25a73a2cd4afb6717f80eae977
CONTENT_OMITTED toc_only=true
FILE_END id=file_1edef35c2f56

---
<a id="file_a642d240b9ab"></a>
FILE_START id=file_a642d240b9ab path=.context/_scripts/health_sync.py domain=source lang=python lines=103 bytes=3798 mtime=2026-04-12T02:49:21.674220+00:00 sha1=e49da12ab25915331abf008d7edd5b95f86fdca0
CONTENT_OMITTED toc_only=true
FILE_END id=file_a642d240b9ab

---
<a id="file_ab41b07fb3fb"></a>
FILE_START id=file_ab41b07fb3fb path=.context/_scripts/lint_wiki.py domain=source lang=python lines=97 bytes=4141 mtime=2026-04-12T00:24:32.722433+00:00 sha1=24366d0cb8d5600c06dbb9d9a7e8d0f89470a576
CONTENT_OMITTED toc_only=true
FILE_END id=file_ab41b07fb3fb

---
<a id="file_d65b48a9d56c"></a>
FILE_START id=file_d65b48a9d56c path=.context/_scripts/migration_registry.py domain=source lang=python lines=44 bytes=1700 mtime=2026-04-12T02:18:47.875961+00:00 sha1=a1e9beb894aba2b44931e9c41522a020b7359ebf
CONTENT_OMITTED toc_only=true
FILE_END id=file_d65b48a9d56c

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=82 bytes=2761 mtime=2026-04-12T02:48:42.689091+00:00 sha1=8b12ecb77b7b91c035a2d7c9752910c71064d1e5
CONTENT_OMITTED toc_only=true
FILE_END id=file_024b28a37d29

---
<a id="file_e98b95e5fb6d"></a>
FILE_START id=file_e98b95e5fb6d path=.context/_scripts/secrets_scanner.py domain=source lang=python lines=61 bytes=2458 mtime=2026-04-12T02:17:08.346225+00:00 sha1=f89861127275e414260a7690cd4e9bd42bee50ba
CONTENT_OMITTED toc_only=true
FILE_END id=file_e98b95e5fb6d

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=102 bytes=3426 mtime=2026-04-12T02:48:59.755191+00:00 sha1=d2b0f3541ccaab8c75f381f47d539c762618a0b7
CONTENT_OMITTED toc_only=true
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=106 bytes=3827 mtime=2026-04-11T02:29:28.743870+00:00 sha1=e6e9a29604fb4a340a2335bbca07488c56baff2a
CONTENT_OMITTED toc_only=true
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=97 bytes=7180 mtime=2026-04-11T02:28:38.100881+00:00 sha1=3232fd65b8b05382d366aa1a8890e6385eb7f705
CONTENT_OMITTED toc_only=true
FILE_END id=file_e7c17acb71ff

---
<a id="file_4b29e274836e"></a>
FILE_START id=file_4b29e274836e path=.context/brain/HARNESS_REGISTRY.md domain=docs lang=markdown lines=20 bytes=1180 mtime=2026-04-11T23:46:58.142679+00:00 sha1=5a29edb2d353e3117e7e904191ef4dadfd322309
CONTENT_OMITTED toc_only=true
FILE_END id=file_4b29e274836e

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=86 bytes=4370 mtime=2026-04-11T02:59:02.297440+00:00 sha1=06ce6786a149620314b57f8231142f652d4fc412
CONTENT_OMITTED toc_only=true
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=67 bytes=2446 mtime=2026-04-11T01:31:37.755946+00:00 sha1=b5c06bc8a67d2a788cc8263f03971f379d04e92e
CONTENT_OMITTED toc_only=true
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=154 bytes=6687 mtime=2026-04-11T02:28:52.575335+00:00 sha1=aa3419c1efa08687a7c551dc44f40b504b422353
CONTENT_OMITTED toc_only=true
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.772397+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CONTENT_OMITTED toc_only=true
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=82 bytes=5460 mtime=2026-04-12T00:33:15.586634+00:00 sha1=270b5c863f91b42f2ef229b18bd87218d95aee53
CONTENT_OMITTED toc_only=true
FILE_END id=file_cd6526d17218

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CONTENT_OMITTED toc_only=true
FILE_END id=file_450d7ec70909

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.800876+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CONTENT_OMITTED toc_only=true
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=69 bytes=2335 mtime=2026-04-12T02:53:33.658657+00:00 sha1=4ec7bccab619b92952bef272d9518e7176fb041b
CONTENT_OMITTED toc_only=true
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=30 bytes=303 mtime=2026-04-12T02:53:33.221751+00:00 sha1=9c19bd0ca0e1f3cd18a7b36ebcccdce4f1aa0b63
CONTENT_OMITTED toc_only=true
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.794384+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CONTENT_OMITTED toc_only=true
FILE_END id=file_0858a02cf53f

---
<a id="file_eaebfc593089"></a>
FILE_START id=file_eaebfc593089 path=.context/maintenance/_archive_context/raw/stripe_docs.md domain=docs lang=markdown lines=4 bytes=184 mtime=2026-04-12T00:21:42.178827+00:00 sha1=a8ca349e81fe936c2d0c8e39de0d94e9f16ae2eb
CONTENT_OMITTED toc_only=true
FILE_END id=file_eaebfc593089

---
<a id="file_618e9f7de1e8"></a>
FILE_START id=file_618e9f7de1e8 path=.context/maintenance/_archive_context/raw/template_inbox.md domain=docs lang=markdown lines=17 bytes=585 mtime=2026-04-12T00:21:32.947043+00:00 sha1=e7906c232c8df4de3d7839e53291826495d57cd8
CONTENT_OMITTED toc_only=true
FILE_END id=file_618e9f7de1e8

---
<a id="file_3707c3aa3239"></a>
FILE_START id=file_3707c3aa3239 path=.context/maintenance/migrations/001_init.sql domain=db lang=sql lines=12 bytes=450 mtime=2026-04-12T02:14:15.429255+00:00 sha1=a4e5465634cd084041656f59f9093be09f5a8fc9
CONTENT_OMITTED toc_only=true
FILE_END id=file_3707c3aa3239

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CONTENT_OMITTED toc_only=true
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=27 bytes=1336 mtime=2026-04-11T02:26:43.636538+00:00 sha1=adb37745498ccfa61a2b793c10240a2b20d3d716
CONTENT_OMITTED toc_only=true
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.789386+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CONTENT_OMITTED toc_only=true
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CONTENT_OMITTED toc_only=true
FILE_END id=file_91d5627a725e

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=37 bytes=1443 mtime=2026-04-12T02:53:34.069247+00:00 sha1=75e9b4255496301209862ce709a568a4b1a4770d
CONTENT_OMITTED toc_only=true
FILE_END id=file_068a21d64bec

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=26 bytes=693 mtime=2026-04-11T00:55:20.246274+00:00 sha1=163dd12b4c98d348f80986ea59afcb4604dc9e0e
CONTENT_OMITTED toc_only=true
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CONTENT_OMITTED toc_only=true
FILE_END id=file_3adfd36c1559

---
<a id="file_3c39185314df"></a>
FILE_START id=file_3c39185314df path=.specs/features/hok-advanced-modules/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-12T02:53:33.661113+00:00 sha1=8628e643ca9dec24a77017bd390e043c561ee427
CONTENT_OMITTED toc_only=true
FILE_END id=file_3c39185314df

---
<a id="file_8746e653f22c"></a>
FILE_START id=file_8746e653f22c path=.specs/features/hok-advanced-modules/spec.md domain=docs lang=markdown lines=24 bytes=1573 mtime=2026-04-12T02:10:32.710904+00:00 sha1=4afa0f114364110370467d1033c99a6a49058746
CONTENT_OMITTED toc_only=true
FILE_END id=file_8746e653f22c

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=92 bytes=4017 mtime=2026-04-12T02:50:09.095504+00:00 sha1=8dd17ddb4907fab2890fd5706df07610aeb55c24
CONTENT_OMITTED toc_only=true
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=123 bytes=5644 mtime=2026-04-12T02:50:25.829553+00:00 sha1=712d7adc5114926d1dec5ba37d7ff87141ef0b7b
CONTENT_OMITTED toc_only=true
FILE_END id=file_4efb6293109d

---
<a id="file_19e76e009f38"></a>
FILE_START id=file_19e76e009f38 path=TEMPLATE_MIGRATION.md domain=docs lang=markdown lines=59 bytes=1926 mtime=2026-04-12T03:07:09.407660+00:00 sha1=20f937b7b3cfaf5e0b5beb46c68112ca84ce7d5e
CONTENT_OMITTED toc_only=true
FILE_END id=file_19e76e009f38

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=11 bytes=416 mtime=2026-04-12T00:57:24.540624+00:00 sha1=9ddd807983a0b3be0e492db5fb2a29f9bfe014f8
CONTENT_OMITTED toc_only=true
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CONTENT_OMITTED toc_only=true
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=399 bytes=16353 mtime=2026-04-12T03:17:11.664666+00:00 sha1=8a148e7ad8f5ce1f7855b502617105b6247112e3
CONTENT_OMITTED toc_only=true
FILE_END id=file_c3916196f58f

---
<a id="file_aa78525fb574"></a>
FILE_START id=file_aa78525fb574 path=contexto.md domain=docs lang=markdown lines=480 bytes=24728 mtime=2026-04-12T03:14:11.257218+00:00 sha1=89ec80e48f9bdd9fa7d52508825c16a5edbaa9a3
CONTENT_OMITTED toc_only=true
FILE_END id=file_aa78525fb574

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=155 bytes=5469 mtime=2026-04-11T02:29:46.289656+00:00 sha1=18e30807c6ef1ce94e3619f19f8ec2bd93f77c52
CONTENT_OMITTED toc_only=true
FILE_END id=file_c59135753d26

---
<a id="file_fa288d1472d2"></a>
FILE_START id=file_fa288d1472d2 path=package-lock.json domain=config lang=json lines=32 bytes=785 mtime=2026-04-11T01:12:03.334672+00:00 sha1=e8450c2eeca43eabd30597b19a6cb24ad70fcddb
CONTENT_OMITTED toc_only=true
FILE_END id=file_fa288d1472d2

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=33 bytes=1178 mtime=2026-04-12T02:15:21.293639+00:00 sha1=ccfed0b4b64de88e6d54ceec22c07086f30f140a
CONTENT_OMITTED toc_only=true
FILE_END id=file_7030d0b2f71b

---
<a id="file_a9422a4b7476"></a>
FILE_START id=file_a9422a4b7476 path=planos/implementation_plan.md domain=docs lang=markdown lines=77 bytes=3338 mtime=2026-04-10T23:15:28.184032+00:00 sha1=37ad3605aae584ee4398621d92edd7b76058413e
CONTENT_OMITTED toc_only=true
FILE_END id=file_a9422a4b7476

---
<a id="file_32db3e3783df"></a>
FILE_START id=file_32db3e3783df path=planos/master_plan.md domain=docs lang=markdown lines=88 bytes=3620 mtime=2026-04-10T23:48:33.652301+00:00 sha1=9269f2e75a4300b61121c540eb8c3e57ba44329f
CONTENT_OMITTED toc_only=true
FILE_END id=file_32db3e3783df

---
<a id="file_2a788cb45159"></a>
FILE_START id=file_2a788cb45159 path=planos/multi_agent_plan.md domain=docs lang=markdown lines=62 bytes=2824 mtime=2026-04-10T23:32:27.825062+00:00 sha1=71ea8355ff980c67c66959bec1e4782108bad081
CONTENT_OMITTED toc_only=true
FILE_END id=file_2a788cb45159

---
<a id="file_7bd2d6af54a4"></a>
FILE_START id=file_7bd2d6af54a4 path=planos/plan_hok_advanced_security_and_db.md domain=docs lang=markdown lines=54 bytes=2567 mtime=2026-04-12T01:55:31.645679+00:00 sha1=cf3305760cc94cf4ce1e359641fe889b16696354
CONTENT_OMITTED toc_only=true
FILE_END id=file_7bd2d6af54a4

---
<a id="file_44c34e6237da"></a>
FILE_START id=file_44c34e6237da path=planos/roadmap_reactive_hok_v2_v3.md domain=docs lang=markdown lines=43 bytes=2070 mtime=2026-04-12T00:16:01.408542+00:00 sha1=bcab4c7525fa8c4ba078bf84d63965f3e60d3e23
CONTENT_OMITTED toc_only=true
FILE_END id=file_44c34e6237da

---
<a id="file_6a4bd0586b20"></a>
FILE_START id=file_6a4bd0586b20 path=planos/walkthrough_hok_triad.md domain=docs lang=markdown lines=32 bytes=2243 mtime=2026-04-12T00:05:31.404227+00:00 sha1=0bbfa5d700f335f10599d185d0fa8e788cf93cac
CONTENT_OMITTED toc_only=true
FILE_END id=file_6a4bd0586b20

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=70 bytes=2796 mtime=2026-04-12T02:17:34.844708+00:00 sha1=9186d63c21dc716dfb7f4fc04a3375f0fc081f46
CONTENT_OMITTED toc_only=true
FILE_END id=file_350a79f8b829

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=38 bytes=1386 mtime=2026-04-11T02:57:36.569915+00:00 sha1=e6604f22108387e02990d6bc08fc703d62cb82f6
CONTENT_OMITTED toc_only=true
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=89 bytes=3753 mtime=2026-04-11T01:08:20.157384+00:00 sha1=7179930319fcc060058fbd50dcb63770bc05bc28
CONTENT_OMITTED toc_only=true
FILE_END id=file_4c6bbd05056e
