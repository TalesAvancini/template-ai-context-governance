# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-14T16:46:42.169149+00:00
root: template_inicío_de_projeto
mode: full | TOC
profile: ai-default
file_count: 61
byte_count: 174610
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
  - `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
  - `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
  - `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
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
  - `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/STATE.md` -> [file_5f4a4ae13ef8](#file_5f4a4ae13ef8)
  - `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/spec.md` -> [file_64bc4e458b6c](#file_64bc4e458b6c)
  - `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
  - `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
  - `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
  - `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
  - `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
  - `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
  - `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
  - `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
  - `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
  - `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
  - `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
  - `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
  - `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
  - `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
  - `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
  - `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
  - `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
  - `planos/plan_hok_advanced_security_and_db.md` -> [file_7bd2d6af54a4](#file_7bd2d6af54a4)
  - `planos/plan_inception_final_v2_4.md` -> [file_385231f1afeb](#file_385231f1afeb)
  - `planos/plan_inception_market_v2_4.md` -> [file_b7594f581e6a](#file_b7594f581e6a)
  - `planos/roadmap_reactive_hok_v2_v3.md` -> [file_44c34e6237da](#file_44c34e6237da)
  - `planos/template_base_v2_3_1.md` -> [file_f23e47398730](#file_f23e47398730)
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
- `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
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
- `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/STATE.md` -> [file_5f4a4ae13ef8](#file_5f4a4ae13ef8)
- `.context/maintenance/_archive_context/specs/hok-advanced-modules_20260414_075508/spec.md` -> [file_64bc4e458b6c](#file_64bc4e458b6c)
- `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
- `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
- `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
- `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
- `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
- `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
- `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
- `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
- `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
- `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
- `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
- `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
- `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
- `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
- `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
- `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
- `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
- `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
- `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
- `planos/plan_hok_advanced_security_and_db.md` -> [file_7bd2d6af54a4](#file_7bd2d6af54a4)
- `planos/plan_inception_final_v2_4.md` -> [file_385231f1afeb](#file_385231f1afeb)
- `planos/plan_inception_market_v2_4.md` -> [file_b7594f581e6a](#file_b7594f581e6a)
- `planos/roadmap_reactive_hok_v2_v3.md` -> [file_44c34e6237da](#file_44c34e6237da)
- `planos/template_base_v2_3_1.md` -> [file_f23e47398730](#file_f23e47398730)
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
FILE_START id=file_10081abf87e1 path=.context/_scripts/context_oracle.py domain=source lang=python lines=78 bytes=2798 mtime=2026-04-14T16:43:56.809132+00:00 sha1=db11007d6624952ee8025467899c8edb829d2c6c
CONTENT_OMITTED toc_only=true
FILE_END id=file_10081abf87e1

---
<a id="file_1edef35c2f56"></a>
FILE_START id=file_1edef35c2f56 path=.context/_scripts/harness_runner.py domain=source lang=python lines=119 bytes=5200 mtime=2026-04-14T16:44:14.745227+00:00 sha1=d3eed97f128b15acd6838c41f2a50ffbaa3d9c6c
CONTENT_OMITTED toc_only=true
FILE_END id=file_1edef35c2f56

---
<a id="file_a642d240b9ab"></a>
FILE_START id=file_a642d240b9ab path=.context/_scripts/health_sync.py domain=source lang=python lines=111 bytes=4132 mtime=2026-04-12T03:40:11.302253+00:00 sha1=1f23d31d0c88fe19ee916b4d6dd9676fb2f0018b
CONTENT_OMITTED toc_only=true
FILE_END id=file_a642d240b9ab

---
<a id="file_ab41b07fb3fb"></a>
FILE_START id=file_ab41b07fb3fb path=.context/_scripts/lint_wiki.py domain=source lang=python lines=103 bytes=4422 mtime=2026-04-12T03:39:45.482564+00:00 sha1=fd071ee8ca5653747a4d2a43de307d90ba19965f
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
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=112 bytes=3995 mtime=2026-04-14T16:43:40.446806+00:00 sha1=36db7de5f6ffa88dab32ae3598f87b2b1fe387ce
CONTENT_OMITTED toc_only=true
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=99 bytes=7608 mtime=2026-04-14T15:00:35.033399+00:00 sha1=65db425505a5b346b38f86cb5367a26b75cc8745
CONTENT_OMITTED toc_only=true
FILE_END id=file_e7c17acb71ff

---
<a id="file_4b29e274836e"></a>
FILE_START id=file_4b29e274836e path=.context/brain/HARNESS_REGISTRY.md domain=docs lang=markdown lines=20 bytes=1180 mtime=2026-04-11T23:46:58.142679+00:00 sha1=5a29edb2d353e3117e7e904191ef4dadfd322309
CONTENT_OMITTED toc_only=true
FILE_END id=file_4b29e274836e

---
<a id="file_de9ef20db2be"></a>
FILE_START id=file_de9ef20db2be path=.context/brain/INCEPTION.md domain=docs lang=markdown lines=26 bytes=847 mtime=2026-04-14T15:02:24.478806+00:00 sha1=1236e289c232f6a7dd04ca408e00b2c665694842
CONTENT_OMITTED toc_only=true
FILE_END id=file_de9ef20db2be

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=94 bytes=4989 mtime=2026-04-14T14:50:11.599857+00:00 sha1=625d3a48cc49a624db746f69ba0286467c5d96e6
CONTENT_OMITTED toc_only=true
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=67 bytes=2446 mtime=2026-04-14T15:02:30.490045+00:00 sha1=b5c06bc8a67d2a788cc8263f03971f379d04e92e
CONTENT_OMITTED toc_only=true
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=179 bytes=8253 mtime=2026-04-14T16:07:34.154588+00:00 sha1=e5ae4734d5073c28f34da257bb88fff751f489e6
CONTENT_OMITTED toc_only=true
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=16 bytes=404 mtime=2026-04-14T12:47:50.541630+00:00 sha1=fa053c5fb84692b6b9fe1736757c0998bf51abb8
CONTENT_OMITTED toc_only=true
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=94 bytes=6285 mtime=2026-04-14T15:00:02.829070+00:00 sha1=5b5782f6d450ea28bd85133ef33d75d782110344
CONTENT_OMITTED toc_only=true
FILE_END id=file_cd6526d17218

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CONTENT_OMITTED toc_only=true
FILE_END id=file_450d7ec70909

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=14 bytes=469 mtime=2026-04-14T12:47:52.604426+00:00 sha1=45a3fb7b057becba5acd3e6677fafc539cecb8b1
CONTENT_OMITTED toc_only=true
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=117 bytes=4378 mtime=2026-04-14T16:46:18.297788+00:00 sha1=2d3855fa50abac33090d1834097b1bb39b650d18
CONTENT_OMITTED toc_only=true
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=40 bytes=313 mtime=2026-04-14T16:46:17.728858+00:00 sha1=e006d9d45d66e98aaaae1386722302972c355071
CONTENT_OMITTED toc_only=true
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=14 bytes=416 mtime=2026-04-14T12:47:54.628006+00:00 sha1=fc4e2ba775d52345277e7a16625e44774a5e2d70
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
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=27 bytes=1336 mtime=2026-04-11T02:26:43.636538+00:00 sha1=adb37745498ccfa61a2b793c10240a2b20d3d716
CONTENT_OMITTED toc_only=true
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=16 bytes=885 mtime=2026-04-14T12:47:56.663727+00:00 sha1=e21edd4ab2bc3e50868ab2274483cd20980468d3
CONTENT_OMITTED toc_only=true
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CONTENT_OMITTED toc_only=true
FILE_END id=file_91d5627a725e

---
<a id="file_81ef387da7b7"></a>
FILE_START id=file_81ef387da7b7 path=.context/market/MARKET_INBOX.md domain=docs lang=markdown lines=12 bytes=772 mtime=2026-04-14T16:45:23.861741+00:00 sha1=a48e688a7723acbcae1af7b9b57af7e66730fd7a
CONTENT_OMITTED toc_only=true
FILE_END id=file_81ef387da7b7

---
<a id="file_65a089176b85"></a>
FILE_START id=file_65a089176b85 path=.context/market/SSOT_MAP.md domain=docs lang=markdown lines=17 bytes=949 mtime=2026-04-14T16:45:51.494110+00:00 sha1=4d21781b5cbfa9f85f27d0013f1045e7394688fc
CONTENT_OMITTED toc_only=true
FILE_END id=file_65a089176b85

---
<a id="file_b5d38697335e"></a>
FILE_START id=file_b5d38697335e path=.context/market/economics.md domain=docs lang=markdown lines=19 bytes=486 mtime=2026-04-14T16:46:05.811354+00:00 sha1=935c22a2a6e1e346902b115f59ebb430920567f9
CONTENT_OMITTED toc_only=true
FILE_END id=file_b5d38697335e

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1505 mtime=2026-04-14T16:46:18.731196+00:00 sha1=bba343e9f2f18a5f070dda24588a4b60275b4503
CONTENT_OMITTED toc_only=true
FILE_END id=file_068a21d64bec

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
<a id="file_238a0e1da225"></a>
FILE_START id=file_238a0e1da225 path=.specs/features/meta-inception/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-14T16:46:18.299370+00:00 sha1=e0b5e5c1838dff1fc982b642fcf4d118b22df216
CONTENT_OMITTED toc_only=true
FILE_END id=file_238a0e1da225

---
<a id="file_9801af51c558"></a>
FILE_START id=file_9801af51c558 path=.specs/features/meta-inception/spec.md domain=docs lang=markdown lines=22 bytes=1094 mtime=2026-04-14T14:46:50.141889+00:00 sha1=9471f4fdc679bb0ff7fd35796e75968de9fc34ec
CONTENT_OMITTED toc_only=true
FILE_END id=file_9801af51c558

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
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=423 bytes=17531 mtime=2026-04-14T16:44:37.932599+00:00 sha1=22de7724ad77c8fd6139284c7100f88e48fa53de
CONTENT_OMITTED toc_only=true
FILE_END id=file_c3916196f58f

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=155 bytes=5469 mtime=2026-04-11T02:29:46.289656+00:00 sha1=18e30807c6ef1ce94e3619f19f8ec2bd93f77c52
CONTENT_OMITTED toc_only=true
FILE_END id=file_c59135753d26

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
<a id="file_385231f1afeb"></a>
FILE_START id=file_385231f1afeb path=planos/plan_inception_final_v2_4.md domain=docs lang=markdown lines=79 bytes=5369 mtime=2026-04-14T14:17:36.087744+00:00 sha1=f065eff9f0cf713fa7a76b33e65e9bf81174228a
CONTENT_OMITTED toc_only=true
FILE_END id=file_385231f1afeb

---
<a id="file_b7594f581e6a"></a>
FILE_START id=file_b7594f581e6a path=planos/plan_inception_market_v2_4.md domain=docs lang=markdown lines=65 bytes=3658 mtime=2026-04-14T11:45:09.915754+00:00 sha1=cd869123cd6543d25a3fe7bbe6b4a4681ee5abbb
CONTENT_OMITTED toc_only=true
FILE_END id=file_b7594f581e6a

---
<a id="file_44c34e6237da"></a>
FILE_START id=file_44c34e6237da path=planos/roadmap_reactive_hok_v2_v3.md domain=docs lang=markdown lines=43 bytes=2070 mtime=2026-04-12T00:16:01.408542+00:00 sha1=bcab4c7525fa8c4ba078bf84d63965f3e60d3e23
CONTENT_OMITTED toc_only=true
FILE_END id=file_44c34e6237da

---
<a id="file_f23e47398730"></a>
FILE_START id=file_f23e47398730 path=planos/template_base_v2_3_1.md domain=docs lang=markdown lines=376 bytes=11814 mtime=2026-04-14T14:42:34.080446+00:00 sha1=b5883553cf4d4667c6381e63b064b87d92e2ba46
CONTENT_OMITTED toc_only=true
FILE_END id=file_f23e47398730

---
<a id="file_6a4bd0586b20"></a>
FILE_START id=file_6a4bd0586b20 path=planos/walkthrough_hok_triad.md domain=docs lang=markdown lines=32 bytes=2243 mtime=2026-04-12T00:05:31.404227+00:00 sha1=0bbfa5d700f335f10599d185d0fa8e788cf93cac
CONTENT_OMITTED toc_only=true
FILE_END id=file_6a4bd0586b20

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=68 bytes=2823 mtime=2026-04-14T16:43:02.192041+00:00 sha1=7e76400fd2380e743022135a65cdaca779826d6d
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
