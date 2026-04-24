# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-23T18:33:23.046365+00:00
root: template_inicío_de_projeto
mode: full | TOC
profile: ai-default
file_count: 74
byte_count: 230293
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
  - RAW
  - __pycache__
  - _archive_context
  - bin
  - build
  - captura_projeto
  - coverage
  - dist
  - node_modules
  - obj
  - out
  - planos
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
  - `.context/maintenance/version_targets.json` -> [file_51ed93c9d8ab](#file_51ed93c9d8ab)
  - `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
  - `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `db`:
  - `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `docs`:
  - ` .specs/features/docs_resenha/STATE.md` -> [file_f6a9dd4e6c97](#file_f6a9dd4e6c97)
  - ` .specs/features/docs_resenha/spec.md` -> [file_736dc30bc94f](#file_736dc30bc94f)
  - ` .specs/features/hardening_v2.5/STATE.md` -> [file_5f4ef6860006](#file_5f4ef6860006)
  - ` .specs/features/hardening_v2.5/spec.md` -> [file_f941f64c38fb](#file_f941f64c38fb)
  - ` .specs/features/sync_maintenance/STATE.md` -> [file_39347a56c033](#file_39347a56c033)
  - ` .specs/features/sync_maintenance/spec.md` -> [file_9c99344c7962](#file_9c99344c7962)
  - `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
  - `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
  - `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
  - `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
  - `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
  - `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
  - `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
  - `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
  - `.context/brain/START_HERE.md` -> [file_e11d89201917](#file_e11d89201917)
  - `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
  - `.context/brain/VISION.md` -> [file_d2f31e4696a6](#file_d2f31e4696a6)
  - `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
  - `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
  - `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
  - `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
  - `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
  - `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
  - `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
  - `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
  - `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
  - `.context/market/WIKI/_index.md` -> [file_578d56cac1a4](#file_578d56cac1a4)
  - `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
  - `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
  - `.context/market/wiki_log.md` -> [file_c255058b56fe](#file_c255058b56fe)
  - `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
  - `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
  - `.context/specs/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_37fb63b0fac5](#file_37fb63b0fac5)
  - `.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_0511c79bd7d2](#file_0511c79bd7d2)
  - `.specs/_template.md` -> [file_b838611f038c](#file_b838611f038c)
  - `.specs/features/harness_fail_closed/STATE.md` -> [file_d4f64fc3b549](#file_d4f64fc3b549)
  - `.specs/features/harness_fail_closed/spec.md` -> [file_a32e3bf74e3d](#file_a32e3bf74e3d)
  - `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
  - `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
  - `.specs/features/wiki_level2/STATE.md` -> [file_638d6695a3f1](#file_638d6695a3f1)
  - `.specs/features/wiki_level2/spec.md` -> [file_86778e912e18](#file_86778e912e18)
  - `.specs/features/wiki_level2/tasks.md` -> [file_fafce66dc671](#file_fafce66dc671)
  - `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` -> [file_95dabcdf3543](#file_95dabcdf3543)
  - `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
  - `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
  - `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
  - `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
  - `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `source`:
  - `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
  - `.context/_scripts/_wiki_log_utils.py` -> [file_9ee5d49278ad](#file_9ee5d49278ad)
  - `.context/_scripts/check_version_consistency.py` -> [file_4ffe1a34765a](#file_4ffe1a34765a)
  - `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
  - `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
  - `.context/_scripts/enrich_context.py` -> [file_e94b4e40315c](#file_e94b4e40315c)
  - `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
  - `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
  - `.context/_scripts/ingest_wiki_guard.py` -> [file_0731dcfd7873](#file_0731dcfd7873)
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
- ` .specs/features/docs_resenha/STATE.md` -> [file_f6a9dd4e6c97](#file_f6a9dd4e6c97)
- ` .specs/features/docs_resenha/spec.md` -> [file_736dc30bc94f](#file_736dc30bc94f)
- ` .specs/features/hardening_v2.5/STATE.md` -> [file_5f4ef6860006](#file_5f4ef6860006)
- ` .specs/features/hardening_v2.5/spec.md` -> [file_f941f64c38fb](#file_f941f64c38fb)
- ` .specs/features/sync_maintenance/STATE.md` -> [file_39347a56c033](#file_39347a56c033)
- ` .specs/features/sync_maintenance/spec.md` -> [file_9c99344c7962](#file_9c99344c7962)
- `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
- `.context/_scripts/_wiki_log_utils.py` -> [file_9ee5d49278ad](#file_9ee5d49278ad)
- `.context/_scripts/check_version_consistency.py` -> [file_4ffe1a34765a](#file_4ffe1a34765a)
- `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
- `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
- `.context/_scripts/enrich_context.py` -> [file_e94b4e40315c](#file_e94b4e40315c)
- `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
- `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
- `.context/_scripts/ingest_wiki_guard.py` -> [file_0731dcfd7873](#file_0731dcfd7873)
- `.context/_scripts/lint_wiki.py` -> [file_ab41b07fb3fb](#file_ab41b07fb3fb)
- `.context/_scripts/migration_registry.py` -> [file_d65b48a9d56c](#file_d65b48a9d56c)
- `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
- `.context/_scripts/secrets_scanner.py` -> [file_e98b95e5fb6d](#file_e98b95e5fb6d)
- `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
- `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
- `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
- `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
- `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
- `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
- `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
- `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
- `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
- `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
- `.context/brain/START_HERE.md` -> [file_e11d89201917](#file_e11d89201917)
- `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
- `.context/brain/VISION.md` -> [file_d2f31e4696a6](#file_d2f31e4696a6)
- `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
- `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
- `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
- `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
- `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
- `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
- `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
- `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
- `.context/maintenance/version_targets.json` -> [file_51ed93c9d8ab](#file_51ed93c9d8ab)
- `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
- `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
- `.context/market/WIKI/_index.md` -> [file_578d56cac1a4](#file_578d56cac1a4)
- `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
- `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
- `.context/market/wiki_log.md` -> [file_c255058b56fe](#file_c255058b56fe)
- `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
- `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
- `.context/specs/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_37fb63b0fac5](#file_37fb63b0fac5)
- `.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_0511c79bd7d2](#file_0511c79bd7d2)
- `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
- `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
- `.specs/_template.md` -> [file_b838611f038c](#file_b838611f038c)
- `.specs/features/harness_fail_closed/STATE.md` -> [file_d4f64fc3b549](#file_d4f64fc3b549)
- `.specs/features/harness_fail_closed/spec.md` -> [file_a32e3bf74e3d](#file_a32e3bf74e3d)
- `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
- `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
- `.specs/features/wiki_level2/STATE.md` -> [file_638d6695a3f1](#file_638d6695a3f1)
- `.specs/features/wiki_level2/spec.md` -> [file_86778e912e18](#file_86778e912e18)
- `.specs/features/wiki_level2/tasks.md` -> [file_fafce66dc671](#file_fafce66dc671)
- `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` -> [file_95dabcdf3543](#file_95dabcdf3543)
- `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
- `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
- `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
- `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
- `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

---
<a id="file_f6a9dd4e6c97"></a>
FILE_START id=file_f6a9dd4e6c97 path= .specs/features/docs_resenha/STATE.md domain=docs lang=markdown lines=5 bytes=82 mtime=2026-04-23T14:06:00.087931+00:00 sha1=55b3a4ebae1aa940ec05b1cdd1a340d3d2a43372
CONTENT_OMITTED toc_only=true
FILE_END id=file_f6a9dd4e6c97

---
<a id="file_736dc30bc94f"></a>
FILE_START id=file_736dc30bc94f path= .specs/features/docs_resenha/spec.md domain=docs lang=markdown lines=9 bytes=274 mtime=2026-04-23T14:06:00.089930+00:00 sha1=8a2e4d88781bc7bcdd94940eb3d745ccb40a0143
CONTENT_OMITTED toc_only=true
FILE_END id=file_736dc30bc94f

---
<a id="file_5f4ef6860006"></a>
FILE_START id=file_5f4ef6860006 path= .specs/features/hardening_v2.5/STATE.md domain=docs lang=markdown lines=5 bytes=84 mtime=2026-04-23T14:06:00.092132+00:00 sha1=bc5c3f83bfe9e8fbb1ee3058dc9dfcda6dcdce91
CONTENT_OMITTED toc_only=true
FILE_END id=file_5f4ef6860006

---
<a id="file_f941f64c38fb"></a>
FILE_START id=file_f941f64c38fb path= .specs/features/hardening_v2.5/spec.md domain=docs lang=markdown lines=13 bytes=449 mtime=2026-04-23T14:06:00.093643+00:00 sha1=54b211d4df661279c1738893d9a114caab2314e7
CONTENT_OMITTED toc_only=true
FILE_END id=file_f941f64c38fb

---
<a id="file_39347a56c033"></a>
FILE_START id=file_39347a56c033 path= .specs/features/sync_maintenance/STATE.md domain=docs lang=markdown lines=5 bytes=101 mtime=2026-04-23T14:06:00.095644+00:00 sha1=bf670324c5382439ece01583d60d3bc540025347
CONTENT_OMITTED toc_only=true
FILE_END id=file_39347a56c033

---
<a id="file_9c99344c7962"></a>
FILE_START id=file_9c99344c7962 path= .specs/features/sync_maintenance/spec.md domain=docs lang=markdown lines=9 bytes=327 mtime=2026-04-23T14:06:00.096642+00:00 sha1=4dc412152491353d37e335453581463266a7c1cb
CONTENT_OMITTED toc_only=true
FILE_END id=file_9c99344c7962

---
<a id="file_dbef1acce0d4"></a>
FILE_START id=file_dbef1acce0d4 path=.context/_scripts/_tz_utils.py domain=source lang=python lines=37 bytes=1257 mtime=2026-04-12T02:47:25.198957+00:00 sha1=a49568f45d4b962ab01f0ed4b359ee4c09f65741
CONTENT_OMITTED toc_only=true
FILE_END id=file_dbef1acce0d4

---
<a id="file_9ee5d49278ad"></a>
FILE_START id=file_9ee5d49278ad path=.context/_scripts/_wiki_log_utils.py domain=source lang=python lines=66 bytes=2541 mtime=2026-04-22T23:47:25.409048+00:00 sha1=eb8650ba121fe8cc8aaabaca70de01214509937e
CONTENT_OMITTED toc_only=true
FILE_END id=file_9ee5d49278ad

---
<a id="file_4ffe1a34765a"></a>
FILE_START id=file_4ffe1a34765a path=.context/_scripts/check_version_consistency.py domain=source lang=python lines=80 bytes=2486 mtime=2026-04-22T12:37:52.914197+00:00 sha1=0f0bcd180ff803df099fc5f865ce6d3106e196d2
CONTENT_OMITTED toc_only=true
FILE_END id=file_4ffe1a34765a

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CONTENT_OMITTED toc_only=true
FILE_END id=file_82cd6bde54ff

---
<a id="file_10081abf87e1"></a>
FILE_START id=file_10081abf87e1 path=.context/_scripts/context_oracle.py domain=source lang=python lines=133 bytes=5290 mtime=2026-04-22T23:34:52.248624+00:00 sha1=61d7e4d041f8821d2240f83a9ad8b5c26baa9cb9
CONTENT_OMITTED toc_only=true
FILE_END id=file_10081abf87e1

---
<a id="file_e94b4e40315c"></a>
FILE_START id=file_e94b4e40315c path=.context/_scripts/enrich_context.py domain=source lang=python lines=125 bytes=4876 mtime=2026-04-17T00:17:17.361963+00:00 sha1=6ab638ce0553fdafde495ea2f64fc30ae300f765
CONTENT_OMITTED toc_only=true
FILE_END id=file_e94b4e40315c

---
<a id="file_1edef35c2f56"></a>
FILE_START id=file_1edef35c2f56 path=.context/_scripts/harness_runner.py domain=source lang=python lines=377 bytes=13475 mtime=2026-04-23T15:09:13.334620+00:00 sha1=c76d3a65d6be246539305f89c25c0963f6184a60
CONTENT_OMITTED toc_only=true
FILE_END id=file_1edef35c2f56

---
<a id="file_a642d240b9ab"></a>
FILE_START id=file_a642d240b9ab path=.context/_scripts/health_sync.py domain=source lang=python lines=111 bytes=4132 mtime=2026-04-12T03:40:11.302253+00:00 sha1=1f23d31d0c88fe19ee916b4d6dd9676fb2f0018b
CONTENT_OMITTED toc_only=true
FILE_END id=file_a642d240b9ab

---
<a id="file_0731dcfd7873"></a>
FILE_START id=file_0731dcfd7873 path=.context/_scripts/ingest_wiki_guard.py domain=source lang=python lines=88 bytes=3112 mtime=2026-04-22T23:34:30.558813+00:00 sha1=8cf96a678ced2d689deb51608c115dcd75a632a8
CONTENT_OMITTED toc_only=true
FILE_END id=file_0731dcfd7873

---
<a id="file_ab41b07fb3fb"></a>
FILE_START id=file_ab41b07fb3fb path=.context/_scripts/lint_wiki.py domain=source lang=python lines=116 bytes=4999 mtime=2026-04-22T23:34:42.090035+00:00 sha1=844cbc05474f73fa7addd3038fbbc60b86ab460a
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
FILE_START id=file_e98b95e5fb6d path=.context/_scripts/secrets_scanner.py domain=source lang=python lines=69 bytes=2622 mtime=2026-04-14T12:47:41.549578+00:00 sha1=f73abf4fe2fa1a6e146de3fefae50c9016b77045
CONTENT_OMITTED toc_only=true
FILE_END id=file_e98b95e5fb6d

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=102 bytes=3426 mtime=2026-04-12T02:48:59.755191+00:00 sha1=d2b0f3541ccaab8c75f381f47d539c762618a0b7
CONTENT_OMITTED toc_only=true
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=253 bytes=8091 mtime=2026-04-22T23:17:08.680799+00:00 sha1=c24e8617c984749da6e65e550b43cf786c4c913c
CONTENT_OMITTED toc_only=true
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=100 bytes=7961 mtime=2026-04-17T14:30:57.702377+00:00 sha1=760dffd6994964389bbcdb387181df2366605a40
CONTENT_OMITTED toc_only=true
FILE_END id=file_e7c17acb71ff

---
<a id="file_4b29e274836e"></a>
FILE_START id=file_4b29e274836e path=.context/brain/HARNESS_REGISTRY.md domain=docs lang=markdown lines=20 bytes=1180 mtime=2026-04-11T23:46:58.142679+00:00 sha1=5a29edb2d353e3117e7e904191ef4dadfd322309
CONTENT_OMITTED toc_only=true
FILE_END id=file_4b29e274836e

---
<a id="file_de9ef20db2be"></a>
FILE_START id=file_de9ef20db2be path=.context/brain/INCEPTION.md domain=docs lang=markdown lines=43 bytes=3455 mtime=2026-04-23T15:10:01.045421+00:00 sha1=1c3639bff80071b9781712b04dfd7edd74ca73bc
CONTENT_OMITTED toc_only=true
FILE_END id=file_de9ef20db2be

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=107 bytes=5912 mtime=2026-04-23T14:41:07.641418+00:00 sha1=e1d7f433195535d0dafdb6ae0a923408328e50fb
CONTENT_OMITTED toc_only=true
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=29 bytes=1406 mtime=2026-04-17T01:21:43.543040+00:00 sha1=c75b72944c19fabc58237fb903784cb79ae6b4da
CONTENT_OMITTED toc_only=true
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=203 bytes=9794 mtime=2026-04-17T14:31:34.213228+00:00 sha1=002c5f92393fcfd0ce78f0ec85aa8d93af6e377d
CONTENT_OMITTED toc_only=true
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=15 bytes=719 mtime=2026-04-21T23:32:04.607493+00:00 sha1=55fb929dd00b9a0eff1c9a253ec37e0609445e92
CONTENT_OMITTED toc_only=true
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=121 bytes=8428 mtime=2026-04-23T16:12:49.465411+00:00 sha1=bda18421976aa89e223cbdfbcbe9a931fba8dbc4
CONTENT_OMITTED toc_only=true
FILE_END id=file_cd6526d17218

---
<a id="file_e11d89201917"></a>
FILE_START id=file_e11d89201917 path=.context/brain/START_HERE.md domain=docs lang=markdown lines=42 bytes=1749 mtime=2026-04-17T00:07:25.637908+00:00 sha1=482d0d056987215305ae88da18b37a59faa64658
CONTENT_OMITTED toc_only=true
FILE_END id=file_e11d89201917

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CONTENT_OMITTED toc_only=true
FILE_END id=file_450d7ec70909

---
<a id="file_d2f31e4696a6"></a>
FILE_START id=file_d2f31e4696a6 path=.context/brain/VISION.md domain=docs lang=markdown lines=44 bytes=7254 mtime=2026-04-23T15:26:57.151891+00:00 sha1=43246ab516dda1697b1efe4e634120aebce63c56
CONTENT_OMITTED toc_only=true
FILE_END id=file_d2f31e4696a6

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=17 bytes=827 mtime=2026-04-21T23:31:39.053793+00:00 sha1=e56f0939f55e5a0897bf89642150226cb048abd1
CONTENT_OMITTED toc_only=true
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=484 bytes=23416 mtime=2026-04-23T18:31:41.954752+00:00 sha1=bd90ab9ecbe4fffe87df6802cc68e0159123010b
CONTENT_OMITTED toc_only=true
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=128 bytes=989 mtime=2026-04-23T16:13:09.768560+00:00 sha1=d37f5068cfdd73f955c65746e68629891162e2a9
CONTENT_OMITTED toc_only=true
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=14 bytes=487 mtime=2026-04-21T23:31:41.224778+00:00 sha1=41caf1bd5e6bf513c1924db0b4dca9fb6f92322b
CONTENT_OMITTED toc_only=true
FILE_END id=file_0858a02cf53f

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
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=36 bytes=2178 mtime=2026-04-20T14:46:26.673206+00:00 sha1=34ca91d2500a5683e58506f31c7ebad4abc34939
CONTENT_OMITTED toc_only=true
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=31 bytes=2068 mtime=2026-04-20T14:46:28.695155+00:00 sha1=b9830614be78ced5077a6accd008a9bb41f5fe2a
CONTENT_OMITTED toc_only=true
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CONTENT_OMITTED toc_only=true
FILE_END id=file_91d5627a725e

---
<a id="file_51ed93c9d8ab"></a>
FILE_START id=file_51ed93c9d8ab path=.context/maintenance/version_targets.json domain=config lang=json lines=22 bytes=538 mtime=2026-04-22T12:37:34.654694+00:00 sha1=c2279f3056490c43cd112154c87f7b6b97e852ac
CONTENT_OMITTED toc_only=true
FILE_END id=file_51ed93c9d8ab

---
<a id="file_81ef387da7b7"></a>
FILE_START id=file_81ef387da7b7 path=.context/market/MARKET_INBOX.md domain=docs lang=markdown lines=11 bytes=341 mtime=2026-04-15T19:15:21.935146+00:00 sha1=66adcca82c5eae73d386371aef29795c87e283b3
CONTENT_OMITTED toc_only=true
FILE_END id=file_81ef387da7b7

---
<a id="file_65a089176b85"></a>
FILE_START id=file_65a089176b85 path=.context/market/SSOT_MAP.md domain=docs lang=markdown lines=26 bytes=1842 mtime=2026-04-20T14:12:07.881449+00:00 sha1=817fcdf3b98f82a751294e12763163f975e890db
CONTENT_OMITTED toc_only=true
FILE_END id=file_65a089176b85

---
<a id="file_578d56cac1a4"></a>
FILE_START id=file_578d56cac1a4 path=.context/market/WIKI/_index.md domain=docs lang=markdown lines=5 bytes=100 mtime=2026-04-22T23:08:43.528195+00:00 sha1=49feb4c64bb2f3a2838a667b4e78b5afb009b2e4
CONTENT_OMITTED toc_only=true
FILE_END id=file_578d56cac1a4

---
<a id="file_491684f3a96e"></a>
FILE_START id=file_491684f3a96e path=.context/market/WIKI/_template.md domain=docs lang=markdown lines=26 bytes=451 mtime=2026-04-21T21:52:58.658989+00:00 sha1=cff3271c1a095ae525f40835ebdcf49adc208d3a
CONTENT_OMITTED toc_only=true
FILE_END id=file_491684f3a96e

---
<a id="file_b5d38697335e"></a>
FILE_START id=file_b5d38697335e path=.context/market/economics.md domain=docs lang=markdown lines=7 bytes=109 mtime=2026-04-15T17:50:11.975520+00:00 sha1=17852efa34dbaea46351dcabac87aa67286e2e93
CONTENT_OMITTED toc_only=true
FILE_END id=file_b5d38697335e

---
<a id="file_c255058b56fe"></a>
FILE_START id=file_c255058b56fe path=.context/market/wiki_log.md domain=docs lang=markdown lines=24 bytes=1756 mtime=2026-04-23T16:13:10.596559+00:00 sha1=b7c18915dc39c03f69bce97b65f9eff45eb05193
CONTENT_OMITTED toc_only=true
FILE_END id=file_c255058b56fe

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1506 mtime=2026-04-23T16:13:10.880297+00:00 sha1=81c613e83d0d6f6a61cd5b1158fcf5173268a56c
CONTENT_OMITTED toc_only=true
FILE_END id=file_068a21d64bec

---
<a id="file_c6d44cc7da35"></a>
FILE_START id=file_c6d44cc7da35 path=.context/monitoring/EXECUTION_BUFFER.md domain=docs lang=markdown lines=10 bytes=327 mtime=2026-04-18T14:24:14.955191+00:00 sha1=d7989e55f1d5b4c9c8c2fa6057d6c8407b80e134
CONTENT_OMITTED toc_only=true
FILE_END id=file_c6d44cc7da35

---
<a id="file_37fb63b0fac5"></a>
FILE_START id=file_37fb63b0fac5 path=.context/specs/DIRECTIVA_V2.4.1_HARDENED.md domain=docs lang=markdown lines=174 bytes=8421 mtime=2026-04-15T17:41:55.756194+00:00 sha1=7b18093a0456bf1be767656576630ad229da9324
CONTENT_OMITTED toc_only=true
FILE_END id=file_37fb63b0fac5

---
<a id="file_0511c79bd7d2"></a>
FILE_START id=file_0511c79bd7d2 path=.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md domain=docs lang=markdown lines=58 bytes=2572 mtime=2026-04-15T19:09:36.074497+00:00 sha1=9069fe10243396ca96cc0b1e8b76b29a7084307e
CONTENT_OMITTED toc_only=true
FILE_END id=file_0511c79bd7d2

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=25 bytes=569 mtime=2026-04-14T12:47:48.321567+00:00 sha1=7c7488139d3c3c4327aa9889700f683ee1f47be1
CONTENT_OMITTED toc_only=true
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CONTENT_OMITTED toc_only=true
FILE_END id=file_3adfd36c1559

---
<a id="file_b838611f038c"></a>
FILE_START id=file_b838611f038c path=.specs/_template.md domain=docs lang=markdown lines=25 bytes=671 mtime=2026-04-23T15:03:29.252894+00:00 sha1=2a614c9cd5347bb1019dff4d36733eb19cc91f7d
CONTENT_OMITTED toc_only=true
FILE_END id=file_b838611f038c

---
<a id="file_d4f64fc3b549"></a>
FILE_START id=file_d4f64fc3b549 path=.specs/features/harness_fail_closed/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-22T23:02:55.455444+00:00 sha1=a627e9b0e39cebcd966bff38fff2869fb72544c9
CONTENT_OMITTED toc_only=true
FILE_END id=file_d4f64fc3b549

---
<a id="file_a32e3bf74e3d"></a>
FILE_START id=file_a32e3bf74e3d path=.specs/features/harness_fail_closed/spec.md domain=docs lang=markdown lines=14 bytes=630 mtime=2026-04-21T22:16:15.283651+00:00 sha1=32ea04febe6e93d0fa8959cc525575f3bd2bb3eb
CONTENT_OMITTED toc_only=true
FILE_END id=file_a32e3bf74e3d

---
<a id="file_238a0e1da225"></a>
FILE_START id=file_238a0e1da225 path=.specs/features/meta-inception/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-21T22:01:44.285888+00:00 sha1=4647d09b6cba8ee228ab2e51d8c647537a9c41a5
CONTENT_OMITTED toc_only=true
FILE_END id=file_238a0e1da225

---
<a id="file_9801af51c558"></a>
FILE_START id=file_9801af51c558 path=.specs/features/meta-inception/spec.md domain=docs lang=markdown lines=30 bytes=1389 mtime=2026-04-17T14:33:18.003175+00:00 sha1=0cd48f6f6251020721a35d1efcec750576473d60
CONTENT_OMITTED toc_only=true
FILE_END id=file_9801af51c558

---
<a id="file_638d6695a3f1"></a>
FILE_START id=file_638d6695a3f1 path=.specs/features/wiki_level2/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-23T16:13:10.105855+00:00 sha1=148beb1b31b7c84b24afa16b4a71d25cf71264bb
CONTENT_OMITTED toc_only=true
FILE_END id=file_638d6695a3f1

---
<a id="file_86778e912e18"></a>
FILE_START id=file_86778e912e18 path=.specs/features/wiki_level2/spec.md domain=docs lang=markdown lines=43 bytes=1834 mtime=2026-04-22T23:11:15.675831+00:00 sha1=71be78a7b5b40a5dd98bb2d0f899312d14766a6d
CONTENT_OMITTED toc_only=true
FILE_END id=file_86778e912e18

---
<a id="file_fafce66dc671"></a>
FILE_START id=file_fafce66dc671 path=.specs/features/wiki_level2/tasks.md domain=docs lang=markdown lines=55 bytes=2460 mtime=2026-04-22T23:32:40.379948+00:00 sha1=161c580635c9ecd7ba0d68aa9fab0db1d788b1af
CONTENT_OMITTED toc_only=true
FILE_END id=file_fafce66dc671

---
<a id="file_95dabcdf3543"></a>
FILE_START id=file_95dabcdf3543 path=GUIA_ESTABILIZACAO_NOTEBOOKLM.md domain=docs lang=markdown lines=56 bytes=2342 mtime=2026-04-16T01:24:16.342106+00:00 sha1=42fda535b309349df1a8c83c959f0cc2e534875a
CONTENT_OMITTED toc_only=true
FILE_END id=file_95dabcdf3543

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=97 bytes=4687 mtime=2026-04-23T16:12:13.144613+00:00 sha1=23e3abb6e9ba9b868808626442bbec6112a64a74
CONTENT_OMITTED toc_only=true
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=124 bytes=6147 mtime=2026-04-23T16:12:19.354400+00:00 sha1=1d7fc538fa85b139c3882b3f40c7525e7ed5429f
CONTENT_OMITTED toc_only=true
FILE_END id=file_4efb6293109d

---
<a id="file_19e76e009f38"></a>
FILE_START id=file_19e76e009f38 path=TEMPLATE_MIGRATION.md domain=docs lang=markdown lines=59 bytes=1930 mtime=2026-04-15T13:55:12.936320+00:00 sha1=a3590439f4c18d976ff928504760f8f35a29d25c
CONTENT_OMITTED toc_only=true
FILE_END id=file_19e76e009f38

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=10 bytes=537 mtime=2026-04-23T15:08:13.037173+00:00 sha1=8f9a8ce10e35a27487d66c85490f535adcdb2d5a
CONTENT_OMITTED toc_only=true
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CONTENT_OMITTED toc_only=true
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=429 bytes=17844 mtime=2026-04-23T18:31:18.210183+00:00 sha1=6108c27d0315281c1f40bec72da49685422fdcc9
CONTENT_OMITTED toc_only=true
FILE_END id=file_c3916196f58f

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=127 bytes=4447 mtime=2026-04-17T02:44:14.961287+00:00 sha1=f14d70f06e7349803e99a3d2521a4f54ff1a669d
CONTENT_OMITTED toc_only=true
FILE_END id=file_c59135753d26

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=38 bytes=1494 mtime=2026-04-23T15:08:31.764449+00:00 sha1=d790fbee1062be196684ab2ca82037ffc394e56a
CONTENT_OMITTED toc_only=true
FILE_END id=file_7030d0b2f71b

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=144 bytes=5190 mtime=2026-04-22T23:16:30.370440+00:00 sha1=d888ea6eb9ffb21318a8abcb892c99af10ca6374
CONTENT_OMITTED toc_only=true
FILE_END id=file_350a79f8b829

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=17 bytes=798 mtime=2026-04-17T02:31:37.204327+00:00 sha1=a6c29d302d9d9c3f99917dd1da64da3d07f635ac
CONTENT_OMITTED toc_only=true
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=135 bytes=6249 mtime=2026-04-17T00:13:58.569614+00:00 sha1=9d17651da9da5326350654941d201d72c37c42c4
CONTENT_OMITTED toc_only=true
FILE_END id=file_4c6bbd05056e
