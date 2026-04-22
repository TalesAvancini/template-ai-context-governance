# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-22T00:14:14.435645+00:00
root: template_inicío_de_projeto
mode: full | TOC
profile: ai-default
file_count: 83
byte_count: 260598
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
  - `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `db`:
  - `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `docs`:
  - ` .specs/features/docs_resenha/STATE.md` -> [file_f6a9dd4e6c97](#file_f6a9dd4e6c97)
  - ` .specs/features/docs_resenha/spec.md` -> [file_736dc30bc94f](#file_736dc30bc94f)
  - ` .specs/features/hardening_v2.5/STATE.md` -> [file_5f4ef6860006](#file_5f4ef6860006)
  - ` .specs/features/hardening_v2.5/spec.md` -> [file_f941f64c38fb](#file_f941f64c38fb)
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
  - `.context/maintenance/_archive_context/prds/PLAN_SPRINT_CONTRACT.md` -> [file_a5acb6406832](#file_a5acb6406832)
  - `.context/maintenance/_archive_context/raw/stripe_docs.md` -> [file_eaebfc593089](#file_eaebfc593089)
  - `.context/maintenance/_archive_context/raw/template_inbox.md` -> [file_618e9f7de1e8](#file_618e9f7de1e8)
  - `.context/maintenance/_archive_context/specs/_template_20260421_204026/spec.md` -> [file_47b9436c72d4](#file_47b9436c72d4)
  - `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/STATE.md` -> [file_5f4a4ae13ef8](#file_5f4a4ae13ef8)
  - `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/spec.md` -> [file_64bc4e458b6c](#file_64bc4e458b6c)
  - `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
  - `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
  - `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
  - `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
  - `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
  - `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
  - `.context/market/WIKI/conceito_teste.md` -> [file_fae1276881db](#file_fae1276881db)
  - `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
  - `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
  - `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
  - `.context/planos/PHASE_3_KARPATHY_WIKI.md` -> [file_e824b208c3a2](#file_e824b208c3a2)
  - `.context/specs/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_37fb63b0fac5](#file_37fb63b0fac5)
  - `.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_0511c79bd7d2](#file_0511c79bd7d2)
  - `.specs/features/harness_fail_closed/STATE.md` -> [file_d4f64fc3b549](#file_d4f64fc3b549)
  - `.specs/features/harness_fail_closed/spec.md` -> [file_a32e3bf74e3d](#file_a32e3bf74e3d)
  - `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
  - `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
  - `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` -> [file_95dabcdf3543](#file_95dabcdf3543)
  - `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
  - `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
  - `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
  - `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
  - `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
  - `planos/RESEARCH_NOTE_SPRINT_CONTRACTS.md` -> [file_7c2f50daa3f4](#file_7c2f50daa3f4)
  - `planos/_arquivo_planos/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_80252595b07f](#file_80252595b07f)
  - `planos/_arquivo_planos/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_482a16303af0](#file_482a16303af0)
  - `planos/_arquivo_planos/implementation_plan.md` -> [file_e7f1855928ad](#file_e7f1855928ad)
  - `planos/_arquivo_planos/master_plan.md` -> [file_2d826d235b59](#file_2d826d235b59)
  - `planos/_arquivo_planos/multi_agent_plan.md` -> [file_9efc22dd3673](#file_9efc22dd3673)
  - `planos/_arquivo_planos/plan_hok_advanced_security_and_db.md` -> [file_5b368adbea18](#file_5b368adbea18)
  - `planos/_arquivo_planos/plan_inception_final_v2_4.md` -> [file_4ebe74105a57](#file_4ebe74105a57)
  - `planos/_arquivo_planos/plan_inception_market_v2_4.md` -> [file_46be75d9b52e](#file_46be75d9b52e)
  - `planos/_arquivo_planos/roadmap_reactive_hok_v2_v3.md` -> [file_cf4807ec6c6c](#file_cf4807ec6c6c)
  - `planos/_arquivo_planos/walkthrough_hok_triad.md` -> [file_6825d8758f8d](#file_6825d8758f8d)
  - `planos/template_base_v2_3_1.md` -> [file_f23e47398730](#file_f23e47398730)
  - `resenha.md` -> [file_013dd7887d0e](#file_013dd7887d0e)
- `source`:
  - `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
  - `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
  - `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
  - `.context/_scripts/enrich_context.py` -> [file_e94b4e40315c](#file_e94b4e40315c)
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
- ` .specs/features/docs_resenha/STATE.md` -> [file_f6a9dd4e6c97](#file_f6a9dd4e6c97)
- ` .specs/features/docs_resenha/spec.md` -> [file_736dc30bc94f](#file_736dc30bc94f)
- ` .specs/features/hardening_v2.5/STATE.md` -> [file_5f4ef6860006](#file_5f4ef6860006)
- ` .specs/features/hardening_v2.5/spec.md` -> [file_f941f64c38fb](#file_f941f64c38fb)
- `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
- `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
- `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
- `.context/_scripts/enrich_context.py` -> [file_e94b4e40315c](#file_e94b4e40315c)
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
- `.context/maintenance/_archive_context/prds/PLAN_SPRINT_CONTRACT.md` -> [file_a5acb6406832](#file_a5acb6406832)
- `.context/maintenance/_archive_context/raw/stripe_docs.md` -> [file_eaebfc593089](#file_eaebfc593089)
- `.context/maintenance/_archive_context/raw/template_inbox.md` -> [file_618e9f7de1e8](#file_618e9f7de1e8)
- `.context/maintenance/_archive_context/specs/_template_20260421_204026/spec.md` -> [file_47b9436c72d4](#file_47b9436c72d4)
- `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/STATE.md` -> [file_5f4a4ae13ef8](#file_5f4a4ae13ef8)
- `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/spec.md` -> [file_64bc4e458b6c](#file_64bc4e458b6c)
- `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
- `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
- `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
- `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
- `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
- `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
- `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
- `.context/market/WIKI/conceito_teste.md` -> [file_fae1276881db](#file_fae1276881db)
- `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
- `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
- `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
- `.context/planos/PHASE_3_KARPATHY_WIKI.md` -> [file_e824b208c3a2](#file_e824b208c3a2)
- `.context/specs/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_37fb63b0fac5](#file_37fb63b0fac5)
- `.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_0511c79bd7d2](#file_0511c79bd7d2)
- `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
- `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
- `.specs/features/harness_fail_closed/STATE.md` -> [file_d4f64fc3b549](#file_d4f64fc3b549)
- `.specs/features/harness_fail_closed/spec.md` -> [file_a32e3bf74e3d](#file_a32e3bf74e3d)
- `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
- `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
- `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` -> [file_95dabcdf3543](#file_95dabcdf3543)
- `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
- `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
- `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
- `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
- `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `planos/RESEARCH_NOTE_SPRINT_CONTRACTS.md` -> [file_7c2f50daa3f4](#file_7c2f50daa3f4)
- `planos/_arquivo_planos/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_80252595b07f](#file_80252595b07f)
- `planos/_arquivo_planos/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_482a16303af0](#file_482a16303af0)
- `planos/_arquivo_planos/implementation_plan.md` -> [file_e7f1855928ad](#file_e7f1855928ad)
- `planos/_arquivo_planos/master_plan.md` -> [file_2d826d235b59](#file_2d826d235b59)
- `planos/_arquivo_planos/multi_agent_plan.md` -> [file_9efc22dd3673](#file_9efc22dd3673)
- `planos/_arquivo_planos/plan_hok_advanced_security_and_db.md` -> [file_5b368adbea18](#file_5b368adbea18)
- `planos/_arquivo_planos/plan_inception_final_v2_4.md` -> [file_4ebe74105a57](#file_4ebe74105a57)
- `planos/_arquivo_planos/plan_inception_market_v2_4.md` -> [file_46be75d9b52e](#file_46be75d9b52e)
- `planos/_arquivo_planos/roadmap_reactive_hok_v2_v3.md` -> [file_cf4807ec6c6c](#file_cf4807ec6c6c)
- `planos/_arquivo_planos/walkthrough_hok_triad.md` -> [file_6825d8758f8d](#file_6825d8758f8d)
- `planos/template_base_v2_3_1.md` -> [file_f23e47398730](#file_f23e47398730)
- `resenha.md` -> [file_013dd7887d0e](#file_013dd7887d0e)
- `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

---
<a id="file_f6a9dd4e6c97"></a>
FILE_START id=file_f6a9dd4e6c97 path= .specs/features/docs_resenha/STATE.md domain=docs lang=markdown lines=5 bytes=82 mtime=2026-04-21T23:04:30.894740+00:00 sha1=55b3a4ebae1aa940ec05b1cdd1a340d3d2a43372
CONTENT_OMITTED toc_only=true
FILE_END id=file_f6a9dd4e6c97

---
<a id="file_736dc30bc94f"></a>
FILE_START id=file_736dc30bc94f path= .specs/features/docs_resenha/spec.md domain=docs lang=markdown lines=9 bytes=274 mtime=2026-04-21T23:04:28.883652+00:00 sha1=8a2e4d88781bc7bcdd94940eb3d745ccb40a0143
CONTENT_OMITTED toc_only=true
FILE_END id=file_736dc30bc94f

---
<a id="file_5f4ef6860006"></a>
FILE_START id=file_5f4ef6860006 path= .specs/features/hardening_v2.5/STATE.md domain=docs lang=markdown lines=5 bytes=84 mtime=2026-04-21T23:40:05.934117+00:00 sha1=bc5c3f83bfe9e8fbb1ee3058dc9dfcda6dcdce91
CONTENT_OMITTED toc_only=true
FILE_END id=file_5f4ef6860006

---
<a id="file_f941f64c38fb"></a>
FILE_START id=file_f941f64c38fb path= .specs/features/hardening_v2.5/spec.md domain=docs lang=markdown lines=13 bytes=449 mtime=2026-04-21T23:40:03.905083+00:00 sha1=54b211d4df661279c1738893d9a114caab2314e7
CONTENT_OMITTED toc_only=true
FILE_END id=file_f941f64c38fb

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
FILE_START id=file_10081abf87e1 path=.context/_scripts/context_oracle.py domain=source lang=python lines=95 bytes=3635 mtime=2026-04-21T21:56:49.416362+00:00 sha1=db678b82aaafb2648992f5e2cab81fb8dcd6fd53
CONTENT_OMITTED toc_only=true
FILE_END id=file_10081abf87e1

---
<a id="file_e94b4e40315c"></a>
FILE_START id=file_e94b4e40315c path=.context/_scripts/enrich_context.py domain=source lang=python lines=125 bytes=4876 mtime=2026-04-17T00:17:17.361963+00:00 sha1=6ab638ce0553fdafde495ea2f64fc30ae300f765
CONTENT_OMITTED toc_only=true
FILE_END id=file_e94b4e40315c

---
<a id="file_1edef35c2f56"></a>
FILE_START id=file_1edef35c2f56 path=.context/_scripts/harness_runner.py domain=source lang=python lines=219 bytes=9550 mtime=2026-04-21T22:16:03.030237+00:00 sha1=fbe6e8c7113378b88136024475d2e15502e16f6b
CONTENT_OMITTED toc_only=true
FILE_END id=file_1edef35c2f56

---
<a id="file_a642d240b9ab"></a>
FILE_START id=file_a642d240b9ab path=.context/_scripts/health_sync.py domain=source lang=python lines=111 bytes=4132 mtime=2026-04-12T03:40:11.302253+00:00 sha1=1f23d31d0c88fe19ee916b4d6dd9676fb2f0018b
CONTENT_OMITTED toc_only=true
FILE_END id=file_a642d240b9ab

---
<a id="file_ab41b07fb3fb"></a>
FILE_START id=file_ab41b07fb3fb path=.context/_scripts/lint_wiki.py domain=source lang=python lines=92 bytes=3862 mtime=2026-04-21T22:17:35.036366+00:00 sha1=d4342a3f1f504fb3505f861cc60e9d42b8b32c4f
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
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=216 bytes=7159 mtime=2026-04-17T14:54:43.645074+00:00 sha1=3768b151f9bc0cd03e1728cb584e5680781858d3
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
FILE_START id=file_de9ef20db2be path=.context/brain/INCEPTION.md domain=docs lang=markdown lines=43 bytes=3454 mtime=2026-04-21T23:31:58.919034+00:00 sha1=2b3dfb00f050711f848cd339df298bff4cbdcf13
CONTENT_OMITTED toc_only=true
FILE_END id=file_de9ef20db2be

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=103 bytes=5406 mtime=2026-04-21T23:32:02.383555+00:00 sha1=4969cf2a25c9b50e8091cd149452a1c5517da068
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
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=112 bytes=7717 mtime=2026-04-21T21:54:08.043023+00:00 sha1=bf4c1ec50309ac5dfcfd438493ce8247ca23b161
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
FILE_START id=file_d2f31e4696a6 path=.context/brain/VISION.md domain=docs lang=markdown lines=42 bytes=7226 mtime=2026-04-21T23:31:32.291938+00:00 sha1=4a538eff2126b2d824abd9d32330a12668af360d
CONTENT_OMITTED toc_only=true
FILE_END id=file_d2f31e4696a6

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=17 bytes=827 mtime=2026-04-21T23:31:39.053793+00:00 sha1=e56f0939f55e5a0897bf89642150226cb048abd1
CONTENT_OMITTED toc_only=true
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=358 bytes=17201 mtime=2026-04-21T23:48:25.722749+00:00 sha1=6ac1d020b3f240d24998f6d9cb16d760ed863290
CONTENT_OMITTED toc_only=true
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=102 bytes=963 mtime=2026-04-21T23:48:25.368969+00:00 sha1=e72e2a83a806dbc39f7342158a034a89dc77585f
CONTENT_OMITTED toc_only=true
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=14 bytes=487 mtime=2026-04-21T23:31:41.224778+00:00 sha1=41caf1bd5e6bf513c1924db0b4dca9fb6f92322b
CONTENT_OMITTED toc_only=true
FILE_END id=file_0858a02cf53f

---
<a id="file_a5acb6406832"></a>
FILE_START id=file_a5acb6406832 path=.context/maintenance/_archive_context/prds/PLAN_SPRINT_CONTRACT.md domain=docs lang=markdown lines=23 bytes=1574 mtime=2026-04-17T14:46:46.697733+00:00 sha1=c57f4931bdccf5eafc25fc8edec8a136fd8b4ec7
CONTENT_OMITTED toc_only=true
FILE_END id=file_a5acb6406832

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
<a id="file_47b9436c72d4"></a>
FILE_START id=file_47b9436c72d4 path=.context/maintenance/_archive_context/specs/_template_20260421_204026/spec.md domain=docs lang=markdown lines=14 bytes=388 mtime=2026-04-17T14:30:46.316419+00:00 sha1=0a5b02cbff3cb6621902e89623b983f6b6d2a20d
CONTENT_OMITTED toc_only=true
FILE_END id=file_47b9436c72d4

---
<a id="file_5f4a4ae13ef8"></a>
FILE_START id=file_5f4a4ae13ef8 path=.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-12T03:41:44.408070+00:00 sha1=a5e7d0331e8f6f74044d9ae52e4930b5bd648d67
CONTENT_OMITTED toc_only=true
FILE_END id=file_5f4a4ae13ef8

---
<a id="file_64bc4e458b6c"></a>
FILE_START id=file_64bc4e458b6c path=.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/spec.md domain=docs lang=markdown lines=24 bytes=1573 mtime=2026-04-12T02:10:32.710904+00:00 sha1=4afa0f114364110370467d1033c99a6a49058746
CONTENT_OMITTED toc_only=true
FILE_END id=file_64bc4e458b6c

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
<a id="file_491684f3a96e"></a>
FILE_START id=file_491684f3a96e path=.context/market/WIKI/_template.md domain=docs lang=markdown lines=26 bytes=451 mtime=2026-04-21T21:52:58.658989+00:00 sha1=cff3271c1a095ae525f40835ebdcf49adc208d3a
CONTENT_OMITTED toc_only=true
FILE_END id=file_491684f3a96e

---
<a id="file_fae1276881db"></a>
FILE_START id=file_fae1276881db path=.context/market/WIKI/conceito_teste.md domain=docs lang=markdown lines=17 bytes=427 mtime=2026-04-21T21:57:23.511976+00:00 sha1=114401ee57ab919ad7729d6b018f5222d7ac4d16
CONTENT_OMITTED toc_only=true
FILE_END id=file_fae1276881db

---
<a id="file_b5d38697335e"></a>
FILE_START id=file_b5d38697335e path=.context/market/economics.md domain=docs lang=markdown lines=7 bytes=109 mtime=2026-04-15T17:50:11.975520+00:00 sha1=17852efa34dbaea46351dcabac87aa67286e2e93
CONTENT_OMITTED toc_only=true
FILE_END id=file_b5d38697335e

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1506 mtime=2026-04-21T23:48:26.622699+00:00 sha1=0a34d8d770aeff418828ea757a28f4b529923ed5
CONTENT_OMITTED toc_only=true
FILE_END id=file_068a21d64bec

---
<a id="file_c6d44cc7da35"></a>
FILE_START id=file_c6d44cc7da35 path=.context/monitoring/EXECUTION_BUFFER.md domain=docs lang=markdown lines=10 bytes=327 mtime=2026-04-18T14:24:14.955191+00:00 sha1=d7989e55f1d5b4c9c8c2fa6057d6c8407b80e134
CONTENT_OMITTED toc_only=true
FILE_END id=file_c6d44cc7da35

---
<a id="file_e824b208c3a2"></a>
FILE_START id=file_e824b208c3a2 path=.context/planos/PHASE_3_KARPATHY_WIKI.md domain=docs lang=markdown lines=49 bytes=2717 mtime=2026-04-21T17:51:48.426815+00:00 sha1=091fec4d117d03dad6a137e4f07dfc219a95f4d6
CONTENT_OMITTED toc_only=true
FILE_END id=file_e824b208c3a2

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
<a id="file_d4f64fc3b549"></a>
FILE_START id=file_d4f64fc3b549 path=.specs/features/harness_fail_closed/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-21T23:48:25.724752+00:00 sha1=d97cc6f9c462384b12cfcc3a8e8ca84acdd950d6
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
<a id="file_95dabcdf3543"></a>
FILE_START id=file_95dabcdf3543 path=GUIA_ESTABILIZACAO_NOTEBOOKLM.md domain=docs lang=markdown lines=56 bytes=2342 mtime=2026-04-16T01:24:16.342106+00:00 sha1=42fda535b309349df1a8c83c959f0cc2e534875a
CONTENT_OMITTED toc_only=true
FILE_END id=file_95dabcdf3543

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=97 bytes=4687 mtime=2026-04-17T02:54:18.326312+00:00 sha1=d90edde9bce80b7d3ab4b7c3663171d4c9ed3806
CONTENT_OMITTED toc_only=true
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=124 bytes=6147 mtime=2026-04-17T02:44:29.651973+00:00 sha1=8bac7d41d2d4d10afd0d0506792f2349f0ccfd36
CONTENT_OMITTED toc_only=true
FILE_END id=file_4efb6293109d

---
<a id="file_19e76e009f38"></a>
FILE_START id=file_19e76e009f38 path=TEMPLATE_MIGRATION.md domain=docs lang=markdown lines=59 bytes=1930 mtime=2026-04-15T13:55:12.936320+00:00 sha1=a3590439f4c18d976ff928504760f8f35a29d25c
CONTENT_OMITTED toc_only=true
FILE_END id=file_19e76e009f38

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=11 bytes=648 mtime=2026-04-21T22:00:44.995971+00:00 sha1=df3f5db87f81f17cbfe8be9abe712d476971a14c
CONTENT_OMITTED toc_only=true
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CONTENT_OMITTED toc_only=true
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=428 bytes=17796 mtime=2026-04-15T17:50:48.490335+00:00 sha1=6daa595e9a20d6ad7dc4d5f51479222aaf235f05
CONTENT_OMITTED toc_only=true
FILE_END id=file_c3916196f58f

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=127 bytes=4447 mtime=2026-04-17T02:44:14.961287+00:00 sha1=f14d70f06e7349803e99a3d2521a4f54ff1a669d
CONTENT_OMITTED toc_only=true
FILE_END id=file_c59135753d26

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=34 bytes=1232 mtime=2026-04-15T19:13:58.308600+00:00 sha1=dc707667997b95d8b8900b73c970f7356df992ef
CONTENT_OMITTED toc_only=true
FILE_END id=file_7030d0b2f71b

---
<a id="file_7c2f50daa3f4"></a>
FILE_START id=file_7c2f50daa3f4 path=planos/RESEARCH_NOTE_SPRINT_CONTRACTS.md domain=docs lang=markdown lines=19 bytes=1321 mtime=2026-04-15T20:04:35.439521+00:00 sha1=c5f557bd5f78146273a135f13f0d6ec82bcd5088
CONTENT_OMITTED toc_only=true
FILE_END id=file_7c2f50daa3f4

---
<a id="file_80252595b07f"></a>
FILE_START id=file_80252595b07f path=planos/_arquivo_planos/DIRECTIVA_V2.4.1_HARDENED.md domain=docs lang=markdown lines=174 bytes=8421 mtime=2026-04-15T17:41:55.756194+00:00 sha1=7b18093a0456bf1be767656576630ad229da9324
CONTENT_OMITTED toc_only=true
FILE_END id=file_80252595b07f

---
<a id="file_482a16303af0"></a>
FILE_START id=file_482a16303af0 path=planos/_arquivo_planos/PLAN_SPEC_ENRICHER_V2.4.1.md domain=docs lang=markdown lines=58 bytes=2572 mtime=2026-04-15T19:09:36.074497+00:00 sha1=9069fe10243396ca96cc0b1e8b76b29a7084307e
CONTENT_OMITTED toc_only=true
FILE_END id=file_482a16303af0

---
<a id="file_e7f1855928ad"></a>
FILE_START id=file_e7f1855928ad path=planos/_arquivo_planos/implementation_plan.md domain=docs lang=markdown lines=77 bytes=3338 mtime=2026-04-10T23:15:28.184032+00:00 sha1=37ad3605aae584ee4398621d92edd7b76058413e
CONTENT_OMITTED toc_only=true
FILE_END id=file_e7f1855928ad

---
<a id="file_2d826d235b59"></a>
FILE_START id=file_2d826d235b59 path=planos/_arquivo_planos/master_plan.md domain=docs lang=markdown lines=88 bytes=3620 mtime=2026-04-10T23:48:33.652301+00:00 sha1=9269f2e75a4300b61121c540eb8c3e57ba44329f
CONTENT_OMITTED toc_only=true
FILE_END id=file_2d826d235b59

---
<a id="file_9efc22dd3673"></a>
FILE_START id=file_9efc22dd3673 path=planos/_arquivo_planos/multi_agent_plan.md domain=docs lang=markdown lines=62 bytes=2824 mtime=2026-04-10T23:32:27.825062+00:00 sha1=71ea8355ff980c67c66959bec1e4782108bad081
CONTENT_OMITTED toc_only=true
FILE_END id=file_9efc22dd3673

---
<a id="file_5b368adbea18"></a>
FILE_START id=file_5b368adbea18 path=planos/_arquivo_planos/plan_hok_advanced_security_and_db.md domain=docs lang=markdown lines=54 bytes=2567 mtime=2026-04-12T01:55:31.645679+00:00 sha1=cf3305760cc94cf4ce1e359641fe889b16696354
CONTENT_OMITTED toc_only=true
FILE_END id=file_5b368adbea18

---
<a id="file_4ebe74105a57"></a>
FILE_START id=file_4ebe74105a57 path=planos/_arquivo_planos/plan_inception_final_v2_4.md domain=docs lang=markdown lines=79 bytes=5369 mtime=2026-04-14T14:17:36.087744+00:00 sha1=f065eff9f0cf713fa7a76b33e65e9bf81174228a
CONTENT_OMITTED toc_only=true
FILE_END id=file_4ebe74105a57

---
<a id="file_46be75d9b52e"></a>
FILE_START id=file_46be75d9b52e path=planos/_arquivo_planos/plan_inception_market_v2_4.md domain=docs lang=markdown lines=65 bytes=3658 mtime=2026-04-14T11:45:09.915754+00:00 sha1=cd869123cd6543d25a3fe7bbe6b4a4681ee5abbb
CONTENT_OMITTED toc_only=true
FILE_END id=file_46be75d9b52e

---
<a id="file_cf4807ec6c6c"></a>
FILE_START id=file_cf4807ec6c6c path=planos/_arquivo_planos/roadmap_reactive_hok_v2_v3.md domain=docs lang=markdown lines=43 bytes=2070 mtime=2026-04-12T00:16:01.408542+00:00 sha1=bcab4c7525fa8c4ba078bf84d63965f3e60d3e23
CONTENT_OMITTED toc_only=true
FILE_END id=file_cf4807ec6c6c

---
<a id="file_6825d8758f8d"></a>
FILE_START id=file_6825d8758f8d path=planos/_arquivo_planos/walkthrough_hok_triad.md domain=docs lang=markdown lines=32 bytes=2243 mtime=2026-04-12T00:05:31.404227+00:00 sha1=0bbfa5d700f335f10599d185d0fa8e788cf93cac
CONTENT_OMITTED toc_only=true
FILE_END id=file_6825d8758f8d

---
<a id="file_f23e47398730"></a>
FILE_START id=file_f23e47398730 path=planos/template_base_v2_3_1.md domain=docs lang=markdown lines=376 bytes=11814 mtime=2026-04-14T14:42:34.080446+00:00 sha1=b5883553cf4d4667c6381e63b064b87d92e2ba46
CONTENT_OMITTED toc_only=true
FILE_END id=file_f23e47398730

---
<a id="file_013dd7887d0e"></a>
FILE_START id=file_013dd7887d0e path=resenha.md domain=docs lang=markdown lines=99 bytes=4790 mtime=2026-04-21T23:04:17.815602+00:00 sha1=68c8395f9a92d1036cd26a65451e3c7ccd051034
CONTENT_OMITTED toc_only=true
FILE_END id=file_013dd7887d0e

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=132 bytes=4701 mtime=2026-04-17T00:17:10.870257+00:00 sha1=6d9a72194cc0708819959eaa59b6027ffaf0a851
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
