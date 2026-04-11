# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-11T23:33:54.890960+00:00
root: template_inicío_de_projeto
mode: full
profile: ai-default
file_count: 37
byte_count: 576367
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
- `docs`:
  - `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
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
  - `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
  - `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
  - `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
  - `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
  - `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
  - `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
  - `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
  - `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
  - `contexto.md` -> [file_aa78525fb574](#file_aa78525fb574)
  - `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
  - `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
  - `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
- `source`:
  - `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
  - `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
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
- `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
- `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
- `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
- `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
- `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
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
- `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
- `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
- `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
- `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
- `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
- `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
- `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
- `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
- `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
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
- `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CONTENT_OMITTED toc_only=true
FILE_END id=file_82cd6bde54ff

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=74 bytes=2507 mtime=2026-04-11T00:15:41.168457+00:00 sha1=772904f793113782bf9cc398ad20f87cefdc018c
CONTENT_OMITTED toc_only=true
FILE_END id=file_024b28a37d29

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=94 bytes=3162 mtime=2026-04-11T00:15:52.626055+00:00 sha1=b9acd032350a262fad7d0995116e5686b8fa2191
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
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=70 bytes=4536 mtime=2026-04-11T02:57:50.282657+00:00 sha1=49f182ecde4e634b51130172a7a7d4e78ac48ee1
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
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=23 bytes=1082 mtime=2026-04-11T01:25:28.436758+00:00 sha1=43293ddbefe17288e0cea85c402cff9f4ed05cea
CONTENT_OMITTED toc_only=true
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=14 bytes=287 mtime=2026-04-11T03:14:23.819547+00:00 sha1=71b173ae91c93ed58cf9027ce03c8ed12ae79b4f
CONTENT_OMITTED toc_only=true
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.794384+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CONTENT_OMITTED toc_only=true
FILE_END id=file_0858a02cf53f

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
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1624 mtime=2026-04-10T23:50:11.304033+00:00 sha1=92934bdfcac044ab34842a1b0131524ead5e2e5b
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
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=68 bytes=2890 mtime=2026-04-11T02:30:31.368152+00:00 sha1=ea66d1b4ed6f174f17b752f28ac358093fb784d2
CONTENT_OMITTED toc_only=true
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=114 bytes=4693 mtime=2026-04-11T01:41:16.589576+00:00 sha1=69a61b75c7697979c8e4ab560e0325f71bd7151d
CONTENT_OMITTED toc_only=true
FILE_END id=file_4efb6293109d

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=5 bytes=138 mtime=2026-04-11T02:58:40.247024+00:00 sha1=19d69e551321040a8c49f683ffcfae2bfbaed5cb
CONTENT_OMITTED toc_only=true
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CONTENT_OMITTED toc_only=true
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=380 bytes=15779 mtime=2026-04-11T02:42:28.056925+00:00 sha1=2dba92559cf404d5e91df067a8fd72b6a965ec8c
CONTENT_OMITTED toc_only=true
FILE_END id=file_c3916196f58f

---
<a id="file_aa78525fb574"></a>
FILE_START id=file_aa78525fb574 path=contexto.md domain=docs lang=markdown lines=11768 bytes=476520 mtime=2026-04-11T23:21:55.013173+00:00 sha1=0d645fa9533d2391cd96326f9b68af5d91607a73
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
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=27 bytes=824 mtime=2026-04-11T03:09:58.961110+00:00 sha1=cf2b6e50daab5aa1b974f11af667be601738252b
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
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=52 bytes=1722 mtime=2026-04-11T03:13:56.439267+00:00 sha1=7dd7ff3a9bf3b72409e48c7e7e770ef8985daba2
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
