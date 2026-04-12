# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-12T00:58:07.415358+00:00
root: template_inicío_de_projeto
mode: full
profile: ai-default
file_count: 47
byte_count: 616871
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
  - `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
  - `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
  - `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
  - `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
  - `contexto.md` -> [file_aa78525fb574](#file_aa78525fb574)
  - `contexto_toc.md` -> [file_9d2a5d7128b5](#file_9d2a5d7128b5)
  - `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
  - `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
  - `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
  - `planos/roadmap_reactive_hok_v2_v3.md` -> [file_44c34e6237da](#file_44c34e6237da)
  - `planos/walkthrough_hok_triad.md` -> [file_6a4bd0586b20](#file_6a4bd0586b20)
- `source`:
  - `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
  - `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
  - `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
  - `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
  - `.context/_scripts/lint_wiki.py` -> [file_ab41b07fb3fb](#file_ab41b07fb3fb)
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
- `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
- `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
- `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
- `.context/_scripts/lint_wiki.py` -> [file_ab41b07fb3fb](#file_ab41b07fb3fb)
- `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
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
- `contexto_toc.md` -> [file_9d2a5d7128b5](#file_9d2a5d7128b5)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package-lock.json` -> [file_fa288d1472d2](#file_fa288d1472d2)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
- `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
- `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
- `planos/roadmap_reactive_hok_v2_v3.md` -> [file_44c34e6237da](#file_44c34e6237da)
- `planos/walkthrough_hok_triad.md` -> [file_6a4bd0586b20](#file_6a4bd0586b20)
- `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

## SYMBOL_INDEX
- `.context/_scripts/cleanup_specs.py`:
  - `get_specs`
  - `archive_spec`
  - `cleanup`
- `.context/_scripts/context_oracle.py`:
  - `build_index`
  - `query_oracle`
- `.context/_scripts/harness_runner.py`:
  - `check_schema_contract`
  - `check_handoff_integrity`
  - `log_harness`
  - `main`
- `.context/_scripts/health_sync.py`:
  - `count_journal_metrics`
  - `count_schema_tables`
  - `estimate_tokens`
  - `update_dashboard`
- `.context/_scripts/lint_wiki.py`:
  - `find_raw_sources`
  - `suggest_source`
  - `check_wiki`
- `.context/_scripts/purge_journal.py`:
  - `parse_entries`
  - `purge_journal`
- `.context/_scripts/sync_project.py`:
  - `get_package_deps`
  - `get_schema_tables`
  - `sync_requirements`
- `.context/_scripts/validate_context.py`:
  - `check_files`
  - `check_journal_lines`
  - `estimate_tokens`
  - `check_registry_structure`
  - `check_specs_structure`
  - `validate`
- `captura_projeto.py`:
  - `is_text_file`
  - `is_sensitive_file`
  - `classify_domain`
  - `should_include_profile`
  - `mask_sensitive`
  - `extract_symbols`
  - `extract_imports`
  - `chunk_content`
  - `make_file_id`
  - `collect_files`
  - `mode_name`
  - `render_frontmatter`
  - `render_index_by_domain`
  - `render_index_by_path`
  - `render_symbols`
  - `render_imports`
  - `pick_fence`
  - `render_file_record`
  - `generate_context_markdown`
  - `write_output`
  - `parse_args`
  - `main`
  - `BundleConfig`
  - `Chunk`
  - `FileRecord`
- `run_context.py`:
  - `run_script`
  - `main`
- `tests/test_context.py`:
  - `TestContextGovernance`

## IMPORT_MAP_MIN
- `.context/_scripts/cleanup_specs.py`:
  - `os`
  - `shutil`
  - `time`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/context_oracle.py`:
  - `re, sys, json, os`
  - `from pathlib import Path`
  - `from collections import Counter`
- `.context/_scripts/harness_runner.py`:
  - `os, re, sys, json`
  - `from pathlib import Path`
- `.context/_scripts/health_sync.py`:
  - `re, sys, os`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/lint_wiki.py`:
  - `sys`
  - `re`
  - `argparse`
  - `from pathlib import Path`
- `.context/_scripts/purge_journal.py`:
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/sync_project.py`:
  - `json`
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/validate_context.py`:
  - `os`
  - `sys`
  - `from pathlib import Path`
- `captura_projeto.py`:
  - `argparse`
  - `hashlib`
  - `logging`
  - `mimetypes`
  - `os`
  - `re`
  - `from __future__ import annotations`
  - `from dataclasses import dataclass`
  - `from datetime import datetime, timezone`
  - `from fnmatch import fnmatch`
  - `from pathlib import Path`
- `run_context.py`:
  - `sys`
  - `subprocess`
  - `from pathlib import Path`
- `tests/test_context.py`:
  - `unittest`
  - `os`
  - `shutil`
  - `tempfile`
  - `subprocess`
  - `sys`
  - `from pathlib import Path`

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CHUNK_START id=82cd6bde54ff_c001 start_line=1 end_line=71
```python
#!/usr/bin/env python3
"""
🧹 cleanup_specs.py
Gerencia a efemeridade da bancada de trabalho (.specs/).
Aplica a regra de 48h de inatividade e limite de 3 specs ativas simultâneas.
Arquiva specs excedentes ou obsoletas em _archive_context/specs/.
"""
import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# Caminhos base
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "specs"

# Configurações
MAX_INACTIVITY_SECONDS = 48 * 3600  # 48 horas
MAX_ACTIVE_SPECS = 3

def get_specs():
    if not SPECS_DIR.exists():
        return []
    return [d for d in SPECS_DIR.iterdir() if d.is_dir()]

def archive_spec(spec_path):
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{spec_path.name}_{timestamp}"
    dest_path = ARCHIVE_DIR / archive_name
    
    print(f"[INFO] Arquivando spec: {spec_path.name} -> {archive_name}")
    shutil.move(str(spec_path), str(dest_path))

def cleanup():
    specs = get_specs()
    if not specs:
        print("[OK] Nenhuma spec ativa encontrada.")
        return

    now = time.time()
    active_specs = []

    # 1. Limpeza por inatividade (48h)
    for spec in specs:
        last_mod = max(os.path.getmtime(root) for root, _, _ in os.walk(spec))
        if (now - last_mod) > MAX_INACTIVITY_SECONDS:
            print(f"[AUTO] Inatividade detectada (>48h) em: {spec.name}")
            archive_spec(spec)
        else:
            active_specs.append(spec)

    # 2. Limpeza por limite de volume (Max 3)
    # Ordena por data de modificação (mais antiga primeiro)
    active_specs.sort(key=lambda s: max(os.path.getmtime(root) for root, _, _ in os.walk(s)))
    
    while len(active_specs) > MAX_ACTIVE_SPECS:
        oldest = active_specs.pop(0)
        print(f"[AUTO] Limite de volume excedido (Max {MAX_ACTIVE_SPECS}). Removendo spec mais antiga: {oldest.name}")
        archive_spec(oldest)

    print(f"[OK] Manutencao de specs concluida. Specs ativas: {len(active_specs)}/{MAX_ACTIVE_SPECS}")

if __name__ == "__main__":
    try:
        cleanup()
    except Exception as e:
        print(f"[ERROR] Falha na limpeza de specs: {e}")

```
CHUNK_END id=82cd6bde54ff_c001
FILE_END id=file_82cd6bde54ff

---
<a id="file_10081abf87e1"></a>
FILE_START id=file_10081abf87e1 path=.context/_scripts/context_oracle.py domain=source lang=python lines=69 bytes=2393 mtime=2026-04-11T23:58:41.287250+00:00 sha1=461ad9521982d5934769db35c938e5956f50a552
CHUNK_START id=10081abf87e1_c001 start_line=1 end_line=69
```python
#!/usr/bin/env python3
"""
🔍 context_oracle.py — Oráculo de consulta local (Oracle Layer)
Indexa arquivos-chave da .context/ e retorna snippets + confianca.
"""
import re, sys, json, os
from pathlib import Path
from collections import Counter

CONTEXT_DIR = Path(__file__).resolve().parents[1]
INDEX_FILES = [
    "brain/PRD.md", "brain/AGENT_REGISTRY.md", "brain/RULES.md",
    "maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md",
    "maintenance/JOURNAL.md"
]

def build_index():
    index = {}
    for rel in INDEX_FILES:
        p = CONTEXT_DIR / rel
        if not p.exists(): continue
        text = p.read_text(encoding="utf-8")
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        for w in set(words):
            index.setdefault(w, []).append(rel)
    return index

def query_oracle(question, role="unknown"):
    idx = build_index()
    keywords = set(re.findall(r'\b[a-zA-Z]{3,}\b', question.lower()))
    hits = Counter()
    for kw in keywords:
        for file in idx.get(kw, []):
            hits[file] += 1
    
    if not hits:
        return {"answer": "[WARN] Nenhuma referencia encontrada.", "confidence": 0.0, "sources": []}
    
    top_files = [f for f, _ in hits.most_common(3)]
    snippets = []
    for f in top_files:
        content = (CONTEXT_DIR / f).read_text(encoding="utf-8")
        for kw in keywords:
            idx_kw = content.lower().find(kw)
            if idx_kw != -1:
                start = max(0, idx_kw - 80)
                end = min(len(content), idx_kw + 80)
                snippets.append(f"DOC {f}: `...{content[start:end].strip()}...`")
                break
                
    conf = min(1.0, len(snippets) * 0.35)
    return {
        "answer": "\n".join(snippets) or "[WARN] Nenhuma referencia direta encontrada.",
        "confidence": conf,
        "sources": top_files
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python context_oracle.py \"sua pergunta aqui\"")
        sys.exit(1)
    # Ensure Windows compatibility by not printing raw json if it contains unmappable chars
    res = query_oracle(sys.argv[1], os.environ.get("AGENT_ROLE", "manual"))
    try:
        print(json.dumps(res, indent=2, ensure_ascii=True))
    except Exception as e:
        print(f"[ERROR] Fail encoding json: {e}")
        
    sys.exit(0 if res["confidence"] >= 0.5 else 2)

```
CHUNK_END id=10081abf87e1_c001
FILE_END id=file_10081abf87e1

---
<a id="file_1edef35c2f56"></a>
FILE_START id=file_1edef35c2f56 path=.context/_scripts/harness_runner.py domain=source lang=python lines=71 bytes=2948 mtime=2026-04-11T23:47:14.164982+00:00 sha1=63ebba7b487cadc471a87b4313d6dd668be01957
CHUNK_START id=1edef35c2f56_c001 start_line=1 end_line=71
```python
#!/usr/bin/env python3
"""
🛡️ harness_runner.py — Validação reativa de contratos (Harness Layer)
Valida spec vs schema, PRD vs código, e integridade de handoffs.
"""
import os, re, sys, json
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
JOURNAL = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SCHEMA = CONTEXT_DIR / "maintenance" / "schema.sql"
HARNESS_REG = CONTEXT_DIR / "brain" / "HARNESS_REGISTRY.md"

def check_schema_contract(spec_path):
    """Valida se campos/tabelas da spec existem no schema.sql"""
    if not spec_path.exists() or not SCHEMA.exists():
        return True, "Schema/spec indisponivel (skip)"
    spec_text = spec_path.read_text(encoding="utf-8")
    schema_text = SCHEMA.read_text(encoding="utf-8")
    tables_spec = set(re.findall(r'`(tabela|table)[\s_]+(\w+)', spec_text, re.I))
    tables_schema = set(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[\"\']?(\w+)', schema_text, re.I))
    
    # We only care about the table name captured in group 2 for specs if the matched syntax was used.
    # A robust extraction gets just the table name.
    spec_tnames = {t[1] for t in tables_spec}
    missing = spec_tnames - tables_schema
    if missing:
        return False, f"Spec pede tabelas inexistentes: {missing}"
    return True, "Schema contract OK"

def check_handoff_integrity(journal_text):
    """Verifica se handoffs recentes estao completos"""
    handoffs = re.findall(r'\[handoff:(.*?)\]', journal_text)
    incomplete = [h for h in handoffs if h.count('|') < 2]
    if incomplete:
        return False, f"Handoff incompleto detectado: {incomplete}"
    return True, "Handoffs integros"

def log_harness(status, detail, spec_name="unknown"):
    """Registra no JOURNAL.md de forma compacta e atomica"""
    entry = f"\n## [HARNESS-{status.upper()}] Report | spec:{spec_name}\n- **Detalhe:** {detail}\n"
    try:
        tmp = JOURNAL.with_suffix(".tmp")
        content = JOURNAL.read_text(encoding="utf-8") if JOURNAL.exists() else "# JOURNAL.md\n"
        tmp.write_text(content + entry, encoding="utf-8")
        tmp.replace(JOURNAL)
    except Exception as e:
        print(f"[WARN] Falha ao logar harness: {e}")

def main():
    spec_name = os.environ.get("ACTIVE_SPEC", "manual")
    spec_path = CONTEXT_DIR.parent / ".specs" / "features" / spec_name / "spec.md"
    
    checks = {
        "schema": check_schema_contract(spec_path),
        "handoff": check_handoff_integrity(JOURNAL.read_text(encoding="utf-8") if JOURNAL.exists() else "")
    }
    
    fails = [f"{k}: {v[1]}" for k, v in checks.items() if not v[0]]
    if fails:
        detail = " | ".join(fails)
        log_harness("fail", detail, spec_name)
        print(f"[ERROR] Harness fail: {detail}")
        sys.exit(1)
    
    log_harness("pass", "All contracts valid", spec_name)
    print("[OK] Harness pass: Contracts validated.")
    sys.exit(0)

if __name__ == "__main__":
    main()

```
CHUNK_END id=1edef35c2f56_c001
FILE_END id=file_1edef35c2f56

---
<a id="file_a642d240b9ab"></a>
FILE_START id=file_a642d240b9ab path=.context/_scripts/health_sync.py domain=source lang=python lines=96 bytes=3545 mtime=2026-04-12T00:32:26.386283+00:00 sha1=4b5cc36c7151dafd78e0312bb6be54075e68bf02
CHUNK_START id=a642d240b9ab_c001 start_line=1 end_line=96
```python
#!/usr/bin/env python3
"""
📊 health_sync.py — Atualizador Dinâmico do Dashboard (Fase 2)
Gera a tabela de métricas em CONTEXT_HEALTH.md baseada na realidade física do repositório.
"""
import re, sys, os
from pathlib import Path
from datetime import datetime

CONTEXT_DIR = Path(__file__).resolve().parents[1]
HEALTH_PATH = CONTEXT_DIR / "monitoring" / "CONTEXT_HEALTH.md"
JOURNAL_PATH = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SCHEMA_PATH = CONTEXT_DIR / "maintenance" / "schema.sql"

def count_journal_metrics():
    if not JOURNAL_PATH.exists(): return 0, 0, "No Data"
    text = JOURNAL_PATH.read_text(encoding="utf-8")
    lines = len(text.splitlines())
    chars = len(text)
    
    # Busca a última entrada do Harness
    harness_matches = re.findall(r'\[HARNESS-(FAIL|PASS)\]', text)
    last_harness = harness_matches[-1] if harness_matches else "N/A"
    
    return lines, chars, last_harness

def count_schema_tables():
    if not SCHEMA_PATH.exists(): return 0
    text = SCHEMA_PATH.read_text(encoding="utf-8")
    tables = re.findall(r'CREATE\s+TABLE', text, re.I)
    return len(tables)

def estimate_tokens():
    total_chars = 0
    # Vasculha todos os arquivos do contexto
    for root, _, files in os.walk(CONTEXT_DIR):
        for file in files:
            p = Path(root) / file
            if p.suffix in {'.md', '.py', '.sql', '.sh'}:
                try:
                    total_chars += len(p.read_text(encoding="utf-8"))
                except: pass
    return total_chars // 4

def update_dashboard():
    j_lines, j_chars, harness = count_journal_metrics()
    tables = count_schema_tables()
    tokens = estimate_tokens()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Determinar status heurísticos
    lines_status = "[OK]" if j_lines < 550 else "[WARN] Limpar!"
    chars_status = "[OK]" if j_chars < 45000 else "[WARN] Pesado"
    tokens_status = "[OK]" if tokens < 100000 else "[WARN] Context Bloat"
    harness_status = f"[{harness}]" if harness != "N/A" else "N/A"
    
    table_content = f"""<!-- HEALTH_TABLE_START -->
| Metrica | Valor Atual | Limite Ideal | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Manutencao** | | | | |
| Linhas do Journal | {j_lines} | 600 | Tracker | {lines_status} |
| Carga do Journal | {j_chars // 1000}k chars | 50k chars | Tracker | {chars_status} |
| **Cognitivo** | | | | |
| Estimativa Tokens | ~{tokens // 1000}k | 128k (Max) | Eficiencia | {tokens_status} |
| **Consistencia** | | | | |
| Tabelas no Schema | {tables} | N/A | DB-First | [OK] |
| Ultimo Harness | Role Check | Pass/Fail | Integridade | {harness_status} |
| Ultima Sincronia | {now} | Real-Time | Automacao | [OK] |
<!-- HEALTH_TABLE_END -->"""

    # Ler o arquivo atual e substituir a tabela usando regex
    if not HEALTH_PATH.exists():
        print(f"[ERROR] {HEALTH_PATH.name} não encontrado.")
        return
        
    content = HEALTH_PATH.read_text(encoding="utf-8")
    new_content = re.sub(
        r'<!-- HEALTH_TABLE_START -->.*?<!-- HEALTH_TABLE_END -->',
        table_content,
        content,
        flags=re.DOTALL
    )
    
    # Atualizar metadado de update se existir
    new_content = re.sub(
        r'(Última Atualização:|Ultima Atualizacao:).*',
        f'Ultima Atualizacao: {now}',
        new_content
    )
    
    HEALTH_PATH.write_text(new_content, encoding="utf-8")
    print(f"[OK] {HEALTH_PATH.name} atualizado (Tokens: ~{tokens//1000}k, Linhas: {j_lines}).")

if __name__ == "__main__":
    update_dashboard()

```
CHUNK_END id=a642d240b9ab_c001
FILE_END id=file_a642d240b9ab

---
<a id="file_ab41b07fb3fb"></a>
FILE_START id=file_ab41b07fb3fb path=.context/_scripts/lint_wiki.py domain=source lang=python lines=97 bytes=4141 mtime=2026-04-12T00:24:32.722433+00:00 sha1=24366d0cb8d5600c06dbb9d9a7e8d0f89470a576
CHUNK_START id=ab41b07fb3fb_c001 start_line=1 end_line=97
```python
#!/usr/bin/env python3
"""
📖 lint_wiki.py — Validacao Epistemologica (Karpathy Layer)
Fase 2: Modo Strict + Sugestao Automatica de Fonte.
"""
import sys
import re
import argparse
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "raw"
WIKI_DIRS = [CONTEXT_DIR / "brain", CONTEXT_DIR / "maintenance"]

# Regex refinado para capturar claims técnicos, ignorando headers e metadados
# Captura frases que parecem afirmações técnicas (ex: "O sistema usa X para Y.")
CLAIM_REGEX = re.compile(
    r'^(?![\s\-\*#>])'                      # Não começa com espaço, lista ou header
    r'([A-ZÁÉÍÓÚÂÊÎÔÛÃÕÇ][a-záéíóúâêîôûãõç\s,]{15,}'  # Começa com maiúscula + texto longo
    r'(?:utiliza|implementa|segue|requer|garante|valida|integra|usa|e|é)\s'  # Verbo técnico chave
    r'.+?\.)',                              # Termina com ponto
    re.MULTILINE
)

def find_raw_sources():
    """Lista arquivos na inbox raw para sugestão."""
    if not RAW_DIR.exists(): return []
    return [f.name for f in RAW_DIR.iterdir() if f.suffix == '.md']

def suggest_source(claim_text, raw_files):
    """Heurística simples: busca palavras-chave do claim nos nomes dos arquivos raw."""
    words = set(re.findall(r'\b\w{5,}\b', claim_text.lower()))
    # Palavras comuns de ignorar
    ignore = {'deve', 'como', 'para', 'sistema', 'projeto', 'este', 'esta', 'ser', 'com', 'sobre'}
    words -= ignore
    
    if not words: return None
    
    matches = []
    for raw_file in raw_files:
        file_lower = raw_file.lower()
        if any(w in file_lower for w in words):
            matches.append(f"raw/{raw_file}")
            
    return matches[0] if matches else None

def check_wiki(strict=False):
    """Varre a wiki em busca de claims sem citação."""
    raw_files = find_raw_sources()
    issues = []
    
    for d in WIKI_DIRS:
        if not d.exists(): continue
        for f in d.rglob("*.md"):
            # Ignora archive e o próprio lint report se existir
            if "_archive" in str(f) or "lint_report" in str(f): continue
            
            text = f.read_text(encoding="utf-8")
            
            # Pula arquivos raiz de documentação geral (opcional, mas recomendado)
            if f.name in ["README.md", "MASTER_FLOW.md", "RULES.md", "CONTEXT_HEALTH.md", "rebuild_guide.md"]: continue

            for match in CLAIM_REGEX.finditer(text):
                claim = match.group(0)
                # Verifica se há citação próxima (janela de -150 a +250 chars)
                start_idx = max(0, match.start() - 150)
                end_idx = min(len(text), match.start() + 250)
                context_window = text[start_idx:end_idx]
                if "> Fonte:" not in context_window and "SSOT" not in text:
                    suggestion = suggest_source(claim, raw_files)
                    
                    error_msg = f"[WARN] [{f.name}] Claim sem fonte: '{claim[:50]}...'"
                    if suggestion:
                        error_msg += f"\n   [DICA] Sugestao: Adicione '> Fonte: {suggestion}'"
                    else:
                        error_msg += f"\n   [DICA] Crie um arquivo em raw/ ou use '> Fonte: raw/novo.md'"
                    
                    issues.append(error_msg)

    if issues:
        print("\n[LINT] Wiki Report:")
        print("\n".join(issues))
        if strict:
            print("\n[FATAL] Commits bloqueados por falta de epistemologia. Resolva os claims acima.")
            sys.exit(1)
        else:
            print("\n[WARN] Warning: Verifique as citacoes para manter a qualidade documental.")
            sys.exit(0) # Não trava o pipeline em warn-mode
    else:
        print("[OK] Wiki limpa: Epistemologia em dia.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint de Citacoes e Epistemologia")
    parser.add_argument("--strict", action="store_true", help="Bloqueia o pipeline se houver erros")
    args = parser.parse_args()
    check_wiki(strict=args.strict)

```
CHUNK_END id=ab41b07fb3fb_c001
FILE_END id=file_ab41b07fb3fb

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=74 bytes=2507 mtime=2026-04-11T00:15:41.168457+00:00 sha1=772904f793113782bf9cc398ad20f87cefdc018c
CHUNK_START id=024b28a37d29_c001 start_line=1 end_line=74
```python
#!/usr/bin/env python3
"""
🗜️ purge_journal.py
Arquiva 70% das entradas mais antigas do JOURNAL.md.
Mantém 30% mais recentes como semente. Backup automático e escrita atômica.
"""
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
JOURNAL_FILE = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "journals"
KEEP_RATIO = 0.3  # 30% mais recentes

def parse_entries(content):
    # Divide por headers markdown (## 📅, ##, etc.) mantendo o header na entrada
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]

def purge_journal():
    if not JOURNAL_FILE.exists():
        print("[WARN] JOURNAL.md nao encontrado. Nada a fazer.")
        return

    content = JOURNAL_FILE.read_text(encoding="utf-8")
    entries = parse_entries(content)

    if len(entries) <= 1:
        print("[INFO] Poucas entradas para purgar.")
        return

    keep_count = max(1, int(len(entries) * KEEP_RATIO))
    archive_entries = entries[:-keep_count]
    keep_entries = entries[-keep_count:]

    # Garante diretório de arquivo
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Backup com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_file = ARCHIVE_DIR / f"journal_archive_{timestamp}.md"
    archive_content = f"# Arquivo de Journal - {timestamp}\n\n" + "\n\n".join(archive_entries) + "\n"
    archive_file.write_text(archive_content, encoding="utf-8")

    # Nova semente
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    seed = f"""---
Criado em: {now}
Ultima Atualizacao: {now}
Status: Ativo
Nota: Semente pos-purge. {len(archive_entries)} entradas arquivadas em {archive_file.name}.
---

# JOURNAL.md (Memoria Curta)
> Mantido por purge_journal.py. Limite heuristico de caracteres atingido.

""" + "\n\n".join(keep_entries) + "\n"

    # Escrita atomica (previne corrupcao se interrupcao ocorrer)
    temp_file = JOURNAL_FILE.with_suffix(".tmp")
    temp_file.write_text(seed, encoding="utf-8")
    temp_file.replace(JOURNAL_FILE)

    print(f"[OK] Purge concluido.")
    print(f"[OK] Arquivadas: {len(archive_entries)} entradas -> {archive_file.name}")
    print(f"[OK] Mantidas: {len(keep_entries)} entradas mais recentes.")

if __name__ == "__main__":
    try:
        purge_journal()
    except Exception as e:
        print(f"[ERROR] Erro no purge: {e}")

```
CHUNK_END id=024b28a37d29_c001
FILE_END id=file_024b28a37d29

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=94 bytes=3162 mtime=2026-04-11T00:15:52.626055+00:00 sha1=b9acd032350a262fad7d0995116e5686b8fa2191
CHUNK_START id=f122711ba9e1_c001 start_line=1 end_line=94
```python
#!/usr/bin/env python3
"""
🔄 sync_project.py
Sincroniza TECH_REQUIREMENTS.md com package.json e schema.sql.
Usa marcadores <!-- AUTO-SYNC START/END --> para preservar edicoes humanas.
"""
import json
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQ_FILE = CONTEXT_DIR / "maintenance" / "TECHNICAL_REQUIREMENTS.md"
PKG_FILE = CONTEXT_DIR.parent / "package.json"
SCHEMA_FILE = CONTEXT_DIR / "maintenance" / "schema.sql"

AUTO_START = "<!-- AUTO-SYNC START -->"
AUTO_END = "<!-- AUTO-SYNC END -->"

def get_package_deps():
    if not PKG_FILE.exists(): return {"dependencies": {}, "devDependencies": {}}
    try:
        with open(PKG_FILE, 'r', encoding='utf-8') as f:
            pkg = json.load(f)
        return {
            "dependencies": pkg.get("dependencies", {}),
            "devDependencies": pkg.get("devDependencies", {})
        }
    except Exception as e:
        print(f"[WARN] Erro ao ler package.json: {e}")
        return {"dependencies": {}, "devDependencies": {}}

def get_schema_tables():
    if not SCHEMA_FILE.exists(): return []
    content = SCHEMA_FILE.read_text(encoding="utf-8")
    # Regex para extrair nomes de tabelas
    return list(set(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["\']?(\w+)["\']?', content, re.IGNORECASE)))

def sync_requirements():
    deps = get_package_deps()
    tables = get_schema_tables()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    block = [
        AUTO_START,
        f"*🤖 Atualizado automaticamente em {now}*",
        ""
    ]

    if deps.get("dependencies"):
        block.append("### Dependencias (package.json)")
        for dep, ver in deps["dependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if deps.get("devDependencies"):
        block.append("### DevDependencies")
        for dep, ver in deps["devDependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if tables:
        block.append("### Tabelas no Schema (schema.sql)")
        for t in sorted(tables):
            block.append(f"- `{t}`")
        block.append("")

    block.append(AUTO_END)
    auto_content = "\n".join(block) + "\n"

    if not REQ_FILE.exists():
        REQ_FILE.write_text(f"# TECHNICAL_REQUIREMENTS.md\n\n{auto_content}", encoding="utf-8")
        print("[OK] TECHNICAL_REQUIREMENTS.md criado.")
        return

    content = REQ_FILE.read_text(encoding="utf-8")
    start_idx = content.find(AUTO_START)
    end_idx = content.find(AUTO_END)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + auto_content + content[end_idx + len(AUTO_END):]
    else:
        new_content = content.rstrip() + "\n\n" + auto_content

    REQ_FILE.write_text(new_content, encoding="utf-8")
    print("[OK] TECHNICAL_REQUIREMENTS.md sincronizado.")
    print(f"[OK] {len(deps.get('dependencies', {}))} deps | {len(tables)} tabelas detectadas.")

if __name__ == "__main__":
    try:
        sync_requirements()
    except Exception as e:
        print(f"[ERROR] Erro no sync: {e}")

```
CHUNK_END id=f122711ba9e1_c001
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=106 bytes=3827 mtime=2026-04-11T02:29:28.743870+00:00 sha1=e6e9a29604fb4a340a2335bbca07488c56baff2a
CHUNK_START id=1077e9084ea1_c001 start_line=1 end_line=106
```python
#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade com AGENT_REGISTRY.md.
"""
import os
import sys
from pathlib import Path

# Caminhos relativos a localização deste script (.context/_scripts/)
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

# Mapeamento para estrutura em camadas
REQUIRED_FILES = [
    "brain/RULES.md", 
    "brain/MASTER_FLOW.md", 
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md", 
    "maintenance/JOURNAL.md", 
    "maintenance/schema.sql", 
    "maintenance/TECHNICAL_REQUIREMENTS.md"
]

JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000  # ~100k tokens

def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]

def check_journal_lines():
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists(): return 0, True
    lines = journal.read_text(encoding="utf-8").splitlines()
    return len(lines), len(lines) <= JOURNAL_MAX_LINES

def estimate_tokens():
    total_chars = 0
    for f in REQUIRED_FILES:
        path = CONTEXT_DIR / f
        if path.exists():
            total_chars += len(path.read_text(encoding="utf-8", errors="ignore"))
    return total_chars, total_chars < TOKEN_WARN_THRESHOLD_CHARS

def check_registry_structure():
    registry = CONTEXT_DIR / "brain/AGENT_REGISTRY.md"
    if not registry.exists(): return False, "Arquivo ausente"
    content = registry.read_text(encoding="utf-8")
    if "| Role |" not in content and "| Role" not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"

def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists(): return True, "Workshop inativo (OK)"
    
    features_dir = specs_dir / "features"
    if not features_dir.exists(): return False, "Diretorio features ausente no .specs"
    
    # Verifica se algum STATE.md esta presente em specs ativas
    active_specs = [d for d in features_dir.iterdir() if d.is_dir()]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
            
    return True, f"OK ({len(active_specs)} specs ativas)"

def validate():
    print("--- Iniciando validacao de contexto (v2.2 Premium+) ---")
    issues = []

    missing = check_files()
    if missing: issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else: print("[OK] Todos os arquivos obrigatorios presentes.")

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok: issues.append(f"[WARN] .specs/: {spec_msg}")
    else: print(f"[OK] .specs/: {spec_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok: issues.append(f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}")
    else: print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, token_ok = estimate_tokens()
    est_tokens = total_chars // 4
    if not token_ok:
        issues.append(f"[WARN] Contexto estimado alto: ~{est_tokens}k tokens. Execute purge.")
    else: print(f"[OK] Estimativa de contexto segura: ~{est_tokens}k tokens")

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok: issues.append(f"[WARN] AGENT_REGISTRY.md: {reg_msg}")
    else: print("[OK] AGENT_REGISTRY.md estrutura valida.")

    print("\n--- Relatorio Final ---")
    if not issues:
        print("[SUCCESS] Contexto integro. Pronto para execucao.")
    else:
        for issue in issues: print(issue)
        print("[ALERT] Resolva os alertas antes de gerar codigo.")

if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        sys.exit(1)

```
CHUNK_END id=1077e9084ea1_c001
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=97 bytes=7180 mtime=2026-04-11T02:28:38.100881+00:00 sha1=3232fd65b8b05382d366aa1a8890e6385eb7f705
CHUNK_START id=e7c17acb71ff_c001 start_line=1 end_line=97
````markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Testes unitários/E2E, edge cases, cobertura, mocks, TDD | `tests/`, `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (apenas leitura para bugs) | `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (critérios de aceite) | "testar", "validar", "cobertura", "mock", "edge case", "TDD", "bug" |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@spec-driver` | Criação e orquestração de specs atômicas | `.specs/` (leitura/gravação temporária) | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (tail 30) | "inicie specify", "crie spec", "modo híbrido" |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |

💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Carregar APENAS: Global + Role-Specific + Task-Ephemeral
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*

````
CHUNK_END id=e7c17acb71ff_c001
FILE_END id=file_e7c17acb71ff

---
<a id="file_4b29e274836e"></a>
FILE_START id=file_4b29e274836e path=.context/brain/HARNESS_REGISTRY.md domain=docs lang=markdown lines=20 bytes=1180 mtime=2026-04-11T23:46:58.142679+00:00 sha1=5a29edb2d353e3117e7e904191ef4dadfd322309
CHUNK_START id=4b29e274836e_c001 start_line=1 end_line=20
```markdown
---
Criado em: 2026-04-11
Status: Ativo
---

# 🛡️ HARNESS_REGISTRY.md
> Superfície de controle para validação de contratos e reação automática.

## 📋 Tabela de Harnesses Ativos
| ID | Tipo | Escopo | Contrato/Schema | Gatilho | Validação | Fallback |
|----|------|--------|-----------------|---------|-----------|----------|
| `H01` | Schema | DB/Queries | `maintenance/schema.sql` | `@db-architect`, `@backend` | Campos existem? Tipos compatíveis? | `@db` cria migration |
| `H02` | AI/LLM | Outputs/Specs | `spec.md` + `PRD.md` | `@spec-driver`, `@frontend` | JSON válido? Critérios cobertos? | `@qa` revalida |
| `H03` | Handoff | Cross-Role | `JOURNAL.md` tags | Troca de domínio | Handoff registrado? Estado limpo? | Pausa + alerta |
| `H04` | Secrets | Segurança | Regex + `.env.example` | Commit/Spec | Zero chaves hardcoded | Rejeita + scrub |

## ⚙️ Regras de Execução
- ✅ `harness_runner.py` deve rodar antes de qualquer merge ou geração de código produtivo.
- ⚠️ Falha consecutiva >2x → pausa automática + log em `JOURNAL.md` com tag `[harness:fail]`.
- 🔒 Nunca sobrescrever `.context/` sem passar por validação de contrato.

```
CHUNK_END id=4b29e274836e_c001
FILE_END id=file_4b29e274836e

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=86 bytes=4370 mtime=2026-04-11T02:59:02.297440+00:00 sha1=06ce6786a149620314b57f8231142f652d4fc412
CHUNK_START id=d833c436f547_c001 start_line=1 end_line=86
````markdown
---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-04-10 23:28
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura do Diretório `.context/`

```text
.context/
├── 🧠 brain/                       # CAMADA COGNITIVA (The Brain)
│   ├── MASTER_FLOW.md             # Este documento
│   ├── RULES.md                   # Protocolos e "A Lei"
│   ├── AGENT_REGISTRY.md          # DNS de Roles e Permissões
│   ├── PROMPT_LIBRARY.md          # Catálogo de templates de prompts
│   ├── PRD.md                     # Requisito em execução (v2.0 - O Contrato)
│   ├── ROADMAP.md                 # Metas e fases (O Planejamento)
│   └── TLC_INTEGRATION.md         # Ponte entre Governança e Execução
│
├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
│   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Curta)
│   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e versões (Inventário)
│   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
│   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
│   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
│   ├── TESTS.md                   # Ledger de padrões e TDDs
│   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
│   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
│   └── _archive_context/          # Histórico imutável (A Biblioteca)
│
├── monitoring/             # CAMADA DE MONITORAMENTO (The Guardian)
│   └── CONTEXT_HEALTH.md   # Dashboard de saúde técnica e cognitiva
│
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── _scripts/               # CAMADA DE AUTOMACAO (The Motor)
    ├── validate_context.py        # Validador de integridade
    ├── purge_journal.py           # Gerenciador de memória (Purge)
    ├── cleanup_specs.py           # Gerenciador de efemeridade (.specs)
    └── sync_project.py            # Sincronizador de requisitos
```

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e a presença do `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões arquiteturais tomadas durante o TLC **devem** ser migradas para o `JOURNAL.md` antes da limpeza da spec.

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*

````
CHUNK_END id=d833c436f547_c001
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=67 bytes=2446 mtime=2026-04-11T01:31:37.755946+00:00 sha1=b5c06bc8a67d2a788cc8263f03971f379d04e92e
CHUNK_START id=d124f6374cab_c001 start_line=1 end_line=67
```markdown
---
Criado em: 2026-04-10 22:35
Ultima Atualizacao: 2026-04-10 22:35
Status: Ativo (EM EXECUCAO)
PRD_ID: #15
---

# 🎯 PRD: Checkout com Integração Stripe
> Implementar um fluxo de pagamento seguro e resiliente usando Stripe Elements e Webhooks para pedidos digitais.

💡 *Insight Humano: Este PRD é um contrato vivo. Ele guia o roteamento de agentes, define criterios de aceite e serve como referência para o JOURNAL.md.*

---

## 📋 1. Visão Geral
| Campo | Valor |
|-------|-------|
| **Objetivo de Negocio** | Reduzir abandono de carrinho e garantir seguranca no processamento. |
| **Publico-Alvo** | Compradores finais da plataforma. |
| **Escopo** | UI de pagamento, Geracao de Session, Webhooks de confirmacao. |
| **MVP vs Futuro** | MVP: Cartao de Credito. Futuro: Apple Pay/Google Pay. |
| **Dependencias** | Stripe API, Tabela `orders`, Variaveis de ambiente seguras. |

---

## 🎯 2. Critérios de Aceite (Definition of Done)
### Funcionais
- [ ] Usuario finaliza compra com cartao valido.
- [ ] Webhook atualiza `orders.status` para 'succeeded'.
- [ ] Erro de cartao exibe mensagem amigavel (WCAG).
- [ ] Idempotencia garantida via `event.id` do Stripe.

### Não-Funcionais
- [ ] Tempo de resposta API < 500ms.
- [ ] Nenhum segredo (Keys) hardcoded no codigo.
- [ ] Logs estruturados para auditoria.

---

## 🤖 3. Roteamento Multi-Agent
| Etapa | Role Responsável | Entregável | Gatilho de Handoff |
|-------|-----------------|------------|-------------------|
| 1. UI Checkout | `@frontend-specialist` | `StripeForm.tsx` | "UI pronta, aguarda contrato de API" |
| 2. API Stripe | `@backend-engineer` | `/api/checkout` + Webhook | "Rotas operacionais, inicia validacao" |
| 3. Testes E2E | `@qa-validator` | Suite de testes | "Cobertura >90%, edge cases validados" |

---

## 🔒 4. Context Gate (Pré-Execução)
- [ ] `maintenance/schema.sql` contem a tabela `orders`? ✅
- [ ] `maintenance/TECHNICAL_REQUIREMENTS.md` atualizado? ✅
- [ ] `maintenance/JOURNAL.md` < 550 linhas? ✅
- [ ] `brain/AGENT_REGISTRY.md` tem as roles necessarias? ✅

---

## 📊 5. Health Check Integrado
| Metrica | Valor | Status |
|---------|-------|--------|
| **Progresso** | 50% | 🟡 Em andamento |
| **Cobertura de Testes** | 92% (Simulada) | ✅ OK |
| **Divergência Schema** | 0 campos | ✅ OK |

---

## 🔄 6. Ciclo de Vida & Arquivamento
Ao concluir, mover para `_archive_context/prds/` e atualizar `ROADMAP.md`.

```
CHUNK_END id=d124f6374cab_c001
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=154 bytes=6687 mtime=2026-04-11T02:28:52.575335+00:00 sha1=aa3419c1efa08687a7c551dc44f40b504b422353
CHUNK_START id=9fe16e5591f0_c001 start_line=1 end_line=154
````markdown
---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo
---

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator`
**Gatilho:** Testes, validacao, edge cases, cobertura, mocks  
**Contexto Obrigatorio:** `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (criterios de aceite)
```text
🤖 Ativando @qa-validator | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{arquivo/feature a ser testada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{criar testes, validar edge cases ou aumentar cobertura}}
🚧 Restricoes:
- Seguir framework de testes definido em maintenance/TECHNICAL_REQUIREMENTS.md
- Mockar servicos externos; nao depender de rede real
- Cobrir happy path + 2 edge cases criticos no minimo
- Documentar falhas conhecidas no maintenance/JOURNAL.md se houver
📤 Saida Esperada:
1. Codigo dos testes (unitarios/integracao)
2. Matriz de cenarios cobertos
3. Recomendacoes de refatoracao se aplicavel
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada
2. spec.md com passos, contratos e critérios de verificação
3. STATE.md: draft → pronto para execução
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*

````
CHUNK_END id=9fe16e5591f0_c001
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.772397+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=c94f001202db_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=c94f001202db_c001
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=82 bytes=5460 mtime=2026-04-12T00:33:15.586634+00:00 sha1=270b5c863f91b42f2ef229b18bd87218d95aee53
CHUNK_START id=cd6526d17218_c001 start_line=1 end_line=82
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 23:55
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança
**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)  
> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas para garantir escala, foco e rastreabilidade.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)
Antes de gerar código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:
1. **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`
2. **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
3. **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`

> ⚠️ **Bloqueio de Execução:** Se qualquer item estiver ausente ou desatualizado, a IA deve parar e solicitar a carga correta antes de prosseguir.

---

## 🔢 2. Session Budget & Heurísticas de Token
Para evitar alucinações por *Token Bloat* (excesso de memória na janela):
- **Gatilhos de Alerta:** ~50.000 caracteres acumulados OU ~15-20 trocas densas de desenvolvimento.
- **Ação ao atingir o limite:** Disparar: *"🔄 Contexto próximo do limite de foco. Deseja que eu execute o purge do JOURNAL, arquive o PRD atual ou inicie uma nova sessão limpa com snapshot de semente?"*

---

## 🧠 3. Protocolo de Manutenção do Contexto
A IA atua como bibliotecário chefe. Consistência entre Código e Contexto é obrigatória.
- **`maintenance/JOURNAL.md`:** Apenas decisões de arquitetura, resoluções de bugs complexos e mudanças de lógica. Proibido logar erros triviais. Ao atingir ~600 linhas ou 50k chars → acionar `_scripts/purge_journal.py`.
- **`maintenance/TECHNICAL_REQUIREMENTS.md`:** Atualizar sempre que houver mudança em `package.json`, alteração de Schema ou integração de novas APIs.
- **`maintenance/rebuild_guide.md`:** Atualizar com hacks de ambiente local, CI/CD ou passos manuais de deploy.
- **`.specs/` (Workshop Efêmero):** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/`. Decisões técnicas devem migrar para o `JOURNAL.md` antes da limpeza.

---

## 🗄️ 4. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.
1. **Verificação Obrigatória:** Antes de criar UI/lógica dependente de dados, validar `maintenance/schema.sql`.
2. **Aviso de Divergência:** Se o código exigir um campo inexistente, parar e avisar: *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro gerar a migration antes de prosseguir."*

---

## 🤖 5. Comportamento do Agente (Transparência & Roteamento)
- **Ativação:** Toda tarefa complexa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`
- **Isolamento:** Carregar APENAS `Global + Role-Specific + Task-Ephemeral`. Ignorar o resto.
- **Handoff:** Cruzar 2+ domínios? Pausar → registrar no `JOURNAL.md`:  
  `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo: [ação]`
- **Context Gate (Pré-Código):** Validar antes de gerar:  
  `[ ] PRD ativo` | `[ ] schema contém estruturas` | `[ ] JOURNAL < 550 linhas` | `[ ] zero secrets hardcoded`

---

## 🔄 6. Gatilhos de Interação (Para o Usuário)
- `"Atualize o contexto"` → IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- `"Qual o estado do projeto?"` → Relatório baseado no `JOURNAL.md` + `ROADMAP.md`.
- `"Roteie esta tarefa"` → Consulta `AGENT_REGISTRY.md`, inicia ativação/handoff.
- `"Use o prompt padrão"` → Seleciona template em `brain/PROMPT_LIBRARY.md`, preenche placeholders, solicita confirmação.
- `"Inicie SPECIFY para PRD #[ID]"` → Cria `.specs/features/`, gera `spec.md` alinhado ao PRD, inicia ciclo TLC.

---

## 🚨 7. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.
---

## 🔍 8. Protocolo Oracle (Consult-Before-Act)
- Se a spec ou PRD contiver ambiguidade técnica, execute: `npm run context:oracle "sua dúvida"`
- Se `confidence < 0.5` -> pause, registre `[oracle:uncertain]` no `JOURNAL.md` e solicite clarificação humana.
- Nunca assuma. Consulte!

## 📖 9. Regra Karpathy (Citação Obrigatória)
- Todo conteúdo/decisão de arquitetura sintetizado em `.context/` DEVE ser lastreado na realidade. Idealmente deve conter `> Fonte: raw/nome-arquivo`.
- `npm run context:lint` avalia (atualmente em modo Warn-Only) se há claims de arquitetura (`implementa X`, `segue padrão Y`) sem lastro de documentação originária.
## 📊 10. Dashboard Health Sync
- Antes de processar features complexas ou abrir Specs Atômicas, verifique o `.context/monitoring/CONTEXT_HEALTH.md` para assegurar que a janela de tokens e a saúde do Journal não exigem repouso ou manutenção prévia.

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.

```
CHUNK_END id=cd6526d17218_c001
FILE_END id=file_cd6526d17218

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CHUNK_START id=450d7ec70909_c001 start_line=1 end_line=32
```markdown
---
Criado em: 2026-04-10 23:29
Ultima Atualizacao: 2026-04-10 23:29
Status: Ativo
---

# 🔗 TLC_INTEGRATION.md
> Ponte entre Governança de Longo Prazo (`.context/`) e Execução Atômica (`.specs/`).  
> 💡 *Insight Humano: O PRD diz O QUÊ e POR QUÊ. A SPEC diz COMO e QUANDO. O TLC orquestra a transição.*

## 🔄 Ciclo de Vida Híbrido
1. **INTENT** → `PRD.md` ativo define escopo e critérios de aceite.
2. **SPECIFY** → IA cria `.specs/features/[nome]/spec.md` com passos atômicos, contratos de API/DB e testes.
3. **IMPLEMENT** → Geração de código baseada na spec. Handoffs registrados no `JOURNAL.md`.
4. **VERIFY** → Testes passam → `STATE.md` marcado como `✅ PASSED`.
5. **SYNC** → Decisões arquiteturais e lições → `JOURNAL.md`. Spec arquivada ou deletada.

## 📏 Regras de Ouro
- 🔒 **Soberania do Contexto:** `.specs/` nunca sobrescreve `.context/`. Apenas alimenta a memória de longo prazo.
- 🧹 **Efemeridade:** Spec inativa >48h ou pós-merge → mover para `_archive_context/specs/` ou deletar.
- 🤝 **Handoff:** Handoff obrigatório no `JOURNAL.md` se a spec cruzar domínios (ex: `@backend` → `@qa`).
- ⚠️ **Divergência:** Se `spec.md` divergir de `schema.sql` ou `PRD.md` → parar e solicitar correção de contexto.

## 🤖 Fluxo de Ativação
`"Inicie a fase de SPECIFY para o PRD #[ID]"` → 
1. IA lê `PRD.md` + `schema.sql` + `JOURNAL.md` (últimas 30).
2. Cria `.specs/features/[nome]/` com `spec.md` e `STATE.md: draft`.
3. Executa passos atômicos → atualiza `STATE.md`.
4. Ao concluir: `✅ Spec passed. Deseja arquivar a spec e sincronizar o JOURNAL.md?`

---
> *Este documento garante que o "Cérebro" (Contexto) e o "Músculo" (TLC) operem em harmonia.*

```
CHUNK_END id=450d7ec70909_c001
FILE_END id=file_450d7ec70909

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.800876+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=9b6470da8849_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=9b6470da8849_c001
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=48 bytes=1740 mtime=2026-04-12T00:57:55.997890+00:00 sha1=b30144cdcaf64b811d2afc9bc3be2d4446c59fea
CHUNK_START id=019509328844_c001 start_line=1 end_line=48
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# JOURNAL.md
> Log vivo de decisoes e bugs. (Max 600 linhas)

## 📅 2026-04-11 01:25
**Decisão/Bug:** 🔄 Handoff: @frontend-specialist → @backend-engineer
**Solução:** Implementada UI do CheckoutForm v1 usando Stripe Elements. Estado local gerenciado; aguardando API `/api/checkout/session`.
**Implicação:** Próximo agente deve configurar a rota backend e garantir o retorno do `clientSecret`.

## 📅 2026-04-11 01:35
**Decisão/Bug:** 🔄 Handoff: @backend-engineer → @qa-validator
**Solução:** Endpoint Stripe Session operacional. Webhook configurado para escutar `payment_intent.succeeded` e atualizar tabela `orders`.
**Implicação:** QA deve validar fluxos de falha e idempotência do webhook.

## 📅 2026-04-11 01:45
**Decisão/Bug:** ✅ Ciclo Checkout Stripe Concluído
**Solução:** Cobertura de testes em 92%. Validado happy path e 'card declined'. Injetado retry pattern no webhook.
**Implicação:** PRD #15 concluído. Tecnologias Stripe adicionadas ao env.

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## Teste Epistemológico
> Fonte: raw/stripe_docs.md
O sistema garante a idempotencia de eventos cruzado com as webhooks da Stripe.

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

```
CHUNK_END id=019509328844_c001
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=21 bytes=294 mtime=2026-04-12T00:57:55.663223+00:00 sha1=47d3bbbb69c4b355a9a7ea1c7ac26e365cfed91c
CHUNK_START id=d069d4f2ebef_c001 start_line=1 end_line=21
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

<!-- AUTO-SYNC START -->
*🤖 Atualizado automaticamente em 2026-04-11 21:57*

### DevDependencies
- `husky`: `^9.1.7`

### Tabelas no Schema (schema.sql)
- `orders`

<!-- AUTO-SYNC END -->










```
CHUNK_END id=d069d4f2ebef_c001
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.794384+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=0858a02cf53f_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=0858a02cf53f_c001
FILE_END id=file_0858a02cf53f

---
<a id="file_eaebfc593089"></a>
FILE_START id=file_eaebfc593089 path=.context/maintenance/_archive_context/raw/stripe_docs.md domain=docs lang=markdown lines=4 bytes=184 mtime=2026-04-12T00:21:42.178827+00:00 sha1=a8ca349e81fe936c2d0c8e39de0d94e9f16ae2eb
CHUNK_START id=eaebfc593089_c001 start_line=1 end_line=4
```markdown
# Documentação Webhooks do Stripe
> Fonte: stripe.com/docs

Para processar pagamentos de forma assíncrona, precisamos lidar com eventos de webhook e validar a assinatura da Stripe.

```
CHUNK_END id=eaebfc593089_c001
FILE_END id=file_eaebfc593089

---
<a id="file_618e9f7de1e8"></a>
FILE_START id=file_618e9f7de1e8 path=.context/maintenance/_archive_context/raw/template_inbox.md domain=docs lang=markdown lines=17 bytes=585 mtime=2026-04-12T00:21:32.947043+00:00 sha1=e7906c232c8df4de3d7839e53291826495d57cd8
CHUNK_START id=618e9f7de1e8_c001 start_line=1 end_line=17
````markdown
# 📚 [TÍTULO DO DOCUMENTO / FONTE]

> **Data de Adição:** YYYY-MM-DD
> **Fonte Original:** [Link ou Descrição]
> **Motivador:** Por que isto está no contexto? (Ex: Definir contrato de API, regra de negócio, base de arquitetura)

## Resumo Executivo
(Uma ou duas frases explicando do que se trata para o RAG/Oracle processar facilmente).

---

## Conteúdo / Excertos / Scripts
Cole abaixo os tutoriais cruéis, referências de código ou diretrizes invioláveis que o AGENT deve usar como "SOT" (Source of Truth) ao sintetizar soluções.

```text
(Seu conteúdo aqui...)
```

````
CHUNK_END id=618e9f7de1e8_c001
FILE_END id=file_618e9f7de1e8

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CHUNK_START id=a5c71962029a_c001 start_line=1 end_line=63
````markdown
---
Criado em: 2026-04-10 21:44
Ultima Atualizacao: 2026-04-10 21:44
Status: Ativo
---

# 🛠️ Manual de Reconstrução & Automação

Este guia contém as instruções para subir o ambiente do zero e operar as ferramentas de governança de contexto.

---

## 🏗️ 1. Setup do Ambiente

### Requisitos Mínimos:
- **Python ≥ 3.8** (Para os scripts de automação)
- **Node.js** (Para os wrappers NPM)
- **Make** (Opcional, para orquestração Unix)
- **Bash** (Para Git Bash, WSL, Linux ou macOS)

---

## ⚙️ 2. Ferramentas de Automação

O projeto oferece três formas de gerenciar a saúde do contexto. Escolha a que melhor se adapta ao seu terminal:

### Opção A: Via NPM (Recomendado para Devs Web)
```bash
npm run context:validate  # Checa integridade e tokens
npm run context:sync      # Sincroniza deps e schema
npm run context:purge     # Limpa e arquiva o log vivo
```

### Opção B: Via Make (Recomendado para CI/CD e Unix)
```bash
make validate
make sync
make purge
make all       # Executa o pipeline completo: Valida -> Sync -> Purge
```

### Opção C: Via Bash (Resiliência Universal)
```bash
./run_context.sh validate
./run_context.sh all
```

---

## 🗃️ 3. Recuperação de Contexto (Archive)

Se precisar restaurar um Journal ou PRD antigo que foi arquivado:
1. Vá até `.context/maintenance/_archive_context/`.
2. Localize o arquivo pelo timestamp `YYYYMMDD_HHMMSS`.
3. Copie o conteúdo necessário de volta para a raiz da camada correspondente (`maintenance/` ou `brain/`).

---

## 🚨 4. Troubleshooting
- **Erro de Encoding (Windows):** Todos os scripts são forçados para UTF-8. Se vir caracteres estranhos, verifique se o seu terminal suporta Unicode.
- **Python não encontrado:** No Windows, o script tenta `python3` e faz fallback para `python`. Se falhar, certifique-se que o executável está no seu PATH.

> *Lembrete: Sem automação, a documentação morre. Use as ferramentas a cada nova funcionalidade iniciada no ROADMAP.md.*

````
CHUNK_END id=a5c71962029a_c001
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=27 bytes=1336 mtime=2026-04-11T02:26:43.636538+00:00 sha1=adb37745498ccfa61a2b793c10240a2b20d3d716
CHUNK_START id=54a6a553d34b_c001 start_line=1 end_line=27
```markdown
---
Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-10 23:27
Status: Ativo
---

# 🧬 rx-anatomy.md (Raio-X de Anatomia)
> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Arquivos de decisão e regras
│   ├── maintenance/        # Logs, db schema e inventários
│   └── monitoring/         # Dashboard de saúde
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.sh          # Orquestrador universal Bash
├── init_ai_project.sh      # Bootstrapper supremo
└── package.json            # Gerenciamento de libs e scripts context:*

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `_archive_context/specs/`
- **Não é fonte da verdade.** O `.context/` permanece como SSOT.

```
CHUNK_END id=54a6a553d34b_c001
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.789386+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=ca8da4f87431_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=ca8da4f87431_c001
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CHUNK_START id=91d5627a725e_c001 start_line=1 end_line=9
```sql
-- Snapshot Real da Tabela de Pedidos
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_session_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending', -- pending, succeeded, failed
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
CHUNK_END id=91d5627a725e_c001
FILE_END id=file_91d5627a725e

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=37 bytes=1443 mtime=2026-04-12T00:57:56.400221+00:00 sha1=54848ffd6e65454bfb244baf979561b4f4065346
CHUNK_START id=068a21d64bec_c001 start_line=1 end_line=37
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-11 21:57
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

<!-- HEALTH_TABLE_START -->
| Metrica | Valor Atual | Limite Ideal | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Manutencao** | | | | |
| Linhas do Journal | 48 | 600 | Tracker | [OK] |
| Carga do Journal | 1k chars | 50k chars | Tracker | [OK] |
| **Cognitivo** | | | | |
| Estimativa Tokens | ~15k | 128k (Max) | Eficiencia | [OK] |
| **Consistencia** | | | | |
| Tabelas no Schema | 1 | N/A | DB-First | [OK] |
| Ultimo Harness | Role Check | Pass/Fail | Integridade | [PASS] |
| Ultima Sincronia | 2026-04-11 21:57 | Real-Time | Automacao | [OK] |
<!-- HEALTH_TABLE_END -->

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até que a migration seja documentada.
- **Se Turns > 18:** Propor Snapshot ou Reset de Sessão antes de iniciar próxima tarefa grande.

---

## 📅 Histórico de Saúde (Log de Purges)
| Data | Ação | Agente | Resultado |
| :--- | :--- | :--- | :--- |
| 2026-04-10 | Purge Completo | @context-keeper | Journal resetado para seed de 30 linhas. |

```
CHUNK_END id=068a21d64bec_c001
FILE_END id=file_068a21d64bec

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=26 bytes=693 mtime=2026-04-11T00:55:20.246274+00:00 sha1=163dd12b4c98d348f80986ea59afcb4604dc9e0e
CHUNK_START id=e477c4c5a96c_c001 start_line=1 end_line=26
```yaml
name: Context Health Check

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  validate-context:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run Context Validation
        # No GitHub Actions (Linux), usamos python3
        run: python3 .context/_scripts/validate_context.py

      - name: Check Journal Limits
        run: python3 .context/_scripts/validate_context.py | grep -q "SUCCESS" || (echo "❌ Contexto quebrado ou Journal excedido!" && exit 1)

```
CHUNK_END id=e477c4c5a96c_c001
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CHUNK_START id=3adfd36c1559_c001 start_line=1 end_line=9
```bash
echo "husky - DEPRECATED

Please remove the following two lines from $0:

#!/usr/bin/env sh
. \"\$(dirname -- \"\$0\")/_/husky.sh\"

They WILL FAIL in v10.0.0
"
```
CHUNK_END id=3adfd36c1559_c001
FILE_END id=file_3adfd36c1559

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=76 bytes=3579 mtime=2026-04-12T00:57:07.195915+00:00 sha1=379fdc900a4e6e8321619d3a5225e1cc536b13d9
CHUNK_START id=8ec9a00bfd09_c001 start_line=1 end_line=76
````markdown
# 🛸 Antigravity Kit v2.3 Premium+ (H.O.K. Enabled)
> **O ecossistema definitivo para engenharia AI-Ready: Governança Macro + Execução Atômica + Controle Ativo.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação. Ele unifica o **Antigravity Kit** com o **TLC Spec-Driven** e eleva a governança ao **Nível 3 (H.O.K.)**, garantindo que Propósito → Execução → Validação operem em loop fechado e autônomo.

---

## 🛡️ A Tríade H.O.K. (Governança Nível 3)
O kit evoluiu de validação passiva para **controle ativo e reativo**:
| Pilar | Função | Script | Gatilho |
|-------|--------|--------|---------|
| 🛡️ **Harness** | Bloqueia specs que violam contratos (Schema vs PRD, Handoffs incompletos) | `harness_runner.py` | `npm run context:all` / `pre-commit` |
| 🔍 **Oracle**  | RAG local `stdlib` que resolve ambiguidades antes da geração de código | `context_oracle.py` | `npm run context:oracle "dúvida"` |
| 📖 **Karpathy**| Linter epistemológico: exige `> Fonte: raw/...` em claims técnicos | `lint_wiki.py` | `npm run context:lint` (Strict no commit) |

> 💡 **Regra de Ouro:** `Se não está no .context, não existe. Se não tem fonte, é alucinação. Se não passa no Harness, não vai pro repositório.`

---

## 🚀 Instalação Ultra-Rapida (One-Click Setup)

Se voce quer inicializar este framework em um novo projeto do zero, basta rodar o nosso bootstrapper supremo:

```bash
# 1. Torne o script executavel
chmod +x init_ai_project.sh

# 2. Execute
./init_ai_project.sh
```

O script ira criar automaticamente toda a estrutura de camadas, os workshops de execução, os motores de manutenção v2.2+, e configurar a blindagem Husky.

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. PRD v2.0, Rules, Registry e a Ponte de Integração TLC.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação (v2.3)
| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Checa integridade, estrutura e estimativa de tokens |
| `npm run context:harness`  | Valida contratos ativos e handoffs (`harness_runner.py`) |
| `npm run context:oracle`   | Roteia consulta proativa ao Oráculo local (com confidence) |
| `npm run context:lint`     | Fiscaliza citações epistemológicas e claims sem fonte |
| `npm run context:all`      | 🟢 Pipeline C-Level: Validate → Sync → Cleanup → Harness → Lint(Strict) |

---

## 🤝 Protocolo de Ativação Híbrida

Para iniciar uma tarefa com poder total, use o prompt mestre:
> *"Inicie a fase de SPECIFY para o PRD #[ID] usando o modo Híbrido TLC."*

Isso ativará a role `@spec-driver` e iniciará o ciclo atômico no `.specs/` alinhado à governança do `.context/`.

---

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*

````
CHUNK_END id=8ec9a00bfd09_c001
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=121 bytes=5487 mtime=2026-04-12T00:57:17.491620+00:00 sha1=0162bca2da8aec12e1ad2f117125e0f583d3e880
CHUNK_START id=4efb6293109d_c001 start_line=1 end_line=121
````markdown
---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-11 23:30
Status: Ativo (v2.3-HOK)
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

## 🧩 Novos Pilares de Operação (v2.3+)
- **🛡️ Harness:** O pipeline aborta automaticamente se uma Spec referenciar tabelas/campos inexistentes no `schema.sql` ou se handoffs estiverem incompletos.
- **🔍 Oracle:** Ao detectar ambiguidade, execute `npm run context:oracle "sua pergunta"`. Retorno com `confidence < 0.5` pausa o fluxo e exige `[oracle:uncertain]` no `JOURNAL.md`.
- **📖 Karpathy:** Todo claim técnico adicionado ao `.context/` deve conter `> Fonte: raw/nome-arquivo.md`. O `pre-commit` roda em modo `--strict` e rejeita commits sem citação.

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria viva, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.sh`, `Makefile` | Validacao, purge, sync e orquestracao. |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `tests/test_context.py` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija antes de forcar.

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rápidos (Cheat Sheet v2.3)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Consultar Oráculo antes de assumir ambiguidades
npm run context:oracle "qual regex de validação?"

# Checar citações epistemológicas (modo manual)
npm run context:lint

# Pipeline completo (orquestrado por run_context.py, zero bash cru)
npm run context:all

# Limpar specs inativas / Sincronizar deps / Purge Journal
npm run context:cleanup
npm run context:sync
npm run context:purge
```
> 💡 *Nota:* Todos os comandos são roteados pelo `run_context.py`. Isso garante compatibilidade nativa Windows/WSL/Linux no `pre-commit`, sem dependências de shell.

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se `validate_context.py` ou `test_context.py` falharem.
- **CI/CD:** O GitHub Actions roda o pipeline em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Clone
- [ ] `.context/` existe com estrutura de camadas ok.
- [ ] `brain/RULES.md` e `brain/MASTER_FLOW.md` alinhados a stack.
- [ ] `brain/AGENT_REGISTRY.md` possui roles registradas.
- [ ] `npm run context:all` executa sem erros.

### 🚀 Inicio de Feature / PRD
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---

> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.

````
CHUNK_END id=4efb6293109d_c001
FILE_END id=file_4efb6293109d

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=11 bytes=416 mtime=2026-04-12T00:57:24.540624+00:00 sha1=9ddd807983a0b3be0e492db5fb2a29f9bfe014f8
CHUNK_START id=f6f7100f063b_c001 start_line=1 end_line=11
```markdown
# 🛸 Antigravity Kit Versioning
v2.3.0-hok
Dash: [Antigravity Kit v2.3.0-hok]
Audit Status: ✅ PASSED
Release Date: 2026-04-11

📜 Changelog:
- Nível 3 de Governança (H.O.K.) ativado.
- Harness, Oracle e Karpathy integrados ao C-Level Orchestrator (`run_context.py`).
- Pipeline `context:all` agora roda em sequência estrita e bloqueante.
- Zero dependência de bash cru no pre-commit (100% cross-platform).

```
CHUNK_END id=f6f7100f063b_c001
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CHUNK_START id=1f98938d3cd9_c001 start_line=1 end_line=140
````markdown
### 🔍 Por que um único arquivo não basta?
A IA não lê apenas um arquivo para definir comportamento. Ela avalia:
- 📁 Estrutura de pastas (`brain/`, `maintenance/`, `monitoring/`, `.specs/`)
- 🤖 `AGENT_REGISTRY.md` (ainda carregará 7 roles se existir)
- 🐍 Scripts Python e hooks do Husky (continuam ativos)
- 📜 Regras de carregamento (`Checklist de Carga` ainda exige camadas)
- 🧠 Memória de sessão (a IA tentará carregar tudo o que encontrar)

Se você só trocar o `RULES.md`, a IA ficará em **estado híbrido confuso**: regras dizem "modo leve", mas a estrutura exige validações pesadas, registry complexo e scripts de automação. Isso gera `token bloat`, alucinação e falhas de contexto gate.

---
### 🛠️ 3 Caminhos Técnicos Viáveis

| Abordagem | Como funciona | Prós | Contras |
|-----------|--------------|------|---------|
| `MODE.md` (Flag) | Arquivo simples: `MODE: LIGHT`. A IA lê primeiro e ajusta comportamento. | Zero destruição, reversível, explícito. | Exige atualização no `RULES_LIGHT.md` para ler a flag. |
| `init_ai_project_light.sh` | Bootstrap que cria estrutura mínima do zero (sem camadas, sem scripts, sem Husky). | Limpo, seguro, ideal para novos MVPs. | Não converte projetos robustos existentes. |
| `downgrade_to_light.sh` | Remove camadas, desativa Husky, arquiva scripts, substitui `RULES.md`. | Converte projeto existente sem perder histórico. | Irreversível sem backup manual. |

---
### ✅ Recomendação: `MODE.md` + `init_ai_project_light.sh`
É a combinação mais segura. Você mantém o robusto como padrão, mas pode ativar o modo leve em qualquer repositório novo ou existente com **um arquivo de flag** ou **um comando de init**.

---
### 📄 1. `MODE.md` (A Chave de Conversão)
Coloque na raiz de `.context/`. A IA **DEVE** ler este arquivo antes de qualquer checklist.

```markdown
---
Criado em: YYYY-MM-DD HH:MM
Última Atualização: YYYY-MM-DD HH:MM
Status: Ativo
---

# 🪶 MODE.md
> Define o perfil operacional do framework. A IA ajusta carregamento, roles e automação conforme este valor.

**MODE:** LIGHT  
**Reason:** MVP < 2 semanas | Time 1-2 devs | Velocidade > Governança  

💡 *Insight IA: Se MODE = LIGHT, ignore camadas, scripts, registry multi-agent e .specs/. Carregue apenas: RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql. Use @fullstack-generalist por padrão.*
```

---
### 📜 2. Patch Obrigatório no `RULES_LIGHT.md`
Adicione este bloco no **topo** do arquivo, antes de qualquer regra:

```markdown
📜 RULES_LIGHT.md — Modo Minimalista (MVP/POC)
Projeto: [NOME DO PROJETO] | Arquitetura: Single-Agent + Database-First
> 🪶 **MODO ATIVO:** Leia `MODE.md`. Se `MODE: LIGHT`, siga estritamente este protocolo enxuto. Ignore `.specs/`, scripts Python, Husky e `AGENT_REGISTRY.md`.

🛡️ Checklist de Carga (Light)
1. [ ] RULES_LIGHT.md (este arquivo)
2. [ ] PRD.md ativo
3. [ ] schema.sql atualizado
4. [ ] JOURNAL.md < 300 linhas
⚠️ Se faltar 1 item → pare e solicite correção.

🔄 Comportamento do Agente (Light)
- Role padrão: `@fullstack-generalist` (única ativa)
- Sem handoff obrigatório. Registre decisões críticas direto no JOURNAL.md
- Database-First mantido. Nunca assuma schema.
- Sem automação. Validação manual: `grep -q "schema.sql" PRD.md && echo "✅ OK"`
- Fim de sessão: `"Contexto atualizado? [S/N]"`
```

---
### 🐚 3. `init_ai_project_light.sh` (Bootstrap Seguro)
Cria uma estrutura flat, sem camadas, sem scripts, sem Husky. Ideal para `git init` de MVPs.

```bash
#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
NC='\033[0m'

[ -d ".context" ] && { echo "❌ .context/ já existe. Abortando."; exit 1; }

echo -e "\n${GREEN}🪶 Inicializando Modo LIGHT...${NC}"
mkdir -p .context

NOW=$(date +%Y-%m-%d\ %H:%M)

# MODE Flag
cat > .context/MODE.md << EOF
---
Criado em: $NOW
Status: Ativo
---
MODE: LIGHT
Reason: MVP rápido | Velocidade > Governança
💡 IA: Ignore camadas, scripts, registry e .specs/. Use apenas RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql.
EOF

# RULES_LIGHT (minimalista)
cat > .context/RULES_LIGHT.md << 'EOF'
📜 RULES_LIGHT.md — Modo Minimalista
> 🪶 MODE: LIGHT ativo. Role única: @fullstack-generalist. Sem scripts, sem Husky, sem handoff complexo.
🛡️ Carga: [ ] RULES_LIGHT.md [ ] PRD.md [ ] schema.sql [ ] JOURNAL.md <300lin
🗄️ DB-First: Valide schema antes de UI. Se faltar campo → pare e avise.
🔄 Fim de sessão: Pergunte "Atualizo contexto?" e registre no JOURNAL.md apenas mudanças de lógica/bug.
⚠️ Sem automação. Sem registry. Sem .specs/. Mantenha enxuto.
EOF

# Arquivos base
for f in PRD.md JOURNAL.md schema.sql; do
  cat > ".context/$f" << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📄 $f
EOF
done

echo -e "${GREEN}✅ Modo LIGHT pronto. Estrutura plana, sem overhead.${NC}"
echo "📖 Próximo: Preencha PRD.md e comece. A IA usará @fullstack por padrão."
```

---
### 🧠 Como a IA Interpreta Isso na Prática
1. **Início de sessão:** A IA lê `MODE.md` primeiro.
2. **Se `MODE: LIGHT`:** 
   - Ignora `brain/`, `maintenance/`, `monitoring/`, `_scripts/`, `.specs/`
   - Carrega apenas os 4 arquivos essenciais
   - Ativa `@fullstack-generalist` implicitamente
   - Desativa validações Python/Husky automaticamente
   - Usa heurística simplificada de tokens (limite ~20k chars)
3. **Se quiser voltar ao robusto:** Troque `MODE: ROBUST` e rode `npm run context:all` para restaurar camadas/scripts.

---
### 🚀 Próximo Passo
Quer que eu:
1. **Gere o `downgrade_to_light.sh`** para converter um projeto robusto existente sem perder histórico?
2. **Ajuste o `init_ai_project.sh` principal** para incluir uma flag `--light` que alterna entre os dois modos automaticamente?
3. **Entregue o `RULES_LIGHT.md` completo** (versão pronta para copiar/colar, com todos os protocolos simplificados)?

Escolha o fechamento. O framework agora tem conversão explícita, segura e reversível. 🏁
````
CHUNK_END id=1f98938d3cd9_c001
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=380 bytes=15779 mtime=2026-04-11T02:42:28.056925+00:00 sha1=2dba92559cf404d5e91df067a8fd72b6a965ec8c
CHUNK_START id=c3916196f58f_c001 start_line=1 end_line=300
```python
#!/usr/bin/env python3
"""captura_projeto.py - Gera bundle markdown AI-first do repositorio. TEMPLATE UNIVERSAL."""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path

# 🛠️ CUSTOMIZE AQUI: Padrões universais + adicione os específicos do seu projeto
PASTAS_IGNORAR = {
    ".git", "node_modules", "dist", "build", "out", "target", "bin", "obj",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache",
    ".next", ".nuxt", ".vercel", ".netlify", ".vite", ".cache",
    ".vscode", ".idea", ".cursor", "coverage", ".pytest_cache",
    "captura_projeto", # 📝 Ignorar a própria pasta do utilitário
}

PASTAS_CORE = {
    # 📝 Defina as pastas ARQUITETURALMENTE essenciais para a IA entender seu projeto
    # Ex: {"src", "lib", "api", "supabase", ".context", ".specs"}
    "src", "lib", "api", ".context", ".specs"
}

# 🛠️ CUSTOMIZE AQUI: Regras de classificação semântica (fallback seguro)
DOMAIN_RULES = {
    r"/api/|/routes/|/handlers/|/controllers/": "api",
    r"/components/|/ui/|/views/|/pages/|/screens/": "ui",
    r"/lib/|/utils/|/helpers/|/core/|/shared/": "lib",
    r"/db/|/migrations/|/models/|/schema/|/supabase/|/prisma/": "db",
    r"/tests/|/spec/|/__tests__/|\.test\.|\.spec\.": "tests",
    r"/config/|/settings/|/env/": "config",
    r"\.md$|\.rst$|\.txt$": "docs",
    r"\.(json|toml|yaml|yml|ini)$": "config",
}

EXTENSOES_PERMITIDAS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".html", ".css", ".json", ".md",
    ".yaml", ".yml", ".toml", ".sh", ".sql", ".graphql", ".vue", ".svelte",
    ".rs", ".go", ".java", ".c", ".h", ".hpp", ".cpp", ".ini",
}

LINGUAGENS = {
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".py": "python", ".html": "html", ".css": "css", ".json": "json", ".md": "markdown",
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".sh": "bash", ".sql": "sql",
    ".graphql": "graphql", ".vue": "html", ".svelte": "html", ".rs": "rust",
    ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".hpp": "cpp", ".cpp": "cpp", ".ini": "ini",
}

ARQUIVOS_SENSIVEIS_GLOBS = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx",
    "credentials*.json", "id_rsa*", "secrets.*", "*.cert",
    # 📝 Adicione padrões sensíveis do SEU projeto aqui
}

SECRET_PATTERNS = (
    re.compile(r'(["\']?)(\w*(?:API_KEY|SECRET|TOKEN|PASSWORD|AUTH_KEY|PRIVATE_KEY|ACCESS_KEY|DB_PASS|CONNECTION_STRING)\w*)\1\s*[:=]\s*["\']?(\S+)["\']?', re.IGNORECASE),
    re.compile(r'(BEGIN\s+(RSA|EC|DSA|OPENSSH|PGP)\s+PRIVATE\s+KEY)', re.IGNORECASE),
)

DEFAULT_OUTPUT = "contexto.md"
logging.basicConfig(level=logging.WARNING, format="⚠️ %(message)s")

@dataclass(frozen=True)
class BundleConfig:
    diretorio: Path
    output: str = DEFAULT_OUTPUT
    only_core: bool = False
    exclude_core: bool = False
    profile: str = "ai-default"
    toc_only: bool = False
    max_lines_per_file: int = 300
    emit_symbol_index: bool = False
    emit_import_map: bool = False
    mask_secrets: bool = False

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_line: int
    end_line: int
    content: str

@dataclass(frozen=True)
class FileRecord:
    file_id: str
    relative_path: str
    domain: str
    language: str
    line_count: int
    byte_count: int
    mtime_utc: str
    sha1: str
    symbols: tuple[str, ...]
    imports: tuple[str, ...]
    chunks: tuple[Chunk, ...]

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXTENSOES_PERMITIDAS:
        return True
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        return False
    return mime.startswith("text/") or mime in {"application/json", "application/xml", "application/javascript"}

def is_sensitive_file(path: Path) -> bool:
    return any(fnmatch(path.name.lower(), pat.lower()) for pat in ARQUIVOS_SENSIVEIS_GLOBS)

def classify_domain(relative_path: str) -> str:
    p = relative_path.lower()
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, p):
            return domain
    return "source"

def should_include_profile(record_domain: str, config: BundleConfig) -> bool:
    if config.profile == "ai-compact":
        return record_domain not in {"tests", "docs"}
    return True

def mask_sensitive(content: str, enabled: bool) -> str:
    if not enabled:
        return content
    out = content
    for pattern in SECRET_PATTERNS:
        out = pattern.sub(r"\1***", out)
    return out

def extract_symbols(content: str, suffix: str) -> tuple[str, ...]:
    symbols: list[str] = []
    if suffix == ".py":
        symbols.extend(re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content, re.MULTILINE))
        symbols.extend(re.findall(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        symbols.extend(re.findall(r"(?:export\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content))
        symbols.extend(re.findall(r"(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\s*", content))
        symbols.extend(re.findall(r"export\s+const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", content))
    seen, seen_set = [], set()
    for s in symbols:
        if s not in seen_set:
            seen.append(s)
            seen_set.add(s)
    return tuple(seen[:80])

def extract_imports(content: str, suffix: str) -> tuple[str, ...]:
    imports: list[str] = []
    if suffix == ".py":
        imports.extend(re.findall(r"^import\s+([^\n]+)", content, re.MULTILINE))
        imports.extend(re.findall(r"^from\s+([^\s]+)\s+import\s+([^\n]+)", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        imports.extend(re.findall(r"^import\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]", content, re.MULTILINE))
        imports.extend(re.findall(r"require\(['\"]([^'\"]+)['\"]\)", content))
    normalized, seen_set = [], set()
    for item in imports:
        val = f"from {item[0]} import {item[1]}" if isinstance(item, tuple) else item
        if val not in seen_set:
            normalized.append(val)
            seen_set.add(val)
    return tuple(normalized[:120])

def chunk_content(content: str, file_id: str, max_lines: int) -> tuple[Chunk, ...]:
    lines = content.splitlines()
    if not lines:
        return (Chunk(f"{file_id}_c001", 1, 1, ""),)
    if max_lines <= 0 or len(lines) <= max_lines:
        return (Chunk(f"{file_id}_c001", 1, len(lines), content),)
    chunks = []
    idx = 1
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        part = "\n".join(lines[start:end])
        if end < len(lines) or content.endswith("\n"):
            part += "\n"
        chunks.append(Chunk(f"{file_id}_c{idx:03d}", start + 1, end, part))
        idx += 1
    return tuple(chunks)

def make_file_id(relative_path: str) -> str:
    return hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:12]

def collect_files(config: BundleConfig) -> tuple[FileRecord, ...]:
    records: list[FileRecord] = []
    root = config.diretorio.resolve()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        is_root = (current == root)

        if config.only_core:
            dirnames[:] = sorted(d for d in dirnames if (d in PASTAS_CORE or not is_root) and d not in PASTAS_IGNORAR)
        elif config.exclude_core:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_CORE and d not in PASTAS_IGNORAR)
        else:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_IGNORAR)

        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root)
            rel_path = rel.as_posix()
            top = rel.parts[0] if rel.parts else ""

            if config.only_core and is_root and top not in PASTAS_CORE:
                continue
            if config.exclude_core and is_root and top in PASTAS_CORE:
                continue
            if is_sensitive_file(path):
                continue
            if not is_text_file(path):
                continue

            try:
                raw_content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    raw_content = path.read_text(encoding="latin-1")
                except OSError as e:
                    logging.warning("Pulando %s: %s", rel_path, e)
                    continue
            except OSError as e:
                logging.warning("Pulando %s: %s", rel_path, e)
                continue

            domain = classify_domain(rel_path)
            if not should_include_profile(domain, config):
                continue

            raw_sha1 = hashlib.sha1(raw_content.encode("utf-8", errors="ignore")).hexdigest()
            content = mask_sensitive(raw_content, config.mask_secrets)
            file_id = make_file_id(rel_path)
            stat = path.stat()
            suffix = path.suffix.lower()

            symbols = extract_symbols(content, suffix) if config.emit_symbol_index else ()
            imports = extract_imports(content, suffix) if config.emit_import_map else ()
            chunks = chunk_content(content, file_id, config.max_lines_per_file)

            records.append(FileRecord(
                file_id=file_id, relative_path=rel_path, domain=domain,
                language=LINGUAGENS.get(suffix, suffix[1:] if suffix else "text"),
                line_count=len(content.splitlines()),
                byte_count=len(content.encode("utf-8", errors="ignore")),
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                sha1=raw_sha1, symbols=symbols, imports=imports, chunks=chunks
            ))

    records.sort(key=lambda r: r.relative_path)
    return tuple(records)

def mode_name(config: BundleConfig) -> str:
    if config.only_core: return "only-core"
    if config.exclude_core: return "exclude-core"
    return "full"

def render_frontmatter(config: BundleConfig, records: tuple[FileRecord, ...]) -> str:
    total_bytes = sum(r.byte_count for r in records)
    lines = [
        "---", "schema_version: 1",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"root: {config.diretorio.resolve().name}",
        f"mode: {mode_name(config)}", f"profile: {config.profile}",
        f"file_count: {len(records)}", f"byte_count: {total_bytes}",
        "ignored_dirs:"
    ]
    lines.extend(f"  - {d}" for d in sorted(PASTAS_IGNORAR))
    lines.append("sensitive_rules:")
    lines.extend(f"  - {r}" for r in sorted(ARQUIVOS_SENSIVEIS_GLOBS))
    lines.append("---")
    return "\n".join(lines)

def render_index_by_domain(records: tuple[FileRecord, ...]) -> str:
    grouped: dict[str, list[FileRecord]] = {}
    for r in records:
        grouped.setdefault(r.domain, []).append(r)
    lines = ["## INDEX_BY_DOMAIN"]
    for domain in sorted(grouped):
        lines.append(f"- `{domain}`:")
        lines.extend(f"  - `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in grouped[domain])
    return "\n".join(lines)

def render_index_by_path(records: tuple[FileRecord, ...]) -> str:
    lines = ["## INDEX_BY_PATH"]
    lines.extend(f"- `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in records)
    return "\n".join(lines)

def render_symbols(records: tuple[FileRecord, ...]) -> str:
    lines = ["## SYMBOL_INDEX"]
    for r in records:
        if not r.symbols: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{s}`" for s in r.symbols)
    return "\n".join(lines)


```
CHUNK_END id=c3916196f58f_c001
CHUNK_START id=c3916196f58f_c002 start_line=301 end_line=380
````python
def render_imports(records: tuple[FileRecord, ...]) -> str:
    lines = ["## IMPORT_MAP_MIN"]
    for r in records:
        if not r.imports: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{i}`" for i in r.imports)
    return "\n".join(lines)

def pick_fence(content: str) -> str:
    return "````" if "```" in content else "```"

def render_file_record(record: FileRecord, toc_only: bool) -> str:
    lines = [
        "---", f'<a id="file_{record.file_id}"></a>',
        f"FILE_START id=file_{record.file_id} path={record.relative_path} "
        f"domain={record.domain} lang={record.language} lines={record.line_count} "
        f"bytes={record.byte_count} mtime={record.mtime_utc} sha1={record.sha1}"
    ]
    if toc_only:
        lines.append("CONTENT_OMITTED toc_only=true")
    else:
        for chunk in record.chunks:
            lines.append(f"CHUNK_START id={chunk.chunk_id} start_line={chunk.start_line} end_line={chunk.end_line}")
            fence = pick_fence(chunk.content)
            lines.extend([f"{fence}{record.language}", chunk.content, fence, f"CHUNK_END id={chunk.chunk_id}"])
    lines.append(f"FILE_END id=file_{record.file_id}")
    return "\n".join(lines)

def generate_context_markdown(config: BundleConfig) -> str:
    if config.only_core and config.exclude_core:
        raise ValueError("only_core e exclude_core nao podem ser usados juntos")
    
    records = collect_files(config)
    blocks = ["# Project Context Bundle", "", render_frontmatter(config, records), "",
              render_index_by_domain(records), "", render_index_by_path(records)]
    if config.emit_symbol_index:
        blocks.extend(["", render_symbols(records)])
    if config.emit_import_map:
        blocks.extend(["", render_imports(records)])
    for r in records:
        blocks.extend(["", render_file_record(r, toc_only=config.toc_only)])
    return "\n".join(blocks) + "\n"

def write_output(config: BundleConfig) -> Path:
    output_path = config.diretorio / config.output
    content = generate_context_markdown(config)
    output_path.write_text(content, encoding="utf-8")
    return output_path

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="captura_projeto.py - Consolida repositorio em markdown AI-first")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretorio raiz")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Arquivo de saida")
    core = parser.add_mutually_exclusive_group()
    core.add_argument("--only-core", action="store_true", help="Inclui apenas escopo core")
    core.add_argument("--exclude-core", action="store_true", help="Exclui escopo core")
    parser.add_argument("--profile", choices=["ai-default", "ai-compact", "ai-forensics"], default="ai-default")
    parser.add_argument("--toc-only", action="store_true", help="Apenas indices e envelopes")
    parser.add_argument("--max-lines-per-file", type=int, default=300, help="Limite de linhas por chunk (0=ilimitado)")
    parser.add_argument("--emit-symbol-index", action="store_true", help="Adiciona SYMBOL_INDEX")
    parser.add_argument("--emit-import-map", action="store_true", help="Adiciona IMPORT_MAP_MIN")
    parser.add_argument("--mask-secrets", action="store_true", help="Ofusca segredos no conteudo")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = BundleConfig(
        diretorio=Path(args.diretorio), output=args.output,
        only_core=args.only_core, exclude_core=args.exclude_core,
        profile=args.profile, toc_only=args.toc_only,
        max_lines_per_file=args.max_lines_per_file,
        emit_symbol_index=args.emit_symbol_index,
        emit_import_map=args.emit_import_map, mask_secrets=args.mask_secrets
    )
    out = write_output(config)
    print(f"\n[OK] Gerado: {out}")
    print(f"   Mode: {mode_name(config)} | Profile: {config.profile}")

if __name__ == "__main__":
    main()
````
CHUNK_END id=c3916196f58f_c002
FILE_END id=file_c3916196f58f

---
<a id="file_aa78525fb574"></a>
FILE_START id=file_aa78525fb574 path=contexto.md domain=docs lang=markdown lines=11768 bytes=476520 mtime=2026-04-11T23:21:55.013173+00:00 sha1=0d645fa9533d2391cd96326f9b68af5d91607a73
CHUNK_START id=aa78525fb574_c001 start_line=1 end_line=300
````markdown
# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-11T23:21:55.003822+00:00
root: template_inicío_de_projeto
mode: full
profile: ai-default
file_count: 37
byte_count: 453344
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
CHUNK_START id=82cd6bde54ff_c001 start_line=1 end_line=71
```python
#!/usr/bin/env python3
"""
🧹 cleanup_specs.py
Gerencia a efemeridade da bancada de trabalho (.specs/).
Aplica a regra de 48h de inatividade e limite de 3 specs ativas simultâneas.
Arquiva specs excedentes ou obsoletas em _archive_context/specs/.
"""
import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# Caminhos base
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "specs"

# Configurações
MAX_INACTIVITY_SECONDS = 48 * 3600  # 48 horas
MAX_ACTIVE_SPECS = 3

def get_specs():
    if not SPECS_DIR.exists():
        return []
    return [d for d in SPECS_DIR.iterdir() if d.is_dir()]

def archive_spec(spec_path):
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{spec_path.name}_{timestamp}"
    dest_path = ARCHIVE_DIR / archive_name
    
    print(f"[INFO] Arquivando spec: {spec_path.name} -> {archive_name}")
    shutil.move(str(spec_path), str(dest_path))

def cleanup():
    specs = get_specs()
    if not specs:
        print("[OK] Nenhuma spec ativa encontrada.")
        return

    now = time.time()
    active_specs = []

    # 1. Limpeza por inatividade (48h)
    for spec in specs:
        last_mod = max(os.path.getmtime(root) for root, _, _ in os.walk(spec))
        if (now - last_mod) > MAX_INACTIVITY_SECONDS:
            print(f"[AUTO] Inatividade detectada (>48h) em: {spec.name}")
            archive_spec(spec)
        else:
            active_specs.append(spec)

    # 2. Limpeza por limite de volume (Max 3)
    # Ordena por data de modificação (mais antiga primeiro)
    active_specs.sort(key=lambda s: max(os.path.getmtime(root) for root, _, _ in os.walk(s)))
    
    while len(active_specs) > MAX_ACTIVE_SPECS:
        oldest = active_specs.pop(0)
        print(f"[AUTO] Limite de volume excedido (Max {MAX_ACTIVE_SPECS}). Removendo spec mais antiga: {oldest.name}")
        archive_spec(oldest)

    print(f"[OK] Manutencao de specs concluida. Specs ativas: {len(active_specs)}/{MAX_ACTIVE_SPECS}")

if __name__ == "__main__":
    try:
        cleanup()
    except Exception as e:
        print(f"[ERROR] Falha na limpeza de specs: {e}")

```
CHUNK_END id=82cd6bde54ff_c001
FILE_END id=file_82cd6bde54ff

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=74 bytes=2507 mtime=2026-04-11T00:15:41.168457+00:00 sha1=772904f793113782bf9cc398ad20f87cefdc018c
CHUNK_START id=024b28a37d29_c001 start_line=1 end_line=74
```python
#!/usr/bin/env python3
"""
🗜️ purge_journal.py
Arquiva 70% das entradas mais antigas do JOURNAL.md.
Mantém 30% mais recentes como semente. Backup automático e escrita atômica.
"""
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
JOURNAL_FILE = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "journals"
KEEP_RATIO = 0.3  # 30% mais recentes

def parse_entries(content):
    # Divide por headers markdown (## 📅, ##, etc.) mantendo o header na entrada
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]

def purge_journal():
    if not JOURNAL_FILE.exists():
        print("[WARN] JOURNAL.md nao encontrado. Nada a fazer.")
        return

    content = JOURNAL_FILE.read_text(encoding="utf-8")
    entries = parse_entries(content)

    if len(entries) <= 1:
        print("[INFO] Poucas entradas para purgar.")
        return

    keep_count = max(1, int(len(entries) * KEEP_RATIO))
    archive_entries = entries[:-keep_count]
    keep_entries = entries[-keep_count:]

    # Garante diretório de arquivo
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Backup com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_file = ARCHIVE_DIR / f"journal_archive_{timestamp}.md"
    archive_content = f"# Arquivo de Journal - {timestamp}\n\n" + "\n\n".join(archive_entries) + "\n"
    archive_file.write_text(archive_content, encoding="utf-8")

    # Nova semente
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    seed = f"""---
Criado em: {now}
Ultima Atualizacao: {now}
Status: Ativo
Nota: Semente pos-purge. {len(archive_entries)} entradas arquivadas em {archive_file.name}.
---

# JOURNAL.md (Memoria Curta)
> Mantido por purge_journal.py. Limite heuristico de caracteres atingido.

""" + "\n\n".join(keep_entries) + "\n"

    # Escrita atomica (previne corrupcao se interrupcao ocorrer)
    temp_file = JOURNAL_FILE.with_suffix(".tmp")
    temp_file.write_text(seed, encoding="utf-8")
    temp_file.replace(JOURNAL_FILE)

    print(f"[OK] Purge concluido.")
    print(f"[OK] Arquivadas: {len(archive_entries)} entradas -> {archive_file.name}")
    print(f"[OK] Mantidas: {len(keep_entries)} entradas mais recentes.")

if __name__ == "__main__":
    try:
        purge_journal()
    except Exception as e:
        print(f"[ERROR] Erro no purge: {e}")

```
CHUNK_END id=024b28a37d29_c001
FILE_END id=file_024b28a37d29

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=94 bytes=3162 mtime=2026-04-11T00:15:52.626055+00:00 sha1=b9acd032350a262fad7d0995116e5686b8fa2191
CHUNK_START id=f122711ba9e1_c001 start_line=1 end_line=94
```python

````
CHUNK_END id=aa78525fb574_c001
CHUNK_START id=aa78525fb574_c002 start_line=301 end_line=600
````markdown
#!/usr/bin/env python3
"""
🔄 sync_project.py
Sincroniza TECH_REQUIREMENTS.md com package.json e schema.sql.
Usa marcadores <!-- AUTO-SYNC START/END --> para preservar edicoes humanas.
"""
import json
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQ_FILE = CONTEXT_DIR / "maintenance" / "TECHNICAL_REQUIREMENTS.md"
PKG_FILE = CONTEXT_DIR.parent / "package.json"
SCHEMA_FILE = CONTEXT_DIR / "maintenance" / "schema.sql"

AUTO_START = "<!-- AUTO-SYNC START -->"
AUTO_END = "<!-- AUTO-SYNC END -->"

def get_package_deps():
    if not PKG_FILE.exists(): return {"dependencies": {}, "devDependencies": {}}
    try:
        with open(PKG_FILE, 'r', encoding='utf-8') as f:
            pkg = json.load(f)
        return {
            "dependencies": pkg.get("dependencies", {}),
            "devDependencies": pkg.get("devDependencies", {})
        }
    except Exception as e:
        print(f"[WARN] Erro ao ler package.json: {e}")
        return {"dependencies": {}, "devDependencies": {}}

def get_schema_tables():
    if not SCHEMA_FILE.exists(): return []
    content = SCHEMA_FILE.read_text(encoding="utf-8")
    # Regex para extrair nomes de tabelas
    return list(set(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["\']?(\w+)["\']?', content, re.IGNORECASE)))

def sync_requirements():
    deps = get_package_deps()
    tables = get_schema_tables()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    block = [
        AUTO_START,
        f"*🤖 Atualizado automaticamente em {now}*",
        ""
    ]

    if deps.get("dependencies"):
        block.append("### Dependencias (package.json)")
        for dep, ver in deps["dependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if deps.get("devDependencies"):
        block.append("### DevDependencies")
        for dep, ver in deps["devDependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if tables:
        block.append("### Tabelas no Schema (schema.sql)")
        for t in sorted(tables):
            block.append(f"- `{t}`")
        block.append("")

    block.append(AUTO_END)
    auto_content = "\n".join(block) + "\n"

    if not REQ_FILE.exists():
        REQ_FILE.write_text(f"# TECHNICAL_REQUIREMENTS.md\n\n{auto_content}", encoding="utf-8")
        print("[OK] TECHNICAL_REQUIREMENTS.md criado.")
        return

    content = REQ_FILE.read_text(encoding="utf-8")
    start_idx = content.find(AUTO_START)
    end_idx = content.find(AUTO_END)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + auto_content + content[end_idx + len(AUTO_END):]
    else:
        new_content = content.rstrip() + "\n\n" + auto_content

    REQ_FILE.write_text(new_content, encoding="utf-8")
    print("[OK] TECHNICAL_REQUIREMENTS.md sincronizado.")
    print(f"[OK] {len(deps.get('dependencies', {}))} deps | {len(tables)} tabelas detectadas.")

if __name__ == "__main__":
    try:
        sync_requirements()
    except Exception as e:
        print(f"[ERROR] Erro no sync: {e}")

```
CHUNK_END id=f122711ba9e1_c001
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=106 bytes=3827 mtime=2026-04-11T02:29:28.743870+00:00 sha1=e6e9a29604fb4a340a2335bbca07488c56baff2a
CHUNK_START id=1077e9084ea1_c001 start_line=1 end_line=106
```python
#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade com AGENT_REGISTRY.md.
"""
import os
import sys
from pathlib import Path

# Caminhos relativos a localização deste script (.context/_scripts/)
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

# Mapeamento para estrutura em camadas
REQUIRED_FILES = [
    "brain/RULES.md", 
    "brain/MASTER_FLOW.md", 
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md", 
    "maintenance/JOURNAL.md", 
    "maintenance/schema.sql", 
    "maintenance/TECHNICAL_REQUIREMENTS.md"
]

JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000  # ~100k tokens

def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]

def check_journal_lines():
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists(): return 0, True
    lines = journal.read_text(encoding="utf-8").splitlines()
    return len(lines), len(lines) <= JOURNAL_MAX_LINES

def estimate_tokens():
    total_chars = 0
    for f in REQUIRED_FILES:
        path = CONTEXT_DIR / f
        if path.exists():
            total_chars += len(path.read_text(encoding="utf-8", errors="ignore"))
    return total_chars, total_chars < TOKEN_WARN_THRESHOLD_CHARS

def check_registry_structure():
    registry = CONTEXT_DIR / "brain/AGENT_REGISTRY.md"
    if not registry.exists(): return False, "Arquivo ausente"
    content = registry.read_text(encoding="utf-8")
    if "| Role |" not in content and "| Role" not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"

def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists(): return True, "Workshop inativo (OK)"
    
    features_dir = specs_dir / "features"
    if not features_dir.exists(): return False, "Diretorio features ausente no .specs"
    
    # Verifica se algum STATE.md esta presente em specs ativas
    active_specs = [d for d in features_dir.iterdir() if d.is_dir()]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
            
    return True, f"OK ({len(active_specs)} specs ativas)"

def validate():
    print("--- Iniciando validacao de contexto (v2.2 Premium+) ---")
    issues = []

    missing = check_files()
    if missing: issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else: print("[OK] Todos os arquivos obrigatorios presentes.")

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok: issues.append(f"[WARN] .specs/: {spec_msg}")
    else: print(f"[OK] .specs/: {spec_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok: issues.append(f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}")
    else: print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, token_ok = estimate_tokens()
    est_tokens = total_chars // 4
    if not token_ok:
        issues.append(f"[WARN] Contexto estimado alto: ~{est_tokens}k tokens. Execute purge.")
    else: print(f"[OK] Estimativa de contexto segura: ~{est_tokens}k tokens")

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok: issues.append(f"[WARN] AGENT_REGISTRY.md: {reg_msg}")
    else: print("[OK] AGENT_REGISTRY.md estrutura valida.")

    print("\n--- Relatorio Final ---")
    if not issues:
        print("[SUCCESS] Contexto integro. Pronto para execucao.")
    else:
        for issue in issues: print(issue)
        print("[ALERT] Resolva os alertas antes de gerar codigo.")

if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        sys.exit(1)

```
CHUNK_END id=1077e9084ea1_c001
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=97 bytes=7180 mtime=2026-04-11T02:28:38.100881+00:00 sha1=3232fd65b8b05382d366aa1a8890e6385eb7f705
CHUNK_START id=e7c17acb71ff_c001 start_line=1 end_line=97
````markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Testes unitários/E2E, edge cases, cobertura, mocks, TDD | `tests/`, `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (apenas leitura para bugs) | `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (critérios de aceite) | "testar", "validar", "cobertura", "mock", "edge case", "TDD", "bug" |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@spec-driver` | Criação e orquestração de specs atômicas | `.specs/` (leitura/gravação temporária) | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (tail 30) | "inicie specify", "crie spec", "modo híbrido" |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |

💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Carregar APENAS: Global + Role-Specific + Task-Ephemeral
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]

````
CHUNK_END id=aa78525fb574_c002
CHUNK_START id=aa78525fb574_c003 start_line=601 end_line=900
````markdown
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*

````
CHUNK_END id=e7c17acb71ff_c001
FILE_END id=file_e7c17acb71ff

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=86 bytes=4370 mtime=2026-04-11T02:59:02.297440+00:00 sha1=06ce6786a149620314b57f8231142f652d4fc412
CHUNK_START id=d833c436f547_c001 start_line=1 end_line=86
````markdown
---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-04-10 23:28
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura do Diretório `.context/`

```text
.context/
├── 🧠 brain/                       # CAMADA COGNITIVA (The Brain)
│   ├── MASTER_FLOW.md             # Este documento
│   ├── RULES.md                   # Protocolos e "A Lei"
│   ├── AGENT_REGISTRY.md          # DNS de Roles e Permissões
│   ├── PROMPT_LIBRARY.md          # Catálogo de templates de prompts
│   ├── PRD.md                     # Requisito em execução (v2.0 - O Contrato)
│   ├── ROADMAP.md                 # Metas e fases (O Planejamento)
│   └── TLC_INTEGRATION.md         # Ponte entre Governança e Execução
│
├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
│   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Curta)
│   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e versões (Inventário)
│   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
│   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
│   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
│   ├── TESTS.md                   # Ledger de padrões e TDDs
│   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
│   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
│   └── _archive_context/          # Histórico imutável (A Biblioteca)
│
├── monitoring/             # CAMADA DE MONITORAMENTO (The Guardian)
│   └── CONTEXT_HEALTH.md   # Dashboard de saúde técnica e cognitiva
│
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── _scripts/               # CAMADA DE AUTOMACAO (The Motor)
    ├── validate_context.py        # Validador de integridade
    ├── purge_journal.py           # Gerenciador de memória (Purge)
    ├── cleanup_specs.py           # Gerenciador de efemeridade (.specs)
    └── sync_project.py            # Sincronizador de requisitos
```

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e a presença do `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões arquiteturais tomadas durante o TLC **devem** ser migradas para o `JOURNAL.md` antes da limpeza da spec.

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*

````
CHUNK_END id=d833c436f547_c001
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=67 bytes=2446 mtime=2026-04-11T01:31:37.755946+00:00 sha1=b5c06bc8a67d2a788cc8263f03971f379d04e92e
CHUNK_START id=d124f6374cab_c001 start_line=1 end_line=67
```markdown
---
Criado em: 2026-04-10 22:35
Ultima Atualizacao: 2026-04-10 22:35
Status: Ativo (EM EXECUCAO)
PRD_ID: #15
---

# 🎯 PRD: Checkout com Integração Stripe
> Implementar um fluxo de pagamento seguro e resiliente usando Stripe Elements e Webhooks para pedidos digitais.

💡 *Insight Humano: Este PRD é um contrato vivo. Ele guia o roteamento de agentes, define criterios de aceite e serve como referência para o JOURNAL.md.*

---

## 📋 1. Visão Geral
| Campo | Valor |
|-------|-------|
| **Objetivo de Negocio** | Reduzir abandono de carrinho e garantir seguranca no processamento. |
| **Publico-Alvo** | Compradores finais da plataforma. |
| **Escopo** | UI de pagamento, Geracao de Session, Webhooks de confirmacao. |
| **MVP vs Futuro** | MVP: Cartao de Credito. Futuro: Apple Pay/Google Pay. |
| **Dependencias** | Stripe API, Tabela `orders`, Variaveis de ambiente seguras. |

---

## 🎯 2. Critérios de Aceite (Definition of Done)
### Funcionais
- [ ] Usuario finaliza compra com cartao valido.
- [ ] Webhook atualiza `orders.status` para 'succeeded'.
- [ ] Erro de cartao exibe mensagem amigavel (WCAG).
- [ ] Idempotencia garantida via `event.id` do Stripe.

### Não-Funcionais
- [ ] Tempo de resposta API < 500ms.
- [ ] Nenhum segredo (Keys) hardcoded no codigo.
- [ ] Logs estruturados para auditoria.

---

## 🤖 3. Roteamento Multi-Agent
| Etapa | Role Responsável | Entregável | Gatilho de Handoff |
|-------|-----------------|------------|-------------------|
| 1. UI Checkout | `@frontend-specialist` | `StripeForm.tsx` | "UI pronta, aguarda contrato de API" |
| 2. API Stripe | `@backend-engineer` | `/api/checkout` + Webhook | "Rotas operacionais, inicia validacao" |
| 3. Testes E2E | `@qa-validator` | Suite de testes | "Cobertura >90%, edge cases validados" |

---

## 🔒 4. Context Gate (Pré-Execução)
- [ ] `maintenance/schema.sql` contem a tabela `orders`? ✅
- [ ] `maintenance/TECHNICAL_REQUIREMENTS.md` atualizado? ✅
- [ ] `maintenance/JOURNAL.md` < 550 linhas? ✅
- [ ] `brain/AGENT_REGISTRY.md` tem as roles necessarias? ✅

---

## 📊 5. Health Check Integrado
| Metrica | Valor | Status |
|---------|-------|--------|
| **Progresso** | 50% | 🟡 Em andamento |
| **Cobertura de Testes** | 92% (Simulada) | ✅ OK |
| **Divergência Schema** | 0 campos | ✅ OK |

---

## 🔄 6. Ciclo de Vida & Arquivamento
Ao concluir, mover para `_archive_context/prds/` e atualizar `ROADMAP.md`.

```
CHUNK_END id=d124f6374cab_c001
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=154 bytes=6687 mtime=2026-04-11T02:28:52.575335+00:00 sha1=aa3419c1efa08687a7c551dc44f40b504b422353
CHUNK_START id=9fe16e5591f0_c001 start_line=1 end_line=154
````markdown
---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo
---

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator`
**Gatilho:** Testes, validacao, edge cases, cobertura, mocks  
**Contexto Obrigatorio:** `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (criterios de aceite)
```text
🤖 Ativando @qa-validator | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{arquivo/feature a ser testada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{criar testes, validar edge cases ou aumentar cobertura}}
🚧 Restricoes:
- Seguir framework de testes definido em maintenance/TECHNICAL_REQUIREMENTS.md
- Mockar servicos externos; nao depender de rede real
- Cobrir happy path + 2 edge cases criticos no minimo
- Documentar falhas conhecidas no maintenance/JOURNAL.md se houver
📤 Saida Esperada:

````
CHUNK_END id=aa78525fb574_c003
CHUNK_START id=aa78525fb574_c004 start_line=901 end_line=1200
````markdown
1. Codigo dos testes (unitarios/integracao)
2. Matriz de cenarios cobertos
3. Recomendacoes de refatoracao se aplicavel
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada
2. spec.md com passos, contratos e critérios de verificação
3. STATE.md: draft → pronto para execução
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*

````
CHUNK_END id=9fe16e5591f0_c001
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.772397+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=c94f001202db_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=c94f001202db_c001
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=70 bytes=4536 mtime=2026-04-11T02:57:50.282657+00:00 sha1=49f182ecde4e634b51130172a7a7d4e78ac48ee1
CHUNK_START id=cd6526d17218_c001 start_line=1 end_line=70
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 23:55
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança
**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)  
> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas para garantir escala, foco e rastreabilidade.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)
Antes de gerar código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:
1. **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`
2. **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
3. **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`

> ⚠️ **Bloqueio de Execução:** Se qualquer item estiver ausente ou desatualizado, a IA deve parar e solicitar a carga correta antes de prosseguir.

---

## 🔢 2. Session Budget & Heurísticas de Token
Para evitar alucinações por *Token Bloat* (excesso de memória na janela):
- **Gatilhos de Alerta:** ~50.000 caracteres acumulados OU ~15-20 trocas densas de desenvolvimento.
- **Ação ao atingir o limite:** Disparar: *"🔄 Contexto próximo do limite de foco. Deseja que eu execute o purge do JOURNAL, arquive o PRD atual ou inicie uma nova sessão limpa com snapshot de semente?"*

---

## 🧠 3. Protocolo de Manutenção do Contexto
A IA atua como bibliotecário chefe. Consistência entre Código e Contexto é obrigatória.
- **`maintenance/JOURNAL.md`:** Apenas decisões de arquitetura, resoluções de bugs complexos e mudanças de lógica. Proibido logar erros triviais. Ao atingir ~600 linhas ou 50k chars → acionar `_scripts/purge_journal.py`.
- **`maintenance/TECHNICAL_REQUIREMENTS.md`:** Atualizar sempre que houver mudança em `package.json`, alteração de Schema ou integração de novas APIs.
- **`maintenance/rebuild_guide.md`:** Atualizar com hacks de ambiente local, CI/CD ou passos manuais de deploy.
- **`.specs/` (Workshop Efêmero):** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/`. Decisões técnicas devem migrar para o `JOURNAL.md` antes da limpeza.

---

## 🗄️ 4. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.
1. **Verificação Obrigatória:** Antes de criar UI/lógica dependente de dados, validar `maintenance/schema.sql`.
2. **Aviso de Divergência:** Se o código exigir um campo inexistente, parar e avisar: *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro gerar a migration antes de prosseguir."*

---

## 🤖 5. Comportamento do Agente (Transparência & Roteamento)
- **Ativação:** Toda tarefa complexa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`
- **Isolamento:** Carregar APENAS `Global + Role-Specific + Task-Ephemeral`. Ignorar o resto.
- **Handoff:** Cruzar 2+ domínios? Pausar → registrar no `JOURNAL.md`:  
  `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo: [ação]`
- **Context Gate (Pré-Código):** Validar antes de gerar:  
  `[ ] PRD ativo` | `[ ] schema contém estruturas` | `[ ] JOURNAL < 550 linhas` | `[ ] zero secrets hardcoded`

---

## 🔄 6. Gatilhos de Interação (Para o Usuário)
- `"Atualize o contexto"` → IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- `"Qual o estado do projeto?"` → Relatório baseado no `JOURNAL.md` + `ROADMAP.md`.
- `"Roteie esta tarefa"` → Consulta `AGENT_REGISTRY.md`, inicia ativação/handoff.
- `"Use o prompt padrão"` → Seleciona template em `brain/PROMPT_LIBRARY.md`, preenche placeholders, solicita confirmação.
- `"Inicie SPECIFY para PRD #[ID]"` → Cria `.specs/features/`, gera `spec.md` alinhado ao PRD, inicia ciclo TLC.

---

## 🚨 7. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.

```
CHUNK_END id=cd6526d17218_c001
FILE_END id=file_cd6526d17218

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CHUNK_START id=450d7ec70909_c001 start_line=1 end_line=32
```markdown
---
Criado em: 2026-04-10 23:29
Ultima Atualizacao: 2026-04-10 23:29
Status: Ativo
---

# 🔗 TLC_INTEGRATION.md
> Ponte entre Governança de Longo Prazo (`.context/`) e Execução Atômica (`.specs/`).  
> 💡 *Insight Humano: O PRD diz O QUÊ e POR QUÊ. A SPEC diz COMO e QUANDO. O TLC orquestra a transição.*

## 🔄 Ciclo de Vida Híbrido
1. **INTENT** → `PRD.md` ativo define escopo e critérios de aceite.
2. **SPECIFY** → IA cria `.specs/features/[nome]/spec.md` com passos atômicos, contratos de API/DB e testes.
3. **IMPLEMENT** → Geração de código baseada na spec. Handoffs registrados no `JOURNAL.md`.
4. **VERIFY** → Testes passam → `STATE.md` marcado como `✅ PASSED`.
5. **SYNC** → Decisões arquiteturais e lições → `JOURNAL.md`. Spec arquivada ou deletada.

## 📏 Regras de Ouro
- 🔒 **Soberania do Contexto:** `.specs/` nunca sobrescreve `.context/`. Apenas alimenta a memória de longo prazo.
- 🧹 **Efemeridade:** Spec inativa >48h ou pós-merge → mover para `_archive_context/specs/` ou deletar.
- 🤝 **Handoff:** Handoff obrigatório no `JOURNAL.md` se a spec cruzar domínios (ex: `@backend` → `@qa`).
- ⚠️ **Divergência:** Se `spec.md` divergir de `schema.sql` ou `PRD.md` → parar e solicitar correção de contexto.

## 🤖 Fluxo de Ativação
`"Inicie a fase de SPECIFY para o PRD #[ID]"` → 
1. IA lê `PRD.md` + `schema.sql` + `JOURNAL.md` (últimas 30).
2. Cria `.specs/features/[nome]/` com `spec.md` e `STATE.md: draft`.
3. Executa passos atômicos → atualiza `STATE.md`.
4. Ao concluir: `✅ Spec passed. Deseja arquivar a spec e sincronizar o JOURNAL.md?`

---
> *Este documento garante que o "Cérebro" (Contexto) e o "Músculo" (TLC) operem em harmonia.*

```
CHUNK_END id=450d7ec70909_c001
FILE_END id=file_450d7ec70909

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.800876+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=9b6470da8849_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=9b6470da8849_c001
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=23 bytes=1082 mtime=2026-04-11T01:25:28.436758+00:00 sha1=43293ddbefe17288e0cea85c402cff9f4ed05cea
CHUNK_START id=019509328844_c001 start_line=1 end_line=23
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# JOURNAL.md
> Log vivo de decisoes e bugs. (Max 600 linhas)

## 📅 2026-04-11 01:25
**Decisão/Bug:** 🔄 Handoff: @frontend-specialist → @backend-engineer
**Solução:** Implementada UI do CheckoutForm v1 usando Stripe Elements. Estado local gerenciado; aguardando API `/api/checkout/session`.
**Implicação:** Próximo agente deve configurar a rota backend e garantir o retorno do `clientSecret`.

## 📅 2026-04-11 01:35
**Decisão/Bug:** 🔄 Handoff: @backend-engineer → @qa-validator
**Solução:** Endpoint Stripe Session operacional. Webhook configurado para escutar `payment_intent.succeeded` e atualizar tabela `orders`.
**Implicação:** QA deve validar fluxos de falha e idempotência do webhook.

## 📅 2026-04-11 01:45
**Decisão/Bug:** ✅ Ciclo Checkout Stripe Concluído
**Solução:** Cobertura de testes em 92%. Validado happy path e 'card declined'. Injetado retry pattern no webhook.
**Implicação:** PRD #15 concluído. Tecnologias Stripe adicionadas ao env.

```
CHUNK_END id=019509328844_c001
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=14 bytes=287 mtime=2026-04-11T03:14:23.819547+00:00 sha1=71b173ae91c93ed58cf9027ce03c8ed12ae79b4f
CHUNK_START id=d069d4f2ebef_c001 start_line=1 end_line=14
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

<!-- AUTO-SYNC START -->
*🤖 Atualizado automaticamente em 2026-04-11 00:14*

### DevDependencies
- `husky`: `^9.1.7`

### Tabelas no Schema (schema.sql)
- `orders`

<!-- AUTO-SYNC END -->



```
CHUNK_END id=d069d4f2ebef_c001
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.794384+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=0858a02cf53f_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=0858a02cf53f_c001
FILE_END id=file_0858a02cf53f

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CHUNK_START id=a5c71962029a_c001 start_line=1 end_line=63
````markdown
---
Criado em: 2026-04-10 21:44
Ultima Atualizacao: 2026-04-10 21:44
Status: Ativo
---

# 🛠️ Manual de Reconstrução & Automação

Este guia contém as instruções para subir o ambiente do zero e operar as ferramentas de governança de contexto.

---

## 🏗️ 1. Setup do Ambiente

### Requisitos Mínimos:
- **Python ≥ 3.8** (Para os scripts de automação)
- **Node.js** (Para os wrappers NPM)
- **Make** (Opcional, para orquestração Unix)
- **Bash** (Para Git Bash, WSL, Linux ou macOS)

---

## ⚙️ 2. Ferramentas de Automação


````
CHUNK_END id=aa78525fb574_c004
CHUNK_START id=aa78525fb574_c005 start_line=1201 end_line=1500
````markdown
O projeto oferece três formas de gerenciar a saúde do contexto. Escolha a que melhor se adapta ao seu terminal:

### Opção A: Via NPM (Recomendado para Devs Web)
```bash
npm run context:validate  # Checa integridade e tokens
npm run context:sync      # Sincroniza deps e schema
npm run context:purge     # Limpa e arquiva o log vivo
```

### Opção B: Via Make (Recomendado para CI/CD e Unix)
```bash
make validate
make sync
make purge
make all       # Executa o pipeline completo: Valida -> Sync -> Purge
```

### Opção C: Via Bash (Resiliência Universal)
```bash
./run_context.sh validate
./run_context.sh all
```

---

## 🗃️ 3. Recuperação de Contexto (Archive)

Se precisar restaurar um Journal ou PRD antigo que foi arquivado:
1. Vá até `.context/maintenance/_archive_context/`.
2. Localize o arquivo pelo timestamp `YYYYMMDD_HHMMSS`.
3. Copie o conteúdo necessário de volta para a raiz da camada correspondente (`maintenance/` ou `brain/`).

---

## 🚨 4. Troubleshooting
- **Erro de Encoding (Windows):** Todos os scripts são forçados para UTF-8. Se vir caracteres estranhos, verifique se o seu terminal suporta Unicode.
- **Python não encontrado:** No Windows, o script tenta `python3` e faz fallback para `python`. Se falhar, certifique-se que o executável está no seu PATH.

> *Lembrete: Sem automação, a documentação morre. Use as ferramentas a cada nova funcionalidade iniciada no ROADMAP.md.*

````
CHUNK_END id=a5c71962029a_c001
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=27 bytes=1336 mtime=2026-04-11T02:26:43.636538+00:00 sha1=adb37745498ccfa61a2b793c10240a2b20d3d716
CHUNK_START id=54a6a553d34b_c001 start_line=1 end_line=27
```markdown
---
Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-10 23:27
Status: Ativo
---

# 🧬 rx-anatomy.md (Raio-X de Anatomia)
> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Arquivos de decisão e regras
│   ├── maintenance/        # Logs, db schema e inventários
│   └── monitoring/         # Dashboard de saúde
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.sh          # Orquestrador universal Bash
├── init_ai_project.sh      # Bootstrapper supremo
└── package.json            # Gerenciamento de libs e scripts context:*

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `_archive_context/specs/`
- **Não é fonte da verdade.** O `.context/` permanece como SSOT.

```
CHUNK_END id=54a6a553d34b_c001
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.789386+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=ca8da4f87431_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=ca8da4f87431_c001
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CHUNK_START id=91d5627a725e_c001 start_line=1 end_line=9
```sql
-- Snapshot Real da Tabela de Pedidos
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_session_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending', -- pending, succeeded, failed
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
CHUNK_END id=91d5627a725e_c001
FILE_END id=file_91d5627a725e

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1624 mtime=2026-04-10T23:50:11.304033+00:00 sha1=92934bdfcac044ab34842a1b0131524ead5e2e5b
CHUNK_START id=068a21d64bec_c001 start_line=1 end_line=38
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

| Métrica | Valor Atual| Limite / Heurística | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Pilar de Manutenção** | | | | |
| JOURNAL.md (linhas) | 412 | 600 | Manutenção | ✅ OK |
| JOURNAL.md (tamanho) | ~12k char | 50k char | Manutenção | ✅ OK |
| **Pilar Cognitivo** | | | | |
| Role Ativa | @frontend-specialist | N/A | Cognitivo | ⚠️ Em Task |
| PRD Ativo | #14 - Auth Flows | 1 por vez | Cognitivo | ✅ OK |
| **Pilar de Consistência** | | | | |
| Schema vs PRD Sync | 0 divergências | 0 | DB-First | ✅ OK |
| Último Sincronismo | 2h atrás | < 24h | Governança | ✅ OK |
| **Pilar de Sessão** | | | | |
| Turns de Sessão | 8 trocas | 20 trocas | Sessão | ✅ OK |
| Token Window Est. | ~78k | 128k | Sessão | ⚠️ 80% |

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até que a migration seja documentada.
- **Se Turns > 18:** Propor Snapshot ou Reset de Sessão antes de iniciar próxima tarefa grande.

---

## 📅 Histórico de Saúde (Log de Purges)
| Data | Ação | Agente | Resultado |
| :--- | :--- | :--- | :--- |
| 2026-04-10 | Purge Completo | @context-keeper | Journal resetado para seed de 30 linhas. |

```
CHUNK_END id=068a21d64bec_c001
FILE_END id=file_068a21d64bec

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=26 bytes=693 mtime=2026-04-11T00:55:20.246274+00:00 sha1=163dd12b4c98d348f80986ea59afcb4604dc9e0e
CHUNK_START id=e477c4c5a96c_c001 start_line=1 end_line=26
```yaml
name: Context Health Check

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  validate-context:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run Context Validation
        # No GitHub Actions (Linux), usamos python3
        run: python3 .context/_scripts/validate_context.py

      - name: Check Journal Limits
        run: python3 .context/_scripts/validate_context.py | grep -q "SUCCESS" || (echo "❌ Contexto quebrado ou Journal excedido!" && exit 1)

```
CHUNK_END id=e477c4c5a96c_c001
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CHUNK_START id=3adfd36c1559_c001 start_line=1 end_line=9
```bash
echo "husky - DEPRECATED

Please remove the following two lines from $0:

#!/usr/bin/env sh
. \"\$(dirname -- \"\$0\")/_/husky.sh\"

They WILL FAIL in v10.0.0
"
```
CHUNK_END id=3adfd36c1559_c001
FILE_END id=file_3adfd36c1559

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=68 bytes=2890 mtime=2026-04-11T02:30:31.368152+00:00 sha1=ea66d1b4ed6f174f17b752f28ac358093fb784d2
CHUNK_START id=8ec9a00bfd09_c001 start_line=1 end_line=68
````markdown
# 🛸 Antigravity Kit v2.2 Premium+
> **O ecossistema definitivo para engenharia AI-Ready: Governança Macro + Execução Atômica.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação (GitHub Copilot, Cursor, Antigravity). Ele unifica o **Antigravity Kit** (Governança Macro) com o **TLC Spec-Driven** (Execução Atômica), garantindo que o Propósito (PRD) se transforme em Ação (Código) com precisão cirúrgica.

---

## 🧠 A Filosofia: "Se não está no Contexto, não existe."

Neste framework, a pasta `.context/` é a **Single Source of Truth (SSOT)**. A pasta `.specs/` é o seu **Workshop Efêmero**. O código é apenas o reflexo físico da inteligência documentada.

## 🚀 Instalação Ultra-Rapida (One-Click Setup)

Se voce quer inicializar este framework em um novo projeto do zero, basta rodar o nosso bootstrapper supremo:

```bash
# 1. Torne o script executavel
chmod +x init_ai_project.sh

# 2. Execute
./init_ai_project.sh
```

O script ira criar automaticamente toda a estrutura de camadas, os workshops de execução, os motores de manutenção v2.2+, e configurar a blindagem Husky.

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. PRD v2.0, Rules, Registry e a Ponte de Integração TLC.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação

| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Verifica a integridade dos arquivos e a estrutura do workshop. |
| `npm run context:sync`     | Sincroniza `TECHNICAL_REQUIREMENTS.md` com dependências e DB. |
| `npm run context:cleanup`  | Gerencia a efemeridade do `.specs/` (Arquiva specs obsoletas). |
| `npm run context:all`      | Pipeline completo de saúde e manutenção. |

---

## 🤝 Protocolo de Ativação Híbrida

Para iniciar uma tarefa com poder total, use o prompt mestre:
> *"Inicie a fase de SPECIFY para o PRD #[ID] usando o modo Híbrido TLC."*

Isso ativará a role `@spec-driver` e iniciará o ciclo atômico no `.specs/` alinhado à governança do `.context/`.

---

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*

````
CHUNK_END id=8ec9a00bfd09_c001
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=114 bytes=4693 mtime=2026-04-11T01:41:16.589576+00:00 sha1=69a61b75c7697979c8e4ab560e0325f71bd7151d
CHUNK_START id=4efb6293109d_c001 start_line=1 end_line=114
````markdown
---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo

````
CHUNK_END id=aa78525fb574_c005
CHUNK_START id=aa78525fb574_c006 start_line=1501 end_line=1800
````markdown
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria viva, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.sh`, `Makefile` | Validacao, purge, sync e orquestracao. |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `tests/test_context.py` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija antes de forcar.

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rapidos (Cheat Sheet)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Sincronizar deps e schema com TECH_REQUIREMENTS.md
npm run context:sync

# Arquivar 70% do journal (mantem 30% como semente)
npm run context:purge

# Pipeline completo (validate -> sync -> purge)
npm run context:all

# Rodar testes do framework manualmente (Universal Python)
npm run context:test
```
> 💡 *Fallbacks:* `make all` ou `bash run_context.sh all`

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se `validate_context.py` ou `test_context.py` falharem.
- **CI/CD:** O GitHub Actions roda o pipeline em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Clone
- [ ] `.context/` existe com estrutura de camadas ok.
- [ ] `brain/RULES.md` e `brain/MASTER_FLOW.md` alinhados a stack.
- [ ] `brain/AGENT_REGISTRY.md` possui roles registradas.
- [ ] `npm run context:all` executa sem erros.

### 🚀 Inicio de Feature / PRD
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---

> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.

````
CHUNK_END id=4efb6293109d_c001
FILE_END id=file_4efb6293109d

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=5 bytes=138 mtime=2026-04-11T02:58:40.247024+00:00 sha1=19d69e551321040a8c49f683ffcfae2bfbaed5cb
CHUNK_START id=f6f7100f063b_c001 start_line=1 end_line=5
```markdown
# 🛸 Antigravity Kit Versioning
v2.2.1-premium
Dash: [Antigravity Kit v2.2.1-premium]
Audit Status: ✅ PASSED
Release Date: 2026-04-10

```
CHUNK_END id=f6f7100f063b_c001
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CHUNK_START id=1f98938d3cd9_c001 start_line=1 end_line=140
````markdown
### 🔍 Por que um único arquivo não basta?
A IA não lê apenas um arquivo para definir comportamento. Ela avalia:
- 📁 Estrutura de pastas (`brain/`, `maintenance/`, `monitoring/`, `.specs/`)
- 🤖 `AGENT_REGISTRY.md` (ainda carregará 7 roles se existir)
- 🐍 Scripts Python e hooks do Husky (continuam ativos)
- 📜 Regras de carregamento (`Checklist de Carga` ainda exige camadas)
- 🧠 Memória de sessão (a IA tentará carregar tudo o que encontrar)

Se você só trocar o `RULES.md`, a IA ficará em **estado híbrido confuso**: regras dizem "modo leve", mas a estrutura exige validações pesadas, registry complexo e scripts de automação. Isso gera `token bloat`, alucinação e falhas de contexto gate.

---
### 🛠️ 3 Caminhos Técnicos Viáveis

| Abordagem | Como funciona | Prós | Contras |
|-----------|--------------|------|---------|
| `MODE.md` (Flag) | Arquivo simples: `MODE: LIGHT`. A IA lê primeiro e ajusta comportamento. | Zero destruição, reversível, explícito. | Exige atualização no `RULES_LIGHT.md` para ler a flag. |
| `init_ai_project_light.sh` | Bootstrap que cria estrutura mínima do zero (sem camadas, sem scripts, sem Husky). | Limpo, seguro, ideal para novos MVPs. | Não converte projetos robustos existentes. |
| `downgrade_to_light.sh` | Remove camadas, desativa Husky, arquiva scripts, substitui `RULES.md`. | Converte projeto existente sem perder histórico. | Irreversível sem backup manual. |

---
### ✅ Recomendação: `MODE.md` + `init_ai_project_light.sh`
É a combinação mais segura. Você mantém o robusto como padrão, mas pode ativar o modo leve em qualquer repositório novo ou existente com **um arquivo de flag** ou **um comando de init**.

---
### 📄 1. `MODE.md` (A Chave de Conversão)
Coloque na raiz de `.context/`. A IA **DEVE** ler este arquivo antes de qualquer checklist.

```markdown
---
Criado em: YYYY-MM-DD HH:MM
Última Atualização: YYYY-MM-DD HH:MM
Status: Ativo
---

# 🪶 MODE.md
> Define o perfil operacional do framework. A IA ajusta carregamento, roles e automação conforme este valor.

**MODE:** LIGHT  
**Reason:** MVP < 2 semanas | Time 1-2 devs | Velocidade > Governança  

💡 *Insight IA: Se MODE = LIGHT, ignore camadas, scripts, registry multi-agent e .specs/. Carregue apenas: RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql. Use @fullstack-generalist por padrão.*
```

---
### 📜 2. Patch Obrigatório no `RULES_LIGHT.md`
Adicione este bloco no **topo** do arquivo, antes de qualquer regra:

```markdown
📜 RULES_LIGHT.md — Modo Minimalista (MVP/POC)
Projeto: [NOME DO PROJETO] | Arquitetura: Single-Agent + Database-First
> 🪶 **MODO ATIVO:** Leia `MODE.md`. Se `MODE: LIGHT`, siga estritamente este protocolo enxuto. Ignore `.specs/`, scripts Python, Husky e `AGENT_REGISTRY.md`.

🛡️ Checklist de Carga (Light)
1. [ ] RULES_LIGHT.md (este arquivo)
2. [ ] PRD.md ativo
3. [ ] schema.sql atualizado
4. [ ] JOURNAL.md < 300 linhas
⚠️ Se faltar 1 item → pare e solicite correção.

🔄 Comportamento do Agente (Light)
- Role padrão: `@fullstack-generalist` (única ativa)
- Sem handoff obrigatório. Registre decisões críticas direto no JOURNAL.md
- Database-First mantido. Nunca assuma schema.
- Sem automação. Validação manual: `grep -q "schema.sql" PRD.md && echo "✅ OK"`
- Fim de sessão: `"Contexto atualizado? [S/N]"`
```

---
### 🐚 3. `init_ai_project_light.sh` (Bootstrap Seguro)
Cria uma estrutura flat, sem camadas, sem scripts, sem Husky. Ideal para `git init` de MVPs.

```bash
#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
NC='\033[0m'

[ -d ".context" ] && { echo "❌ .context/ já existe. Abortando."; exit 1; }

echo -e "\n${GREEN}🪶 Inicializando Modo LIGHT...${NC}"
mkdir -p .context

NOW=$(date +%Y-%m-%d\ %H:%M)

# MODE Flag
cat > .context/MODE.md << EOF
---
Criado em: $NOW
Status: Ativo
---
MODE: LIGHT
Reason: MVP rápido | Velocidade > Governança
💡 IA: Ignore camadas, scripts, registry e .specs/. Use apenas RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql.
EOF

# RULES_LIGHT (minimalista)
cat > .context/RULES_LIGHT.md << 'EOF'
📜 RULES_LIGHT.md — Modo Minimalista
> 🪶 MODE: LIGHT ativo. Role única: @fullstack-generalist. Sem scripts, sem Husky, sem handoff complexo.
🛡️ Carga: [ ] RULES_LIGHT.md [ ] PRD.md [ ] schema.sql [ ] JOURNAL.md <300lin
🗄️ DB-First: Valide schema antes de UI. Se faltar campo → pare e avise.
🔄 Fim de sessão: Pergunte "Atualizo contexto?" e registre no JOURNAL.md apenas mudanças de lógica/bug.
⚠️ Sem automação. Sem registry. Sem .specs/. Mantenha enxuto.
EOF

# Arquivos base
for f in PRD.md JOURNAL.md schema.sql; do
  cat > ".context/$f" << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📄 $f
EOF
done

echo -e "${GREEN}✅ Modo LIGHT pronto. Estrutura plana, sem overhead.${NC}"
echo "📖 Próximo: Preencha PRD.md e comece. A IA usará @fullstack por padrão."
```

---
### 🧠 Como a IA Interpreta Isso na Prática
1. **Início de sessão:** A IA lê `MODE.md` primeiro.
2. **Se `MODE: LIGHT`:** 
   - Ignora `brain/`, `maintenance/`, `monitoring/`, `_scripts/`, `.specs/`
   - Carrega apenas os 4 arquivos essenciais
   - Ativa `@fullstack-generalist` implicitamente
   - Desativa validações Python/Husky automaticamente
   - Usa heurística simplificada de tokens (limite ~20k chars)
3. **Se quiser voltar ao robusto:** Troque `MODE: ROBUST` e rode `npm run context:all` para restaurar camadas/scripts.

---
### 🚀 Próximo Passo
Quer que eu:
1. **Gere o `downgrade_to_light.sh`** para converter um projeto robusto existente sem perder histórico?
2. **Ajuste o `init_ai_project.sh` principal** para incluir uma flag `--light` que alterna entre os dois modos automaticamente?
3. **Entregue o `RULES_LIGHT.md` completo** (versão pronta para copiar/colar, com todos os protocolos simplificados)?

Escolha o fechamento. O framework agora tem conversão explícita, segura e reversível. 🏁
````
CHUNK_END id=1f98938d3cd9_c001
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=380 bytes=15779 mtime=2026-04-11T02:42:28.056925+00:00 sha1=2dba92559cf404d5e91df067a8fd72b6a965ec8c
CHUNK_START id=c3916196f58f_c001 start_line=1 end_line=300
```python
#!/usr/bin/env python3
"""captura_projeto.py - Gera bundle markdown AI-first do repositorio. TEMPLATE UNIVERSAL."""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path


````
CHUNK_END id=aa78525fb574_c006
CHUNK_START id=aa78525fb574_c007 start_line=1801 end_line=2100
````markdown
# 🛠️ CUSTOMIZE AQUI: Padrões universais + adicione os específicos do seu projeto
PASTAS_IGNORAR = {
    ".git", "node_modules", "dist", "build", "out", "target", "bin", "obj",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache",
    ".next", ".nuxt", ".vercel", ".netlify", ".vite", ".cache",
    ".vscode", ".idea", ".cursor", "coverage", ".pytest_cache",
    "captura_projeto", # 📝 Ignorar a própria pasta do utilitário
}

PASTAS_CORE = {
    # 📝 Defina as pastas ARQUITETURALMENTE essenciais para a IA entender seu projeto
    # Ex: {"src", "lib", "api", "supabase", ".context", ".specs"}
    "src", "lib", "api", ".context", ".specs"
}

# 🛠️ CUSTOMIZE AQUI: Regras de classificação semântica (fallback seguro)
DOMAIN_RULES = {
    r"/api/|/routes/|/handlers/|/controllers/": "api",
    r"/components/|/ui/|/views/|/pages/|/screens/": "ui",
    r"/lib/|/utils/|/helpers/|/core/|/shared/": "lib",
    r"/db/|/migrations/|/models/|/schema/|/supabase/|/prisma/": "db",
    r"/tests/|/spec/|/__tests__/|\.test\.|\.spec\.": "tests",
    r"/config/|/settings/|/env/": "config",
    r"\.md$|\.rst$|\.txt$": "docs",
    r"\.(json|toml|yaml|yml|ini)$": "config",
}

EXTENSOES_PERMITIDAS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".html", ".css", ".json", ".md",
    ".yaml", ".yml", ".toml", ".sh", ".sql", ".graphql", ".vue", ".svelte",
    ".rs", ".go", ".java", ".c", ".h", ".hpp", ".cpp", ".ini",
}

LINGUAGENS = {
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".py": "python", ".html": "html", ".css": "css", ".json": "json", ".md": "markdown",
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".sh": "bash", ".sql": "sql",
    ".graphql": "graphql", ".vue": "html", ".svelte": "html", ".rs": "rust",
    ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".hpp": "cpp", ".cpp": "cpp", ".ini": "ini",
}

ARQUIVOS_SENSIVEIS_GLOBS = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx",
    "credentials*.json", "id_rsa*", "secrets.*", "*.cert",
    # 📝 Adicione padrões sensíveis do SEU projeto aqui
}

SECRET_PATTERNS = (
    re.compile(r'(["\']?)(\w*(?:API_KEY|SECRET|TOKEN|PASSWORD|AUTH_KEY|PRIVATE_KEY|ACCESS_KEY|DB_PASS|CONNECTION_STRING)\w*)\1\s*[:=]\s*["\']?(\S+)["\']?', re.IGNORECASE),
    re.compile(r'(BEGIN\s+(RSA|EC|DSA|OPENSSH|PGP)\s+PRIVATE\s+KEY)', re.IGNORECASE),
)

DEFAULT_OUTPUT = "contexto.md"
logging.basicConfig(level=logging.WARNING, format="⚠️ %(message)s")

@dataclass(frozen=True)
class BundleConfig:
    diretorio: Path
    output: str = DEFAULT_OUTPUT
    only_core: bool = False
    exclude_core: bool = False
    profile: str = "ai-default"
    toc_only: bool = False
    max_lines_per_file: int = 300
    emit_symbol_index: bool = False
    emit_import_map: bool = False
    mask_secrets: bool = False

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_line: int
    end_line: int
    content: str

@dataclass(frozen=True)
class FileRecord:
    file_id: str
    relative_path: str
    domain: str
    language: str
    line_count: int
    byte_count: int
    mtime_utc: str
    sha1: str
    symbols: tuple[str, ...]
    imports: tuple[str, ...]
    chunks: tuple[Chunk, ...]

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXTENSOES_PERMITIDAS:
        return True
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        return False
    return mime.startswith("text/") or mime in {"application/json", "application/xml", "application/javascript"}

def is_sensitive_file(path: Path) -> bool:
    return any(fnmatch(path.name.lower(), pat.lower()) for pat in ARQUIVOS_SENSIVEIS_GLOBS)

def classify_domain(relative_path: str) -> str:
    p = relative_path.lower()
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, p):
            return domain
    return "source"

def should_include_profile(record_domain: str, config: BundleConfig) -> bool:
    if config.profile == "ai-compact":
        return record_domain not in {"tests", "docs"}
    return True

def mask_sensitive(content: str, enabled: bool) -> str:
    if not enabled:
        return content
    out = content
    for pattern in SECRET_PATTERNS:
        out = pattern.sub(r"\1***", out)
    return out

def extract_symbols(content: str, suffix: str) -> tuple[str, ...]:
    symbols: list[str] = []
    if suffix == ".py":
        symbols.extend(re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content, re.MULTILINE))
        symbols.extend(re.findall(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        symbols.extend(re.findall(r"(?:export\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content))
        symbols.extend(re.findall(r"(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\s*", content))
        symbols.extend(re.findall(r"export\s+const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", content))
    seen, seen_set = [], set()
    for s in symbols:
        if s not in seen_set:
            seen.append(s)
            seen_set.add(s)
    return tuple(seen[:80])

def extract_imports(content: str, suffix: str) -> tuple[str, ...]:
    imports: list[str] = []
    if suffix == ".py":
        imports.extend(re.findall(r"^import\s+([^\n]+)", content, re.MULTILINE))
        imports.extend(re.findall(r"^from\s+([^\s]+)\s+import\s+([^\n]+)", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        imports.extend(re.findall(r"^import\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]", content, re.MULTILINE))
        imports.extend(re.findall(r"require\(['\"]([^'\"]+)['\"]\)", content))
    normalized, seen_set = [], set()
    for item in imports:
        val = f"from {item[0]} import {item[1]}" if isinstance(item, tuple) else item
        if val not in seen_set:
            normalized.append(val)
            seen_set.add(val)
    return tuple(normalized[:120])

def chunk_content(content: str, file_id: str, max_lines: int) -> tuple[Chunk, ...]:
    lines = content.splitlines()
    if not lines:
        return (Chunk(f"{file_id}_c001", 1, 1, ""),)
    if max_lines <= 0 or len(lines) <= max_lines:
        return (Chunk(f"{file_id}_c001", 1, len(lines), content),)
    chunks = []
    idx = 1
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        part = "\n".join(lines[start:end])
        if end < len(lines) or content.endswith("\n"):
            part += "\n"
        chunks.append(Chunk(f"{file_id}_c{idx:03d}", start + 1, end, part))
        idx += 1
    return tuple(chunks)

def make_file_id(relative_path: str) -> str:
    return hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:12]

def collect_files(config: BundleConfig) -> tuple[FileRecord, ...]:
    records: list[FileRecord] = []
    root = config.diretorio.resolve()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        is_root = (current == root)

        if config.only_core:
            dirnames[:] = sorted(d for d in dirnames if (d in PASTAS_CORE or not is_root) and d not in PASTAS_IGNORAR)
        elif config.exclude_core:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_CORE and d not in PASTAS_IGNORAR)
        else:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_IGNORAR)

        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root)
            rel_path = rel.as_posix()
            top = rel.parts[0] if rel.parts else ""

            if config.only_core and is_root and top not in PASTAS_CORE:
                continue
            if config.exclude_core and is_root and top in PASTAS_CORE:
                continue
            if is_sensitive_file(path):
                continue
            if not is_text_file(path):
                continue

            try:
                raw_content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    raw_content = path.read_text(encoding="latin-1")
                except OSError as e:
                    logging.warning("Pulando %s: %s", rel_path, e)
                    continue
            except OSError as e:
                logging.warning("Pulando %s: %s", rel_path, e)
                continue

            domain = classify_domain(rel_path)
            if not should_include_profile(domain, config):
                continue

            raw_sha1 = hashlib.sha1(raw_content.encode("utf-8", errors="ignore")).hexdigest()
            content = mask_sensitive(raw_content, config.mask_secrets)
            file_id = make_file_id(rel_path)
            stat = path.stat()
            suffix = path.suffix.lower()

            symbols = extract_symbols(content, suffix) if config.emit_symbol_index else ()
            imports = extract_imports(content, suffix) if config.emit_import_map else ()
            chunks = chunk_content(content, file_id, config.max_lines_per_file)

            records.append(FileRecord(
                file_id=file_id, relative_path=rel_path, domain=domain,
                language=LINGUAGENS.get(suffix, suffix[1:] if suffix else "text"),
                line_count=len(content.splitlines()),
                byte_count=len(content.encode("utf-8", errors="ignore")),
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                sha1=raw_sha1, symbols=symbols, imports=imports, chunks=chunks
            ))

    records.sort(key=lambda r: r.relative_path)
    return tuple(records)

def mode_name(config: BundleConfig) -> str:
    if config.only_core: return "only-core"
    if config.exclude_core: return "exclude-core"
    return "full"

def render_frontmatter(config: BundleConfig, records: tuple[FileRecord, ...]) -> str:
    total_bytes = sum(r.byte_count for r in records)
    lines = [
        "---", "schema_version: 1",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"root: {config.diretorio.resolve().name}",
        f"mode: {mode_name(config)}", f"profile: {config.profile}",
        f"file_count: {len(records)}", f"byte_count: {total_bytes}",
        "ignored_dirs:"
    ]
    lines.extend(f"  - {d}" for d in sorted(PASTAS_IGNORAR))
    lines.append("sensitive_rules:")
    lines.extend(f"  - {r}" for r in sorted(ARQUIVOS_SENSIVEIS_GLOBS))
    lines.append("---")
    return "\n".join(lines)

def render_index_by_domain(records: tuple[FileRecord, ...]) -> str:
    grouped: dict[str, list[FileRecord]] = {}
    for r in records:
        grouped.setdefault(r.domain, []).append(r)
    lines = ["## INDEX_BY_DOMAIN"]
    for domain in sorted(grouped):
        lines.append(f"- `{domain}`:")
        lines.extend(f"  - `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in grouped[domain])
    return "\n".join(lines)

def render_index_by_path(records: tuple[FileRecord, ...]) -> str:
    lines = ["## INDEX_BY_PATH"]
    lines.extend(f"- `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in records)
    return "\n".join(lines)

def render_symbols(records: tuple[FileRecord, ...]) -> str:
    lines = ["## SYMBOL_INDEX"]
    for r in records:
        if not r.symbols: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{s}`" for s in r.symbols)
    return "\n".join(lines)


```
CHUNK_END id=c3916196f58f_c001
CHUNK_START id=c3916196f58f_c002 start_line=301 end_line=380
````python
def render_imports(records: tuple[FileRecord, ...]) -> str:
    lines = ["## IMPORT_MAP_MIN"]
    for r in records:
        if not r.imports: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{i}`" for i in r.imports)
    return "\n".join(lines)

def pick_fence(content: str) -> str:
    return "````" if "```" in content else "```"


````
CHUNK_END id=aa78525fb574_c007
CHUNK_START id=aa78525fb574_c008 start_line=2101 end_line=2400
````markdown
def render_file_record(record: FileRecord, toc_only: bool) -> str:
    lines = [
        "---", f'<a id="file_{record.file_id}"></a>',
        f"FILE_START id=file_{record.file_id} path={record.relative_path} "
        f"domain={record.domain} lang={record.language} lines={record.line_count} "
        f"bytes={record.byte_count} mtime={record.mtime_utc} sha1={record.sha1}"
    ]
    if toc_only:
        lines.append("CONTENT_OMITTED toc_only=true")
    else:
        for chunk in record.chunks:
            lines.append(f"CHUNK_START id={chunk.chunk_id} start_line={chunk.start_line} end_line={chunk.end_line}")
            fence = pick_fence(chunk.content)
            lines.extend([f"{fence}{record.language}", chunk.content, fence, f"CHUNK_END id={chunk.chunk_id}"])
    lines.append(f"FILE_END id=file_{record.file_id}")
    return "\n".join(lines)

def generate_context_markdown(config: BundleConfig) -> str:
    if config.only_core and config.exclude_core:
        raise ValueError("only_core e exclude_core nao podem ser usados juntos")
    
    records = collect_files(config)
    blocks = ["# Project Context Bundle", "", render_frontmatter(config, records), "",
              render_index_by_domain(records), "", render_index_by_path(records)]
    if config.emit_symbol_index:
        blocks.extend(["", render_symbols(records)])
    if config.emit_import_map:
        blocks.extend(["", render_imports(records)])
    for r in records:
        blocks.extend(["", render_file_record(r, toc_only=config.toc_only)])
    return "\n".join(blocks) + "\n"

def write_output(config: BundleConfig) -> Path:
    output_path = config.diretorio / config.output
    content = generate_context_markdown(config)
    output_path.write_text(content, encoding="utf-8")
    return output_path

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="captura_projeto.py - Consolida repositorio em markdown AI-first")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretorio raiz")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Arquivo de saida")
    core = parser.add_mutually_exclusive_group()
    core.add_argument("--only-core", action="store_true", help="Inclui apenas escopo core")
    core.add_argument("--exclude-core", action="store_true", help="Exclui escopo core")
    parser.add_argument("--profile", choices=["ai-default", "ai-compact", "ai-forensics"], default="ai-default")
    parser.add_argument("--toc-only", action="store_true", help="Apenas indices e envelopes")
    parser.add_argument("--max-lines-per-file", type=int, default=300, help="Limite de linhas por chunk (0=ilimitado)")
    parser.add_argument("--emit-symbol-index", action="store_true", help="Adiciona SYMBOL_INDEX")
    parser.add_argument("--emit-import-map", action="store_true", help="Adiciona IMPORT_MAP_MIN")
    parser.add_argument("--mask-secrets", action="store_true", help="Ofusca segredos no conteudo")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = BundleConfig(
        diretorio=Path(args.diretorio), output=args.output,
        only_core=args.only_core, exclude_core=args.exclude_core,
        profile=args.profile, toc_only=args.toc_only,
        max_lines_per_file=args.max_lines_per_file,
        emit_symbol_index=args.emit_symbol_index,
        emit_import_map=args.emit_import_map, mask_secrets=args.mask_secrets
    )
    out = write_output(config)
    print(f"\n[OK] Gerado: {out}")
    print(f"   Mode: {mode_name(config)} | Profile: {config.profile}")

if __name__ == "__main__":
    main()
````
CHUNK_END id=c3916196f58f_c002
FILE_END id=file_c3916196f58f

---
<a id="file_aa78525fb574"></a>
FILE_START id=file_aa78525fb574 path=contexto.md domain=docs lang=markdown lines=8731 bytes=353497 mtime=2026-04-11T03:19:12.264357+00:00 sha1=4b395874ffa810b94524e991db3f0b3b39a4c668
CHUNK_START id=aa78525fb574_c001 start_line=1 end_line=300
````markdown
# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-11T03:19:12.258311+00:00
root: template_inicío_de_projeto
mode: full
profile: ai-default
file_count: 37
byte_count: 329430
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

## SYMBOL_INDEX
- `.context/_scripts/cleanup_specs.py`:
  - `get_specs`
  - `archive_spec`
  - `cleanup`
- `.context/_scripts/purge_journal.py`:
  - `parse_entries`
  - `purge_journal`
- `.context/_scripts/sync_project.py`:
  - `get_package_deps`
  - `get_schema_tables`
  - `sync_requirements`
- `.context/_scripts/validate_context.py`:
  - `check_files`
  - `check_journal_lines`
  - `estimate_tokens`
  - `check_registry_structure`
  - `check_specs_structure`
  - `validate`
- `captura_projeto.py`:
  - `is_text_file`
  - `is_sensitive_file`
  - `classify_domain`
  - `should_include_profile`
  - `mask_sensitive`
  - `extract_symbols`
  - `extract_imports`
  - `chunk_content`
  - `make_file_id`
  - `collect_files`
  - `mode_name`
  - `render_frontmatter`
  - `render_index_by_domain`
  - `render_index_by_path`
  - `render_symbols`
  - `render_imports`
  - `pick_fence`
  - `render_file_record`
  - `generate_context_markdown`
  - `write_output`
  - `parse_args`
  - `main`
  - `BundleConfig`
  - `Chunk`
  - `FileRecord`
- `run_context.py`:
  - `run_script`
  - `main`
- `tests/test_context.py`:
  - `TestContextGovernance`

## IMPORT_MAP_MIN
- `.context/_scripts/cleanup_specs.py`:
  - `os`
  - `shutil`
  - `time`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/purge_journal.py`:
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/sync_project.py`:
  - `json`
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/validate_context.py`:
  - `os`
  - `sys`
  - `from pathlib import Path`
- `captura_projeto.py`:
  - `argparse`
  - `hashlib`
  - `logging`
  - `mimetypes`
  - `os`
  - `re`
  - `from __future__ import annotations`
  - `from dataclasses import dataclass`
  - `from datetime import datetime, timezone`
  - `from fnmatch import fnmatch`
  - `from pathlib import Path`
- `run_context.py`:
  - `sys`
  - `subprocess`
  - `from pathlib import Path`
- `tests/test_context.py`:
  - `unittest`
  - `os`
  - `shutil`
  - `tempfile`

````
CHUNK_END id=aa78525fb574_c008
CHUNK_START id=aa78525fb574_c009 start_line=2401 end_line=2700
````markdown
  - `subprocess`
  - `sys`
  - `from pathlib import Path`

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CHUNK_START id=82cd6bde54ff_c001 start_line=1 end_line=71
```python
#!/usr/bin/env python3
"""
🧹 cleanup_specs.py
Gerencia a efemeridade da bancada de trabalho (.specs/).
Aplica a regra de 48h de inatividade e limite de 3 specs ativas simultâneas.
Arquiva specs excedentes ou obsoletas em _archive_context/specs/.
"""
import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# Caminhos base
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "specs"

# Configurações
MAX_INACTIVITY_SECONDS = 48 * 3600  # 48 horas
MAX_ACTIVE_SPECS = 3

def get_specs():
    if not SPECS_DIR.exists():
        return []
    return [d for d in SPECS_DIR.iterdir() if d.is_dir()]

def archive_spec(spec_path):
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{spec_path.name}_{timestamp}"
    dest_path = ARCHIVE_DIR / archive_name
    
    print(f"[INFO] Arquivando spec: {spec_path.name} -> {archive_name}")
    shutil.move(str(spec_path), str(dest_path))

def cleanup():
    specs = get_specs()
    if not specs:
        print("[OK] Nenhuma spec ativa encontrada.")
        return

    now = time.time()
    active_specs = []

    # 1. Limpeza por inatividade (48h)
    for spec in specs:
        last_mod = max(os.path.getmtime(root) for root, _, _ in os.walk(spec))
        if (now - last_mod) > MAX_INACTIVITY_SECONDS:
            print(f"[AUTO] Inatividade detectada (>48h) em: {spec.name}")
            archive_spec(spec)
        else:
            active_specs.append(spec)

    # 2. Limpeza por limite de volume (Max 3)
    # Ordena por data de modificação (mais antiga primeiro)
    active_specs.sort(key=lambda s: max(os.path.getmtime(root) for root, _, _ in os.walk(s)))
    
    while len(active_specs) > MAX_ACTIVE_SPECS:
        oldest = active_specs.pop(0)
        print(f"[AUTO] Limite de volume excedido (Max {MAX_ACTIVE_SPECS}). Removendo spec mais antiga: {oldest.name}")
        archive_spec(oldest)

    print(f"[OK] Manutencao de specs concluida. Specs ativas: {len(active_specs)}/{MAX_ACTIVE_SPECS}")

if __name__ == "__main__":
    try:
        cleanup()

````
CHUNK_END id=aa78525fb574_c001
CHUNK_START id=aa78525fb574_c002 start_line=301 end_line=600
````markdown
    except Exception as e:
        print(f"[ERROR] Falha na limpeza de specs: {e}")

```
CHUNK_END id=82cd6bde54ff_c001
FILE_END id=file_82cd6bde54ff

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=74 bytes=2507 mtime=2026-04-11T00:15:41.168457+00:00 sha1=772904f793113782bf9cc398ad20f87cefdc018c
CHUNK_START id=024b28a37d29_c001 start_line=1 end_line=74
```python
#!/usr/bin/env python3
"""
🗜️ purge_journal.py
Arquiva 70% das entradas mais antigas do JOURNAL.md.
Mantém 30% mais recentes como semente. Backup automático e escrita atômica.
"""
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
JOURNAL_FILE = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "journals"
KEEP_RATIO = 0.3  # 30% mais recentes

def parse_entries(content):
    # Divide por headers markdown (## 📅, ##, etc.) mantendo o header na entrada
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]

def purge_journal():
    if not JOURNAL_FILE.exists():
        print("[WARN] JOURNAL.md nao encontrado. Nada a fazer.")
        return

    content = JOURNAL_FILE.read_text(encoding="utf-8")
    entries = parse_entries(content)

    if len(entries) <= 1:
        print("[INFO] Poucas entradas para purgar.")
        return

    keep_count = max(1, int(len(entries) * KEEP_RATIO))
    archive_entries = entries[:-keep_count]
    keep_entries = entries[-keep_count:]

    # Garante diretório de arquivo
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Backup com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_file = ARCHIVE_DIR / f"journal_archive_{timestamp}.md"
    archive_content = f"# Arquivo de Journal - {timestamp}\n\n" + "\n\n".join(archive_entries) + "\n"
    archive_file.write_text(archive_content, encoding="utf-8")

    # Nova semente
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    seed = f"""---
Criado em: {now}
Ultima Atualizacao: {now}
Status: Ativo
Nota: Semente pos-purge. {len(archive_entries)} entradas arquivadas em {archive_file.name}.
---

# JOURNAL.md (Memoria Curta)
> Mantido por purge_journal.py. Limite heuristico de caracteres atingido.

""" + "\n\n".join(keep_entries) + "\n"

    # Escrita atomica (previne corrupcao se interrupcao ocorrer)
    temp_file = JOURNAL_FILE.with_suffix(".tmp")
    temp_file.write_text(seed, encoding="utf-8")
    temp_file.replace(JOURNAL_FILE)

    print(f"[OK] Purge concluido.")
    print(f"[OK] Arquivadas: {len(archive_entries)} entradas -> {archive_file.name}")
    print(f"[OK] Mantidas: {len(keep_entries)} entradas mais recentes.")

if __name__ == "__main__":
    try:
        purge_journal()
    except Exception as e:
        print(f"[ERROR] Erro no purge: {e}")

```
CHUNK_END id=024b28a37d29_c001
FILE_END id=file_024b28a37d29

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=94 bytes=3162 mtime=2026-04-11T00:15:52.626055+00:00 sha1=b9acd032350a262fad7d0995116e5686b8fa2191
CHUNK_START id=f122711ba9e1_c001 start_line=1 end_line=94
```python
#!/usr/bin/env python3
"""
🔄 sync_project.py
Sincroniza TECH_REQUIREMENTS.md com package.json e schema.sql.
Usa marcadores <!-- AUTO-SYNC START/END --> para preservar edicoes humanas.
"""
import json
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQ_FILE = CONTEXT_DIR / "maintenance" / "TECHNICAL_REQUIREMENTS.md"
PKG_FILE = CONTEXT_DIR.parent / "package.json"
SCHEMA_FILE = CONTEXT_DIR / "maintenance" / "schema.sql"

AUTO_START = "<!-- AUTO-SYNC START -->"
AUTO_END = "<!-- AUTO-SYNC END -->"

def get_package_deps():
    if not PKG_FILE.exists(): return {"dependencies": {}, "devDependencies": {}}
    try:
        with open(PKG_FILE, 'r', encoding='utf-8') as f:
            pkg = json.load(f)
        return {
            "dependencies": pkg.get("dependencies", {}),
            "devDependencies": pkg.get("devDependencies", {})
        }
    except Exception as e:
        print(f"[WARN] Erro ao ler package.json: {e}")
        return {"dependencies": {}, "devDependencies": {}}

def get_schema_tables():
    if not SCHEMA_FILE.exists(): return []
    content = SCHEMA_FILE.read_text(encoding="utf-8")
    # Regex para extrair nomes de tabelas
    return list(set(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["\']?(\w+)["\']?', content, re.IGNORECASE)))

def sync_requirements():
    deps = get_package_deps()
    tables = get_schema_tables()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    block = [
        AUTO_START,
        f"*🤖 Atualizado automaticamente em {now}*",
        ""
    ]

    if deps.get("dependencies"):
        block.append("### Dependencias (package.json)")
        for dep, ver in deps["dependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if deps.get("devDependencies"):
        block.append("### DevDependencies")
        for dep, ver in deps["devDependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if tables:
        block.append("### Tabelas no Schema (schema.sql)")
        for t in sorted(tables):
            block.append(f"- `{t}`")
        block.append("")

    block.append(AUTO_END)
    auto_content = "\n".join(block) + "\n"

    if not REQ_FILE.exists():
        REQ_FILE.write_text(f"# TECHNICAL_REQUIREMENTS.md\n\n{auto_content}", encoding="utf-8")
        print("[OK] TECHNICAL_REQUIREMENTS.md criado.")
        return

    content = REQ_FILE.read_text(encoding="utf-8")
    start_idx = content.find(AUTO_START)
    end_idx = content.find(AUTO_END)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + auto_content + content[end_idx + len(AUTO_END):]
    else:
        new_content = content.rstrip() + "\n\n" + auto_content

    REQ_FILE.write_text(new_content, encoding="utf-8")
    print("[OK] TECHNICAL_REQUIREMENTS.md sincronizado.")
    print(f"[OK] {len(deps.get('dependencies', {}))} deps | {len(tables)} tabelas detectadas.")

if __name__ == "__main__":
    try:
        sync_requirements()
    except Exception as e:
        print(f"[ERROR] Erro no sync: {e}")

```
CHUNK_END id=f122711ba9e1_c001
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=106 bytes=3827 mtime=2026-04-11T02:29:28.743870+00:00 sha1=e6e9a29604fb4a340a2335bbca07488c56baff2a
CHUNK_START id=1077e9084ea1_c001 start_line=1 end_line=106
```python
#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade com AGENT_REGISTRY.md.
"""
import os
import sys
from pathlib import Path

# Caminhos relativos a localização deste script (.context/_scripts/)
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

# Mapeamento para estrutura em camadas
REQUIRED_FILES = [
    "brain/RULES.md", 
    "brain/MASTER_FLOW.md", 

````
CHUNK_END id=aa78525fb574_c009
CHUNK_START id=aa78525fb574_c010 start_line=2701 end_line=3000
````markdown
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md", 
    "maintenance/JOURNAL.md", 
    "maintenance/schema.sql", 
    "maintenance/TECHNICAL_REQUIREMENTS.md"
]

JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000  # ~100k tokens

def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]

def check_journal_lines():
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists(): return 0, True
    lines = journal.read_text(encoding="utf-8").splitlines()
    return len(lines), len(lines) <= JOURNAL_MAX_LINES

def estimate_tokens():
    total_chars = 0
    for f in REQUIRED_FILES:
        path = CONTEXT_DIR / f
        if path.exists():
            total_chars += len(path.read_text(encoding="utf-8", errors="ignore"))
    return total_chars, total_chars < TOKEN_WARN_THRESHOLD_CHARS

def check_registry_structure():
    registry = CONTEXT_DIR / "brain/AGENT_REGISTRY.md"
    if not registry.exists(): return False, "Arquivo ausente"
    content = registry.read_text(encoding="utf-8")
    if "| Role |" not in content and "| Role" not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"

def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists(): return True, "Workshop inativo (OK)"
    
    features_dir = specs_dir / "features"
    if not features_dir.exists(): return False, "Diretorio features ausente no .specs"
    
    # Verifica se algum STATE.md esta presente em specs ativas
    active_specs = [d for d in features_dir.iterdir() if d.is_dir()]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
            
    return True, f"OK ({len(active_specs)} specs ativas)"

def validate():
    print("--- Iniciando validacao de contexto (v2.2 Premium+) ---")
    issues = []

    missing = check_files()
    if missing: issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else: print("[OK] Todos os arquivos obrigatorios presentes.")

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok: issues.append(f"[WARN] .specs/: {spec_msg}")
    else: print(f"[OK] .specs/: {spec_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok: issues.append(f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}")
    else: print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, token_ok = estimate_tokens()
    est_tokens = total_chars // 4
    if not token_ok:
        issues.append(f"[WARN] Contexto estimado alto: ~{est_tokens}k tokens. Execute purge.")
    else: print(f"[OK] Estimativa de contexto segura: ~{est_tokens}k tokens")

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok: issues.append(f"[WARN] AGENT_REGISTRY.md: {reg_msg}")
    else: print("[OK] AGENT_REGISTRY.md estrutura valida.")

    print("\n--- Relatorio Final ---")
    if not issues:
        print("[SUCCESS] Contexto integro. Pronto para execucao.")
    else:
        for issue in issues: print(issue)
        print("[ALERT] Resolva os alertas antes de gerar codigo.")


````
CHUNK_END id=aa78525fb574_c002
CHUNK_START id=aa78525fb574_c003 start_line=601 end_line=900
````markdown
if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        sys.exit(1)

```
CHUNK_END id=1077e9084ea1_c001
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=97 bytes=7180 mtime=2026-04-11T02:28:38.100881+00:00 sha1=3232fd65b8b05382d366aa1a8890e6385eb7f705
CHUNK_START id=e7c17acb71ff_c001 start_line=1 end_line=97
````markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Testes unitários/E2E, edge cases, cobertura, mocks, TDD | `tests/`, `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (apenas leitura para bugs) | `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (critérios de aceite) | "testar", "validar", "cobertura", "mock", "edge case", "TDD", "bug" |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@spec-driver` | Criação e orquestração de specs atômicas | `.specs/` (leitura/gravação temporária) | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (tail 30) | "inicie specify", "crie spec", "modo híbrido" |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |

💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Carregar APENAS: Global + Role-Specific + Task-Ephemeral
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*

````
CHUNK_END id=e7c17acb71ff_c001
FILE_END id=file_e7c17acb71ff

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=86 bytes=4370 mtime=2026-04-11T02:59:02.297440+00:00 sha1=06ce6786a149620314b57f8231142f652d4fc412
CHUNK_START id=d833c436f547_c001 start_line=1 end_line=86
````markdown
---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-04-10 23:28
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura do Diretório `.context/`

```text
.context/
├── 🧠 brain/                       # CAMADA COGNITIVA (The Brain)
│   ├── MASTER_FLOW.md             # Este documento
│   ├── RULES.md                   # Protocolos e "A Lei"
│   ├── AGENT_REGISTRY.md          # DNS de Roles e Permissões
│   ├── PROMPT_LIBRARY.md          # Catálogo de templates de prompts
│   ├── PRD.md                     # Requisito em execução (v2.0 - O Contrato)
│   ├── ROADMAP.md                 # Metas e fases (O Planejamento)
│   └── TLC_INTEGRATION.md         # Ponte entre Governança e Execução
│
├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
│   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Curta)
│   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e versões (Inventário)
│   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
│   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
│   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
│   ├── TESTS.md                   # Ledger de padrões e TDDs
│   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
│   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
│   └── _archive_context/          # Histórico imutável (A Biblioteca)
│
├── monitoring/             # CAMADA DE MONITORAMENTO (The Guardian)
│   └── CONTEXT_HEALTH.md   # Dashboard de saúde técnica e cognitiva
│
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── _scripts/               # CAMADA DE AUTOMACAO (The Motor)
    ├── validate_context.py        # Validador de integridade
    ├── purge_journal.py           # Gerenciador de memória (Purge)
    ├── cleanup_specs.py           # Gerenciador de efemeridade (.specs)
    └── sync_project.py            # Sincronizador de requisitos
```

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e a presença do `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões arquiteturais tomadas durante o TLC **devem** ser migradas para o `JOURNAL.md` antes da limpeza da spec.

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*

````
CHUNK_END id=d833c436f547_c001

````
CHUNK_END id=aa78525fb574_c010
CHUNK_START id=aa78525fb574_c011 start_line=3001 end_line=3300
````markdown
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=67 bytes=2446 mtime=2026-04-11T01:31:37.755946+00:00 sha1=b5c06bc8a67d2a788cc8263f03971f379d04e92e
CHUNK_START id=d124f6374cab_c001 start_line=1 end_line=67
```markdown
---
Criado em: 2026-04-10 22:35
Ultima Atualizacao: 2026-04-10 22:35
Status: Ativo (EM EXECUCAO)
PRD_ID: #15
---

# 🎯 PRD: Checkout com Integração Stripe
> Implementar um fluxo de pagamento seguro e resiliente usando Stripe Elements e Webhooks para pedidos digitais.

💡 *Insight Humano: Este PRD é um contrato vivo. Ele guia o roteamento de agentes, define criterios de aceite e serve como referência para o JOURNAL.md.*

---

## 📋 1. Visão Geral
| Campo | Valor |
|-------|-------|
| **Objetivo de Negocio** | Reduzir abandono de carrinho e garantir seguranca no processamento. |
| **Publico-Alvo** | Compradores finais da plataforma. |
| **Escopo** | UI de pagamento, Geracao de Session, Webhooks de confirmacao. |
| **MVP vs Futuro** | MVP: Cartao de Credito. Futuro: Apple Pay/Google Pay. |
| **Dependencias** | Stripe API, Tabela `orders`, Variaveis de ambiente seguras. |

---

## 🎯 2. Critérios de Aceite (Definition of Done)
### Funcionais
- [ ] Usuario finaliza compra com cartao valido.
- [ ] Webhook atualiza `orders.status` para 'succeeded'.
- [ ] Erro de cartao exibe mensagem amigavel (WCAG).
- [ ] Idempotencia garantida via `event.id` do Stripe.

### Não-Funcionais
- [ ] Tempo de resposta API < 500ms.
- [ ] Nenhum segredo (Keys) hardcoded no codigo.
- [ ] Logs estruturados para auditoria.

---

## 🤖 3. Roteamento Multi-Agent
| Etapa | Role Responsável | Entregável | Gatilho de Handoff |
|-------|-----------------|------------|-------------------|
| 1. UI Checkout | `@frontend-specialist` | `StripeForm.tsx` | "UI pronta, aguarda contrato de API" |
| 2. API Stripe | `@backend-engineer` | `/api/checkout` + Webhook | "Rotas operacionais, inicia validacao" |
| 3. Testes E2E | `@qa-validator` | Suite de testes | "Cobertura >90%, edge cases validados" |

---

## 🔒 4. Context Gate (Pré-Execução)
- [ ] `maintenance/schema.sql` contem a tabela `orders`? ✅
- [ ] `maintenance/TECHNICAL_REQUIREMENTS.md` atualizado? ✅
- [ ] `maintenance/JOURNAL.md` < 550 linhas? ✅
- [ ] `brain/AGENT_REGISTRY.md` tem as roles necessarias? ✅

---

## 📊 5. Health Check Integrado
| Metrica | Valor | Status |
|---------|-------|--------|
| **Progresso** | 50% | 🟡 Em andamento |
| **Cobertura de Testes** | 92% (Simulada) | ✅ OK |
| **Divergência Schema** | 0 campos | ✅ OK |

---

## 🔄 6. Ciclo de Vida & Arquivamento
Ao concluir, mover para `_archive_context/prds/` e atualizar `ROADMAP.md`.

```
CHUNK_END id=d124f6374cab_c001
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=154 bytes=6687 mtime=2026-04-11T02:28:52.575335+00:00 sha1=aa3419c1efa08687a7c551dc44f40b504b422353
CHUNK_START id=9fe16e5591f0_c001 start_line=1 end_line=154
````markdown
---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo

````
CHUNK_END id=aa78525fb574_c003
CHUNK_START id=aa78525fb574_c004 start_line=901 end_line=1200
````markdown
---

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator`
**Gatilho:** Testes, validacao, edge cases, cobertura, mocks  
**Contexto Obrigatorio:** `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (criterios de aceite)
```text
🤖 Ativando @qa-validator | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{arquivo/feature a ser testada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{criar testes, validar edge cases ou aumentar cobertura}}
🚧 Restricoes:
- Seguir framework de testes definido em maintenance/TECHNICAL_REQUIREMENTS.md
- Mockar servicos externos; nao depender de rede real
- Cobrir happy path + 2 edge cases criticos no minimo
- Documentar falhas conhecidas no maintenance/JOURNAL.md se houver
📤 Saida Esperada:
1. Codigo dos testes (unitarios/integracao)
2. Matriz de cenarios cobertos
3. Recomendacoes de refatoracao se aplicavel
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada
2. spec.md com passos, contratos e critérios de verificação
3. STATE.md: draft → pronto para execução
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*

````
CHUNK_END id=9fe16e5591f0_c001
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.772397+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=c94f001202db_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=c94f001202db_c001
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=70 bytes=4536 mtime=2026-04-11T02:57:50.282657+00:00 sha1=49f182ecde4e634b51130172a7a7d4e78ac48ee1
CHUNK_START id=cd6526d17218_c001 start_line=1 end_line=70
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 23:55
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança
**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)  
> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas para garantir escala, foco e rastreabilidade.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)
Antes de gerar código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:
1. **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`
2. **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
3. **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`

> ⚠️ **Bloqueio de Execução:** Se qualquer item estiver ausente ou desatualizado, a IA deve parar e solicitar a carga correta antes de prosseguir.

---

## 🔢 2. Session Budget & Heurísticas de Token
Para evitar alucinações por *Token Bloat* (excesso de memória na janela):
- **Gatilhos de Alerta:** ~50.000 caracteres acumulados OU ~15-20 trocas densas de desenvolvimento.
- **Ação ao atingir o limite:** Disparar: *"🔄 Contexto próximo do limite de foco. Deseja que eu execute o purge do JOURNAL, arquive o PRD atual ou inicie uma nova sessão limpa com snapshot de semente?"*

---

## 🧠 3. Protocolo de Manutenção do Contexto
A IA atua como bibliotecário chefe. Consistência entre Código e Contexto é obrigatória.
- **`maintenance/JOURNAL.md`:** Apenas decisões de arquitetura, resoluções de bugs complexos e mudanças de lógica. Proibido logar erros triviais. Ao atingir ~600 linhas ou 50k chars → acionar `_scripts/purge_journal.py`.
- **`maintenance/TECHNICAL_REQUIREMENTS.md`:** Atualizar sempre que houver mudança em `package.json`, alteração de Schema ou integração de novas APIs.
- **`maintenance/rebuild_guide.md`:** Atualizar com hacks de ambiente local, CI/CD ou passos manuais de deploy.
- **`.specs/` (Workshop Efêmero):** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/`. Decisões técnicas devem migrar para o `JOURNAL.md` antes da limpeza.

````
CHUNK_END id=aa78525fb574_c011
CHUNK_START id=aa78525fb574_c012 start_line=3301 end_line=3600
````markdown

---

## 🗄️ 4. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.
1. **Verificação Obrigatória:** Antes de criar UI/lógica dependente de dados, validar `maintenance/schema.sql`.
2. **Aviso de Divergência:** Se o código exigir um campo inexistente, parar e avisar: *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro gerar a migration antes de prosseguir."*

---

## 🤖 5. Comportamento do Agente (Transparência & Roteamento)
- **Ativação:** Toda tarefa complexa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`
- **Isolamento:** Carregar APENAS `Global + Role-Specific + Task-Ephemeral`. Ignorar o resto.
- **Handoff:** Cruzar 2+ domínios? Pausar → registrar no `JOURNAL.md`:  
  `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo: [ação]`
- **Context Gate (Pré-Código):** Validar antes de gerar:  
  `[ ] PRD ativo` | `[ ] schema contém estruturas` | `[ ] JOURNAL < 550 linhas` | `[ ] zero secrets hardcoded`

---

## 🔄 6. Gatilhos de Interação (Para o Usuário)
- `"Atualize o contexto"` → IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- `"Qual o estado do projeto?"` → Relatório baseado no `JOURNAL.md` + `ROADMAP.md`.
- `"Roteie esta tarefa"` → Consulta `AGENT_REGISTRY.md`, inicia ativação/handoff.
- `"Use o prompt padrão"` → Seleciona template em `brain/PROMPT_LIBRARY.md`, preenche placeholders, solicita confirmação.
- `"Inicie SPECIFY para PRD #[ID]"` → Cria `.specs/features/`, gera `spec.md` alinhado ao PRD, inicia ciclo TLC.

---

## 🚨 7. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.

```
CHUNK_END id=cd6526d17218_c001
FILE_END id=file_cd6526d17218

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CHUNK_START id=450d7ec70909_c001 start_line=1 end_line=32
```markdown
---
Criado em: 2026-04-10 23:29
Ultima Atualizacao: 2026-04-10 23:29
Status: Ativo
---

# 🔗 TLC_INTEGRATION.md
> Ponte entre Governança de Longo Prazo (`.context/`) e Execução Atômica (`.specs/`).  
> 💡 *Insight Humano: O PRD diz O QUÊ e POR QUÊ. A SPEC diz COMO e QUANDO. O TLC orquestra a transição.*

## 🔄 Ciclo de Vida Híbrido
1. **INTENT** → `PRD.md` ativo define escopo e critérios de aceite.
2. **SPECIFY** → IA cria `.specs/features/[nome]/spec.md` com passos atômicos, contratos de API/DB e testes.
3. **IMPLEMENT** → Geração de código baseada na spec. Handoffs registrados no `JOURNAL.md`.
4. **VERIFY** → Testes passam → `STATE.md` marcado como `✅ PASSED`.
5. **SYNC** → Decisões arquiteturais e lições → `JOURNAL.md`. Spec arquivada ou deletada.

## 📏 Regras de Ouro
- 🔒 **Soberania do Contexto:** `.specs/` nunca sobrescreve `.context/`. Apenas alimenta a memória de longo prazo.
- 🧹 **Efemeridade:** Spec inativa >48h ou pós-merge → mover para `_archive_context/specs/` ou deletar.
- 🤝 **Handoff:** Handoff obrigatório no `JOURNAL.md` se a spec cruzar domínios (ex: `@backend` → `@qa`).
- ⚠️ **Divergência:** Se `spec.md` divergir de `schema.sql` ou `PRD.md` → parar e solicitar correção de contexto.

## 🤖 Fluxo de Ativação
`"Inicie a fase de SPECIFY para o PRD #[ID]"` → 
1. IA lê `PRD.md` + `schema.sql` + `JOURNAL.md` (últimas 30).
2. Cria `.specs/features/[nome]/` com `spec.md` e `STATE.md: draft`.
3. Executa passos atômicos → atualiza `STATE.md`.
4. Ao concluir: `✅ Spec passed. Deseja arquivar a spec e sincronizar o JOURNAL.md?`

---
> *Este documento garante que o "Cérebro" (Contexto) e o "Músculo" (TLC) operem em harmonia.*

```
CHUNK_END id=450d7ec70909_c001
FILE_END id=file_450d7ec70909

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.800876+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=9b6470da8849_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=9b6470da8849_c001
FILE_END id=file_9b6470da8849

---

````
CHUNK_END id=aa78525fb574_c004
CHUNK_START id=aa78525fb574_c005 start_line=1201 end_line=1500
````markdown
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=23 bytes=1082 mtime=2026-04-11T01:25:28.436758+00:00 sha1=43293ddbefe17288e0cea85c402cff9f4ed05cea
CHUNK_START id=019509328844_c001 start_line=1 end_line=23
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# JOURNAL.md
> Log vivo de decisoes e bugs. (Max 600 linhas)

## 📅 2026-04-11 01:25
**Decisão/Bug:** 🔄 Handoff: @frontend-specialist → @backend-engineer
**Solução:** Implementada UI do CheckoutForm v1 usando Stripe Elements. Estado local gerenciado; aguardando API `/api/checkout/session`.
**Implicação:** Próximo agente deve configurar a rota backend e garantir o retorno do `clientSecret`.

## 📅 2026-04-11 01:35
**Decisão/Bug:** 🔄 Handoff: @backend-engineer → @qa-validator
**Solução:** Endpoint Stripe Session operacional. Webhook configurado para escutar `payment_intent.succeeded` e atualizar tabela `orders`.
**Implicação:** QA deve validar fluxos de falha e idempotência do webhook.

## 📅 2026-04-11 01:45
**Decisão/Bug:** ✅ Ciclo Checkout Stripe Concluído
**Solução:** Cobertura de testes em 92%. Validado happy path e 'card declined'. Injetado retry pattern no webhook.
**Implicação:** PRD #15 concluído. Tecnologias Stripe adicionadas ao env.

```
CHUNK_END id=019509328844_c001
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=14 bytes=287 mtime=2026-04-11T03:14:23.819547+00:00 sha1=71b173ae91c93ed58cf9027ce03c8ed12ae79b4f
CHUNK_START id=d069d4f2ebef_c001 start_line=1 end_line=14
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

<!-- AUTO-SYNC START -->
*🤖 Atualizado automaticamente em 2026-04-11 00:14*

### DevDependencies
- `husky`: `^9.1.7`

### Tabelas no Schema (schema.sql)
- `orders`

<!-- AUTO-SYNC END -->



```
CHUNK_END id=d069d4f2ebef_c001
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.794384+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=0858a02cf53f_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=0858a02cf53f_c001
FILE_END id=file_0858a02cf53f

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CHUNK_START id=a5c71962029a_c001 start_line=1 end_line=63
````markdown
---
Criado em: 2026-04-10 21:44
Ultima Atualizacao: 2026-04-10 21:44
Status: Ativo
---

# 🛠️ Manual de Reconstrução & Automação

Este guia contém as instruções para subir o ambiente do zero e operar as ferramentas de governança de contexto.

---

## 🏗️ 1. Setup do Ambiente

### Requisitos Mínimos:
- **Python ≥ 3.8** (Para os scripts de automação)
- **Node.js** (Para os wrappers NPM)
- **Make** (Opcional, para orquestração Unix)
- **Bash** (Para Git Bash, WSL, Linux ou macOS)

---

## ⚙️ 2. Ferramentas de Automação

O projeto oferece três formas de gerenciar a saúde do contexto. Escolha a que melhor se adapta ao seu terminal:

### Opção A: Via NPM (Recomendado para Devs Web)
```bash
npm run context:validate  # Checa integridade e tokens
npm run context:sync      # Sincroniza deps e schema
npm run context:purge     # Limpa e arquiva o log vivo
```

### Opção B: Via Make (Recomendado para CI/CD e Unix)
```bash
make validate
make sync
make purge
make all       # Executa o pipeline completo: Valida -> Sync -> Purge
```

### Opção C: Via Bash (Resiliência Universal)
```bash
./run_context.sh validate
./run_context.sh all
```

---

## 🗃️ 3. Recuperação de Contexto (Archive)

Se precisar restaurar um Journal ou PRD antigo que foi arquivado:
1. Vá até `.context/maintenance/_archive_context/`.
2. Localize o arquivo pelo timestamp `YYYYMMDD_HHMMSS`.
3. Copie o conteúdo necessário de volta para a raiz da camada correspondente (`maintenance/` ou `brain/`).

---

## 🚨 4. Troubleshooting
- **Erro de Encoding (Windows):** Todos os scripts são forçados para UTF-8. Se vir caracteres estranhos, verifique se o seu terminal suporta Unicode.
- **Python não encontrado:** No Windows, o script tenta `python3` e faz fallback para `python`. Se falhar, certifique-se que o executável está no seu PATH.

> *Lembrete: Sem automação, a documentação morre. Use as ferramentas a cada nova funcionalidade iniciada no ROADMAP.md.*

````
CHUNK_END id=a5c71962029a_c001
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=27 bytes=1336 mtime=2026-04-11T02:26:43.636538+00:00 sha1=adb37745498ccfa61a2b793c10240a2b20d3d716
CHUNK_START id=54a6a553d34b_c001 start_line=1 end_line=27
```markdown
---
Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-10 23:27
Status: Ativo
---

# 🧬 rx-anatomy.md (Raio-X de Anatomia)
> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Arquivos de decisão e regras
│   ├── maintenance/        # Logs, db schema e inventários
│   └── monitoring/         # Dashboard de saúde
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.sh          # Orquestrador universal Bash
├── init_ai_project.sh      # Bootstrapper supremo
└── package.json            # Gerenciamento de libs e scripts context:*

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `_archive_context/specs/`
- **Não é fonte da verdade.** O `.context/` permanece como SSOT.

```
CHUNK_END id=54a6a553d34b_c001
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.789386+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=ca8da4f87431_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=ca8da4f87431_c001
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CHUNK_START id=91d5627a725e_c001 start_line=1 end_line=9
```sql
-- Snapshot Real da Tabela de Pedidos
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_session_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending', -- pending, succeeded, failed
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

````
CHUNK_END id=aa78525fb574_c012
CHUNK_START id=aa78525fb574_c013 start_line=3601 end_line=3900
````markdown

```
CHUNK_END id=91d5627a725e_c001
FILE_END id=file_91d5627a725e

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1624 mtime=2026-04-10T23:50:11.304033+00:00 sha1=92934bdfcac044ab34842a1b0131524ead5e2e5b
CHUNK_START id=068a21d64bec_c001 start_line=1 end_line=38
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

| Métrica | Valor Atual| Limite / Heurística | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Pilar de Manutenção** | | | | |
| JOURNAL.md (linhas) | 412 | 600 | Manutenção | ✅ OK |
| JOURNAL.md (tamanho) | ~12k char | 50k char | Manutenção | ✅ OK |
| **Pilar Cognitivo** | | | | |
| Role Ativa | @frontend-specialist | N/A | Cognitivo | ⚠️ Em Task |
| PRD Ativo | #14 - Auth Flows | 1 por vez | Cognitivo | ✅ OK |
| **Pilar de Consistência** | | | | |
| Schema vs PRD Sync | 0 divergências | 0 | DB-First | ✅ OK |
| Último Sincronismo | 2h atrás | < 24h | Governança | ✅ OK |
| **Pilar de Sessão** | | | | |
| Turns de Sessão | 8 trocas | 20 trocas | Sessão | ✅ OK |
| Token Window Est. | ~78k | 128k | Sessão | ⚠️ 80% |

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até que a migration seja documentada.
- **Se Turns > 18:** Propor Snapshot ou Reset de Sessão antes de iniciar próxima tarefa grande.

---

## 📅 Histórico de Saúde (Log de Purges)
| Data | Ação | Agente | Resultado |
| :--- | :--- | :--- | :--- |
| 2026-04-10 | Purge Completo | @context-keeper | Journal resetado para seed de 30 linhas. |

```
CHUNK_END id=068a21d64bec_c001
FILE_END id=file_068a21d64bec

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=26 bytes=693 mtime=2026-04-11T00:55:20.246274+00:00 sha1=163dd12b4c98d348f80986ea59afcb4604dc9e0e
CHUNK_START id=e477c4c5a96c_c001 start_line=1 end_line=26
```yaml
name: Context Health Check

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  validate-context:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run Context Validation
        # No GitHub Actions (Linux), usamos python3
        run: python3 .context/_scripts/validate_context.py

      - name: Check Journal Limits
        run: python3 .context/_scripts/validate_context.py | grep -q "SUCCESS" || (echo "❌ Contexto quebrado ou Journal excedido!" && exit 1)

```
CHUNK_END id=e477c4c5a96c_c001
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CHUNK_START id=3adfd36c1559_c001 start_line=1 end_line=9
```bash
echo "husky - DEPRECATED

Please remove the following two lines from $0:


````
CHUNK_END id=aa78525fb574_c005
CHUNK_START id=aa78525fb574_c006 start_line=1501 end_line=1800
````markdown
#!/usr/bin/env sh
. \"\$(dirname -- \"\$0\")/_/husky.sh\"

They WILL FAIL in v10.0.0
"
```
CHUNK_END id=3adfd36c1559_c001
FILE_END id=file_3adfd36c1559

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=68 bytes=2890 mtime=2026-04-11T02:30:31.368152+00:00 sha1=ea66d1b4ed6f174f17b752f28ac358093fb784d2
CHUNK_START id=8ec9a00bfd09_c001 start_line=1 end_line=68
````markdown
# 🛸 Antigravity Kit v2.2 Premium+
> **O ecossistema definitivo para engenharia AI-Ready: Governança Macro + Execução Atômica.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação (GitHub Copilot, Cursor, Antigravity). Ele unifica o **Antigravity Kit** (Governança Macro) com o **TLC Spec-Driven** (Execução Atômica), garantindo que o Propósito (PRD) se transforme em Ação (Código) com precisão cirúrgica.

---

## 🧠 A Filosofia: "Se não está no Contexto, não existe."

Neste framework, a pasta `.context/` é a **Single Source of Truth (SSOT)**. A pasta `.specs/` é o seu **Workshop Efêmero**. O código é apenas o reflexo físico da inteligência documentada.

## 🚀 Instalação Ultra-Rapida (One-Click Setup)

Se voce quer inicializar este framework em um novo projeto do zero, basta rodar o nosso bootstrapper supremo:

```bash
# 1. Torne o script executavel
chmod +x init_ai_project.sh

# 2. Execute
./init_ai_project.sh
```

O script ira criar automaticamente toda a estrutura de camadas, os workshops de execução, os motores de manutenção v2.2+, e configurar a blindagem Husky.

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. PRD v2.0, Rules, Registry e a Ponte de Integração TLC.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação

| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Verifica a integridade dos arquivos e a estrutura do workshop. |
| `npm run context:sync`     | Sincroniza `TECHNICAL_REQUIREMENTS.md` com dependências e DB. |
| `npm run context:cleanup`  | Gerencia a efemeridade do `.specs/` (Arquiva specs obsoletas). |
| `npm run context:all`      | Pipeline completo de saúde e manutenção. |

---

## 🤝 Protocolo de Ativação Híbrida

Para iniciar uma tarefa com poder total, use o prompt mestre:
> *"Inicie a fase de SPECIFY para o PRD #[ID] usando o modo Híbrido TLC."*

Isso ativará a role `@spec-driver` e iniciará o ciclo atômico no `.specs/` alinhado à governança do `.context/`.

---

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*

````
CHUNK_END id=8ec9a00bfd09_c001
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=114 bytes=4693 mtime=2026-04-11T01:41:16.589576+00:00 sha1=69a61b75c7697979c8e4ab560e0325f71bd7151d
CHUNK_START id=4efb6293109d_c001 start_line=1 end_line=114
````markdown
---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria viva, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.sh`, `Makefile` | Validacao, purge, sync e orquestracao. |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `tests/test_context.py` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija antes de forcar.

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rapidos (Cheat Sheet)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Sincronizar deps e schema com TECH_REQUIREMENTS.md
npm run context:sync

# Arquivar 70% do journal (mantem 30% como semente)
npm run context:purge

# Pipeline completo (validate -> sync -> purge)
npm run context:all

# Rodar testes do framework manualmente (Universal Python)
npm run context:test
```
> 💡 *Fallbacks:* `make all` ou `bash run_context.sh all`

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se `validate_context.py` ou `test_context.py` falharem.
- **CI/CD:** O GitHub Actions roda o pipeline em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Clone
- [ ] `.context/` existe com estrutura de camadas ok.
- [ ] `brain/RULES.md` e `brain/MASTER_FLOW.md` alinhados a stack.
- [ ] `brain/AGENT_REGISTRY.md` possui roles registradas.
- [ ] `npm run context:all` executa sem erros.

### 🚀 Inicio de Feature / PRD
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR

````
CHUNK_END id=aa78525fb574_c013
CHUNK_START id=aa78525fb574_c014 start_line=3901 end_line=4200
````markdown
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---

> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.

````
CHUNK_END id=4efb6293109d_c001
FILE_END id=file_4efb6293109d

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=5 bytes=138 mtime=2026-04-11T02:58:40.247024+00:00 sha1=19d69e551321040a8c49f683ffcfae2bfbaed5cb
CHUNK_START id=f6f7100f063b_c001 start_line=1 end_line=5
```markdown
# 🛸 Antigravity Kit Versioning
v2.2.1-premium
Dash: [Antigravity Kit v2.2.1-premium]
Audit Status: ✅ PASSED
Release Date: 2026-04-10

```
CHUNK_END id=f6f7100f063b_c001
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CHUNK_START id=1f98938d3cd9_c001 start_line=1 end_line=140
````markdown
### 🔍 Por que um único arquivo não basta?
A IA não lê apenas um arquivo para definir comportamento. Ela avalia:
- 📁 Estrutura de pastas (`brain/`, `maintenance/`, `monitoring/`, `.specs/`)
- 🤖 `AGENT_REGISTRY.md` (ainda carregará 7 roles se existir)
- 🐍 Scripts Python e hooks do Husky (continuam ativos)
- 📜 Regras de carregamento (`Checklist de Carga` ainda exige camadas)
- 🧠 Memória de sessão (a IA tentará carregar tudo o que encontrar)

Se você só trocar o `RULES.md`, a IA ficará em **estado híbrido confuso**: regras dizem "modo leve", mas a estrutura exige validações pesadas, registry complexo e scripts de automação. Isso gera `token bloat`, alucinação e falhas de contexto gate.

---
### 🛠️ 3 Caminhos Técnicos Viáveis

| Abordagem | Como funciona | Prós | Contras |
|-----------|--------------|------|---------|
| `MODE.md` (Flag) | Arquivo simples: `MODE: LIGHT`. A IA lê primeiro e ajusta comportamento. | Zero destruição, reversível, explícito. | Exige atualização no `RULES_LIGHT.md` para ler a flag. |
| `init_ai_project_light.sh` | Bootstrap que cria estrutura mínima do zero (sem camadas, sem scripts, sem Husky). | Limpo, seguro, ideal para novos MVPs. | Não converte projetos robustos existentes. |
| `downgrade_to_light.sh` | Remove camadas, desativa Husky, arquiva scripts, substitui `RULES.md`. | Converte projeto existente sem perder histórico. | Irreversível sem backup manual. |

---
### ✅ Recomendação: `MODE.md` + `init_ai_project_light.sh`
É a combinação mais segura. Você mantém o robusto como padrão, mas pode ativar o modo leve em qualquer repositório novo ou existente com **um arquivo de flag** ou **um comando de init**.

---
### 📄 1. `MODE.md` (A Chave de Conversão)
Coloque na raiz de `.context/`. A IA **DEVE** ler este arquivo antes de qualquer checklist.

```markdown
---
Criado em: YYYY-MM-DD HH:MM
Última Atualização: YYYY-MM-DD HH:MM
Status: Ativo
---

# 🪶 MODE.md
> Define o perfil operacional do framework. A IA ajusta carregamento, roles e automação conforme este valor.

**MODE:** LIGHT  
**Reason:** MVP < 2 semanas | Time 1-2 devs | Velocidade > Governança  

💡 *Insight IA: Se MODE = LIGHT, ignore camadas, scripts, registry multi-agent e .specs/. Carregue apenas: RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql. Use @fullstack-generalist por padrão.*
```

---
### 📜 2. Patch Obrigatório no `RULES_LIGHT.md`
Adicione este bloco no **topo** do arquivo, antes de qualquer regra:

```markdown
📜 RULES_LIGHT.md — Modo Minimalista (MVP/POC)
Projeto: [NOME DO PROJETO] | Arquitetura: Single-Agent + Database-First
> 🪶 **MODO ATIVO:** Leia `MODE.md`. Se `MODE: LIGHT`, siga estritamente este protocolo enxuto. Ignore `.specs/`, scripts Python, Husky e `AGENT_REGISTRY.md`.

🛡️ Checklist de Carga (Light)
1. [ ] RULES_LIGHT.md (este arquivo)
2. [ ] PRD.md ativo
3. [ ] schema.sql atualizado
4. [ ] JOURNAL.md < 300 linhas
⚠️ Se faltar 1 item → pare e solicite correção.

🔄 Comportamento do Agente (Light)
- Role padrão: `@fullstack-generalist` (única ativa)
- Sem handoff obrigatório. Registre decisões críticas direto no JOURNAL.md
- Database-First mantido. Nunca assuma schema.
- Sem automação. Validação manual: `grep -q "schema.sql" PRD.md && echo "✅ OK"`
- Fim de sessão: `"Contexto atualizado? [S/N]"`
```

---
### 🐚 3. `init_ai_project_light.sh` (Bootstrap Seguro)

````
CHUNK_END id=aa78525fb574_c006
CHUNK_START id=aa78525fb574_c007 start_line=1801 end_line=2100
````markdown
Cria uma estrutura flat, sem camadas, sem scripts, sem Husky. Ideal para `git init` de MVPs.

```bash
#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
NC='\033[0m'

[ -d ".context" ] && { echo "❌ .context/ já existe. Abortando."; exit 1; }

echo -e "\n${GREEN}🪶 Inicializando Modo LIGHT...${NC}"
mkdir -p .context

NOW=$(date +%Y-%m-%d\ %H:%M)

# MODE Flag
cat > .context/MODE.md << EOF
---
Criado em: $NOW
Status: Ativo
---
MODE: LIGHT
Reason: MVP rápido | Velocidade > Governança
💡 IA: Ignore camadas, scripts, registry e .specs/. Use apenas RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql.
EOF

# RULES_LIGHT (minimalista)
cat > .context/RULES_LIGHT.md << 'EOF'
📜 RULES_LIGHT.md — Modo Minimalista
> 🪶 MODE: LIGHT ativo. Role única: @fullstack-generalist. Sem scripts, sem Husky, sem handoff complexo.
🛡️ Carga: [ ] RULES_LIGHT.md [ ] PRD.md [ ] schema.sql [ ] JOURNAL.md <300lin
🗄️ DB-First: Valide schema antes de UI. Se faltar campo → pare e avise.
🔄 Fim de sessão: Pergunte "Atualizo contexto?" e registre no JOURNAL.md apenas mudanças de lógica/bug.
⚠️ Sem automação. Sem registry. Sem .specs/. Mantenha enxuto.
EOF

# Arquivos base
for f in PRD.md JOURNAL.md schema.sql; do
  cat > ".context/$f" << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📄 $f
EOF
done

echo -e "${GREEN}✅ Modo LIGHT pronto. Estrutura plana, sem overhead.${NC}"
echo "📖 Próximo: Preencha PRD.md e comece. A IA usará @fullstack por padrão."
```

---
### 🧠 Como a IA Interpreta Isso na Prática
1. **Início de sessão:** A IA lê `MODE.md` primeiro.
2. **Se `MODE: LIGHT`:** 
   - Ignora `brain/`, `maintenance/`, `monitoring/`, `_scripts/`, `.specs/`
   - Carrega apenas os 4 arquivos essenciais
   - Ativa `@fullstack-generalist` implicitamente
   - Desativa validações Python/Husky automaticamente
   - Usa heurística simplificada de tokens (limite ~20k chars)
3. **Se quiser voltar ao robusto:** Troque `MODE: ROBUST` e rode `npm run context:all` para restaurar camadas/scripts.

---
### 🚀 Próximo Passo
Quer que eu:
1. **Gere o `downgrade_to_light.sh`** para converter um projeto robusto existente sem perder histórico?
2. **Ajuste o `init_ai_project.sh` principal** para incluir uma flag `--light` que alterna entre os dois modos automaticamente?
3. **Entregue o `RULES_LIGHT.md` completo** (versão pronta para copiar/colar, com todos os protocolos simplificados)?

Escolha o fechamento. O framework agora tem conversão explícita, segura e reversível. 🏁
````
CHUNK_END id=1f98938d3cd9_c001
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=380 bytes=15779 mtime=2026-04-11T02:42:28.056925+00:00 sha1=2dba92559cf404d5e91df067a8fd72b6a965ec8c
CHUNK_START id=c3916196f58f_c001 start_line=1 end_line=300
```python
#!/usr/bin/env python3
"""captura_projeto.py - Gera bundle markdown AI-first do repositorio. TEMPLATE UNIVERSAL."""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path

# 🛠️ CUSTOMIZE AQUI: Padrões universais + adicione os específicos do seu projeto
PASTAS_IGNORAR = {
    ".git", "node_modules", "dist", "build", "out", "target", "bin", "obj",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache",
    ".next", ".nuxt", ".vercel", ".netlify", ".vite", ".cache",
    ".vscode", ".idea", ".cursor", "coverage", ".pytest_cache",
    "captura_projeto", # 📝 Ignorar a própria pasta do utilitário
}

PASTAS_CORE = {
    # 📝 Defina as pastas ARQUITETURALMENTE essenciais para a IA entender seu projeto
    # Ex: {"src", "lib", "api", "supabase", ".context", ".specs"}
    "src", "lib", "api", ".context", ".specs"
}

# 🛠️ CUSTOMIZE AQUI: Regras de classificação semântica (fallback seguro)
DOMAIN_RULES = {
    r"/api/|/routes/|/handlers/|/controllers/": "api",
    r"/components/|/ui/|/views/|/pages/|/screens/": "ui",
    r"/lib/|/utils/|/helpers/|/core/|/shared/": "lib",
    r"/db/|/migrations/|/models/|/schema/|/supabase/|/prisma/": "db",
    r"/tests/|/spec/|/__tests__/|\.test\.|\.spec\.": "tests",
    r"/config/|/settings/|/env/": "config",
    r"\.md$|\.rst$|\.txt$": "docs",
    r"\.(json|toml|yaml|yml|ini)$": "config",
}

EXTENSOES_PERMITIDAS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".html", ".css", ".json", ".md",
    ".yaml", ".yml", ".toml", ".sh", ".sql", ".graphql", ".vue", ".svelte",
    ".rs", ".go", ".java", ".c", ".h", ".hpp", ".cpp", ".ini",
}

LINGUAGENS = {
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".py": "python", ".html": "html", ".css": "css", ".json": "json", ".md": "markdown",
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".sh": "bash", ".sql": "sql",
    ".graphql": "graphql", ".vue": "html", ".svelte": "html", ".rs": "rust",
    ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".hpp": "cpp", ".cpp": "cpp", ".ini": "ini",
}

ARQUIVOS_SENSIVEIS_GLOBS = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx",
    "credentials*.json", "id_rsa*", "secrets.*", "*.cert",
    # 📝 Adicione padrões sensíveis do SEU projeto aqui
}

SECRET_PATTERNS = (
    re.compile(r'(["\']?)(\w*(?:API_KEY|SECRET|TOKEN|PASSWORD|AUTH_KEY|PRIVATE_KEY|ACCESS_KEY|DB_PASS|CONNECTION_STRING)\w*)\1\s*[:=]\s*["\']?(\S+)["\']?', re.IGNORECASE),
    re.compile(r'(BEGIN\s+(RSA|EC|DSA|OPENSSH|PGP)\s+PRIVATE\s+KEY)', re.IGNORECASE),
)

DEFAULT_OUTPUT = "contexto.md"
logging.basicConfig(level=logging.WARNING, format="⚠️ %(message)s")

@dataclass(frozen=True)
class BundleConfig:
    diretorio: Path
    output: str = DEFAULT_OUTPUT
    only_core: bool = False
    exclude_core: bool = False
    profile: str = "ai-default"
    toc_only: bool = False
    max_lines_per_file: int = 300
    emit_symbol_index: bool = False
    emit_import_map: bool = False
    mask_secrets: bool = False

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_line: int
    end_line: int
    content: str

@dataclass(frozen=True)
class FileRecord:
    file_id: str
    relative_path: str
    domain: str
    language: str
    line_count: int
    byte_count: int
    mtime_utc: str
    sha1: str
    symbols: tuple[str, ...]
    imports: tuple[str, ...]
    chunks: tuple[Chunk, ...]

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXTENSOES_PERMITIDAS:
        return True
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        return False
    return mime.startswith("text/") or mime in {"application/json", "application/xml", "application/javascript"}

````
CHUNK_END id=aa78525fb574_c014
CHUNK_START id=aa78525fb574_c015 start_line=4201 end_line=4500
````markdown

def is_sensitive_file(path: Path) -> bool:
    return any(fnmatch(path.name.lower(), pat.lower()) for pat in ARQUIVOS_SENSIVEIS_GLOBS)

def classify_domain(relative_path: str) -> str:
    p = relative_path.lower()
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, p):
            return domain
    return "source"

def should_include_profile(record_domain: str, config: BundleConfig) -> bool:
    if config.profile == "ai-compact":
        return record_domain not in {"tests", "docs"}
    return True

def mask_sensitive(content: str, enabled: bool) -> str:
    if not enabled:
        return content
    out = content
    for pattern in SECRET_PATTERNS:
        out = pattern.sub(r"\1***", out)
    return out

def extract_symbols(content: str, suffix: str) -> tuple[str, ...]:
    symbols: list[str] = []
    if suffix == ".py":
        symbols.extend(re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content, re.MULTILINE))
        symbols.extend(re.findall(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        symbols.extend(re.findall(r"(?:export\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content))
        symbols.extend(re.findall(r"(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\s*", content))
        symbols.extend(re.findall(r"export\s+const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", content))
    seen, seen_set = [], set()
    for s in symbols:
        if s not in seen_set:
            seen.append(s)
            seen_set.add(s)
    return tuple(seen[:80])

def extract_imports(content: str, suffix: str) -> tuple[str, ...]:
    imports: list[str] = []
    if suffix == ".py":
        imports.extend(re.findall(r"^import\s+([^\n]+)", content, re.MULTILINE))
        imports.extend(re.findall(r"^from\s+([^\s]+)\s+import\s+([^\n]+)", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        imports.extend(re.findall(r"^import\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]", content, re.MULTILINE))
        imports.extend(re.findall(r"require\(['\"]([^'\"]+)['\"]\)", content))
    normalized, seen_set = [], set()
    for item in imports:
        val = f"from {item[0]} import {item[1]}" if isinstance(item, tuple) else item
        if val not in seen_set:
            normalized.append(val)
            seen_set.add(val)
    return tuple(normalized[:120])

def chunk_content(content: str, file_id: str, max_lines: int) -> tuple[Chunk, ...]:
    lines = content.splitlines()
    if not lines:
        return (Chunk(f"{file_id}_c001", 1, 1, ""),)
    if max_lines <= 0 or len(lines) <= max_lines:
        return (Chunk(f"{file_id}_c001", 1, len(lines), content),)
    chunks = []
    idx = 1
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        part = "\n".join(lines[start:end])
        if end < len(lines) or content.endswith("\n"):
            part += "\n"
        chunks.append(Chunk(f"{file_id}_c{idx:03d}", start + 1, end, part))
        idx += 1
    return tuple(chunks)

def make_file_id(relative_path: str) -> str:
    return hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:12]

def collect_files(config: BundleConfig) -> tuple[FileRecord, ...]:
    records: list[FileRecord] = []
    root = config.diretorio.resolve()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        is_root = (current == root)

        if config.only_core:
            dirnames[:] = sorted(d for d in dirnames if (d in PASTAS_CORE or not is_root) and d not in PASTAS_IGNORAR)
        elif config.exclude_core:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_CORE and d not in PASTAS_IGNORAR)
        else:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_IGNORAR)

        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root)
            rel_path = rel.as_posix()
            top = rel.parts[0] if rel.parts else ""

            if config.only_core and is_root and top not in PASTAS_CORE:
                continue
            if config.exclude_core and is_root and top in PASTAS_CORE:
                continue
            if is_sensitive_file(path):
                continue
            if not is_text_file(path):
                continue

            try:
                raw_content = path.read_text(encoding="utf-8")

````
CHUNK_END id=aa78525fb574_c007
CHUNK_START id=aa78525fb574_c008 start_line=2101 end_line=2400
````markdown
            except UnicodeDecodeError:
                try:
                    raw_content = path.read_text(encoding="latin-1")
                except OSError as e:
                    logging.warning("Pulando %s: %s", rel_path, e)
                    continue
            except OSError as e:
                logging.warning("Pulando %s: %s", rel_path, e)
                continue

            domain = classify_domain(rel_path)
            if not should_include_profile(domain, config):
                continue

            raw_sha1 = hashlib.sha1(raw_content.encode("utf-8", errors="ignore")).hexdigest()
            content = mask_sensitive(raw_content, config.mask_secrets)
            file_id = make_file_id(rel_path)
            stat = path.stat()
            suffix = path.suffix.lower()

            symbols = extract_symbols(content, suffix) if config.emit_symbol_index else ()
            imports = extract_imports(content, suffix) if config.emit_import_map else ()
            chunks = chunk_content(content, file_id, config.max_lines_per_file)

            records.append(FileRecord(
                file_id=file_id, relative_path=rel_path, domain=domain,
                language=LINGUAGENS.get(suffix, suffix[1:] if suffix else "text"),
                line_count=len(content.splitlines()),
                byte_count=len(content.encode("utf-8", errors="ignore")),
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                sha1=raw_sha1, symbols=symbols, imports=imports, chunks=chunks
            ))

    records.sort(key=lambda r: r.relative_path)
    return tuple(records)

def mode_name(config: BundleConfig) -> str:
    if config.only_core: return "only-core"
    if config.exclude_core: return "exclude-core"
    return "full"

def render_frontmatter(config: BundleConfig, records: tuple[FileRecord, ...]) -> str:
    total_bytes = sum(r.byte_count for r in records)
    lines = [
        "---", "schema_version: 1",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"root: {config.diretorio.resolve().name}",
        f"mode: {mode_name(config)}", f"profile: {config.profile}",
        f"file_count: {len(records)}", f"byte_count: {total_bytes}",
        "ignored_dirs:"
    ]
    lines.extend(f"  - {d}" for d in sorted(PASTAS_IGNORAR))
    lines.append("sensitive_rules:")
    lines.extend(f"  - {r}" for r in sorted(ARQUIVOS_SENSIVEIS_GLOBS))
    lines.append("---")
    return "\n".join(lines)

def render_index_by_domain(records: tuple[FileRecord, ...]) -> str:
    grouped: dict[str, list[FileRecord]] = {}
    for r in records:
        grouped.setdefault(r.domain, []).append(r)
    lines = ["## INDEX_BY_DOMAIN"]
    for domain in sorted(grouped):
        lines.append(f"- `{domain}`:")
        lines.extend(f"  - `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in grouped[domain])
    return "\n".join(lines)

def render_index_by_path(records: tuple[FileRecord, ...]) -> str:
    lines = ["## INDEX_BY_PATH"]
    lines.extend(f"- `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in records)
    return "\n".join(lines)

def render_symbols(records: tuple[FileRecord, ...]) -> str:
    lines = ["## SYMBOL_INDEX"]
    for r in records:
        if not r.symbols: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{s}`" for s in r.symbols)
    return "\n".join(lines)


```
CHUNK_END id=c3916196f58f_c001
CHUNK_START id=c3916196f58f_c002 start_line=301 end_line=380
````python
def render_imports(records: tuple[FileRecord, ...]) -> str:
    lines = ["## IMPORT_MAP_MIN"]
    for r in records:
        if not r.imports: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{i}`" for i in r.imports)
    return "\n".join(lines)

def pick_fence(content: str) -> str:
    return "````" if "```" in content else "```"

def render_file_record(record: FileRecord, toc_only: bool) -> str:
    lines = [
        "---", f'<a id="file_{record.file_id}"></a>',
        f"FILE_START id=file_{record.file_id} path={record.relative_path} "
        f"domain={record.domain} lang={record.language} lines={record.line_count} "
        f"bytes={record.byte_count} mtime={record.mtime_utc} sha1={record.sha1}"
    ]
    if toc_only:
        lines.append("CONTENT_OMITTED toc_only=true")
    else:
        for chunk in record.chunks:
            lines.append(f"CHUNK_START id={chunk.chunk_id} start_line={chunk.start_line} end_line={chunk.end_line}")
            fence = pick_fence(chunk.content)
            lines.extend([f"{fence}{record.language}", chunk.content, fence, f"CHUNK_END id={chunk.chunk_id}"])
    lines.append(f"FILE_END id=file_{record.file_id}")
    return "\n".join(lines)

def generate_context_markdown(config: BundleConfig) -> str:
    if config.only_core and config.exclude_core:
        raise ValueError("only_core e exclude_core nao podem ser usados juntos")
    
    records = collect_files(config)
    blocks = ["# Project Context Bundle", "", render_frontmatter(config, records), "",
              render_index_by_domain(records), "", render_index_by_path(records)]
    if config.emit_symbol_index:
        blocks.extend(["", render_symbols(records)])
    if config.emit_import_map:
        blocks.extend(["", render_imports(records)])
    for r in records:
        blocks.extend(["", render_file_record(r, toc_only=config.toc_only)])
    return "\n".join(blocks) + "\n"

def write_output(config: BundleConfig) -> Path:
    output_path = config.diretorio / config.output
    content = generate_context_markdown(config)
    output_path.write_text(content, encoding="utf-8")
    return output_path

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="captura_projeto.py - Consolida repositorio em markdown AI-first")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretorio raiz")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Arquivo de saida")
    core = parser.add_mutually_exclusive_group()
    core.add_argument("--only-core", action="store_true", help="Inclui apenas escopo core")
    core.add_argument("--exclude-core", action="store_true", help="Exclui escopo core")
    parser.add_argument("--profile", choices=["ai-default", "ai-compact", "ai-forensics"], default="ai-default")
    parser.add_argument("--toc-only", action="store_true", help="Apenas indices e envelopes")
    parser.add_argument("--max-lines-per-file", type=int, default=300, help="Limite de linhas por chunk (0=ilimitado)")
    parser.add_argument("--emit-symbol-index", action="store_true", help="Adiciona SYMBOL_INDEX")
    parser.add_argument("--emit-import-map", action="store_true", help="Adiciona IMPORT_MAP_MIN")
    parser.add_argument("--mask-secrets", action="store_true", help="Ofusca segredos no conteudo")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = BundleConfig(
        diretorio=Path(args.diretorio), output=args.output,
        only_core=args.only_core, exclude_core=args.exclude_core,
        profile=args.profile, toc_only=args.toc_only,
        max_lines_per_file=args.max_lines_per_file,
        emit_symbol_index=args.emit_symbol_index,
        emit_import_map=args.emit_import_map, mask_secrets=args.mask_secrets
    )
    out = write_output(config)
    print(f"\n[OK] Gerado: {out}")
    print(f"   Mode: {mode_name(config)} | Profile: {config.profile}")

if __name__ == "__main__":
    main()
````
CHUNK_END id=c3916196f58f_c002
FILE_END id=file_c3916196f58f

---
<a id="file_aa78525fb574"></a>
FILE_START id=file_aa78525fb574 path=contexto.md domain=docs lang=markdown lines=5653 bytes=229583 mtime=2026-04-11T02:42:57.123821+00:00 sha1=d081e8656c9a28265430560e843d258eba7ad4f1
CHUNK_START id=aa78525fb574_c001 start_line=1 end_line=300
````markdown
# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-11T02:42:57.119117+00:00
root: template_inicío_de_projeto
mode: full
profile: ai-default
file_count: 34
byte_count: 208117
ignored_dirs:
  - .cache
  - .cursor

````
CHUNK_END id=aa78525fb574_c015
CHUNK_START id=aa78525fb574_c016 start_line=4501 end_line=4800
````markdown
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
- `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
- `contexto.md` -> [file_aa78525fb574](#file_aa78525fb574)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package-lock.json` -> [file_fa288d1472d2](#file_fa288d1472d2)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
- `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
- `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

## SYMBOL_INDEX
- `.context/_scripts/cleanup_specs.py`:

````
CHUNK_END id=aa78525fb574_c008
CHUNK_START id=aa78525fb574_c009 start_line=2401 end_line=2700
````markdown
  - `get_specs`
  - `archive_spec`
  - `cleanup`
- `.context/_scripts/purge_journal.py`:
  - `parse_entries`
  - `purge_journal`
- `.context/_scripts/sync_project.py`:
  - `get_package_deps`
  - `get_schema_tables`
  - `sync_requirements`
- `.context/_scripts/validate_context.py`:
  - `check_files`
  - `check_journal_lines`
  - `estimate_tokens`
  - `check_registry_structure`
  - `check_specs_structure`
  - `validate`
- `captura_projeto.py`:
  - `is_text_file`
  - `is_sensitive_file`
  - `classify_domain`
  - `should_include_profile`
  - `mask_sensitive`
  - `extract_symbols`
  - `extract_imports`
  - `chunk_content`
  - `make_file_id`
  - `collect_files`
  - `mode_name`
  - `render_frontmatter`
  - `render_index_by_domain`
  - `render_index_by_path`
  - `render_symbols`
  - `render_imports`
  - `pick_fence`
  - `render_file_record`
  - `generate_context_markdown`
  - `write_output`
  - `parse_args`
  - `main`
  - `BundleConfig`
  - `Chunk`
  - `FileRecord`
- `tests/test_context.py`:
  - `TestContextGovernance`

## IMPORT_MAP_MIN
- `.context/_scripts/cleanup_specs.py`:
  - `os`
  - `shutil`
  - `time`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/purge_journal.py`:
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/sync_project.py`:
  - `json`
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/validate_context.py`:
  - `os`
  - `sys`
  - `from pathlib import Path`
- `captura_projeto.py`:
  - `argparse`
  - `hashlib`
  - `logging`
  - `mimetypes`
  - `os`
  - `re`
  - `from __future__ import annotations`
  - `from dataclasses import dataclass`
  - `from datetime import datetime, timezone`
  - `from fnmatch import fnmatch`
  - `from pathlib import Path`
- `tests/test_context.py`:
  - `unittest`
  - `os`
  - `shutil`
  - `tempfile`
  - `subprocess`
  - `sys`
  - `from pathlib import Path`

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CHUNK_START id=82cd6bde54ff_c001 start_line=1 end_line=71
```python
#!/usr/bin/env python3
"""
🧹 cleanup_specs.py
Gerencia a efemeridade da bancada de trabalho (.specs/).
Aplica a regra de 48h de inatividade e limite de 3 specs ativas simultâneas.
Arquiva specs excedentes ou obsoletas em _archive_context/specs/.
"""
import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# Caminhos base
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "specs"

# Configurações
MAX_INACTIVITY_SECONDS = 48 * 3600  # 48 horas
MAX_ACTIVE_SPECS = 3

def get_specs():
    if not SPECS_DIR.exists():
        return []
    return [d for d in SPECS_DIR.iterdir() if d.is_dir()]

def archive_spec(spec_path):
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{spec_path.name}_{timestamp}"
    dest_path = ARCHIVE_DIR / archive_name
    
    print(f"[INFO] Arquivando spec: {spec_path.name} -> {archive_name}")
    shutil.move(str(spec_path), str(dest_path))

def cleanup():
    specs = get_specs()
    if not specs:
        print("[OK] Nenhuma spec ativa encontrada.")
        return

    now = time.time()
    active_specs = []

    # 1. Limpeza por inatividade (48h)
    for spec in specs:
        last_mod = max(os.path.getmtime(root) for root, _, _ in os.walk(spec))
        if (now - last_mod) > MAX_INACTIVITY_SECONDS:
            print(f"[AUTO] Inatividade detectada (>48h) em: {spec.name}")
            archive_spec(spec)
        else:
            active_specs.append(spec)

    # 2. Limpeza por limite de volume (Max 3)
    # Ordena por data de modificação (mais antiga primeiro)
    active_specs.sort(key=lambda s: max(os.path.getmtime(root) for root, _, _ in os.walk(s)))
    
    while len(active_specs) > MAX_ACTIVE_SPECS:
        oldest = active_specs.pop(0)
        print(f"[AUTO] Limite de volume excedido (Max {MAX_ACTIVE_SPECS}). Removendo spec mais antiga: {oldest.name}")
        archive_spec(oldest)

    print(f"[OK] Manutencao de specs concluida. Specs ativas: {len(active_specs)}/{MAX_ACTIVE_SPECS}")

if __name__ == "__main__":
    try:
        cleanup()
    except Exception as e:
        print(f"[ERROR] Falha na limpeza de specs: {e}")

```
CHUNK_END id=82cd6bde54ff_c001
FILE_END id=file_82cd6bde54ff

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=74 bytes=2507 mtime=2026-04-11T00:15:41.168457+00:00 sha1=772904f793113782bf9cc398ad20f87cefdc018c
CHUNK_START id=024b28a37d29_c001 start_line=1 end_line=74
```python
#!/usr/bin/env python3

````
CHUNK_END id=aa78525fb574_c001
CHUNK_START id=aa78525fb574_c002 start_line=301 end_line=600
````markdown
"""
🗜️ purge_journal.py
Arquiva 70% das entradas mais antigas do JOURNAL.md.

````
CHUNK_END id=aa78525fb574_c016
CHUNK_START id=aa78525fb574_c017 start_line=4801 end_line=5100
````markdown
Mantém 30% mais recentes como semente. Backup automático e escrita atômica.
"""
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
JOURNAL_FILE = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "journals"
KEEP_RATIO = 0.3  # 30% mais recentes

def parse_entries(content):
    # Divide por headers markdown (## 📅, ##, etc.) mantendo o header na entrada
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]

def purge_journal():
    if not JOURNAL_FILE.exists():
        print("[WARN] JOURNAL.md nao encontrado. Nada a fazer.")
        return

    content = JOURNAL_FILE.read_text(encoding="utf-8")
    entries = parse_entries(content)

    if len(entries) <= 1:
        print("[INFO] Poucas entradas para purgar.")
        return

    keep_count = max(1, int(len(entries) * KEEP_RATIO))
    archive_entries = entries[:-keep_count]
    keep_entries = entries[-keep_count:]

    # Garante diretório de arquivo
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Backup com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_file = ARCHIVE_DIR / f"journal_archive_{timestamp}.md"
    archive_content = f"# Arquivo de Journal - {timestamp}\n\n" + "\n\n".join(archive_entries) + "\n"
    archive_file.write_text(archive_content, encoding="utf-8")

    # Nova semente
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    seed = f"""---
Criado em: {now}
Ultima Atualizacao: {now}
Status: Ativo
Nota: Semente pos-purge. {len(archive_entries)} entradas arquivadas em {archive_file.name}.
---

# JOURNAL.md (Memoria Curta)
> Mantido por purge_journal.py. Limite heuristico de caracteres atingido.

""" + "\n\n".join(keep_entries) + "\n"

    # Escrita atomica (previne corrupcao se interrupcao ocorrer)
    temp_file = JOURNAL_FILE.with_suffix(".tmp")
    temp_file.write_text(seed, encoding="utf-8")
    temp_file.replace(JOURNAL_FILE)

    print(f"[OK] Purge concluido.")
    print(f"[OK] Arquivadas: {len(archive_entries)} entradas -> {archive_file.name}")
    print(f"[OK] Mantidas: {len(keep_entries)} entradas mais recentes.")

if __name__ == "__main__":
    try:
        purge_journal()
    except Exception as e:
        print(f"[ERROR] Erro no purge: {e}")

```
CHUNK_END id=024b28a37d29_c001
FILE_END id=file_024b28a37d29

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=94 bytes=3162 mtime=2026-04-11T00:15:52.626055+00:00 sha1=b9acd032350a262fad7d0995116e5686b8fa2191
CHUNK_START id=f122711ba9e1_c001 start_line=1 end_line=94
```python
#!/usr/bin/env python3
"""
🔄 sync_project.py
Sincroniza TECH_REQUIREMENTS.md com package.json e schema.sql.
Usa marcadores <!-- AUTO-SYNC START/END --> para preservar edicoes humanas.
"""
import json
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQ_FILE = CONTEXT_DIR / "maintenance" / "TECHNICAL_REQUIREMENTS.md"
PKG_FILE = CONTEXT_DIR.parent / "package.json"
SCHEMA_FILE = CONTEXT_DIR / "maintenance" / "schema.sql"

AUTO_START = "<!-- AUTO-SYNC START -->"
AUTO_END = "<!-- AUTO-SYNC END -->"

def get_package_deps():
    if not PKG_FILE.exists(): return {"dependencies": {}, "devDependencies": {}}
    try:
        with open(PKG_FILE, 'r', encoding='utf-8') as f:
            pkg = json.load(f)
        return {
            "dependencies": pkg.get("dependencies", {}),
            "devDependencies": pkg.get("devDependencies", {})
        }
    except Exception as e:
        print(f"[WARN] Erro ao ler package.json: {e}")
        return {"dependencies": {}, "devDependencies": {}}

def get_schema_tables():
    if not SCHEMA_FILE.exists(): return []
    content = SCHEMA_FILE.read_text(encoding="utf-8")
    # Regex para extrair nomes de tabelas
    return list(set(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["\']?(\w+)["\']?', content, re.IGNORECASE)))

````
CHUNK_END id=aa78525fb574_c009
CHUNK_START id=aa78525fb574_c010 start_line=2701 end_line=3000
````markdown

def sync_requirements():
    deps = get_package_deps()
    tables = get_schema_tables()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    block = [
        AUTO_START,
        f"*🤖 Atualizado automaticamente em {now}*",
        ""
    ]

    if deps.get("dependencies"):
        block.append("### Dependencias (package.json)")
        for dep, ver in deps["dependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if deps.get("devDependencies"):
        block.append("### DevDependencies")
        for dep, ver in deps["devDependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if tables:
        block.append("### Tabelas no Schema (schema.sql)")
        for t in sorted(tables):
            block.append(f"- `{t}`")
        block.append("")

    block.append(AUTO_END)
    auto_content = "\n".join(block) + "\n"

    if not REQ_FILE.exists():
        REQ_FILE.write_text(f"# TECHNICAL_REQUIREMENTS.md\n\n{auto_content}", encoding="utf-8")
        print("[OK] TECHNICAL_REQUIREMENTS.md criado.")
        return

    content = REQ_FILE.read_text(encoding="utf-8")
    start_idx = content.find(AUTO_START)
    end_idx = content.find(AUTO_END)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + auto_content + content[end_idx + len(AUTO_END):]
    else:
        new_content = content.rstrip() + "\n\n" + auto_content

    REQ_FILE.write_text(new_content, encoding="utf-8")
    print("[OK] TECHNICAL_REQUIREMENTS.md sincronizado.")
    print(f"[OK] {len(deps.get('dependencies', {}))} deps | {len(tables)} tabelas detectadas.")

if __name__ == "__main__":
    try:
        sync_requirements()
    except Exception as e:
        print(f"[ERROR] Erro no sync: {e}")

```
CHUNK_END id=f122711ba9e1_c001
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=106 bytes=3827 mtime=2026-04-11T02:29:28.743870+00:00 sha1=e6e9a29604fb4a340a2335bbca07488c56baff2a
CHUNK_START id=1077e9084ea1_c001 start_line=1 end_line=106
```python
#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade com AGENT_REGISTRY.md.
"""
import os
import sys
from pathlib import Path

# Caminhos relativos a localização deste script (.context/_scripts/)
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

# Mapeamento para estrutura em camadas
REQUIRED_FILES = [
    "brain/RULES.md", 
    "brain/MASTER_FLOW.md", 
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md", 
    "maintenance/JOURNAL.md", 
    "maintenance/schema.sql", 
    "maintenance/TECHNICAL_REQUIREMENTS.md"
]

JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000  # ~100k tokens

def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]

def check_journal_lines():
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists(): return 0, True
    lines = journal.read_text(encoding="utf-8").splitlines()
    return len(lines), len(lines) <= JOURNAL_MAX_LINES

def estimate_tokens():
    total_chars = 0
    for f in REQUIRED_FILES:
        path = CONTEXT_DIR / f
        if path.exists():
            total_chars += len(path.read_text(encoding="utf-8", errors="ignore"))
    return total_chars, total_chars < TOKEN_WARN_THRESHOLD_CHARS

def check_registry_structure():
    registry = CONTEXT_DIR / "brain/AGENT_REGISTRY.md"
    if not registry.exists(): return False, "Arquivo ausente"
    content = registry.read_text(encoding="utf-8")
    if "| Role |" not in content and "| Role" not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"

def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists(): return True, "Workshop inativo (OK)"
    
    features_dir = specs_dir / "features"
    if not features_dir.exists(): return False, "Diretorio features ausente no .specs"
    
    # Verifica se algum STATE.md esta presente em specs ativas
    active_specs = [d for d in features_dir.iterdir() if d.is_dir()]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
            
    return True, f"OK ({len(active_specs)} specs ativas)"

def validate():
    print("--- Iniciando validacao de contexto (v2.2 Premium+) ---")
    issues = []

    missing = check_files()
    if missing: issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else: print("[OK] Todos os arquivos obrigatorios presentes.")

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok: issues.append(f"[WARN] .specs/: {spec_msg}")
    else: print(f"[OK] .specs/: {spec_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok: issues.append(f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}")
    else: print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, token_ok = estimate_tokens()
    est_tokens = total_chars // 4
    if not token_ok:
        issues.append(f"[WARN] Contexto estimado alto: ~{est_tokens}k tokens. Execute purge.")
    else: print(f"[OK] Estimativa de contexto segura: ~{est_tokens}k tokens")

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok: issues.append(f"[WARN] AGENT_REGISTRY.md: {reg_msg}")
    else: print("[OK] AGENT_REGISTRY.md estrutura valida.")

    print("\n--- Relatorio Final ---")
    if not issues:
        print("[SUCCESS] Contexto integro. Pronto para execucao.")
    else:
        for issue in issues: print(issue)
        print("[ALERT] Resolva os alertas antes de gerar codigo.")

if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        sys.exit(1)

```
CHUNK_END id=1077e9084ea1_c001
FILE_END id=file_1077e9084ea1


````
CHUNK_END id=aa78525fb574_c017
CHUNK_START id=aa78525fb574_c018 start_line=5101 end_line=5400
````markdown
---
<a id="file_e7c17acb71ff"></a>

````
CHUNK_END id=aa78525fb574_c002
CHUNK_START id=aa78525fb574_c003 start_line=601 end_line=900
````markdown
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=97 bytes=7180 mtime=2026-04-11T02:28:38.100881+00:00 sha1=3232fd65b8b05382d366aa1a8890e6385eb7f705
CHUNK_START id=e7c17acb71ff_c001 start_line=1 end_line=97
````markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Testes unitários/E2E, edge cases, cobertura, mocks, TDD | `tests/`, `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (apenas leitura para bugs) | `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (critérios de aceite) | "testar", "validar", "cobertura", "mock", "edge case", "TDD", "bug" |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@spec-driver` | Criação e orquestração de specs atômicas | `.specs/` (leitura/gravação temporária) | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (tail 30) | "inicie specify", "crie spec", "modo híbrido" |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |

💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Carregar APENAS: Global + Role-Specific + Task-Ephemeral
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*

````
CHUNK_END id=e7c17acb71ff_c001
FILE_END id=file_e7c17acb71ff

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=86 bytes=4370 mtime=2026-04-11T02:28:25.945198+00:00 sha1=06ce6786a149620314b57f8231142f652d4fc412
CHUNK_START id=d833c436f547_c001 start_line=1 end_line=86
````markdown
---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-04-10 23:28
Status: Ativo
---


````
CHUNK_END id=aa78525fb574_c010
CHUNK_START id=aa78525fb574_c011 start_line=3001 end_line=3300
````markdown
# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura do Diretório `.context/`

```text
.context/
├── 🧠 brain/                       # CAMADA COGNITIVA (The Brain)
│   ├── MASTER_FLOW.md             # Este documento
│   ├── RULES.md                   # Protocolos e "A Lei"
│   ├── AGENT_REGISTRY.md          # DNS de Roles e Permissões
│   ├── PROMPT_LIBRARY.md          # Catálogo de templates de prompts
│   ├── PRD.md                     # Requisito em execução (v2.0 - O Contrato)
│   ├── ROADMAP.md                 # Metas e fases (O Planejamento)
│   └── TLC_INTEGRATION.md         # Ponte entre Governança e Execução
│
├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
│   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Curta)
│   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e versões (Inventário)
│   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
│   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
│   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
│   ├── TESTS.md                   # Ledger de padrões e TDDs
│   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
│   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
│   └── _archive_context/          # Histórico imutável (A Biblioteca)
│
├── monitoring/             # CAMADA DE MONITORAMENTO (The Guardian)
│   └── CONTEXT_HEALTH.md   # Dashboard de saúde técnica e cognitiva
│
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── _scripts/               # CAMADA DE AUTOMACAO (The Motor)
    ├── validate_context.py        # Validador de integridade
    ├── purge_journal.py           # Gerenciador de memória (Purge)
    ├── cleanup_specs.py           # Gerenciador de efemeridade (.specs)
    └── sync_project.py            # Sincronizador de requisitos
```

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e a presença do `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões arquiteturais tomadas durante o TLC **devem** ser migradas para o `JOURNAL.md` antes da limpeza da spec.

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*

````
CHUNK_END id=d833c436f547_c001
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=67 bytes=2446 mtime=2026-04-11T01:31:37.755946+00:00 sha1=b5c06bc8a67d2a788cc8263f03971f379d04e92e
CHUNK_START id=d124f6374cab_c001 start_line=1 end_line=67
```markdown
---
Criado em: 2026-04-10 22:35
Ultima Atualizacao: 2026-04-10 22:35
Status: Ativo (EM EXECUCAO)
PRD_ID: #15
---

# 🎯 PRD: Checkout com Integração Stripe
> Implementar um fluxo de pagamento seguro e resiliente usando Stripe Elements e Webhooks para pedidos digitais.

💡 *Insight Humano: Este PRD é um contrato vivo. Ele guia o roteamento de agentes, define criterios de aceite e serve como referência para o JOURNAL.md.*

---

## 📋 1. Visão Geral
| Campo | Valor |
|-------|-------|
| **Objetivo de Negocio** | Reduzir abandono de carrinho e garantir seguranca no processamento. |
| **Publico-Alvo** | Compradores finais da plataforma. |
| **Escopo** | UI de pagamento, Geracao de Session, Webhooks de confirmacao. |
| **MVP vs Futuro** | MVP: Cartao de Credito. Futuro: Apple Pay/Google Pay. |
| **Dependencias** | Stripe API, Tabela `orders`, Variaveis de ambiente seguras. |

---

## 🎯 2. Critérios de Aceite (Definition of Done)
### Funcionais
- [ ] Usuario finaliza compra com cartao valido.
- [ ] Webhook atualiza `orders.status` para 'succeeded'.
- [ ] Erro de cartao exibe mensagem amigavel (WCAG).
- [ ] Idempotencia garantida via `event.id` do Stripe.

### Não-Funcionais
- [ ] Tempo de resposta API < 500ms.
- [ ] Nenhum segredo (Keys) hardcoded no codigo.
- [ ] Logs estruturados para auditoria.

---

## 🤖 3. Roteamento Multi-Agent
| Etapa | Role Responsável | Entregável | Gatilho de Handoff |
|-------|-----------------|------------|-------------------|
| 1. UI Checkout | `@frontend-specialist` | `StripeForm.tsx` | "UI pronta, aguarda contrato de API" |
| 2. API Stripe | `@backend-engineer` | `/api/checkout` + Webhook | "Rotas operacionais, inicia validacao" |
| 3. Testes E2E | `@qa-validator` | Suite de testes | "Cobertura >90%, edge cases validados" |

---

## 🔒 4. Context Gate (Pré-Execução)
- [ ] `maintenance/schema.sql` contem a tabela `orders`? ✅
- [ ] `maintenance/TECHNICAL_REQUIREMENTS.md` atualizado? ✅
- [ ] `maintenance/JOURNAL.md` < 550 linhas? ✅
- [ ] `brain/AGENT_REGISTRY.md` tem as roles necessarias? ✅

---

## 📊 5. Health Check Integrado
| Metrica | Valor | Status |
|---------|-------|--------|
| **Progresso** | 50% | 🟡 Em andamento |
| **Cobertura de Testes** | 92% (Simulada) | ✅ OK |
| **Divergência Schema** | 0 campos | ✅ OK |

---

## 🔄 6. Ciclo de Vida & Arquivamento
Ao concluir, mover para `_archive_context/prds/` e atualizar `ROADMAP.md`.

```
CHUNK_END id=d124f6374cab_c001
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=154 bytes=6687 mtime=2026-04-11T02:28:52.575335+00:00 sha1=aa3419c1efa08687a7c551dc44f40b504b422353
CHUNK_START id=9fe16e5591f0_c001 start_line=1 end_line=154
````markdown
---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo
---

````
CHUNK_END id=aa78525fb574_c018
CHUNK_START id=aa78525fb574_c019 start_line=5401 end_line=5700
````markdown

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`

````
CHUNK_END id=aa78525fb574_c003
CHUNK_START id=aa78525fb574_c004 start_line=901 end_line=1200
````markdown
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator`
**Gatilho:** Testes, validacao, edge cases, cobertura, mocks  
**Contexto Obrigatorio:** `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (criterios de aceite)
```text
🤖 Ativando @qa-validator | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{arquivo/feature a ser testada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{criar testes, validar edge cases ou aumentar cobertura}}
🚧 Restricoes:
- Seguir framework de testes definido em maintenance/TECHNICAL_REQUIREMENTS.md
- Mockar servicos externos; nao depender de rede real
- Cobrir happy path + 2 edge cases criticos no minimo
- Documentar falhas conhecidas no maintenance/JOURNAL.md se houver
📤 Saida Esperada:
1. Codigo dos testes (unitarios/integracao)
2. Matriz de cenarios cobertos
3. Recomendacoes de refatoracao se aplicavel
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso

````
CHUNK_END id=aa78525fb574_c011
CHUNK_START id=aa78525fb574_c012 start_line=3301 end_line=3600
````markdown
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada
2. spec.md com passos, contratos e critérios de verificação
3. STATE.md: draft → pronto para execução
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*

````
CHUNK_END id=9fe16e5591f0_c001
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.772397+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=c94f001202db_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=c94f001202db_c001
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=116 bytes=6333 mtime=2026-04-11T02:28:07.351671+00:00 sha1=01365a42e1b2cf0a5fb21f635bec7261b184b164
CHUNK_START id=cd6526d17218_c001 start_line=1 end_line=116
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança

**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)

> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas (Cognitiva, Manutenção, Monitoramento e Automação) para garantir escala e foco operacional.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)

Antes de gerar qualquer código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:

1.  **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`.
2.  **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
3.  **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`.

> ⚠️ **Bloqueio de Execução:** Se qualquer um dos itens acima não estiver carregado ou visível, a IA deve parar e solicitar a carga antes de prosseguir.

---

## 🔢 2. Session Budget & Heurísticas de Token

Para evitar alucinações por "Token Bloat" (excesso de memória na janela), adotamos limites práticos:

### 🚩 Gatilhos de Reset/Purge
A IA deve monitorar o estado da sessão e sugerir uma limpeza ou snapshot quando detectar:
- **Volume:** Aprox. **50.000 caracteres** acumulados no buffer de prompt/repost.
- **Duração:** Aprox. **15 a 20 trocas (mensagens)** densas de desenvolvimento.

### 🔄 Ação ao atingir o limite:
A IA deve disparar a seguinte mensagem ao usuário:
> *"🔄 Contexto próximo do limite de foco (~20 trocas). Deseja que eu execute o purge do JOURNAL, arquive o PRD atual ou inicie uma nova sessão limpa com um snapshot de semente?"*

---

## 🧠 1. Protocolo de Manutenção do Contexto
A IA deve agir como o "bibliotecário chefe". A consistência entre Código e Contexto é obrigatória.

### 📖 `maintenance/JOURNAL.md` (O Diário de Bordo)
- **O que logar:** Decisões de arquitetura, resoluções de bugs complexos e mudanças em lógica de negócio.
- **Proibido:** Erros de sintaxe triviais, mudanças de estilo (CSS) ou indentação.
- **O Purge:** Ao atingir o limite heurístico (~50k char), acionar `_scripts/purge_journal.py` para arquivar 70% e gerar semente de contexto.

### ⚙️ `maintenance/TECHNICAL_REQUIREMENTS.md`
- **Atualização Obrigatória:** Mudanças no `package.json`, alteração de Schema ou integração de novas APIs/Serviços.

### 🛠️ `maintenance/rebuild_guide.md` (Manual de Reconstrução)
- **Atualização Obrigatória:** Descoberta de hacks de ambiente local, configurações críticas de CI/CD ou passos manuais de deploy.

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e o `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões tomadas na spec devem ser transferidas para o `JOURNAL.md` no momento do merge.

---

## 🗄️ 2. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.

1.  **Verificação Obrigatória:** Antes de criar UI ou lógica que dependa de dados, o Agente DEVE verificar `maintenance/schema.sql`.
2.  **Aviso de Divergência:** Se a IA identificar que o código exige um campo inexistente no DB, ela deve parar e avisar: 
    *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro a migration antes de prosseguir."*

---

## 🤖 3. Comportamento do Agente (Transparência & Roteamento)

### 📋 3.1 Registro & Ativação
- **DNS de Roles:** `brain/AGENT_REGISTRY.md` é a única fonte oficial de papéis.
- **Identificação:** Toda tarefa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`.
- **Isolamento de Contexto:** Carregar apenas: Global (`brain/` base) + Role-Specific + Task-Ephemeral (`brain/PRD.md` + tail de `maintenance/JOURNAL.md`).

### 🤝 3.2 Handoff & Cruzamento de Domínios
Se uma tarefa exigir 2+ especialidades, o agente atual deve pausar e registrar:
- `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado Tecnico: [Resumo] | Próximo Passo: [Ação]`
O próximo agente inicia com contexto limpo + estado transferido.

### ⚖️ 3.3 Validação Pré-Código (Context Gate)
Antes de gerar código de produção, validar mentalmente ou via script:
- [ ] `brain/PRD.md` ativo e alinhado.
- [ ] `maintenance/schema.sql` contém as estruturas referenciadas.
- [ ] `maintenance/JOURNAL.md` < 550 linhas.
- [ ] Nenhuma variável sensível hardcoded.

---

## 🔢 4. Session Budget & Heurísticas de Token
- **Volume:** Aprox. **50.000 caracteres** ou **15-20 trocas** densas.
- **Alerta:** Ao detectar o limite, propor purge ou reset de sessão imediatamente.

---

## 🔄 5. Gatilhos de Interação (Para o Usuário)
- **"Atualize o contexto":** IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- **"Qual o estado do projeto?":** IA gera relatório baseado no `JOURNAL.md` e `ROADMAP.md`.
- **"Roteie esta tarefa":** IA consulta `AGENT_REGISTRY.md` e inicia o fluxo de ativação/handoff.
- **"Use o prompt padrão":** IA seleciona o template no `brain/PROMPT_LIBRARY.md`, preenche placeholders e solicita confirmação.
- **"Novo PRD":** IA deve usar o template v2.0 (`brain/PRD.md`), preencher metadados, validar Context Gate e registrar no `ROADMAP.md`.
- **"Inicie a fase de SPECIFY para o PRD #[ID]":** A IA cria a estrutura em `.specs/features/`, gera o `spec.md` alinhado ao PRD e inicia o ciclo TLC.

---

## 🚨 6. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se uma função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.

---

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.

```
CHUNK_END id=cd6526d17218_c001
FILE_END id=file_cd6526d17218

````
CHUNK_END id=aa78525fb574_c019
CHUNK_START id=aa78525fb574_c020 start_line=5701 end_line=6000
````markdown

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CHUNK_START id=450d7ec70909_c001 start_line=1 end_line=32
```markdown
---
Criado em: 2026-04-10 23:29
Ultima Atualizacao: 2026-04-10 23:29
Status: Ativo
---

# 🔗 TLC_INTEGRATION.md
> Ponte entre Governança de Longo Prazo (`.context/`) e Execução Atômica (`.specs/`).  
> 💡 *Insight Humano: O PRD diz O QUÊ e POR QUÊ. A SPEC diz COMO e QUANDO. O TLC orquestra a transição.*

## 🔄 Ciclo de Vida Híbrido
1. **INTENT** → `PRD.md` ativo define escopo e critérios de aceite.
2. **SPECIFY** → IA cria `.specs/features/[nome]/spec.md` com passos atômicos, contratos de API/DB e testes.
3. **IMPLEMENT** → Geração de código baseada na spec. Handoffs registrados no `JOURNAL.md`.
4. **VERIFY** → Testes passam → `STATE.md` marcado como `✅ PASSED`.
5. **SYNC** → Decisões arquiteturais e lições → `JOURNAL.md`. Spec arquivada ou deletada.

````
CHUNK_END id=aa78525fb574_c004
CHUNK_START id=aa78525fb574_c005 start_line=1201 end_line=1500
````markdown

## 📏 Regras de Ouro
- 🔒 **Soberania do Contexto:** `.specs/` nunca sobrescreve `.context/`. Apenas alimenta a memória de longo prazo.
- 🧹 **Efemeridade:** Spec inativa >48h ou pós-merge → mover para `_archive_context/specs/` ou deletar.
- 🤝 **Handoff:** Handoff obrigatório no `JOURNAL.md` se a spec cruzar domínios (ex: `@backend` → `@qa`).
- ⚠️ **Divergência:** Se `spec.md` divergir de `schema.sql` ou `PRD.md` → parar e solicitar correção de contexto.

## 🤖 Fluxo de Ativação
`"Inicie a fase de SPECIFY para o PRD #[ID]"` → 
1. IA lê `PRD.md` + `schema.sql` + `JOURNAL.md` (últimas 30).
2. Cria `.specs/features/[nome]/` com `spec.md` e `STATE.md: draft`.
3. Executa passos atômicos → atualiza `STATE.md`.
4. Ao concluir: `✅ Spec passed. Deseja arquivar a spec e sincronizar o JOURNAL.md?`

---
> *Este documento garante que o "Cérebro" (Contexto) e o "Músculo" (TLC) operem em harmonia.*

```
CHUNK_END id=450d7ec70909_c001
FILE_END id=file_450d7ec70909

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.800876+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=9b6470da8849_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=9b6470da8849_c001
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=23 bytes=1082 mtime=2026-04-11T01:25:28.436758+00:00 sha1=43293ddbefe17288e0cea85c402cff9f4ed05cea
CHUNK_START id=019509328844_c001 start_line=1 end_line=23
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# JOURNAL.md
> Log vivo de decisoes e bugs. (Max 600 linhas)

## 📅 2026-04-11 01:25
**Decisão/Bug:** 🔄 Handoff: @frontend-specialist → @backend-engineer
**Solução:** Implementada UI do CheckoutForm v1 usando Stripe Elements. Estado local gerenciado; aguardando API `/api/checkout/session`.
**Implicação:** Próximo agente deve configurar a rota backend e garantir o retorno do `clientSecret`.

## 📅 2026-04-11 01:35
**Decisão/Bug:** 🔄 Handoff: @backend-engineer → @qa-validator
**Solução:** Endpoint Stripe Session operacional. Webhook configurado para escutar `payment_intent.succeeded` e atualizar tabela `orders`.
**Implicação:** QA deve validar fluxos de falha e idempotência do webhook.

## 📅 2026-04-11 01:45
**Decisão/Bug:** ✅ Ciclo Checkout Stripe Concluído
**Solução:** Cobertura de testes em 92%. Validado happy path e 'card declined'. Injetado retry pattern no webhook.
**Implicação:** PRD #15 concluído. Tecnologias Stripe adicionadas ao env.

```
CHUNK_END id=019509328844_c001
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=13 bytes=286 mtime=2026-04-11T01:26:25.980990+00:00 sha1=26974391beb474138a05628058c4c0c9010cdf07
CHUNK_START id=d069d4f2ebef_c001 start_line=1 end_line=13
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

<!-- AUTO-SYNC START -->
*🤖 Atualizado automaticamente em 2026-04-10 22:26*

### DevDependencies
- `husky`: `^9.1.7`

### Tabelas no Schema (schema.sql)
- `orders`

<!-- AUTO-SYNC END -->


```
CHUNK_END id=d069d4f2ebef_c001
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.794384+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=0858a02cf53f_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=0858a02cf53f_c001
FILE_END id=file_0858a02cf53f

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CHUNK_START id=a5c71962029a_c001 start_line=1 end_line=63
````markdown
---
Criado em: 2026-04-10 21:44

````
CHUNK_END id=aa78525fb574_c012
CHUNK_START id=aa78525fb574_c013 start_line=3601 end_line=3900
````markdown
Ultima Atualizacao: 2026-04-10 21:44
Status: Ativo
---

# 🛠️ Manual de Reconstrução & Automação

Este guia contém as instruções para subir o ambiente do zero e operar as ferramentas de governança de contexto.

---

## 🏗️ 1. Setup do Ambiente

### Requisitos Mínimos:
- **Python ≥ 3.8** (Para os scripts de automação)
- **Node.js** (Para os wrappers NPM)
- **Make** (Opcional, para orquestração Unix)
- **Bash** (Para Git Bash, WSL, Linux ou macOS)

---

## ⚙️ 2. Ferramentas de Automação

O projeto oferece três formas de gerenciar a saúde do contexto. Escolha a que melhor se adapta ao seu terminal:

### Opção A: Via NPM (Recomendado para Devs Web)
```bash
npm run context:validate  # Checa integridade e tokens
npm run context:sync      # Sincroniza deps e schema
npm run context:purge     # Limpa e arquiva o log vivo
```

### Opção B: Via Make (Recomendado para CI/CD e Unix)
```bash
make validate
make sync
make purge
make all       # Executa o pipeline completo: Valida -> Sync -> Purge
```

### Opção C: Via Bash (Resiliência Universal)
```bash
./run_context.sh validate
./run_context.sh all
```

---

## 🗃️ 3. Recuperação de Contexto (Archive)

Se precisar restaurar um Journal ou PRD antigo que foi arquivado:
1. Vá até `.context/maintenance/_archive_context/`.
2. Localize o arquivo pelo timestamp `YYYYMMDD_HHMMSS`.
3. Copie o conteúdo necessário de volta para a raiz da camada correspondente (`maintenance/` ou `brain/`).

---

## 🚨 4. Troubleshooting
- **Erro de Encoding (Windows):** Todos os scripts são forçados para UTF-8. Se vir caracteres estranhos, verifique se o seu terminal suporta Unicode.
- **Python não encontrado:** No Windows, o script tenta `python3` e faz fallback para `python`. Se falhar, certifique-se que o executável está no seu PATH.

> *Lembrete: Sem automação, a documentação morre. Use as ferramentas a cada nova funcionalidade iniciada no ROADMAP.md.*

````
CHUNK_END id=a5c71962029a_c001
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=27 bytes=1336 mtime=2026-04-11T02:26:43.636538+00:00 sha1=adb37745498ccfa61a2b793c10240a2b20d3d716
CHUNK_START id=54a6a553d34b_c001 start_line=1 end_line=27
```markdown
---
Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-10 23:27
Status: Ativo
---

# 🧬 rx-anatomy.md (Raio-X de Anatomia)
> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Arquivos de decisão e regras
│   ├── maintenance/        # Logs, db schema e inventários
│   └── monitoring/         # Dashboard de saúde
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.sh          # Orquestrador universal Bash
├── init_ai_project.sh      # Bootstrapper supremo
└── package.json            # Gerenciamento de libs e scripts context:*

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `_archive_context/specs/`
- **Não é fonte da verdade.** O `.context/` permanece como SSOT.

```
CHUNK_END id=54a6a553d34b_c001
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.789386+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=ca8da4f87431_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=ca8da4f87431_c001
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CHUNK_START id=91d5627a725e_c001 start_line=1 end_line=9
```sql
-- Snapshot Real da Tabela de Pedidos
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_session_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending', -- pending, succeeded, failed
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
CHUNK_END id=91d5627a725e_c001
FILE_END id=file_91d5627a725e

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1624 mtime=2026-04-10T23:50:11.304033+00:00 sha1=92934bdfcac044ab34842a1b0131524ead5e2e5b
CHUNK_START id=068a21d64bec_c001 start_line=1 end_line=38
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

| Métrica | Valor Atual| Limite / Heurística | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Pilar de Manutenção** | | | | |
| JOURNAL.md (linhas) | 412 | 600 | Manutenção | ✅ OK |
| JOURNAL.md (tamanho) | ~12k char | 50k char | Manutenção | ✅ OK |
| **Pilar Cognitivo** | | | | |
| Role Ativa | @frontend-specialist | N/A | Cognitivo | ⚠️ Em Task |
| PRD Ativo | #14 - Auth Flows | 1 por vez | Cognitivo | ✅ OK |
| **Pilar de Consistência** | | | | |
| Schema vs PRD Sync | 0 divergências | 0 | DB-First | ✅ OK |
| Último Sincronismo | 2h atrás | < 24h | Governança | ✅ OK |
| **Pilar de Sessão** | | | | |
| Turns de Sessão | 8 trocas | 20 trocas | Sessão | ✅ OK |
| Token Window Est. | ~78k | 128k | Sessão | ⚠️ 80% |

````
CHUNK_END id=aa78525fb574_c020
CHUNK_START id=aa78525fb574_c021 start_line=6001 end_line=6300
````markdown

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até que a migration seja documentada.
- **Se Turns > 18:** Propor Snapshot ou Reset de Sessão antes de iniciar próxima tarefa grande.

---

## 📅 Histórico de Saúde (Log de Purges)
| Data | Ação | Agente | Resultado |
| :--- | :--- | :--- | :--- |
| 2026-04-10 | Purge Completo | @context-keeper | Journal resetado para seed de 30 linhas. |

```
CHUNK_END id=068a21d64bec_c001
FILE_END id=file_068a21d64bec

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=26 bytes=693 mtime=2026-04-11T00:55:20.246274+00:00 sha1=163dd12b4c98d348f80986ea59afcb4604dc9e0e
CHUNK_START id=e477c4c5a96c_c001 start_line=1 end_line=26
```yaml
name: Context Health Check

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]


````
CHUNK_END id=aa78525fb574_c005
CHUNK_START id=aa78525fb574_c006 start_line=1501 end_line=1800
````markdown
jobs:
  validate-context:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run Context Validation
        # No GitHub Actions (Linux), usamos python3
        run: python3 .context/_scripts/validate_context.py

      - name: Check Journal Limits
        run: python3 .context/_scripts/validate_context.py | grep -q "SUCCESS" || (echo "❌ Contexto quebrado ou Journal excedido!" && exit 1)

```
CHUNK_END id=e477c4c5a96c_c001
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CHUNK_START id=3adfd36c1559_c001 start_line=1 end_line=9
```bash
echo "husky - DEPRECATED

Please remove the following two lines from $0:

#!/usr/bin/env sh
. \"\$(dirname -- \"\$0\")/_/husky.sh\"

They WILL FAIL in v10.0.0
"
```
CHUNK_END id=3adfd36c1559_c001
FILE_END id=file_3adfd36c1559

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=68 bytes=2890 mtime=2026-04-11T02:30:31.368152+00:00 sha1=ea66d1b4ed6f174f17b752f28ac358093fb784d2
CHUNK_START id=8ec9a00bfd09_c001 start_line=1 end_line=68
````markdown
# 🛸 Antigravity Kit v2.2 Premium+
> **O ecossistema definitivo para engenharia AI-Ready: Governança Macro + Execução Atômica.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação (GitHub Copilot, Cursor, Antigravity). Ele unifica o **Antigravity Kit** (Governança Macro) com o **TLC Spec-Driven** (Execução Atômica), garantindo que o Propósito (PRD) se transforme em Ação (Código) com precisão cirúrgica.

---

## 🧠 A Filosofia: "Se não está no Contexto, não existe."

Neste framework, a pasta `.context/` é a **Single Source of Truth (SSOT)**. A pasta `.specs/` é o seu **Workshop Efêmero**. O código é apenas o reflexo físico da inteligência documentada.

## 🚀 Instalação Ultra-Rapida (One-Click Setup)

Se voce quer inicializar este framework em um novo projeto do zero, basta rodar o nosso bootstrapper supremo:

```bash
# 1. Torne o script executavel
chmod +x init_ai_project.sh

# 2. Execute
./init_ai_project.sh
```

O script ira criar automaticamente toda a estrutura de camadas, os workshops de execução, os motores de manutenção v2.2+, e configurar a blindagem Husky.

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. PRD v2.0, Rules, Registry e a Ponte de Integração TLC.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação

| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Verifica a integridade dos arquivos e a estrutura do workshop. |
| `npm run context:sync`     | Sincroniza `TECHNICAL_REQUIREMENTS.md` com dependências e DB. |
| `npm run context:cleanup`  | Gerencia a efemeridade do `.specs/` (Arquiva specs obsoletas). |
| `npm run context:all`      | Pipeline completo de saúde e manutenção. |

---

## 🤝 Protocolo de Ativação Híbrida

Para iniciar uma tarefa com poder total, use o prompt mestre:
> *"Inicie a fase de SPECIFY para o PRD #[ID] usando o modo Híbrido TLC."*


````
CHUNK_END id=aa78525fb574_c013
CHUNK_START id=aa78525fb574_c014 start_line=3901 end_line=4200
````markdown
Isso ativará a role `@spec-driver` e iniciará o ciclo atômico no `.specs/` alinhado à governança do `.context/`.

---

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*

````
CHUNK_END id=8ec9a00bfd09_c001
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=114 bytes=4693 mtime=2026-04-11T01:41:16.589576+00:00 sha1=69a61b75c7697979c8e4ab560e0325f71bd7151d
CHUNK_START id=4efb6293109d_c001 start_line=1 end_line=114
````markdown
---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria viva, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.sh`, `Makefile` | Validacao, purge, sync e orquestracao. |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `tests/test_context.py` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija antes de forcar.

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rapidos (Cheat Sheet)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Sincronizar deps e schema com TECH_REQUIREMENTS.md
npm run context:sync

# Arquivar 70% do journal (mantem 30% como semente)
npm run context:purge

# Pipeline completo (validate -> sync -> purge)
npm run context:all

# Rodar testes do framework manualmente (Universal Python)
npm run context:test
```
> 💡 *Fallbacks:* `make all` ou `bash run_context.sh all`

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se `validate_context.py` ou `test_context.py` falharem.
- **CI/CD:** O GitHub Actions roda o pipeline em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Clone
- [ ] `.context/` existe com estrutura de camadas ok.
- [ ] `brain/RULES.md` e `brain/MASTER_FLOW.md` alinhados a stack.
- [ ] `brain/AGENT_REGISTRY.md` possui roles registradas.
- [ ] `npm run context:all` executa sem erros.

### 🚀 Inicio de Feature / PRD
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---

> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.

````
CHUNK_END id=4efb6293109d_c001
FILE_END id=file_4efb6293109d

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=380 bytes=15779 mtime=2026-04-11T02:42:28.056925+00:00 sha1=2dba92559cf404d5e91df067a8fd72b6a965ec8c
CHUNK_START id=c3916196f58f_c001 start_line=1 end_line=300
```python
#!/usr/bin/env python3
"""captura_projeto.py - Gera bundle markdown AI-first do repositorio. TEMPLATE UNIVERSAL."""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import os

````
CHUNK_END id=aa78525fb574_c021
CHUNK_START id=aa78525fb574_c022 start_line=6301 end_line=6600
````markdown
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path

# 🛠️ CUSTOMIZE AQUI: Padrões universais + adicione os específicos do seu projeto
PASTAS_IGNORAR = {
    ".git", "node_modules", "dist", "build", "out", "target", "bin", "obj",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache",
    ".next", ".nuxt", ".vercel", ".netlify", ".vite", ".cache",
    ".vscode", ".idea", ".cursor", "coverage", ".pytest_cache",
    "captura_projeto", # 📝 Ignorar a própria pasta do utilitário
}

PASTAS_CORE = {
    # 📝 Defina as pastas ARQUITETURALMENTE essenciais para a IA entender seu projeto
    # Ex: {"src", "lib", "api", "supabase", ".context", ".specs"}
    "src", "lib", "api", ".context", ".specs"
}

# 🛠️ CUSTOMIZE AQUI: Regras de classificação semântica (fallback seguro)
DOMAIN_RULES = {
    r"/api/|/routes/|/handlers/|/controllers/": "api",
    r"/components/|/ui/|/views/|/pages/|/screens/": "ui",
    r"/lib/|/utils/|/helpers/|/core/|/shared/": "lib",
    r"/db/|/migrations/|/models/|/schema/|/supabase/|/prisma/": "db",
    r"/tests/|/spec/|/__tests__/|\.test\.|\.spec\.": "tests",
    r"/config/|/settings/|/env/": "config",
    r"\.md$|\.rst$|\.txt$": "docs",
    r"\.(json|toml|yaml|yml|ini)$": "config",
}

EXTENSOES_PERMITIDAS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".html", ".css", ".json", ".md",
    ".yaml", ".yml", ".toml", ".sh", ".sql", ".graphql", ".vue", ".svelte",
    ".rs", ".go", ".java", ".c", ".h", ".hpp", ".cpp", ".ini",
}

LINGUAGENS = {
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".py": "python", ".html": "html", ".css": "css", ".json": "json", ".md": "markdown",

````
CHUNK_END id=aa78525fb574_c006
CHUNK_START id=aa78525fb574_c007 start_line=1801 end_line=2100
````markdown
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".sh": "bash", ".sql": "sql",
    ".graphql": "graphql", ".vue": "html", ".svelte": "html", ".rs": "rust",
    ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".hpp": "cpp", ".cpp": "cpp", ".ini": "ini",
}

ARQUIVOS_SENSIVEIS_GLOBS = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx",
    "credentials*.json", "id_rsa*", "secrets.*", "*.cert",
    # 📝 Adicione padrões sensíveis do SEU projeto aqui
}

SECRET_PATTERNS = (
    re.compile(r'(["\']?)(\w*(?:API_KEY|SECRET|TOKEN|PASSWORD|AUTH_KEY|PRIVATE_KEY|ACCESS_KEY|DB_PASS|CONNECTION_STRING)\w*)\1\s*[:=]\s*["\']?(\S+)["\']?', re.IGNORECASE),
    re.compile(r'(BEGIN\s+(RSA|EC|DSA|OPENSSH|PGP)\s+PRIVATE\s+KEY)', re.IGNORECASE),
)

DEFAULT_OUTPUT = "contexto.md"
logging.basicConfig(level=logging.WARNING, format="⚠️ %(message)s")

@dataclass(frozen=True)
class BundleConfig:
    diretorio: Path
    output: str = DEFAULT_OUTPUT
    only_core: bool = False
    exclude_core: bool = False
    profile: str = "ai-default"
    toc_only: bool = False
    max_lines_per_file: int = 300
    emit_symbol_index: bool = False
    emit_import_map: bool = False
    mask_secrets: bool = False

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_line: int
    end_line: int
    content: str

@dataclass(frozen=True)
class FileRecord:
    file_id: str
    relative_path: str
    domain: str
    language: str
    line_count: int
    byte_count: int
    mtime_utc: str
    sha1: str
    symbols: tuple[str, ...]
    imports: tuple[str, ...]
    chunks: tuple[Chunk, ...]

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXTENSOES_PERMITIDAS:
        return True
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        return False
    return mime.startswith("text/") or mime in {"application/json", "application/xml", "application/javascript"}

def is_sensitive_file(path: Path) -> bool:
    return any(fnmatch(path.name.lower(), pat.lower()) for pat in ARQUIVOS_SENSIVEIS_GLOBS)

def classify_domain(relative_path: str) -> str:
    p = relative_path.lower()
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, p):
            return domain
    return "source"

def should_include_profile(record_domain: str, config: BundleConfig) -> bool:
    if config.profile == "ai-compact":
        return record_domain not in {"tests", "docs"}
    return True

def mask_sensitive(content: str, enabled: bool) -> str:
    if not enabled:
        return content
    out = content
    for pattern in SECRET_PATTERNS:
        out = pattern.sub(r"\1***", out)
    return out

def extract_symbols(content: str, suffix: str) -> tuple[str, ...]:
    symbols: list[str] = []
    if suffix == ".py":
        symbols.extend(re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content, re.MULTILINE))
        symbols.extend(re.findall(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        symbols.extend(re.findall(r"(?:export\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content))
        symbols.extend(re.findall(r"(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\s*", content))
        symbols.extend(re.findall(r"export\s+const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", content))
    seen, seen_set = [], set()
    for s in symbols:
        if s not in seen_set:

````
CHUNK_END id=aa78525fb574_c014
CHUNK_START id=aa78525fb574_c015 start_line=4201 end_line=4500
````markdown
            seen.append(s)
            seen_set.add(s)
    return tuple(seen[:80])

def extract_imports(content: str, suffix: str) -> tuple[str, ...]:
    imports: list[str] = []
    if suffix == ".py":
        imports.extend(re.findall(r"^import\s+([^\n]+)", content, re.MULTILINE))
        imports.extend(re.findall(r"^from\s+([^\s]+)\s+import\s+([^\n]+)", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        imports.extend(re.findall(r"^import\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]", content, re.MULTILINE))
        imports.extend(re.findall(r"require\(['\"]([^'\"]+)['\"]\)", content))
    normalized, seen_set = [], set()
    for item in imports:
        val = f"from {item[0]} import {item[1]}" if isinstance(item, tuple) else item
        if val not in seen_set:
            normalized.append(val)
            seen_set.add(val)
    return tuple(normalized[:120])

def chunk_content(content: str, file_id: str, max_lines: int) -> tuple[Chunk, ...]:
    lines = content.splitlines()
    if not lines:
        return (Chunk(f"{file_id}_c001", 1, 1, ""),)
    if max_lines <= 0 or len(lines) <= max_lines:
        return (Chunk(f"{file_id}_c001", 1, len(lines), content),)
    chunks = []
    idx = 1
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        part = "\n".join(lines[start:end])
        if end < len(lines) or content.endswith("\n"):
            part += "\n"
        chunks.append(Chunk(f"{file_id}_c{idx:03d}", start + 1, end, part))
        idx += 1
    return tuple(chunks)

def make_file_id(relative_path: str) -> str:
    return hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:12]

def collect_files(config: BundleConfig) -> tuple[FileRecord, ...]:
    records: list[FileRecord] = []
    root = config.diretorio.resolve()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        is_root = (current == root)

        if config.only_core:
            dirnames[:] = sorted(d for d in dirnames if (d in PASTAS_CORE or not is_root) and d not in PASTAS_IGNORAR)
        elif config.exclude_core:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_CORE and d not in PASTAS_IGNORAR)
        else:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_IGNORAR)

        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root)
            rel_path = rel.as_posix()
            top = rel.parts[0] if rel.parts else ""

            if config.only_core and is_root and top not in PASTAS_CORE:
                continue
            if config.exclude_core and is_root and top in PASTAS_CORE:
                continue
            if is_sensitive_file(path):
                continue
            if not is_text_file(path):
                continue

            try:
                raw_content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    raw_content = path.read_text(encoding="latin-1")
                except OSError as e:
                    logging.warning("Pulando %s: %s", rel_path, e)
                    continue
            except OSError as e:
                logging.warning("Pulando %s: %s", rel_path, e)
                continue

            domain = classify_domain(rel_path)
            if not should_include_profile(domain, config):
                continue

            raw_sha1 = hashlib.sha1(raw_content.encode("utf-8", errors="ignore")).hexdigest()
            content = mask_sensitive(raw_content, config.mask_secrets)
            file_id = make_file_id(rel_path)
            stat = path.stat()
            suffix = path.suffix.lower()

            symbols = extract_symbols(content, suffix) if config.emit_symbol_index else ()
            imports = extract_imports(content, suffix) if config.emit_import_map else ()
            chunks = chunk_content(content, file_id, config.max_lines_per_file)

            records.append(FileRecord(
                file_id=file_id, relative_path=rel_path, domain=domain,
                language=LINGUAGENS.get(suffix, suffix[1:] if suffix else "text"),
                line_count=len(content.splitlines()),
                byte_count=len(content.encode("utf-8", errors="ignore")),
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                sha1=raw_sha1, symbols=symbols, imports=imports, chunks=chunks
            ))

    records.sort(key=lambda r: r.relative_path)
    return tuple(records)

def mode_name(config: BundleConfig) -> str:
    if config.only_core: return "only-core"
    if config.exclude_core: return "exclude-core"
    return "full"

def render_frontmatter(config: BundleConfig, records: tuple[FileRecord, ...]) -> str:
    total_bytes = sum(r.byte_count for r in records)
    lines = [
        "---", "schema_version: 1",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"root: {config.diretorio.resolve().name}",
        f"mode: {mode_name(config)}", f"profile: {config.profile}",
        f"file_count: {len(records)}", f"byte_count: {total_bytes}",
        "ignored_dirs:"
    ]
    lines.extend(f"  - {d}" for d in sorted(PASTAS_IGNORAR))
    lines.append("sensitive_rules:")
    lines.extend(f"  - {r}" for r in sorted(ARQUIVOS_SENSIVEIS_GLOBS))
    lines.append("---")
    return "\n".join(lines)

def render_index_by_domain(records: tuple[FileRecord, ...]) -> str:
    grouped: dict[str, list[FileRecord]] = {}
    for r in records:
        grouped.setdefault(r.domain, []).append(r)
    lines = ["## INDEX_BY_DOMAIN"]
    for domain in sorted(grouped):
        lines.append(f"- `{domain}`:")
        lines.extend(f"  - `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in grouped[domain])
    return "\n".join(lines)

def render_index_by_path(records: tuple[FileRecord, ...]) -> str:
    lines = ["## INDEX_BY_PATH"]
    lines.extend(f"- `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in records)
    return "\n".join(lines)

def render_symbols(records: tuple[FileRecord, ...]) -> str:
    lines = ["## SYMBOL_INDEX"]
    for r in records:
        if not r.symbols: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{s}`" for s in r.symbols)
    return "\n".join(lines)


````
CHUNK_END id=aa78525fb574_c022
CHUNK_START id=aa78525fb574_c023 start_line=6601 end_line=6900
````markdown

```
CHUNK_END id=c3916196f58f_c001
CHUNK_START id=c3916196f58f_c002 start_line=301 end_line=380
````python
def render_imports(records: tuple[FileRecord, ...]) -> str:
    lines = ["## IMPORT_MAP_MIN"]
    for r in records:
        if not r.imports: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{i}`" for i in r.imports)
    return "\n".join(lines)

def pick_fence(content: str) -> str:
    return "````" if "```" in content else "```"

def render_file_record(record: FileRecord, toc_only: bool) -> str:
    lines = [
        "---", f'<a id="file_{record.file_id}"></a>',
        f"FILE_START id=file_{record.file_id} path={record.relative_path} "
        f"domain={record.domain} lang={record.language} lines={record.line_count} "
        f"bytes={record.byte_count} mtime={record.mtime_utc} sha1={record.sha1}"
    ]
    if toc_only:
        lines.append("CONTENT_OMITTED toc_only=true")
    else:
        for chunk in record.chunks:
            lines.append(f"CHUNK_START id={chunk.chunk_id} start_line={chunk.start_line} end_line={chunk.end_line}")
            fence = pick_fence(chunk.content)
            lines.extend([f"{fence}{record.language}", chunk.content, fence, f"CHUNK_END id={chunk.chunk_id}"])
    lines.append(f"FILE_END id=file_{record.file_id}")
    return "\n".join(lines)

def generate_context_markdown(config: BundleConfig) -> str:
    if config.only_core and config.exclude_core:
        raise ValueError("only_core e exclude_core nao podem ser usados juntos")
    
    records = collect_files(config)
    blocks = ["# Project Context Bundle", "", render_frontmatter(config, records), "",
              render_index_by_domain(records), "", render_index_by_path(records)]
    if config.emit_symbol_index:
        blocks.extend(["", render_symbols(records)])
    if config.emit_import_map:
        blocks.extend(["", render_imports(records)])
    for r in records:
        blocks.extend(["", render_file_record(r, toc_only=config.toc_only)])
    return "\n".join(blocks) + "\n"

def write_output(config: BundleConfig) -> Path:
    output_path = config.diretorio / config.output
    content = generate_context_markdown(config)
    output_path.write_text(content, encoding="utf-8")

````
CHUNK_END id=aa78525fb574_c007
CHUNK_START id=aa78525fb574_c008 start_line=2101 end_line=2400
````markdown
    return output_path

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="captura_projeto.py - Consolida repositorio em markdown AI-first")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretorio raiz")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Arquivo de saida")
    core = parser.add_mutually_exclusive_group()
    core.add_argument("--only-core", action="store_true", help="Inclui apenas escopo core")
    core.add_argument("--exclude-core", action="store_true", help="Exclui escopo core")
    parser.add_argument("--profile", choices=["ai-default", "ai-compact", "ai-forensics"], default="ai-default")
    parser.add_argument("--toc-only", action="store_true", help="Apenas indices e envelopes")
    parser.add_argument("--max-lines-per-file", type=int, default=300, help="Limite de linhas por chunk (0=ilimitado)")
    parser.add_argument("--emit-symbol-index", action="store_true", help="Adiciona SYMBOL_INDEX")
    parser.add_argument("--emit-import-map", action="store_true", help="Adiciona IMPORT_MAP_MIN")
    parser.add_argument("--mask-secrets", action="store_true", help="Ofusca segredos no conteudo")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = BundleConfig(
        diretorio=Path(args.diretorio), output=args.output,
        only_core=args.only_core, exclude_core=args.exclude_core,
        profile=args.profile, toc_only=args.toc_only,
        max_lines_per_file=args.max_lines_per_file,
        emit_symbol_index=args.emit_symbol_index,
        emit_import_map=args.emit_import_map, mask_secrets=args.mask_secrets
    )
    out = write_output(config)
    print(f"\n[OK] Gerado: {out}")
    print(f"   Mode: {mode_name(config)} | Profile: {config.profile}")

if __name__ == "__main__":
    main()
````
CHUNK_END id=c3916196f58f_c002
FILE_END id=file_c3916196f58f

---
<a id="file_aa78525fb574"></a>
FILE_START id=file_aa78525fb574 path=contexto.md domain=docs lang=markdown lines=2798 bytes=114045 mtime=2026-04-11T02:42:10.878553+00:00 sha1=5d3d571af0bcd047f20eb4f506346b74d89c495e
CHUNK_START id=aa78525fb574_c001 start_line=1 end_line=300
````markdown
# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-11T02:42:10.874463+00:00
root: template_inicío_de_projeto
mode: full
profile: ai-default
file_count: 33
byte_count: 94071
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


````
CHUNK_END id=aa78525fb574_c015
CHUNK_START id=aa78525fb574_c016 start_line=4501 end_line=4800
````markdown
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
- `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package-lock.json` -> [file_fa288d1472d2](#file_fa288d1472d2)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `planos/implementation_plan.md` -> [file_a9422a4b7476](#file_a9422a4b7476)
- `planos/master_plan.md` -> [file_32db3e3783df](#file_32db3e3783df)
- `planos/multi_agent_plan.md` -> [file_2a788cb45159](#file_2a788cb45159)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

## SYMBOL_INDEX
- `.context/_scripts/cleanup_specs.py`:
  - `get_specs`
  - `archive_spec`
  - `cleanup`
- `.context/_scripts/purge_journal.py`:
  - `parse_entries`
  - `purge_journal`
- `.context/_scripts/sync_project.py`:
  - `get_package_deps`
  - `get_schema_tables`
  - `sync_requirements`
- `.context/_scripts/validate_context.py`:
  - `check_files`
  - `check_journal_lines`
  - `estimate_tokens`
  - `check_registry_structure`
  - `check_specs_structure`
  - `validate`
- `captura_projeto.py`:
  - `is_text_file`
  - `is_sensitive_file`
  - `classify_domain`
  - `should_include_profile`
  - `mask_sensitive`
  - `extract_symbols`
  - `extract_imports`
  - `chunk_content`
  - `make_file_id`
  - `collect_files`
  - `mode_name`
  - `render_frontmatter`
  - `render_index_by_domain`
  - `render_index_by_path`
  - `render_symbols`
  - `render_imports`
  - `pick_fence`
  - `render_file_record`
  - `generate_context_markdown`
  - `write_output`
  - `parse_args`
  - `main`
  - `BundleConfig`
  - `Chunk`
  - `FileRecord`
- `tests/test_context.py`:
  - `TestContextGovernance`

## IMPORT_MAP_MIN
- `.context/_scripts/cleanup_specs.py`:
  - `os`
  - `shutil`
  - `time`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/purge_journal.py`:
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/sync_project.py`:
  - `json`
  - `re`
  - `from pathlib import Path`
  - `from datetime import datetime`
- `.context/_scripts/validate_context.py`:
  - `os`
  - `sys`
  - `from pathlib import Path`
- `captura_projeto.py`:
  - `argparse`
  - `hashlib`
  - `logging`
  - `mimetypes`
  - `os`

````
CHUNK_END id=aa78525fb574_c023
CHUNK_START id=aa78525fb574_c024 start_line=6901 end_line=7200
````markdown
  - `re`
  - `from __future__ import annotations`
  - `from dataclasses import dataclass`
  - `from datetime import datetime, timezone`
  - `from fnmatch import fnmatch`
  - `from pathlib import Path`
- `tests/test_context.py`:
  - `unittest`
  - `os`
  - `shutil`
  - `tempfile`
  - `subprocess`
  - `sys`
  - `from pathlib import Path`

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CHUNK_START id=82cd6bde54ff_c001 start_line=1 end_line=71
```python
#!/usr/bin/env python3
"""
🧹 cleanup_specs.py
Gerencia a efemeridade da bancada de trabalho (.specs/).
Aplica a regra de 48h de inatividade e limite de 3 specs ativas simultâneas.
Arquiva specs excedentes ou obsoletas em _archive_context/specs/.
"""
import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# Caminhos base
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "specs"

# Configurações
MAX_INACTIVITY_SECONDS = 48 * 3600  # 48 horas
MAX_ACTIVE_SPECS = 3

def get_specs():
    if not SPECS_DIR.exists():
        return []
    return [d for d in SPECS_DIR.iterdir() if d.is_dir()]

def archive_spec(spec_path):
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{spec_path.name}_{timestamp}"
    dest_path = ARCHIVE_DIR / archive_name
    
    print(f"[INFO] Arquivando spec: {spec_path.name} -> {archive_name}")
    shutil.move(str(spec_path), str(dest_path))

def cleanup():
    specs = get_specs()
    if not specs:
        print("[OK] Nenhuma spec ativa encontrada.")
        return

````
CHUNK_END id=aa78525fb574_c008
CHUNK_START id=aa78525fb574_c009 start_line=2401 end_line=2700
````markdown

    now = time.time()
    active_specs = []

    # 1. Limpeza por inatividade (48h)
    for spec in specs:
        last_mod = max(os.path.getmtime(root) for root, _, _ in os.walk(spec))
        if (now - last_mod) > MAX_INACTIVITY_SECONDS:
            print(f"[AUTO] Inatividade detectada (>48h) em: {spec.name}")
            archive_spec(spec)
        else:
            active_specs.append(spec)

    # 2. Limpeza por limite de volume (Max 3)
    # Ordena por data de modificação (mais antiga primeiro)
    active_specs.sort(key=lambda s: max(os.path.getmtime(root) for root, _, _ in os.walk(s)))
    
    while len(active_specs) > MAX_ACTIVE_SPECS:
        oldest = active_specs.pop(0)
        print(f"[AUTO] Limite de volume excedido (Max {MAX_ACTIVE_SPECS}). Removendo spec mais antiga: {oldest.name}")
        archive_spec(oldest)

    print(f"[OK] Manutencao de specs concluida. Specs ativas: {len(active_specs)}/{MAX_ACTIVE_SPECS}")

if __name__ == "__main__":
    try:
        cleanup()
    except Exception as e:
        print(f"[ERROR] Falha na limpeza de specs: {e}")

```
CHUNK_END id=82cd6bde54ff_c001
FILE_END id=file_82cd6bde54ff

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=74 bytes=2507 mtime=2026-04-11T00:15:41.168457+00:00 sha1=772904f793113782bf9cc398ad20f87cefdc018c
CHUNK_START id=024b28a37d29_c001 start_line=1 end_line=74
```python
#!/usr/bin/env python3
"""
🗜️ purge_journal.py

````
CHUNK_END id=aa78525fb574_c001
CHUNK_START id=aa78525fb574_c002 start_line=301 end_line=600
````markdown
Arquiva 70% das entradas mais antigas do JOURNAL.md.
Mantém 30% mais recentes como semente. Backup automático e escrita atômica.
"""
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
JOURNAL_FILE = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "journals"
KEEP_RATIO = 0.3  # 30% mais recentes

def parse_entries(content):
    # Divide por headers markdown (## 📅, ##, etc.) mantendo o header na entrada
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]

def purge_journal():
    if not JOURNAL_FILE.exists():
        print("[WARN] JOURNAL.md nao encontrado. Nada a fazer.")
        return

    content = JOURNAL_FILE.read_text(encoding="utf-8")
    entries = parse_entries(content)

    if len(entries) <= 1:
        print("[INFO] Poucas entradas para purgar.")
        return

    keep_count = max(1, int(len(entries) * KEEP_RATIO))
    archive_entries = entries[:-keep_count]
    keep_entries = entries[-keep_count:]

    # Garante diretório de arquivo
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Backup com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

````
CHUNK_END id=aa78525fb574_c016
CHUNK_START id=aa78525fb574_c017 start_line=4801 end_line=5100
````markdown
    archive_file = ARCHIVE_DIR / f"journal_archive_{timestamp}.md"
    archive_content = f"# Arquivo de Journal - {timestamp}\n\n" + "\n\n".join(archive_entries) + "\n"
    archive_file.write_text(archive_content, encoding="utf-8")

    # Nova semente
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    seed = f"""---
Criado em: {now}
Ultima Atualizacao: {now}
Status: Ativo
Nota: Semente pos-purge. {len(archive_entries)} entradas arquivadas em {archive_file.name}.
---

# JOURNAL.md (Memoria Curta)
> Mantido por purge_journal.py. Limite heuristico de caracteres atingido.

""" + "\n\n".join(keep_entries) + "\n"

    # Escrita atomica (previne corrupcao se interrupcao ocorrer)
    temp_file = JOURNAL_FILE.with_suffix(".tmp")
    temp_file.write_text(seed, encoding="utf-8")
    temp_file.replace(JOURNAL_FILE)

    print(f"[OK] Purge concluido.")
    print(f"[OK] Arquivadas: {len(archive_entries)} entradas -> {archive_file.name}")
    print(f"[OK] Mantidas: {len(keep_entries)} entradas mais recentes.")

if __name__ == "__main__":
    try:
        purge_journal()
    except Exception as e:
        print(f"[ERROR] Erro no purge: {e}")

```
CHUNK_END id=024b28a37d29_c001
FILE_END id=file_024b28a37d29

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=94 bytes=3162 mtime=2026-04-11T00:15:52.626055+00:00 sha1=b9acd032350a262fad7d0995116e5686b8fa2191
CHUNK_START id=f122711ba9e1_c001 start_line=1 end_line=94
```python
#!/usr/bin/env python3
"""
🔄 sync_project.py
Sincroniza TECH_REQUIREMENTS.md com package.json e schema.sql.
Usa marcadores <!-- AUTO-SYNC START/END --> para preservar edicoes humanas.
"""
import json
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQ_FILE = CONTEXT_DIR / "maintenance" / "TECHNICAL_REQUIREMENTS.md"
PKG_FILE = CONTEXT_DIR.parent / "package.json"
SCHEMA_FILE = CONTEXT_DIR / "maintenance" / "schema.sql"

AUTO_START = "<!-- AUTO-SYNC START -->"
AUTO_END = "<!-- AUTO-SYNC END -->"

def get_package_deps():
    if not PKG_FILE.exists(): return {"dependencies": {}, "devDependencies": {}}
    try:
        with open(PKG_FILE, 'r', encoding='utf-8') as f:
            pkg = json.load(f)
        return {
            "dependencies": pkg.get("dependencies", {}),
            "devDependencies": pkg.get("devDependencies", {})
        }
    except Exception as e:
        print(f"[WARN] Erro ao ler package.json: {e}")
        return {"dependencies": {}, "devDependencies": {}}

def get_schema_tables():
    if not SCHEMA_FILE.exists(): return []
    content = SCHEMA_FILE.read_text(encoding="utf-8")
    # Regex para extrair nomes de tabelas
    return list(set(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["\']?(\w+)["\']?', content, re.IGNORECASE)))

def sync_requirements():
    deps = get_package_deps()
    tables = get_schema_tables()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    block = [
        AUTO_START,
        f"*🤖 Atualizado automaticamente em {now}*",
        ""
    ]

    if deps.get("dependencies"):
        block.append("### Dependencias (package.json)")
        for dep, ver in deps["dependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if deps.get("devDependencies"):
        block.append("### DevDependencies")
        for dep, ver in deps["devDependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if tables:
        block.append("### Tabelas no Schema (schema.sql)")
        for t in sorted(tables):
            block.append(f"- `{t}`")
        block.append("")

    block.append(AUTO_END)
    auto_content = "\n".join(block) + "\n"

    if not REQ_FILE.exists():
        REQ_FILE.write_text(f"# TECHNICAL_REQUIREMENTS.md\n\n{auto_content}", encoding="utf-8")
        print("[OK] TECHNICAL_REQUIREMENTS.md criado.")
        return

    content = REQ_FILE.read_text(encoding="utf-8")
    start_idx = content.find(AUTO_START)
    end_idx = content.find(AUTO_END)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + auto_content + content[end_idx + len(AUTO_END):]
    else:
        new_content = content.rstrip() + "\n\n" + auto_content

    REQ_FILE.write_text(new_content, encoding="utf-8")
    print("[OK] TECHNICAL_REQUIREMENTS.md sincronizado.")
    print(f"[OK] {len(deps.get('dependencies', {}))} deps | {len(tables)} tabelas detectadas.")

if __name__ == "__main__":
    try:
        sync_requirements()
    except Exception as e:
        print(f"[ERROR] Erro no sync: {e}")

```
CHUNK_END id=f122711ba9e1_c001
FILE_END id=file_f122711ba9e1

---

````
CHUNK_END id=aa78525fb574_c024
CHUNK_START id=aa78525fb574_c025 start_line=7201 end_line=7500
````markdown
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=106 bytes=3827 mtime=2026-04-11T02:29:28.743870+00:00 sha1=e6e9a29604fb4a340a2335bbca07488c56baff2a
CHUNK_START id=1077e9084ea1_c001 start_line=1 end_line=106
```python
#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade com AGENT_REGISTRY.md.
"""
import os
import sys
from pathlib import Path

# Caminhos relativos a localização deste script (.context/_scripts/)
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

# Mapeamento para estrutura em camadas
REQUIRED_FILES = [
    "brain/RULES.md", 
    "brain/MASTER_FLOW.md", 
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md", 
    "maintenance/JOURNAL.md", 
    "maintenance/schema.sql", 
    "maintenance/TECHNICAL_REQUIREMENTS.md"
]

JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000  # ~100k tokens

def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]

def check_journal_lines():
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists(): return 0, True
    lines = journal.read_text(encoding="utf-8").splitlines()
    return len(lines), len(lines) <= JOURNAL_MAX_LINES

def estimate_tokens():
    total_chars = 0
    for f in REQUIRED_FILES:
        path = CONTEXT_DIR / f
        if path.exists():
            total_chars += len(path.read_text(encoding="utf-8", errors="ignore"))
    return total_chars, total_chars < TOKEN_WARN_THRESHOLD_CHARS

def check_registry_structure():
    registry = CONTEXT_DIR / "brain/AGENT_REGISTRY.md"
    if not registry.exists(): return False, "Arquivo ausente"
    content = registry.read_text(encoding="utf-8")
    if "| Role |" not in content and "| Role" not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"

def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists(): return True, "Workshop inativo (OK)"
    
    features_dir = specs_dir / "features"
    if not features_dir.exists(): return False, "Diretorio features ausente no .specs"
    
    # Verifica se algum STATE.md esta presente em specs ativas
    active_specs = [d for d in features_dir.iterdir() if d.is_dir()]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
            
    return True, f"OK ({len(active_specs)} specs ativas)"

def validate():

````
CHUNK_END id=aa78525fb574_c009
CHUNK_START id=aa78525fb574_c010 start_line=2701 end_line=3000
````markdown
    print("--- Iniciando validacao de contexto (v2.2 Premium+) ---")
    issues = []

    missing = check_files()
    if missing: issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else: print("[OK] Todos os arquivos obrigatorios presentes.")

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok: issues.append(f"[WARN] .specs/: {spec_msg}")
    else: print(f"[OK] .specs/: {spec_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok: issues.append(f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}")
    else: print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, token_ok = estimate_tokens()
    est_tokens = total_chars // 4
    if not token_ok:
        issues.append(f"[WARN] Contexto estimado alto: ~{est_tokens}k tokens. Execute purge.")
    else: print(f"[OK] Estimativa de contexto segura: ~{est_tokens}k tokens")

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok: issues.append(f"[WARN] AGENT_REGISTRY.md: {reg_msg}")
    else: print("[OK] AGENT_REGISTRY.md estrutura valida.")

    print("\n--- Relatorio Final ---")
    if not issues:
        print("[SUCCESS] Contexto integro. Pronto para execucao.")
    else:
        for issue in issues: print(issue)
        print("[ALERT] Resolva os alertas antes de gerar codigo.")

if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        sys.exit(1)

```
CHUNK_END id=1077e9084ea1_c001
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=97 bytes=7180 mtime=2026-04-11T02:28:38.100881+00:00 sha1=3232fd65b8b05382d366aa1a8890e6385eb7f705
CHUNK_START id=e7c17acb71ff_c001 start_line=1 end_line=97

````
CHUNK_END id=aa78525fb574_c002
CHUNK_START id=aa78525fb574_c003 start_line=601 end_line=900
````markdown
````markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

````
CHUNK_END id=aa78525fb574_c017
CHUNK_START id=aa78525fb574_c018 start_line=5101 end_line=5400
````markdown

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Testes unitários/E2E, edge cases, cobertura, mocks, TDD | `tests/`, `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (apenas leitura para bugs) | `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (critérios de aceite) | "testar", "validar", "cobertura", "mock", "edge case", "TDD", "bug" |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@spec-driver` | Criação e orquestração de specs atômicas | `.specs/` (leitura/gravação temporária) | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (tail 30) | "inicie specify", "crie spec", "modo híbrido" |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |

💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Carregar APENAS: Global + Role-Specific + Task-Ephemeral
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*

````
CHUNK_END id=e7c17acb71ff_c001
FILE_END id=file_e7c17acb71ff

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=86 bytes=4370 mtime=2026-04-11T02:28:25.945198+00:00 sha1=06ce6786a149620314b57f8231142f652d4fc412
CHUNK_START id=d833c436f547_c001 start_line=1 end_line=86
````markdown
---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-04-10 23:28
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura do Diretório `.context/`

```text
.context/
├── 🧠 brain/                       # CAMADA COGNITIVA (The Brain)
│   ├── MASTER_FLOW.md             # Este documento
│   ├── RULES.md                   # Protocolos e "A Lei"
│   ├── AGENT_REGISTRY.md          # DNS de Roles e Permissões
│   ├── PROMPT_LIBRARY.md          # Catálogo de templates de prompts
│   ├── PRD.md                     # Requisito em execução (v2.0 - O Contrato)
│   ├── ROADMAP.md                 # Metas e fases (O Planejamento)
│   └── TLC_INTEGRATION.md         # Ponte entre Governança e Execução
│
├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
│   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Curta)
│   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e versões (Inventário)
│   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
│   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
│   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
│   ├── TESTS.md                   # Ledger de padrões e TDDs
│   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
│   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
│   └── _archive_context/          # Histórico imutável (A Biblioteca)
│
├── monitoring/             # CAMADA DE MONITORAMENTO (The Guardian)
│   └── CONTEXT_HEALTH.md   # Dashboard de saúde técnica e cognitiva
│
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── _scripts/               # CAMADA DE AUTOMACAO (The Motor)
    ├── validate_context.py        # Validador de integridade
    ├── purge_journal.py           # Gerenciador de memória (Purge)
    ├── cleanup_specs.py           # Gerenciador de efemeridade (.specs)

````
CHUNK_END id=aa78525fb574_c025
CHUNK_START id=aa78525fb574_c026 start_line=7501 end_line=7800
````markdown
    └── sync_project.py            # Sincronizador de requisitos
```

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e a presença do `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões arquiteturais tomadas durante o TLC **devem** ser migradas para o `JOURNAL.md` antes da limpeza da spec.

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*

````
CHUNK_END id=d833c436f547_c001
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=67 bytes=2446 mtime=2026-04-11T01:31:37.755946+00:00 sha1=b5c06bc8a67d2a788cc8263f03971f379d04e92e
CHUNK_START id=d124f6374cab_c001 start_line=1 end_line=67
```markdown
---
Criado em: 2026-04-10 22:35
Ultima Atualizacao: 2026-04-10 22:35
Status: Ativo (EM EXECUCAO)
PRD_ID: #15
---

# 🎯 PRD: Checkout com Integração Stripe
> Implementar um fluxo de pagamento seguro e resiliente usando Stripe Elements e Webhooks para pedidos digitais.

💡 *Insight Humano: Este PRD é um contrato vivo. Ele guia o roteamento de agentes, define criterios de aceite e serve como referência para o JOURNAL.md.*

---

## 📋 1. Visão Geral
| Campo | Valor |
|-------|-------|
| **Objetivo de Negocio** | Reduzir abandono de carrinho e garantir seguranca no processamento. |
| **Publico-Alvo** | Compradores finais da plataforma. |
| **Escopo** | UI de pagamento, Geracao de Session, Webhooks de confirmacao. |
| **MVP vs Futuro** | MVP: Cartao de Credito. Futuro: Apple Pay/Google Pay. |
| **Dependencias** | Stripe API, Tabela `orders`, Variaveis de ambiente seguras. |

---

## 🎯 2. Critérios de Aceite (Definition of Done)
### Funcionais
- [ ] Usuario finaliza compra com cartao valido.
- [ ] Webhook atualiza `orders.status` para 'succeeded'.
- [ ] Erro de cartao exibe mensagem amigavel (WCAG).
- [ ] Idempotencia garantida via `event.id` do Stripe.

### Não-Funcionais
- [ ] Tempo de resposta API < 500ms.
- [ ] Nenhum segredo (Keys) hardcoded no codigo.
- [ ] Logs estruturados para auditoria.

---

## 🤖 3. Roteamento Multi-Agent
| Etapa | Role Responsável | Entregável | Gatilho de Handoff |
|-------|-----------------|------------|-------------------|
| 1. UI Checkout | `@frontend-specialist` | `StripeForm.tsx` | "UI pronta, aguarda contrato de API" |
| 2. API Stripe | `@backend-engineer` | `/api/checkout` + Webhook | "Rotas operacionais, inicia validacao" |

````
CHUNK_END id=aa78525fb574_c010
CHUNK_START id=aa78525fb574_c011 start_line=3001 end_line=3300
````markdown
| 3. Testes E2E | `@qa-validator` | Suite de testes | "Cobertura >90%, edge cases validados" |

---

## 🔒 4. Context Gate (Pré-Execução)
- [ ] `maintenance/schema.sql` contem a tabela `orders`? ✅
- [ ] `maintenance/TECHNICAL_REQUIREMENTS.md` atualizado? ✅
- [ ] `maintenance/JOURNAL.md` < 550 linhas? ✅
- [ ] `brain/AGENT_REGISTRY.md` tem as roles necessarias? ✅

---

## 📊 5. Health Check Integrado
| Metrica | Valor | Status |
|---------|-------|--------|
| **Progresso** | 50% | 🟡 Em andamento |
| **Cobertura de Testes** | 92% (Simulada) | ✅ OK |
| **Divergência Schema** | 0 campos | ✅ OK |

---

## 🔄 6. Ciclo de Vida & Arquivamento
Ao concluir, mover para `_archive_context/prds/` e atualizar `ROADMAP.md`.

```
CHUNK_END id=d124f6374cab_c001
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=154 bytes=6687 mtime=2026-04-11T02:28:52.575335+00:00 sha1=aa3419c1efa08687a7c551dc44f40b504b422353
CHUNK_START id=9fe16e5591f0_c001 start_line=1 end_line=154
````markdown
---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo
---

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

````
CHUNK_END id=aa78525fb574_c003
CHUNK_START id=aa78525fb574_c004 start_line=901 end_line=1200
````markdown

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern

````
CHUNK_END id=aa78525fb574_c018
CHUNK_START id=aa78525fb574_c019 start_line=5401 end_line=5700
````markdown
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator`
**Gatilho:** Testes, validacao, edge cases, cobertura, mocks  
**Contexto Obrigatorio:** `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (criterios de aceite)
```text
🤖 Ativando @qa-validator | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{arquivo/feature a ser testada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{criar testes, validar edge cases ou aumentar cobertura}}
🚧 Restricoes:
- Seguir framework de testes definido em maintenance/TECHNICAL_REQUIREMENTS.md
- Mockar servicos externos; nao depender de rede real
- Cobrir happy path + 2 edge cases criticos no minimo
- Documentar falhas conhecidas no maintenance/JOURNAL.md se houver
📤 Saida Esperada:
1. Codigo dos testes (unitarios/integracao)
2. Matriz de cenarios cobertos
3. Recomendacoes de refatoracao se aplicavel
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada
2. spec.md com passos, contratos e critérios de verificação
3. STATE.md: draft → pronto para execução
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*

````
CHUNK_END id=9fe16e5591f0_c001
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.772397+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=c94f001202db_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=c94f001202db_c001
FILE_END id=file_c94f001202db


````
CHUNK_END id=aa78525fb574_c026
CHUNK_START id=aa78525fb574_c027 start_line=7801 end_line=8100
````markdown
---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=116 bytes=6333 mtime=2026-04-11T02:28:07.351671+00:00 sha1=01365a42e1b2cf0a5fb21f635bec7261b184b164
CHUNK_START id=cd6526d17218_c001 start_line=1 end_line=116
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança

**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)

> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas (Cognitiva, Manutenção, Monitoramento e Automação) para garantir escala e foco operacional.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)

Antes de gerar qualquer código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:

1.  **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`.
2.  **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
3.  **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`.

> ⚠️ **Bloqueio de Execução:** Se qualquer um dos itens acima não estiver carregado ou visível, a IA deve parar e solicitar a carga antes de prosseguir.

---

## 🔢 2. Session Budget & Heurísticas de Token

Para evitar alucinações por "Token Bloat" (excesso de memória na janela), adotamos limites práticos:

### 🚩 Gatilhos de Reset/Purge
A IA deve monitorar o estado da sessão e sugerir uma limpeza ou snapshot quando detectar:
- **Volume:** Aprox. **50.000 caracteres** acumulados no buffer de prompt/repost.
- **Duração:** Aprox. **15 a 20 trocas (mensagens)** densas de desenvolvimento.

### 🔄 Ação ao atingir o limite:
A IA deve disparar a seguinte mensagem ao usuário:
> *"🔄 Contexto próximo do limite de foco (~20 trocas). Deseja que eu execute o purge do JOURNAL, arquive o PRD atual ou inicie uma nova sessão limpa com um snapshot de semente?"*

---

## 🧠 1. Protocolo de Manutenção do Contexto
A IA deve agir como o "bibliotecário chefe". A consistência entre Código e Contexto é obrigatória.

### 📖 `maintenance/JOURNAL.md` (O Diário de Bordo)
- **O que logar:** Decisões de arquitetura, resoluções de bugs complexos e mudanças em lógica de negócio.
- **Proibido:** Erros de sintaxe triviais, mudanças de estilo (CSS) ou indentação.
- **O Purge:** Ao atingir o limite heurístico (~50k char), acionar `_scripts/purge_journal.py` para arquivar 70% e gerar semente de contexto.

### ⚙️ `maintenance/TECHNICAL_REQUIREMENTS.md`
- **Atualização Obrigatória:** Mudanças no `package.json`, alteração de Schema ou integração de novas APIs/Serviços.

### 🛠️ `maintenance/rebuild_guide.md` (Manual de Reconstrução)
- **Atualização Obrigatória:** Descoberta de hacks de ambiente local, configurações críticas de CI/CD ou passos manuais de deploy.

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e o `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões tomadas na spec devem ser transferidas para o `JOURNAL.md` no momento do merge.

---

## 🗄️ 2. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.

1.  **Verificação Obrigatória:** Antes de criar UI ou lógica que dependa de dados, o Agente DEVE verificar `maintenance/schema.sql`.
2.  **Aviso de Divergência:** Se a IA identificar que o código exige um campo inexistente no DB, ela deve parar e avisar: 
    *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro a migration antes de prosseguir."*

---

## 🤖 3. Comportamento do Agente (Transparência & Roteamento)

### 📋 3.1 Registro & Ativação
- **DNS de Roles:** `brain/AGENT_REGISTRY.md` é a única fonte oficial de papéis.
- **Identificação:** Toda tarefa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`.
- **Isolamento de Contexto:** Carregar apenas: Global (`brain/` base) + Role-Specific + Task-Ephemeral (`brain/PRD.md` + tail de `maintenance/JOURNAL.md`).

### 🤝 3.2 Handoff & Cruzamento de Domínios
Se uma tarefa exigir 2+ especialidades, o agente atual deve pausar e registrar:
- `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado Tecnico: [Resumo] | Próximo Passo: [Ação]`
O próximo agente inicia com contexto limpo + estado transferido.

### ⚖️ 3.3 Validação Pré-Código (Context Gate)
Antes de gerar código de produção, validar mentalmente ou via script:
- [ ] `brain/PRD.md` ativo e alinhado.

````
CHUNK_END id=aa78525fb574_c011
CHUNK_START id=aa78525fb574_c012 start_line=3301 end_line=3600
````markdown
- [ ] `maintenance/schema.sql` contém as estruturas referenciadas.
- [ ] `maintenance/JOURNAL.md` < 550 linhas.
- [ ] Nenhuma variável sensível hardcoded.

---

## 🔢 4. Session Budget & Heurísticas de Token
- **Volume:** Aprox. **50.000 caracteres** ou **15-20 trocas** densas.
- **Alerta:** Ao detectar o limite, propor purge ou reset de sessão imediatamente.

---

## 🔄 5. Gatilhos de Interação (Para o Usuário)
- **"Atualize o contexto":** IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- **"Qual o estado do projeto?":** IA gera relatório baseado no `JOURNAL.md` e `ROADMAP.md`.
- **"Roteie esta tarefa":** IA consulta `AGENT_REGISTRY.md` e inicia o fluxo de ativação/handoff.
- **"Use o prompt padrão":** IA seleciona o template no `brain/PROMPT_LIBRARY.md`, preenche placeholders e solicita confirmação.
- **"Novo PRD":** IA deve usar o template v2.0 (`brain/PRD.md`), preencher metadados, validar Context Gate e registrar no `ROADMAP.md`.
- **"Inicie a fase de SPECIFY para o PRD #[ID]":** A IA cria a estrutura em `.specs/features/`, gera o `spec.md` alinhado ao PRD e inicia o ciclo TLC.

---

## 🚨 6. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se uma função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.

---

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.

```
CHUNK_END id=cd6526d17218_c001
FILE_END id=file_cd6526d17218

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CHUNK_START id=450d7ec70909_c001 start_line=1 end_line=32
```markdown
---
Criado em: 2026-04-10 23:29
Ultima Atualizacao: 2026-04-10 23:29
Status: Ativo
---

# 🔗 TLC_INTEGRATION.md
> Ponte entre Governança de Longo Prazo (`.context/`) e Execução Atômica (`.specs/`).  
> 💡 *Insight Humano: O PRD diz O QUÊ e POR QUÊ. A SPEC diz COMO e QUANDO. O TLC orquestra a transição.*

## 🔄 Ciclo de Vida Híbrido
1. **INTENT** → `PRD.md` ativo define escopo e critérios de aceite.
2. **SPECIFY** → IA cria `.specs/features/[nome]/spec.md` com passos atômicos, contratos de API/DB e testes.
3. **IMPLEMENT** → Geração de código baseada na spec. Handoffs registrados no `JOURNAL.md`.
4. **VERIFY** → Testes passam → `STATE.md` marcado como `✅ PASSED`.
5. **SYNC** → Decisões arquiteturais e lições → `JOURNAL.md`. Spec arquivada ou deletada.

## 📏 Regras de Ouro

````
CHUNK_END id=aa78525fb574_c004
CHUNK_START id=aa78525fb574_c005 start_line=1201 end_line=1500
````markdown
- 🔒 **Soberania do Contexto:** `.specs/` nunca sobrescreve `.context/`. Apenas alimenta a memória de longo prazo.
- 🧹 **Efemeridade:** Spec inativa >48h ou pós-merge → mover para `_archive_context/specs/` ou deletar.
- 🤝 **Handoff:** Handoff obrigatório no `JOURNAL.md` se a spec cruzar domínios (ex: `@backend` → `@qa`).
- ⚠️ **Divergência:** Se `spec.md` divergir de `schema.sql` ou `PRD.md` → parar e solicitar correção de contexto.

## 🤖 Fluxo de Ativação
`"Inicie a fase de SPECIFY para o PRD #[ID]"` → 
1. IA lê `PRD.md` + `schema.sql` + `JOURNAL.md` (últimas 30).
2. Cria `.specs/features/[nome]/` com `spec.md` e `STATE.md: draft`.

````
CHUNK_END id=aa78525fb574_c019
CHUNK_START id=aa78525fb574_c020 start_line=5701 end_line=6000
````markdown
3. Executa passos atômicos → atualiza `STATE.md`.
4. Ao concluir: `✅ Spec passed. Deseja arquivar a spec e sincronizar o JOURNAL.md?`

---
> *Este documento garante que o "Cérebro" (Contexto) e o "Músculo" (TLC) operem em harmonia.*

```
CHUNK_END id=450d7ec70909_c001
FILE_END id=file_450d7ec70909

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.800876+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=9b6470da8849_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=9b6470da8849_c001
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=23 bytes=1082 mtime=2026-04-11T01:25:28.436758+00:00 sha1=43293ddbefe17288e0cea85c402cff9f4ed05cea
CHUNK_START id=019509328844_c001 start_line=1 end_line=23
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# JOURNAL.md
> Log vivo de decisoes e bugs. (Max 600 linhas)

## 📅 2026-04-11 01:25
**Decisão/Bug:** 🔄 Handoff: @frontend-specialist → @backend-engineer
**Solução:** Implementada UI do CheckoutForm v1 usando Stripe Elements. Estado local gerenciado; aguardando API `/api/checkout/session`.
**Implicação:** Próximo agente deve configurar a rota backend e garantir o retorno do `clientSecret`.

## 📅 2026-04-11 01:35
**Decisão/Bug:** 🔄 Handoff: @backend-engineer → @qa-validator
**Solução:** Endpoint Stripe Session operacional. Webhook configurado para escutar `payment_intent.succeeded` e atualizar tabela `orders`.
**Implicação:** QA deve validar fluxos de falha e idempotência do webhook.

## 📅 2026-04-11 01:45
**Decisão/Bug:** ✅ Ciclo Checkout Stripe Concluído
**Solução:** Cobertura de testes em 92%. Validado happy path e 'card declined'. Injetado retry pattern no webhook.
**Implicação:** PRD #15 concluído. Tecnologias Stripe adicionadas ao env.

```
CHUNK_END id=019509328844_c001
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=13 bytes=286 mtime=2026-04-11T01:26:25.980990+00:00 sha1=26974391beb474138a05628058c4c0c9010cdf07
CHUNK_START id=d069d4f2ebef_c001 start_line=1 end_line=13
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

<!-- AUTO-SYNC START -->
*🤖 Atualizado automaticamente em 2026-04-10 22:26*

### DevDependencies
- `husky`: `^9.1.7`

### Tabelas no Schema (schema.sql)
- `orders`

<!-- AUTO-SYNC END -->


```
CHUNK_END id=d069d4f2ebef_c001
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.794384+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=0858a02cf53f_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=0858a02cf53f_c001
FILE_END id=file_0858a02cf53f

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CHUNK_START id=a5c71962029a_c001 start_line=1 end_line=63
````markdown
---
Criado em: 2026-04-10 21:44
Ultima Atualizacao: 2026-04-10 21:44
Status: Ativo
---

# 🛠️ Manual de Reconstrução & Automação

Este guia contém as instruções para subir o ambiente do zero e operar as ferramentas de governança de contexto.

---

## 🏗️ 1. Setup do Ambiente

### Requisitos Mínimos:
- **Python ≥ 3.8** (Para os scripts de automação)
- **Node.js** (Para os wrappers NPM)
- **Make** (Opcional, para orquestração Unix)
- **Bash** (Para Git Bash, WSL, Linux ou macOS)

---

## ⚙️ 2. Ferramentas de Automação

O projeto oferece três formas de gerenciar a saúde do contexto. Escolha a que melhor se adapta ao seu terminal:

### Opção A: Via NPM (Recomendado para Devs Web)
```bash
npm run context:validate  # Checa integridade e tokens
npm run context:sync      # Sincroniza deps e schema
npm run context:purge     # Limpa e arquiva o log vivo
```

### Opção B: Via Make (Recomendado para CI/CD e Unix)

````
CHUNK_END id=aa78525fb574_c027
CHUNK_START id=aa78525fb574_c028 start_line=8101 end_line=8400
````markdown
```bash
make validate
make sync
make purge
make all       # Executa o pipeline completo: Valida -> Sync -> Purge
```

### Opção C: Via Bash (Resiliência Universal)
```bash
./run_context.sh validate
./run_context.sh all
```

---

## 🗃️ 3. Recuperação de Contexto (Archive)

Se precisar restaurar um Journal ou PRD antigo que foi arquivado:
1. Vá até `.context/maintenance/_archive_context/`.
2. Localize o arquivo pelo timestamp `YYYYMMDD_HHMMSS`.
3. Copie o conteúdo necessário de volta para a raiz da camada correspondente (`maintenance/` ou `brain/`).

---

## 🚨 4. Troubleshooting
- **Erro de Encoding (Windows):** Todos os scripts são forçados para UTF-8. Se vir caracteres estranhos, verifique se o seu terminal suporta Unicode.
- **Python não encontrado:** No Windows, o script tenta `python3` e faz fallback para `python`. Se falhar, certifique-se que o executável está no seu PATH.

> *Lembrete: Sem automação, a documentação morre. Use as ferramentas a cada nova funcionalidade iniciada no ROADMAP.md.*

````
CHUNK_END id=a5c71962029a_c001
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=27 bytes=1336 mtime=2026-04-11T02:26:43.636538+00:00 sha1=adb37745498ccfa61a2b793c10240a2b20d3d716
CHUNK_START id=54a6a553d34b_c001 start_line=1 end_line=27
```markdown
---
Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-10 23:27
Status: Ativo
---

# 🧬 rx-anatomy.md (Raio-X de Anatomia)
> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Arquivos de decisão e regras
│   ├── maintenance/        # Logs, db schema e inventários
│   └── monitoring/         # Dashboard de saúde
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.sh          # Orquestrador universal Bash
├── init_ai_project.sh      # Bootstrapper supremo
└── package.json            # Gerenciamento de libs e scripts context:*

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `_archive_context/specs/`
- **Não é fonte da verdade.** O `.context/` permanece como SSOT.

```
CHUNK_END id=54a6a553d34b_c001
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=1 bytes=93 mtime=2026-04-10T23:54:29.789386+00:00 sha1=6ce5abcb8d49b1e31f741778b50586f3cb5c2e24
CHUNK_START id=ca8da4f87431_c001 start_line=1 end_line=1
```markdown
---\nCriado em: 2026-04-10 20:50\nUltima Atualizacao: 2026-04-10 20:50\nStatus: Ativo\n---\n

```
CHUNK_END id=ca8da4f87431_c001
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CHUNK_START id=91d5627a725e_c001 start_line=1 end_line=9
```sql
-- Snapshot Real da Tabela de Pedidos
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_session_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending', -- pending, succeeded, failed
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
CHUNK_END id=91d5627a725e_c001
FILE_END id=file_91d5627a725e

---

````
CHUNK_END id=aa78525fb574_c012
CHUNK_START id=aa78525fb574_c013 start_line=3601 end_line=3900
````markdown
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1624 mtime=2026-04-10T23:50:11.304033+00:00 sha1=92934bdfcac044ab34842a1b0131524ead5e2e5b
CHUNK_START id=068a21d64bec_c001 start_line=1 end_line=38
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

| Métrica | Valor Atual| Limite / Heurística | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Pilar de Manutenção** | | | | |
| JOURNAL.md (linhas) | 412 | 600 | Manutenção | ✅ OK |
| JOURNAL.md (tamanho) | ~12k char | 50k char | Manutenção | ✅ OK |
| **Pilar Cognitivo** | | | | |
| Role Ativa | @frontend-specialist | N/A | Cognitivo | ⚠️ Em Task |
| PRD Ativo | #14 - Auth Flows | 1 por vez | Cognitivo | ✅ OK |
| **Pilar de Consistência** | | | | |
| Schema vs PRD Sync | 0 divergências | 0 | DB-First | ✅ OK |
| Último Sincronismo | 2h atrás | < 24h | Governança | ✅ OK |
| **Pilar de Sessão** | | | | |
| Turns de Sessão | 8 trocas | 20 trocas | Sessão | ✅ OK |
| Token Window Est. | ~78k | 128k | Sessão | ⚠️ 80% |

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até que a migration seja documentada.
- **Se Turns > 18:** Propor Snapshot ou Reset de Sessão antes de iniciar próxima tarefa grande.

---

## 📅 Histórico de Saúde (Log de Purges)
| Data | Ação | Agente | Resultado |
| :--- | :--- | :--- | :--- |
| 2026-04-10 | Purge Completo | @context-keeper | Journal resetado para seed de 30 linhas. |

```
CHUNK_END id=068a21d64bec_c001
FILE_END id=file_068a21d64bec

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=26 bytes=693 mtime=2026-04-11T00:55:20.246274+00:00 sha1=163dd12b4c98d348f80986ea59afcb4604dc9e0e
CHUNK_START id=e477c4c5a96c_c001 start_line=1 end_line=26
```yaml
name: Context Health Check

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  validate-context:

````
CHUNK_END id=aa78525fb574_c005
CHUNK_START id=aa78525fb574_c006 start_line=1501 end_line=1800

````
CHUNK_END id=aa78525fb574_c020
CHUNK_START id=aa78525fb574_c021 start_line=6001 end_line=6300
````markdown
````markdown
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run Context Validation
        # No GitHub Actions (Linux), usamos python3
        run: python3 .context/_scripts/validate_context.py

      - name: Check Journal Limits
        run: python3 .context/_scripts/validate_context.py | grep -q "SUCCESS" || (echo "❌ Contexto quebrado ou Journal excedido!" && exit 1)

```
CHUNK_END id=e477c4c5a96c_c001
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CHUNK_START id=3adfd36c1559_c001 start_line=1 end_line=9
```bash
echo "husky - DEPRECATED

Please remove the following two lines from $0:

#!/usr/bin/env sh
. \"\$(dirname -- \"\$0\")/_/husky.sh\"

They WILL FAIL in v10.0.0
"
```
CHUNK_END id=3adfd36c1559_c001
FILE_END id=file_3adfd36c1559

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=68 bytes=2890 mtime=2026-04-11T02:30:31.368152+00:00 sha1=ea66d1b4ed6f174f17b752f28ac358093fb784d2
CHUNK_START id=8ec9a00bfd09_c001 start_line=1 end_line=68
````markdown
# 🛸 Antigravity Kit v2.2 Premium+
> **O ecossistema definitivo para engenharia AI-Ready: Governança Macro + Execução Atômica.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação (GitHub Copilot, Cursor, Antigravity). Ele unifica o **Antigravity Kit** (Governança Macro) com o **TLC Spec-Driven** (Execução Atômica), garantindo que o Propósito (PRD) se transforme em Ação (Código) com precisão cirúrgica.

---

## 🧠 A Filosofia: "Se não está no Contexto, não existe."

Neste framework, a pasta `.context/` é a **Single Source of Truth (SSOT)**. A pasta `.specs/` é o seu **Workshop Efêmero**. O código é apenas o reflexo físico da inteligência documentada.

## 🚀 Instalação Ultra-Rapida (One-Click Setup)

Se voce quer inicializar este framework em um novo projeto do zero, basta rodar o nosso bootstrapper supremo:

```bash
# 1. Torne o script executavel
chmod +x init_ai_project.sh

# 2. Execute
./init_ai_project.sh
```

O script ira criar automaticamente toda a estrutura de camadas, os workshops de execução, os motores de manutenção v2.2+, e configurar a blindagem Husky.

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. PRD v2.0, Rules, Registry e a Ponte de Integração TLC.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação

| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Verifica a integridade dos arquivos e a estrutura do workshop. |
| `npm run context:sync`     | Sincroniza `TECHNICAL_REQUIREMENTS.md` com dependências e DB. |
| `npm run context:cleanup`  | Gerencia a efemeridade do `.specs/` (Arquiva specs obsoletas). |
| `npm run context:all`      | Pipeline completo de saúde e manutenção. |

---

## 🤝 Protocolo de Ativação Híbrida

Para iniciar uma tarefa com poder total, use o prompt mestre:
> *"Inicie a fase de SPECIFY para o PRD #[ID] usando o modo Híbrido TLC."*

Isso ativará a role `@spec-driver` e iniciará o ciclo atômico no `.specs/` alinhado à governança do `.context/`.

---

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*

````
CHUNK_END id=8ec9a00bfd09_c001
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=114 bytes=4693 mtime=2026-04-11T01:41:16.589576+00:00 sha1=69a61b75c7697979c8e4ab560e0325f71bd7151d
CHUNK_START id=4efb6293109d_c001 start_line=1 end_line=114

````
CHUNK_END id=aa78525fb574_c028
CHUNK_START id=aa78525fb574_c029 start_line=8401 end_line=8700
````markdown
````markdown
---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-10 22:45
Status: Ativo
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria viva, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.sh`, `Makefile` | Validacao, purge, sync e orquestracao. |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `tests/test_context.py` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija antes de forcar.

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rapidos (Cheat Sheet)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Sincronizar deps e schema com TECH_REQUIREMENTS.md
npm run context:sync

# Arquivar 70% do journal (mantem 30% como semente)
npm run context:purge

# Pipeline completo (validate -> sync -> purge)
npm run context:all

# Rodar testes do framework manualmente (Universal Python)
npm run context:test
```
> 💡 *Fallbacks:* `make all` ou `bash run_context.sh all`

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se `validate_context.py` ou `test_context.py` falharem.
- **CI/CD:** O GitHub Actions roda o pipeline em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Clone
- [ ] `.context/` existe com estrutura de camadas ok.
- [ ] `brain/RULES.md` e `brain/MASTER_FLOW.md` alinhados a stack.
- [ ] `brain/AGENT_REGISTRY.md` possui roles registradas.
- [ ] `npm run context:all` executa sem erros.

### 🚀 Inicio de Feature / PRD
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---


````
CHUNK_END id=aa78525fb574_c013
CHUNK_START id=aa78525fb574_c014 start_line=3901 end_line=4200
````markdown
> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.

````
CHUNK_END id=4efb6293109d_c001
FILE_END id=file_4efb6293109d

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=380 bytes=15778 mtime=2026-04-11T02:41:35.553852+00:00 sha1=af470185afa6c524f7b949d0246c80164bcce678
CHUNK_START id=c3916196f58f_c001 start_line=1 end_line=300
```python
#!/usr/bin/env python3
"""captura_projeto.py - Gera bundle markdown AI-first do repositorio. TEMPLATE UNIVERSAL."""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path

# 🛠️ CUSTOMIZE AQUI: Padrões universais + adicione os específicos do seu projeto
PASTAS_IGNORAR = {
    ".git", "node_modules", "dist", "build", "out", "target", "bin", "obj",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache",
    ".next", ".nuxt", ".vercel", ".netlify", ".vite", ".cache",
    ".vscode", ".idea", ".cursor", "coverage", ".pytest_cache",
    "captura_projeto", # 📝 Ignorar a própria pasta do utilitário
}

PASTAS_CORE = {
    # 📝 Defina as pastas ARQUITETURALMENTE essenciais para a IA entender seu projeto
    # Ex: {"src", "lib", "api", "supabase", ".context", ".specs"}
    "src", "lib", "api", ".context", ".specs"
}

# 🛠️ CUSTOMIZE AQUI: Regras de classificação semântica (fallback seguro)
DOMAIN_RULES = {
    r"/api/|/routes/|/handlers/|/controllers/": "api",
    r"/components/|/ui/|/views/|/pages/|/screens/": "ui",
    r"/lib/|/utils/|/helpers/|/core/|/shared/": "lib",
    r"/db/|/migrations/|/models/|/schema/|/supabase/|/prisma/": "db",
    r"/tests/|/spec/|/__tests__/|\.test\.|\.spec\.": "tests",
    r"/config/|/settings/|/env/": "config",
    r"\.md$|\.rst$|\.txt$": "docs",
    r"\.(json|toml|yaml|yml|ini)$": "config",
}

EXTENSOES_PERMITIDAS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".html", ".css", ".json", ".md",
    ".yaml", ".yml", ".toml", ".sh", ".sql", ".graphql", ".vue", ".svelte",
    ".rs", ".go", ".java", ".c", ".h", ".hpp", ".cpp", ".ini",
}

````
CHUNK_END id=aa78525fb574_c021
CHUNK_START id=aa78525fb574_c022 start_line=6301 end_line=6600
````markdown

LINGUAGENS = {
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".py": "python", ".html": "html", ".css": "css", ".json": "json", ".md": "markdown",
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".sh": "bash", ".sql": "sql",
    ".graphql": "graphql", ".vue": "html", ".svelte": "html", ".rs": "rust",

````
CHUNK_END id=aa78525fb574_c006
CHUNK_START id=aa78525fb574_c007 start_line=1801 end_line=2100
````markdown
    ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".hpp": "cpp", ".cpp": "cpp", ".ini": "ini",
}

ARQUIVOS_SENSIVEIS_GLOBS = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx",
    "credentials*.json", "id_rsa*", "secrets.*", "*.cert",
    # 📝 Adicione padrões sensíveis do SEU projeto aqui
}

SECRET_PATTERNS = (
    re.compile(r'(["\']?)(\w*(?:API_KEY|SECRET|TOKEN|PASSWORD|AUTH_KEY|PRIVATE_KEY|ACCESS_KEY|DB_PASS|CONNECTION_STRING)\w*)\1\s*[:=]\s*["\']?(\S+)["\']?', re.IGNORECASE),
    re.compile(r'(BEGIN\s+(RSA|EC|DSA|OPENSSH|PGP)\s+PRIVATE\s+KEY)', re.IGNORECASE),
)

DEFAULT_OUTPUT = "contexto.md"
logging.basicConfig(level=logging.WARNING, format="⚠️ %(message)s")

@dataclass(frozen=True)
class BundleConfig:
    diretorio: Path
    output: str = DEFAULT_OUTPUT
    only_core: bool = False
    exclude_core: bool = False
    profile: str = "ai-default"
    toc_only: bool = False
    max_lines_per_file: int = 300
    emit_symbol_index: bool = False
    emit_import_map: bool = False
    mask_secrets: bool = False

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_line: int
    end_line: int
    content: str

@dataclass(frozen=True)
class FileRecord:
    file_id: str
    relative_path: str
    domain: str
    language: str
    line_count: int
    byte_count: int
    mtime_utc: str
    sha1: str
    symbols: tuple[str, ...]
    imports: tuple[str, ...]
    chunks: tuple[Chunk, ...]

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXTENSOES_PERMITIDAS:
        return True
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        return False
    return mime.startswith("text/") or mime in {"application/json", "application/xml", "application/javascript"}

def is_sensitive_file(path: Path) -> bool:
    return any(fnmatch(path.name.lower(), pat.lower()) for pat in ARQUIVOS_SENSIVEIS_GLOBS)

def classify_domain(relative_path: str) -> str:
    p = relative_path.lower()
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, p):
            return domain
    return "source"

def should_include_profile(record_domain: str, config: BundleConfig) -> bool:
    if config.profile == "ai-compact":
        return record_domain not in {"tests", "docs"}
    return True

def mask_sensitive(content: str, enabled: bool) -> str:
    if not enabled:
        return content
    out = content
    for pattern in SECRET_PATTERNS:
        out = pattern.sub(r"\1***", out)
    return out

def extract_symbols(content: str, suffix: str) -> tuple[str, ...]:
    symbols: list[str] = []
    if suffix == ".py":
        symbols.extend(re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content, re.MULTILINE))
        symbols.extend(re.findall(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        symbols.extend(re.findall(r"(?:export\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content))
        symbols.extend(re.findall(r"(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\s*", content))
        symbols.extend(re.findall(r"export\s+const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", content))
    seen, seen_set = [], set()
    for s in symbols:
        if s not in seen_set:
            seen.append(s)
            seen_set.add(s)
    return tuple(seen[:80])

def extract_imports(content: str, suffix: str) -> tuple[str, ...]:
    imports: list[str] = []
    if suffix == ".py":
        imports.extend(re.findall(r"^import\s+([^\n]+)", content, re.MULTILINE))
        imports.extend(re.findall(r"^from\s+([^\s]+)\s+import\s+([^\n]+)", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        imports.extend(re.findall(r"^import\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]", content, re.MULTILINE))
        imports.extend(re.findall(r"require\(['\"]([^'\"]+)['\"]\)", content))

````
CHUNK_END id=aa78525fb574_c029
CHUNK_START id=aa78525fb574_c030 start_line=8701 end_line=9000
````markdown
    normalized, seen_set = [], set()
    for item in imports:
        val = f"from {item[0]} import {item[1]}" if isinstance(item, tuple) else item
        if val not in seen_set:
            normalized.append(val)
            seen_set.add(val)
    return tuple(normalized[:120])

def chunk_content(content: str, file_id: str, max_lines: int) -> tuple[Chunk, ...]:
    lines = content.splitlines()
    if not lines:
        return (Chunk(f"{file_id}_c001", 1, 1, ""),)
    if max_lines <= 0 or len(lines) <= max_lines:
        return (Chunk(f"{file_id}_c001", 1, len(lines), content),)
    chunks = []
    idx = 1
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        part = "\n".join(lines[start:end])
        if end < len(lines) or content.endswith("\n"):
            part += "\n"
        chunks.append(Chunk(f"{file_id}_c{idx:03d}", start + 1, end, part))
        idx += 1
    return tuple(chunks)

def make_file_id(relative_path: str) -> str:
    return hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:12]

def collect_files(config: BundleConfig) -> tuple[FileRecord, ...]:
    records: list[FileRecord] = []
    root = config.diretorio.resolve()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        is_root = (current == root)

        if config.only_core:
            dirnames[:] = sorted(d for d in dirnames if (d in PASTAS_CORE or not is_root) and d not in PASTAS_IGNORAR)
        elif config.exclude_core:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_CORE and d not in PASTAS_IGNORAR)
        else:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_IGNORAR)

        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root)
            rel_path = rel.as_posix()
            top = rel.parts[0] if rel.parts else ""

            if config.only_core and is_root and top not in PASTAS_CORE:
                continue
            if config.exclude_core and is_root and top in PASTAS_CORE:
                continue
            if is_sensitive_file(path):
                continue
            if not is_text_file(path):
                continue

            try:
                raw_content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    raw_content = path.read_text(encoding="latin-1")
                except OSError as e:
                    logging.warning("Pulando %s: %s", rel_path, e)
                    continue
            except OSError as e:
                logging.warning("Pulando %s: %s", rel_path, e)
                continue

            domain = classify_domain(rel_path)
            if not should_include_profile(domain, config):
                continue

            raw_sha1 = hashlib.sha1(raw_content.encode("utf-8", errors="ignore")).hexdigest()
            content = mask_sensitive(raw_content, config.mask_secrets)
            file_id = make_file_id(rel_path)
            stat = path.stat()
            suffix = path.suffix.lower()

            symbols = extract_symbols(content, suffix) if config.emit_symbol_index else ()
            imports = extract_imports(content, suffix) if config.emit_import_map else ()
            chunks = chunk_content(content, file_id, config.max_lines_per_file)

            records.append(FileRecord(
                file_id=file_id, relative_path=rel_path, domain=domain,
                language=LINGUAGENS.get(suffix, suffix[1:] if suffix else "text"),
                line_count=len(content.splitlines()),
                byte_count=len(content.encode("utf-8", errors="ignore")),
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                sha1=raw_sha1, symbols=symbols, imports=imports, chunks=chunks
            ))

    records.sort(key=lambda r: r.relative_path)
    return tuple(records)

def mode_name(config: BundleConfig) -> str:
    if config.only_core: return "only-core"
    if config.exclude_core: return "exclude-core"
    return "full"

def render_frontmatter(config: BundleConfig, records: tuple[FileRecord, ...]) -> str:
    total_bytes = sum(r.byte_count for r in records)
    lines = [
        "---", "schema_version: 1",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"root: {config.diretorio.resolve().name}",
        f"mode: {mode_name(config)}", f"profile: {config.profile}",
        f"file_count: {len(records)}", f"byte_count: {total_bytes}",
        "ignored_dirs:"
    ]
    lines.extend(f"  - {d}" for d in sorted(PASTAS_IGNORAR))
    lines.append("sensitive_rules:")
    lines.extend(f"  - {r}" for r in sorted(ARQUIVOS_SENSIVEIS_GLOBS))
    lines.append("---")
    return "\n".join(lines)

def render_index_by_domain(records: tuple[FileRecord, ...]) -> str:
    grouped: dict[str, list[FileRecord]] = {}
    for r in records:
        grouped.setdefault(r.domain, []).append(r)
    lines = ["## INDEX_BY_DOMAIN"]

````
CHUNK_END id=aa78525fb574_c014
CHUNK_START id=aa78525fb574_c015 start_line=4201 end_line=4500
````markdown
    for domain in sorted(grouped):
        lines.append(f"- `{domain}`:")
        lines.extend(f"  - `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in grouped[domain])
    return "\n".join(lines)

def render_index_by_path(records: tuple[FileRecord, ...]) -> str:
    lines = ["## INDEX_BY_PATH"]
    lines.extend(f"- `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in records)
    return "\n".join(lines)

def render_symbols(records: tuple[FileRecord, ...]) -> str:
    lines = ["## SYMBOL_INDEX"]
    for r in records:
        if not r.symbols: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{s}`" for s in r.symbols)
    return "\n".join(lines)


```
CHUNK_END id=c3916196f58f_c001
CHUNK_START id=c3916196f58f_c002 start_line=301 end_line=380
````python
def render_imports(records: tuple[FileRecord, ...]) -> str:
    lines = ["## IMPORT_MAP_MIN"]
    for r in records:
        if not r.imports: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{i}`" for i in r.imports)
    return "\n".join(lines)

def pick_fence(content: str) -> str:
    return "````" if "```" in content else "```"

def render_file_record(record: FileRecord, toc_only: bool) -> str:
    lines = [
        "---", f'<a id="file_{record.file_id}"></a>',
        f"FILE_START id=file_{record.file_id} path={record.relative_path} "
        f"domain={record.domain} lang={record.language} lines={record.line_count} "
        f"bytes={record.byte_count} mtime={record.mtime_utc} sha1={record.sha1}"
    ]
    if toc_only:
        lines.append("CONTENT_OMITTED toc_only=true")
    else:
        for chunk in record.chunks:
            lines.append(f"CHUNK_START id={chunk.chunk_id} start_line={chunk.start_line} end_line={chunk.end_line}")
            fence = pick_fence(chunk.content)
            lines.extend([f"{fence}{record.language}", chunk.content, fence, f"CHUNK_END id={chunk.chunk_id}"])
    lines.append(f"FILE_END id=file_{record.file_id}")
    return "\n".join(lines)

def generate_context_markdown(config: BundleConfig) -> str:
    if config.only_core and config.exclude_core:
        raise ValueError("only_core e exclude_core nao podem ser usados juntos")
    
    records = collect_files(config)

````
CHUNK_END id=aa78525fb574_c022
CHUNK_START id=aa78525fb574_c023 start_line=6601 end_line=6900
````markdown
    blocks = ["# Project Context Bundle", "", render_frontmatter(config, records), "",
              render_index_by_domain(records), "", render_index_by_path(records)]
    if config.emit_symbol_index:
        blocks.extend(["", render_symbols(records)])
    if config.emit_import_map:
        blocks.extend(["", render_imports(records)])
    for r in records:
        blocks.extend(["", render_file_record(r, toc_only=config.toc_only)])
    return "\n".join(blocks) + "\n"

def write_output(config: BundleConfig) -> Path:
    output_path = config.diretorio / config.output
    content = generate_context_markdown(config)
    output_path.write_text(content, encoding="utf-8")
    return output_path


````
CHUNK_END id=aa78525fb574_c007
CHUNK_START id=aa78525fb574_c008 start_line=2101 end_line=2400
````markdown
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="captura_projeto.py - Consolida repositorio em markdown AI-first")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretorio raiz")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Arquivo de saida")
    core = parser.add_mutually_exclusive_group()
    core.add_argument("--only-core", action="store_true", help="Inclui apenas escopo core")
    core.add_argument("--exclude-core", action="store_true", help="Exclui escopo core")
    parser.add_argument("--profile", choices=["ai-default", "ai-compact", "ai-forensics"], default="ai-default")
    parser.add_argument("--toc-only", action="store_true", help="Apenas indices e envelopes")
    parser.add_argument("--max-lines-per-file", type=int, default=300, help="Limite de linhas por chunk (0=ilimitado)")
    parser.add_argument("--emit-symbol-index", action="store_true", help="Adiciona SYMBOL_INDEX")
    parser.add_argument("--emit-import-map", action="store_true", help="Adiciona IMPORT_MAP_MIN")
    parser.add_argument("--mask-secrets", action="store_true", help="Ofusca segredos no conteudo")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = BundleConfig(
        diretorio=Path(args.diretorio), output=args.output,
        only_core=args.only_core, exclude_core=args.exclude_core,
        profile=args.profile, toc_only=args.toc_only,
        max_lines_per_file=args.max_lines_per_file,
        emit_symbol_index=args.emit_symbol_index,
        emit_import_map=args.emit_import_map, mask_secrets=args.mask_secrets
    )
    out = write_output(config)
    print(f"\n✅ Gerado: {out}")
    print(f"   Mode: {mode_name(config)} | Profile: {config.profile}")

if __name__ == "__main__":
    main()
````
CHUNK_END id=c3916196f58f_c002
FILE_END id=file_c3916196f58f

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=155 bytes=5469 mtime=2026-04-11T02:29:46.289656+00:00 sha1=18e30807c6ef1ce94e3619f19f8ec2bd93f77c52
CHUNK_START id=c59135753d26_c001 start_line=1 end_line=155
```bash
#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.2 Premium+)
# -----------------------------------------------------------------------------
# Versão Suprema: Fusão Antigravity + TLC Spec-Driven.
# Com detecção automática de gerenciador e motores de manutenção completos.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  command -v python3 >/dev/null 2>&1 || PYTHON="python3"
  command -v python >/dev/null 2>&1 || PYTHON="python"
  [ -z "${PYTHON:-}" ] && error "python3 ou python e obrigatorio."
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity AI-Ready Framework v2.2 Premium+..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop TLC..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}

````
CHUNK_END id=aa78525fb574_c030
CHUNK_START id=aa78525fb574_c031 start_line=9001 end_line=9300
````markdown
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança e integração TLC..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit + TLC Fusion)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT). O workshop \`.specs\` e o espaco de execucao efemera.

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo e handoffs.
- .specs/: Workbench atômico (Regra de 48h/Max 3).

🔄 4. Gatilhos Operacionais
- "Inicie a fase de SPECIFY para o PRD #[ID]": IA cria spec atômica no .specs/.
- "Atualize contexto": Sincronizacao proativa via sync_project.py.
EOF

cat > .context/brain/TLC_INTEGRATION.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 🔗 TLC_INTEGRATION.md
Ponte entre Governança (.context/) e Execução Atômica (.specs/).

## 🔄 Ciclo de Vida Híbrido
1. INTENT -> PRD.md ativo define escopo.
2. SPECIFY -> IA cria .specs/features/[nome]/spec.md.
3. IMPLEMENT -> Geração de código baseada na spec.
4. VERIFY -> STATE.md marcado como ✅ PASSED.
5. SYNC -> Lições para o JOURNAL.md e limpeza da spec.
EOF

# (Injeção dos Motores Reais v2.2 Premium+)
cat > .context/_scripts/validate_context.py << 'EOF'
#!/usr/bin/env python3
import os, sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQUIRED = ["brain/RULES.md", "brain/PRD.md", "maintenance/JOURNAL.md"]
def check_specs():
    specs = CONTEXT_DIR.parent / ".specs/features"
    if not specs.exists(): return True
    return all((d / "STATE.md").exists() for d in specs.iterdir() if d.is_dir())
def validate():
    print("--- Validacao v2.2 Premium+ ---")
    missing = [f for f in REQUIRED if not (CONTEXT_DIR / f).exists()]
    if missing or not check_specs(): sys.exit(1)
    print("✅ Contexto e Workshop integros.")
if __name__ == "__main__": validate()
EOF

cat > .context/_scripts/cleanup_specs.py << 'EOF'
#!/usr/bin/env python3
import os, shutil, time
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
SPECS_DIR = SCRIPT_DIR.parent.parent / ".specs" / "features"
ARCHIVE_DIR = SCRIPT_DIR.parent / "maintenance" / "_archive_context" / "specs"
def cleanup():
    if not SPECS_DIR.exists(): return
    specs = sorted([d for d in SPECS_DIR.iterdir() if d.is_dir()], key=os.path.getmtime)
    while len(specs) > 3:
        shutil.move(str(specs.pop(0)), str(ARCHIVE_DIR))
    print("[OK] Manutencao de specs concluida.")
if __name__ == "__main__": cleanup()
EOF

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
const runner = '$PKG_MGR' === 'npm' ? 'npm run' : '$PKG_MGR';
Object.assign(pkg.scripts, {
  'context:validate': 'bash run_context.sh validate',
  'context:cleanup': 'bash run_context.sh cleanup',
  'context:all': runner + ' context:validate && ' + runner + ' context:cleanup',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:validate" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."

```
CHUNK_END id=c59135753d26_c001
FILE_END id=file_c59135753d26

---
<a id="file_fa288d1472d2"></a>
FILE_START id=file_fa288d1472d2 path=package-lock.json domain=config lang=json lines=32 bytes=785 mtime=2026-04-11T01:12:03.334672+00:00 sha1=e8450c2eeca43eabd30597b19a6cb24ad70fcddb
CHUNK_START id=fa288d1472d2_c001 start_line=1 end_line=32
```json
{
  "name": "template-ai-context-governance",
  "version": "2.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "template-ai-context-governance",
      "version": "2.0.0",
      "license": "MIT",
      "devDependencies": {
        "husky": "^9.1.7"
      }
    },
    "node_modules/husky": {
      "version": "9.1.7",
      "resolved": "https://registry.npmjs.org/husky/-/husky-9.1.7.tgz",
      "integrity": "sha512-5gs5ytaNjBrh5Ow3zrvdUUY+0VxIuWVL4i9irt6friV+BqdCfmV11CQTWMiBYWHbXhco+J1kHfTOUkePhCDvMA==",

````
CHUNK_END id=aa78525fb574_c015
CHUNK_START id=aa78525fb574_c016 start_line=4501 end_line=4800
````markdown
      "dev": true,
      "license": "MIT",
      "bin": {
        "husky": "bin.js"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/typicode"
      }
    }
  }
}

```
CHUNK_END id=fa288d1472d2_c001
FILE_END id=file_fa288d1472d2

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=24 bytes=735 mtime=2026-04-11T02:41:48.186770+00:00 sha1=6f0d247a0f4e8dd35e8359d4399b2ddbe60eabca
CHUNK_START id=7030d0b2f71b_c001 start_line=1 end_line=24
```json
{
  "name": "template-ai-context-governance",
  "version": "2.0.0",
  "description": "AI-Ready Template with Context Governance Framework",
  "scripts": {
    "context:validate": "bash run_context.sh validate",
    "context:cleanup": "bash run_context.sh cleanup",
    "context:capture": "python captura_projeto.py --emit-symbol-index --emit-import-map",
    "context:all": "npm run context:validate && npm run context:cleanup && npm run context:capture",
    "context:help": "echo \"Comandos: validate | purge | sync | all\"",
    "prepare": "husky"
  },
  "keywords": [
    "ai",
    "context",
    "governance",
    "template"
  ],
  "author": "TalesAvancini",
  "license": "MIT",
  "devDependencies": {
    "husky": "^9.1.7"
  }
}

```
CHUNK_END id=7030d0b2f71b_c001

````
CHUNK_END id=aa78525fb574_c023
CHUNK_START id=aa78525fb574_c024 start_line=6901 end_line=7200
````markdown
FILE_END id=file_7030d0b2f71b

---
<a id="file_a9422a4b7476"></a>
FILE_START id=file_a9422a4b7476 path=planos/implementation_plan.md domain=docs lang=markdown lines=77 bytes=3338 mtime=2026-04-10T23:15:28.184032+00:00 sha1=37ad3605aae584ee4398621d92edd7b76058413e
CHUNK_START id=a9422a4b7476_c001 start_line=1 end_line=77
```markdown
# 🏛️ Plano de Expansão: Context Governance Framework (v2.0)

Este plano detalha a transição do template de um sistema de documentação estática para um framework de governança ativa, focado em **escala**, **automação** e **prevenção de drift**.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Automação em Python e Escala de Contexto
- **Status:** Aguardando Aprovação

---

## 🧩 1. Estrutura de Arquivos Ampliada

Vamos expandir a pasta `.context/` para incluir novas camadas de inteligência:

### [NEW] Novos Documentos de Governança
- **`PROMPT_LIBRARY.md`**: Catálogo de personas e templates de prompts específicos para garantir consistência entre sessões.
- **`SESSION_MANAGER.md`**: Regras de gerenciamento de janela de tokens, limites de sessão e snapshots de resumo.
- **`CONTEXT_HEALTH.md`**: Dashboard de saúde do contexto (métricas de linhas, divergências e obsolescência).

````
CHUNK_END id=aa78525fb574_c008
CHUNK_START id=aa78525fb574_c009 start_line=2401 end_line=2700
````markdown
- **`AGENT_REGISTRY.md`**: Definição de papéis (Expertises) e permissões de escrita/leitura nos arquivos do contexto.

---

## 📜 2. Atualização dos Protocolos (`RULES.md`)

Injetaremos novos protocolos de segurança e eficiência no arquivo de leis do agente:

### 🔹 Context Gate (Validação Pré-Voo)
O Agente deve realizar um "Checklist de Integridade" antes de gerar código, validando se o PRD e o Schema estão sincronizados.

### 🔹 Session Budget (Gestão de Tokens)
Definição de limites claros: ao atingir 80% da janela de contexto (estimada), o agente **deve** realizar um purge do `JOURNAL.md` (via script) e gerar um resumo semente.

---

## 🛠️ 3. Automação com Python (`.context/_scripts/`)

Criaremos scripts em Python para tornar a governança ativa e independente do ambiente da IDE.

### #### [NEW] `validate_context.py`
- Verifica se o `schema.sql` contém os campos referenciados no PRD atual.
- Valida o limite de linhas do `JOURNAL.md`.
- Gera um alerta visual se o status em qualquer arquivo for `Stale` ou `Deprecated`.

### #### [NEW] `purge_journal.py`
- Executa a lógica de arquivamento: move os primeiros 70% do log para `_archive_context/journals/`.
- Mantém os 30% finais e insere um resumo gerado pela IA no topo como conexão lógica.

### #### [NEW] `init_context.py`
- Script de bootstrap que inicializa a estrutura em novos projetos, gera os metadados de tempo reais e cria o `schema.sql` inicial.

---

## 📈 4. Monitoramento (`CONTEXT_HEALTH.md`)

Criação do dashboard dinâmico que será atualizado periodicamente pelos scripts ou manualmente pela IA.

| Métrica | Limite | Ação em caso de Falha |
| :--- | :--- | :--- |
| JOURNAL size | 600 linhas | Trigger `purge_journal.py` |
| PRD sync | 100% | Bloqueio de geração de UI |
| Token Window | 128k (80%) | Trigger Snapshot de Sessão |

---

## 🚦 Próximos Passos (Workflow)

1.  **Aprovação do Plano** (Você).
2.  **Criação dos Arquivos MD** com os templates propostos.
3.  **Geração do Código Python** para cada script de automação.
4.  **Atualização do `MASTER_FLOW.md` e `RULES.md`** para refletir a nova arquitetura.
5.  **Validação Final** da estrutura completa.

---

> [!IMPORTANT]
> A implementação será feita de forma **não invasiva** e **não executável** conforme solicitado, apenas preparando o repositório para ser exportado para o GitHub.

```
CHUNK_END id=a9422a4b7476_c001
FILE_END id=file_a9422a4b7476

---
<a id="file_32db3e3783df"></a>
FILE_START id=file_32db3e3783df path=planos/master_plan.md domain=docs lang=markdown lines=88 bytes=3620 mtime=2026-04-10T23:48:33.652301+00:00 sha1=9269f2e75a4300b61121c540eb8c3e57ba44329f
CHUNK_START id=32db3e3783df_c001 start_line=1 end_line=88
````markdown
# 🏛️ MASTER PLAN: Context Governance Framework (v2.0 + Multi-Agent)

Este plano consolida as estratégias de **Automação de Manutenção** e **Especialização Cognitiva (Multi-Agent)** em um único framework modular, pronto para escalar de pequenos MVPs a grandes sistemas.

## 🕒 Metadados
- **Versão:** 2.0 (Consolidada)
- **Foco:** Eficiência de Tokens, Governança Rígida e Automação Python
- **Status:** Aguardando Aprovação Final

````
CHUNK_END id=aa78525fb574_c031
CHUNK_START id=aa78525fb574_c032 start_line=9301 end_line=9600
````markdown

---

## 🧩 1. Estrutura de Arquivos em Camadas (`.context/`)

A pasta será organizada em quatro camadas lógicas para isolamento operacional:

### 🧠 Camada Cognitiva (The Brain)
- **`MASTER_FLOW.md`**: Diretriz mestre de navegação.
- **`RULES.md`**: Protocolos de conduta ("A Lei").
- **`AGENT_REGISTRY.md`**: DNS de papéis, permissões e isolamento.
- **`PROMPT_LIBRARY.md`**: Biblioteca de templates de prompts.
- **`PRD.md`**: Requisito em execução (O "Norte").
- **`ROADMAP.md`**: Metas e fases (O Planejamento).

### 🛠️ Camada de Manutenção (The Housekeeper)
- **`JOURNAL.md`**: Log vivo (limite heurístico de tokens).
- **`TECHNICAL_REQUIREMENTS.md`**: Inventário técnico consolidado.
- **`rebuild_guide.md`**: Manual de setup e infra.
- **`schema.sql`**: Snapshot do banco de dados.
- **`ARCHITECTURE.md`**, `TESTS.md`, `rx-anatomy.md`, `rx-biology.md`.
- **`_archive_context/`**: Memória de longo prazo.

### 📊 Camada de Monitoramento (The Dashboard)
- **`CONTEXT_HEALTH.md`**: Status dashboard técnico e cognitivo.

### ⚙️ Camada de Automação (The Arms)
- **`_scripts/`**: Scripts Python com `#!/usr/bin/env python3`.

---

## 📜 2. Protocolos Integrados em `RULES.md`

1.  **🛡️ Checklist de Carga (Obrigatório):** Antes de codificar, validar carga de:
    - [ ] Global (Rules, MasterFlow, Roadmap)
    - [ ] Role (Registry-defined)
    - [ ] Ephemeral (PRD ativo + Journal tail 30-50 lines)
2.  **🔒 Context Gate:** Verificação de integridade Schema vs PRD.
3.  **🤖 Active Role Declaration:** Início de tarefa com `🤖 Ativando @[role]`.
4.  **🔢 Heurística de Token (Session Budget):** Disparar alerta de reset/purge ao detectar:
    - `~15-20 trocas densas` OU `~50k caracteres no prompt`.
5.  **🤝 Handoff Protocol:** Registro estruturado no `JOURNAL.md` em trocas de domínio.

---

## 🐍 3. Automação Python (`.context/_scripts/`)

Scripts unificados que entendem a hierarquia de agentes:

- **`validate_context.py`**: Checa integridade de arquivos, conformidade de roles e saúde geral.
- **`purge_journal.py`**: Arquiva 70% do log e gera uma semente de contexto no topo do arquivo atual.
- **`sync_project.py`**: Atualiza `TECHNICAL_REQUIREMENTS.md` lendo o `package.json` e `schema.sql`.

---

## 📈 4. Dashboard de Saúde (`CONTEXT_HEALTH.md`)

```markdown
# 📊 Context Health Check
| Métrica | Status | Pilar |
| :--- | :--- | :--- |
| Journal Line Count | [ 412 / 600 ] | Manutenção |
| Active Role | @frontend-specialist | Cognitivo |
| Schema Consistency | ✅ Synchronized | DB-First |
| Token Window | ⚠️ 78k (80%) | Sessão |
```

---

## 🚦 Roadmap de Execução

1.  **Fase 1: Estrutura MD** (Criar Registry, Prompt Library e Health).
2.  **Fase 2: As Leis** (Atualizar Master Flow e Rules com a lógica Multi-Agent).
3.  **Fase 3: Os Braços** (Implementar scripts Python em `_scripts/`).
4.  **Fase 4: Finalização** (Git Commit + Walkthrough).

---

> [!IMPORTANT]
> Este plano prioriza a **independência**. O projeto pode ser operado em "Modo Solo" (Single Agent) usando a role `@fullstack-generalist`, ou em "Modo Escala" (Multi-Agent) conforme a necessidade.

````
CHUNK_END id=32db3e3783df_c001
FILE_END id=file_32db3e3783df

---
<a id="file_2a788cb45159"></a>
FILE_START id=file_2a788cb45159 path=planos/multi_agent_plan.md domain=docs lang=markdown lines=62 bytes=2824 mtime=2026-04-10T23:32:27.825062+00:00 sha1=71ea8355ff980c67c66959bec1e4782108bad081
CHUNK_START id=2a788cb45159_c001 start_line=1 end_line=62
```markdown
# 🤖 Plano de Implementação: Arquitetura Multi-Agent

Este plano detalha a especialização do template com foco em **Especialização de Papéis**, **Isolamento de Contexto** e **Protocolos de Handoff**. O objetivo é transformar o agente em um sistema de engenharia cognitiva coordenado.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Roles, Context Isolation & Token Efficiency
- **Status:** Aguardando Aprovação (Em Separado)

---

## 🧩 1. Novos Componentes de Estrutura

### [REFINED] `AGENT_REGISTRY.md`
- **Conceito:** DNS cognitivo e Manifesto de Especialidades.
- **Regra de Ouro:** "Não registrado = Não executado".
- **Conteúdo Robusto:** Tabela com Roles (`@db-architect`, `@frontend-specialist`, `@backend-engineer`, `@qa-validator`, `@devops-guardian`, `@context-keeper`, `@fullstack-generalist`), permissões granulares de escrita e gatilhos de ativação.
- **Human Insights:** Blocos de contexto explicando o "porquê" das decisões técnicas para futuras IAs.

### [NEW] `PROMPT_LIBRARY.md`
- **Função:** Catálogo de templates de prompts de alta performance.
- **Conteúdo:** Instruções estruturadas para tarefas repetitivas (ex: "Criação de Componente", "Análise de Bug Crítico", "Escrita de Documentação").

---

## 📑 2. Protocolos de Handoff & Isolamento

### 🛡️ Camadas de Isolamento (Context Layering)
Implementação de carregamento por camadas no `RULES.md`:
1.  **🌍 Global (Sempre):** `RULES.md`, `MASTER_FLOW.md`, `ROADMAP.md`.
2.  **🎯 Role-Specific:** Definido no registry (ex: `@db` lê `schema.sql`).
3.  **📦 Task-Ephemeral:** `PRD.md` ativo e últimas 30-50 linhas do `JOURNAL.md`.
4.  **🗃️ Deep Archive:** Acesso apenas sob demanda explícita.

### 🤝 Protocolo de Handoff Estruturado
Tarefas cross-domain exigem registro de estado no `JOURNAL.md` antes da troca:
- **Formato:** `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [Checkpoint Técnico] | Próximo: [Ação]`

---

## 🛠️ 3. Integração com o Workflow Atual

### [MODIFY] `RULES.md`
- Adicionar a seção **3.1 Protocolo Multi-Agent**.
- Definir a obrigatoriedade da declaração de ativação: `🤖 Ativando @[role] | Tarefa: [X]`.

### [MODIFY] `MASTER_FLOW.md`
- Incluir `AGENT_REGISTRY.md` e `PROMPT_LIBRARY.md` no diagrama de árvore.
- Adicionar o ciclo de vida da sessão Multi-Agent.

---


````
CHUNK_END id=aa78525fb574_c016
CHUNK_START id=aa78525fb574_c017 start_line=4801 end_line=5100
````markdown
## 🚦 Próximos Passos

1.  **Revisão do Plano** em paralelo com o plano de Automação (v2.0).
2.  **Criação dos arquivos MD** com os templates pré-definidos.
3.  **Simulação de Handoff** para testagem da lógica de semente (`Seed Context`).

---

> [!TIP]
> Esta arquitetura permite que o projeto escale para milhares de linhas de código sem que a IA perca o foco ou alucine por excesso de arquivos irrelevantes na janela de contexto.

```
CHUNK_END id=2a788cb45159_c001
FILE_END id=file_2a788cb45159

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=57 bytes=1725 mtime=2026-04-11T00:43:01.095378+00:00 sha1=7a852c11cf920e6d3f718b626d23b2960360b95a
CHUNK_START id=86bac54f32d7_c001 start_line=1 end_line=57
```bash
#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - Orquestrador Universal de Contexto
# ---------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"

# Detecção inteligente de Python (Windows vs Unix)
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "❌ Erro: Python não encontrado no PATH."
    exit 1
fi

usage() {
    echo "🛠️ Context Management Runner"
    echo "Usage: ./run_context.sh [command]"
    echo ""
    echo "Commands:"
    echo "  validate  - Check .context integrity & estimate tokens"
    echo "  purge     - Archive 70% of oldest journal entries"
    echo "  sync      - Sync TECH_REQUIREMENTS.md with package.json & schema.sql"

````
CHUNK_END id=aa78525fb574_c024
CHUNK_START id=aa78525fb574_c025 start_line=7201 end_line=7500
````markdown
    echo "  all       - Run full pipeline (validate -> sync -> purge)"
    echo "  help      - Show this message"
    exit 1
}

run_script() {
    local script_name="$1"
    echo "▶️ Running $script_name..."
    if ! $PYTHON "$SCRIPT_DIR/$script_name"; then
        echo "❌ Failed: $script_name"
        exit 1
    fi
    echo "✅ Completed: $script_name"
    echo ""
}

[[ $# -eq 0 ]] && usage

case "$1" in
    validate) run_script "validate_context.py" ;;
    purge)    run_script "purge_journal.py" ;;
    sync)     run_script "sync_project.py" ;;
    all)
        run_script "validate_context.py"
        run_script "sync_project.py"
        run_script "purge_journal.py"
        echo "🎉 Full pipeline completed successfully."
        ;;
    help|--help|-h) usage ;;
    *) echo "❌ Unknown command: $1"; usage ;;
esac

```
CHUNK_END id=86bac54f32d7_c001
FILE_END id=file_86bac54f32d7


````
CHUNK_END id=aa78525fb574_c009
CHUNK_START id=aa78525fb574_c010 start_line=2701 end_line=2798
````markdown
---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=89 bytes=3753 mtime=2026-04-11T01:08:20.157384+00:00 sha1=7179930319fcc060058fbd50dcb63770bc05bc28
CHUNK_START id=4c6bbd05056e_c001 start_line=1 end_line=89
```python
import unittest
import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

class TestContextGovernance(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_root = self.test_dir
        self.context_dir = self.project_root / ".context"
        self.scripts_dir = self.context_dir / "_scripts"
        
        # Caminho real dos scripts
        self.repo_root = Path(__file__).parent.parent
        self.real_scripts_dir = self.repo_root / ".context" / "_scripts"
        
        # Cria estrutura de camadas
        for layer in ["brain", "maintenance", "monitoring", "_scripts"]:
            (self.context_dir / layer).mkdir(parents=True, exist_ok=True)
        (self.context_dir / "maintenance" / "_archive_context" / "journals").mkdir(parents=True, exist_ok=True)

        # Copia scripts reais para o sandbox
        for script in ["validate_context.py", "purge_journal.py", "sync_project.py"]:
            shutil.copy(self.real_scripts_dir / script, self.scripts_dir / script)

        # Cria arquivos base vazios
        for f in ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")
        
        for f in ["maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md", "maintenance/JOURNAL.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")

        self.python_cmd = sys.executable

    def tearDown(self):
        # Limpa sandbox
        shutil.rmtree(self.test_dir)

    def run_script(self, name):
        script_path = self.scripts_dir / name
        result = subprocess.run(
            [self.python_cmd, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=self.project_root
        )
        return result

    def test_validate_integrity(self):
        # Adiciona uma tabela válida em AGENT_REGISTRY para passar no check
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")

````
CHUNK_END id=aa78525fb574_c032
CHUNK_START id=aa78525fb574_c033 start_line=9601 end_line=9900
````markdown
        
        res = self.run_script("validate_context.py")
        self.assertIn("[SUCCESS]", res.stdout)

    def test_validate_missing_file(self):
        (self.context_dir / "brain/AGENT_REGISTRY.md").unlink()
        res = self.run_script("validate_context.py")
        self.assertIn("Arquivos ausentes", res.stdout)

    def test_purge_journal(self):
        journal = self.context_dir / "maintenance/JOURNAL.md"
        journal.write_text("## 📅 2024\nEntry 1\n\n## 📅 2024\nEntry 2", encoding="utf-8")
        res = self.run_script("purge_journal.py")
        self.assertIn("[OK] Purge concluido", res.stdout)
        
        # Verifica se arquivo foi criado no archive
        archive_files = list((self.context_dir / "maintenance/_archive_context/journals").glob("*.md"))
        self.assertGreaterEqual(len(archive_files), 1)

    def test_sync_project(self):
        # Simula package.json e schema.sql
        (self.project_root / "package.json").write_text('{"dependencies":{"test":"1.0"}}', encoding="utf-8")
        (self.context_dir / "maintenance/schema.sql").write_text("CREATE TABLE users (id INT);", encoding="utf-8")
        
        res = self.run_script("sync_project.py")
        self.assertIn("[OK] TECHNICAL_REQUIREMENTS.md sincronizado", res.stdout)
        
        req_content = (self.context_dir / "maintenance/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")
        self.assertIn("users", req_content)
        self.assertIn("test", req_content)

if __name__ == "__main__":
    unittest.main()

```
CHUNK_END id=4c6bbd05056e_c001
FILE_END id=file_4c6bbd05056e

````
CHUNK_END id=aa78525fb574_c010
FILE_END id=file_aa78525fb574

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=155 bytes=5469 mtime=2026-04-11T02:29:46.289656+00:00 sha1=18e30807c6ef1ce94e3619f19f8ec2bd93f77c52
CHUNK_START id=c59135753d26_c001 start_line=1 end_line=155
```bash
#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.2 Premium+)
# -----------------------------------------------------------------------------
# Versão Suprema: Fusão Antigravity + TLC Spec-Driven.
# Com detecção automática de gerenciador e motores de manutenção completos.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  command -v python3 >/dev/null 2>&1 || PYTHON="python3"
  command -v python >/dev/null 2>&1 || PYTHON="python"
  [ -z "${PYTHON:-}" ] && error "python3 ou python e obrigatorio."
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity AI-Ready Framework v2.2 Premium+..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop TLC..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança e integração TLC..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit + TLC Fusion)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT). O workshop \`.specs\` e o espaco de execucao efemera.

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo e handoffs.
- .specs/: Workbench atômico (Regra de 48h/Max 3).

🔄 4. Gatilhos Operacionais
- "Inicie a fase de SPECIFY para o PRD #[ID]": IA cria spec atômica no .specs/.
- "Atualize contexto": Sincronizacao proativa via sync_project.py.
EOF

cat > .context/brain/TLC_INTEGRATION.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 🔗 TLC_INTEGRATION.md
Ponte entre Governança (.context/) e Execução Atômica (.specs/).

## 🔄 Ciclo de Vida Híbrido
1. INTENT -> PRD.md ativo define escopo.
2. SPECIFY -> IA cria .specs/features/[nome]/spec.md.
3. IMPLEMENT -> Geração de código baseada na spec.
4. VERIFY -> STATE.md marcado como ✅ PASSED.
5. SYNC -> Lições para o JOURNAL.md e limpeza da spec.
EOF

# (Injeção dos Motores Reais v2.2 Premium+)
cat > .context/_scripts/validate_context.py << 'EOF'
#!/usr/bin/env python3
import os, sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQUIRED = ["brain/RULES.md", "brain/PRD.md", "maintenance/JOURNAL.md"]
def check_specs():

````
CHUNK_END id=aa78525fb574_c017
CHUNK_START id=aa78525fb574_c018 start_line=5101 end_line=5400
````markdown
    specs = CONTEXT_DIR.parent / ".specs/features"
    if not specs.exists(): return True
    return all((d / "STATE.md").exists() for d in specs.iterdir() if d.is_dir())
def validate():
    print("--- Validacao v2.2 Premium+ ---")
    missing = [f for f in REQUIRED if not (CONTEXT_DIR / f).exists()]
    if missing or not check_specs(): sys.exit(1)
    print("✅ Contexto e Workshop integros.")
if __name__ == "__main__": validate()
EOF

cat > .context/_scripts/cleanup_specs.py << 'EOF'
#!/usr/bin/env python3
import os, shutil, time
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
SPECS_DIR = SCRIPT_DIR.parent.parent / ".specs" / "features"
ARCHIVE_DIR = SCRIPT_DIR.parent / "maintenance" / "_archive_context" / "specs"
def cleanup():
    if not SPECS_DIR.exists(): return
    specs = sorted([d for d in SPECS_DIR.iterdir() if d.is_dir()], key=os.path.getmtime)
    while len(specs) > 3:
        shutil.move(str(specs.pop(0)), str(ARCHIVE_DIR))
    print("[OK] Manutencao de specs concluida.")
if __name__ == "__main__": cleanup()
EOF

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
const runner = '$PKG_MGR' === 'npm' ? 'npm run' : '$PKG_MGR';
Object.assign(pkg.scripts, {
  'context:validate': 'bash run_context.sh validate',
  'context:cleanup': 'bash run_context.sh cleanup',
  'context:all': runner + ' context:validate && ' + runner + ' context:cleanup',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));

````
CHUNK_END id=aa78525fb574_c025
CHUNK_START id=aa78525fb574_c026 start_line=7501 end_line=7800
````markdown
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:validate" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."

```
CHUNK_END id=c59135753d26_c001
FILE_END id=file_c59135753d26

---
<a id="file_fa288d1472d2"></a>
FILE_START id=file_fa288d1472d2 path=package-lock.json domain=config lang=json lines=32 bytes=785 mtime=2026-04-11T01:12:03.334672+00:00 sha1=e8450c2eeca43eabd30597b19a6cb24ad70fcddb
CHUNK_START id=fa288d1472d2_c001 start_line=1 end_line=32
```json
{
  "name": "template-ai-context-governance",
  "version": "2.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "template-ai-context-governance",
      "version": "2.0.0",
      "license": "MIT",
      "devDependencies": {
        "husky": "^9.1.7"
      }
    },
    "node_modules/husky": {
      "version": "9.1.7",
      "resolved": "https://registry.npmjs.org/husky/-/husky-9.1.7.tgz",
      "integrity": "sha512-5gs5ytaNjBrh5Ow3zrvdUUY+0VxIuWVL4i9irt6friV+BqdCfmV11CQTWMiBYWHbXhco+J1kHfTOUkePhCDvMA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "husky": "bin.js"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/typicode"
      }
    }
  }
}

```
CHUNK_END id=fa288d1472d2_c001
FILE_END id=file_fa288d1472d2

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=24 bytes=735 mtime=2026-04-11T02:41:48.186770+00:00 sha1=6f0d247a0f4e8dd35e8359d4399b2ddbe60eabca
CHUNK_START id=7030d0b2f71b_c001 start_line=1 end_line=24
```json
{
  "name": "template-ai-context-governance",
  "version": "2.0.0",
  "description": "AI-Ready Template with Context Governance Framework",
  "scripts": {
    "context:validate": "bash run_context.sh validate",
    "context:cleanup": "bash run_context.sh cleanup",
    "context:capture": "python captura_projeto.py --emit-symbol-index --emit-import-map",
    "context:all": "npm run context:validate && npm run context:cleanup && npm run context:capture",
    "context:help": "echo \"Comandos: validate | purge | sync | all\"",
    "prepare": "husky"
  },
  "keywords": [
    "ai",
    "context",
    "governance",
    "template"
  ],
  "author": "TalesAvancini",
  "license": "MIT",
  "devDependencies": {
    "husky": "^9.1.7"
  }
}

```
CHUNK_END id=7030d0b2f71b_c001
FILE_END id=file_7030d0b2f71b

---
<a id="file_a9422a4b7476"></a>
FILE_START id=file_a9422a4b7476 path=planos/implementation_plan.md domain=docs lang=markdown lines=77 bytes=3338 mtime=2026-04-10T23:15:28.184032+00:00 sha1=37ad3605aae584ee4398621d92edd7b76058413e
CHUNK_START id=a9422a4b7476_c001 start_line=1 end_line=77
```markdown
# 🏛️ Plano de Expansão: Context Governance Framework (v2.0)


````
CHUNK_END id=aa78525fb574_c033
CHUNK_START id=aa78525fb574_c034 start_line=9901 end_line=10200
````markdown
Este plano detalha a transição do template de um sistema de documentação estática para um framework de governança ativa, focado em **escala**, **automação** e **prevenção de drift**.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Automação em Python e Escala de Contexto
- **Status:** Aguardando Aprovação

---

## 🧩 1. Estrutura de Arquivos Ampliada

Vamos expandir a pasta `.context/` para incluir novas camadas de inteligência:

### [NEW] Novos Documentos de Governança
- **`PROMPT_LIBRARY.md`**: Catálogo de personas e templates de prompts específicos para garantir consistência entre sessões.
- **`SESSION_MANAGER.md`**: Regras de gerenciamento de janela de tokens, limites de sessão e snapshots de resumo.
- **`CONTEXT_HEALTH.md`**: Dashboard de saúde do contexto (métricas de linhas, divergências e obsolescência).
- **`AGENT_REGISTRY.md`**: Definição de papéis (Expertises) e permissões de escrita/leitura nos arquivos do contexto.

---

## 📜 2. Atualização dos Protocolos (`RULES.md`)

Injetaremos novos protocolos de segurança e eficiência no arquivo de leis do agente:

### 🔹 Context Gate (Validação Pré-Voo)
O Agente deve realizar um "Checklist de Integridade" antes de gerar código, validando se o PRD e o Schema estão sincronizados.

### 🔹 Session Budget (Gestão de Tokens)
Definição de limites claros: ao atingir 80% da janela de contexto (estimada), o agente **deve** realizar um purge do `JOURNAL.md` (via script) e gerar um resumo semente.

---

## 🛠️ 3. Automação com Python (`.context/_scripts/`)

Criaremos scripts em Python para tornar a governança ativa e independente do ambiente da IDE.

### #### [NEW] `validate_context.py`
- Verifica se o `schema.sql` contém os campos referenciados no PRD atual.
- Valida o limite de linhas do `JOURNAL.md`.
- Gera um alerta visual se o status em qualquer arquivo for `Stale` ou `Deprecated`.

### #### [NEW] `purge_journal.py`
- Executa a lógica de arquivamento: move os primeiros 70% do log para `_archive_context/journals/`.
- Mantém os 30% finais e insere um resumo gerado pela IA no topo como conexão lógica.

### #### [NEW] `init_context.py`
- Script de bootstrap que inicializa a estrutura em novos projetos, gera os metadados de tempo reais e cria o `schema.sql` inicial.

---

## 📈 4. Monitoramento (`CONTEXT_HEALTH.md`)

Criação do dashboard dinâmico que será atualizado periodicamente pelos scripts ou manualmente pela IA.

| Métrica | Limite | Ação em caso de Falha |
| :--- | :--- | :--- |
| JOURNAL size | 600 linhas | Trigger `purge_journal.py` |
| PRD sync | 100% | Bloqueio de geração de UI |
| Token Window | 128k (80%) | Trigger Snapshot de Sessão |

---

## 🚦 Próximos Passos (Workflow)

1.  **Aprovação do Plano** (Você).
2.  **Criação dos Arquivos MD** com os templates propostos.
3.  **Geração do Código Python** para cada script de automação.
4.  **Atualização do `MASTER_FLOW.md` e `RULES.md`** para refletir a nova arquitetura.
5.  **Validação Final** da estrutura completa.

---

> [!IMPORTANT]
> A implementação será feita de forma **não invasiva** e **não executável** conforme solicitado, apenas preparando o repositório para ser exportado para o GitHub.

```
CHUNK_END id=a9422a4b7476_c001
FILE_END id=file_a9422a4b7476

---
<a id="file_32db3e3783df"></a>
FILE_START id=file_32db3e3783df path=planos/master_plan.md domain=docs lang=markdown lines=88 bytes=3620 mtime=2026-04-10T23:48:33.652301+00:00 sha1=9269f2e75a4300b61121c540eb8c3e57ba44329f
CHUNK_START id=32db3e3783df_c001 start_line=1 end_line=88
````markdown
# 🏛️ MASTER PLAN: Context Governance Framework (v2.0 + Multi-Agent)

Este plano consolida as estratégias de **Automação de Manutenção** e **Especialização Cognitiva (Multi-Agent)** em um único framework modular, pronto para escalar de pequenos MVPs a grandes sistemas.

## 🕒 Metadados
- **Versão:** 2.0 (Consolidada)
- **Foco:** Eficiência de Tokens, Governança Rígida e Automação Python
- **Status:** Aguardando Aprovação Final

---

## 🧩 1. Estrutura de Arquivos em Camadas (`.context/`)

A pasta será organizada em quatro camadas lógicas para isolamento operacional:

### 🧠 Camada Cognitiva (The Brain)
- **`MASTER_FLOW.md`**: Diretriz mestre de navegação.
- **`RULES.md`**: Protocolos de conduta ("A Lei").
- **`AGENT_REGISTRY.md`**: DNS de papéis, permissões e isolamento.
- **`PROMPT_LIBRARY.md`**: Biblioteca de templates de prompts.
- **`PRD.md`**: Requisito em execução (O "Norte").
- **`ROADMAP.md`**: Metas e fases (O Planejamento).

### 🛠️ Camada de Manutenção (The Housekeeper)
- **`JOURNAL.md`**: Log vivo (limite heurístico de tokens).
- **`TECHNICAL_REQUIREMENTS.md`**: Inventário técnico consolidado.
- **`rebuild_guide.md`**: Manual de setup e infra.
- **`schema.sql`**: Snapshot do banco de dados.
- **`ARCHITECTURE.md`**, `TESTS.md`, `rx-anatomy.md`, `rx-biology.md`.
- **`_archive_context/`**: Memória de longo prazo.

### 📊 Camada de Monitoramento (The Dashboard)
- **`CONTEXT_HEALTH.md`**: Status dashboard técnico e cognitivo.

### ⚙️ Camada de Automação (The Arms)
- **`_scripts/`**: Scripts Python com `#!/usr/bin/env python3`.

---

## 📜 2. Protocolos Integrados em `RULES.md`

1.  **🛡️ Checklist de Carga (Obrigatório):** Antes de codificar, validar carga de:
    - [ ] Global (Rules, MasterFlow, Roadmap)
    - [ ] Role (Registry-defined)
    - [ ] Ephemeral (PRD ativo + Journal tail 30-50 lines)
2.  **🔒 Context Gate:** Verificação de integridade Schema vs PRD.
3.  **🤖 Active Role Declaration:** Início de tarefa com `🤖 Ativando @[role]`.
4.  **🔢 Heurística de Token (Session Budget):** Disparar alerta de reset/purge ao detectar:
    - `~15-20 trocas densas` OU `~50k caracteres no prompt`.
5.  **🤝 Handoff Protocol:** Registro estruturado no `JOURNAL.md` em trocas de domínio.

---

## 🐍 3. Automação Python (`.context/_scripts/`)

Scripts unificados que entendem a hierarquia de agentes:

- **`validate_context.py`**: Checa integridade de arquivos, conformidade de roles e saúde geral.
- **`purge_journal.py`**: Arquiva 70% do log e gera uma semente de contexto no topo do arquivo atual.
- **`sync_project.py`**: Atualiza `TECHNICAL_REQUIREMENTS.md` lendo o `package.json` e `schema.sql`.

---

## 📈 4. Dashboard de Saúde (`CONTEXT_HEALTH.md`)

```markdown
# 📊 Context Health Check
| Métrica | Status | Pilar |
| :--- | :--- | :--- |
| Journal Line Count | [ 412 / 600 ] | Manutenção |
| Active Role | @frontend-specialist | Cognitivo |
| Schema Consistency | ✅ Synchronized | DB-First |
| Token Window | ⚠️ 78k (80%) | Sessão |
```

---


````
CHUNK_END id=aa78525fb574_c018
CHUNK_START id=aa78525fb574_c019 start_line=5401 end_line=5653
````markdown
## 🚦 Roadmap de Execução

1.  **Fase 1: Estrutura MD** (Criar Registry, Prompt Library e Health).
2.  **Fase 2: As Leis** (Atualizar Master Flow e Rules com a lógica Multi-Agent).
3.  **Fase 3: Os Braços** (Implementar scripts Python em `_scripts/`).
4.  **Fase 4: Finalização** (Git Commit + Walkthrough).

---

> [!IMPORTANT]
> Este plano prioriza a **independência**. O projeto pode ser operado em "Modo Solo" (Single Agent) usando a role `@fullstack-generalist`, ou em "Modo Escala" (Multi-Agent) conforme a necessidade.

````
CHUNK_END id=32db3e3783df_c001
FILE_END id=file_32db3e3783df

---
<a id="file_2a788cb45159"></a>
FILE_START id=file_2a788cb45159 path=planos/multi_agent_plan.md domain=docs lang=markdown lines=62 bytes=2824 mtime=2026-04-10T23:32:27.825062+00:00 sha1=71ea8355ff980c67c66959bec1e4782108bad081
CHUNK_START id=2a788cb45159_c001 start_line=1 end_line=62
```markdown
# 🤖 Plano de Implementação: Arquitetura Multi-Agent

Este plano detalha a especialização do template com foco em **Especialização de Papéis**, **Isolamento de Contexto** e **Protocolos de Handoff**. O objetivo é transformar o agente em um sistema de engenharia cognitiva coordenado.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Roles, Context Isolation & Token Efficiency
- **Status:** Aguardando Aprovação (Em Separado)

---

## 🧩 1. Novos Componentes de Estrutura

### [REFINED] `AGENT_REGISTRY.md`
- **Conceito:** DNS cognitivo e Manifesto de Especialidades.

````
CHUNK_END id=aa78525fb574_c026
CHUNK_START id=aa78525fb574_c027 start_line=7801 end_line=8100
````markdown
- **Regra de Ouro:** "Não registrado = Não executado".
- **Conteúdo Robusto:** Tabela com Roles (`@db-architect`, `@frontend-specialist`, `@backend-engineer`, `@qa-validator`, `@devops-guardian`, `@context-keeper`, `@fullstack-generalist`), permissões granulares de escrita e gatilhos de ativação.
- **Human Insights:** Blocos de contexto explicando o "porquê" das decisões técnicas para futuras IAs.

### [NEW] `PROMPT_LIBRARY.md`
- **Função:** Catálogo de templates de prompts de alta performance.
- **Conteúdo:** Instruções estruturadas para tarefas repetitivas (ex: "Criação de Componente", "Análise de Bug Crítico", "Escrita de Documentação").

---

## 📑 2. Protocolos de Handoff & Isolamento

### 🛡️ Camadas de Isolamento (Context Layering)
Implementação de carregamento por camadas no `RULES.md`:
1.  **🌍 Global (Sempre):** `RULES.md`, `MASTER_FLOW.md`, `ROADMAP.md`.
2.  **🎯 Role-Specific:** Definido no registry (ex: `@db` lê `schema.sql`).
3.  **📦 Task-Ephemeral:** `PRD.md` ativo e últimas 30-50 linhas do `JOURNAL.md`.
4.  **🗃️ Deep Archive:** Acesso apenas sob demanda explícita.

### 🤝 Protocolo de Handoff Estruturado
Tarefas cross-domain exigem registro de estado no `JOURNAL.md` antes da troca:
- **Formato:** `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [Checkpoint Técnico] | Próximo: [Ação]`

---

## 🛠️ 3. Integração com o Workflow Atual

### [MODIFY] `RULES.md`
- Adicionar a seção **3.1 Protocolo Multi-Agent**.
- Definir a obrigatoriedade da declaração de ativação: `🤖 Ativando @[role] | Tarefa: [X]`.

### [MODIFY] `MASTER_FLOW.md`
- Incluir `AGENT_REGISTRY.md` e `PROMPT_LIBRARY.md` no diagrama de árvore.
- Adicionar o ciclo de vida da sessão Multi-Agent.

---

## 🚦 Próximos Passos

1.  **Revisão do Plano** em paralelo com o plano de Automação (v2.0).
2.  **Criação dos arquivos MD** com os templates pré-definidos.
3.  **Simulação de Handoff** para testagem da lógica de semente (`Seed Context`).

---

> [!TIP]
> Esta arquitetura permite que o projeto escale para milhares de linhas de código sem que a IA perca o foco ou alucine por excesso de arquivos irrelevantes na janela de contexto.

```
CHUNK_END id=2a788cb45159_c001
FILE_END id=file_2a788cb45159

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=57 bytes=1725 mtime=2026-04-11T00:43:01.095378+00:00 sha1=7a852c11cf920e6d3f718b626d23b2960360b95a
CHUNK_START id=86bac54f32d7_c001 start_line=1 end_line=57
```bash
#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - Orquestrador Universal de Contexto
# ---------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"

# Detecção inteligente de Python (Windows vs Unix)
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "❌ Erro: Python não encontrado no PATH."
    exit 1
fi

usage() {
    echo "🛠️ Context Management Runner"
    echo "Usage: ./run_context.sh [command]"
    echo ""
    echo "Commands:"
    echo "  validate  - Check .context integrity & estimate tokens"
    echo "  purge     - Archive 70% of oldest journal entries"
    echo "  sync      - Sync TECH_REQUIREMENTS.md with package.json & schema.sql"
    echo "  all       - Run full pipeline (validate -> sync -> purge)"
    echo "  help      - Show this message"
    exit 1
}

run_script() {
    local script_name="$1"
    echo "▶️ Running $script_name..."
    if ! $PYTHON "$SCRIPT_DIR/$script_name"; then

````
CHUNK_END id=aa78525fb574_c034
CHUNK_START id=aa78525fb574_c035 start_line=10201 end_line=10500
````markdown
        echo "❌ Failed: $script_name"
        exit 1
    fi
    echo "✅ Completed: $script_name"
    echo ""
}

[[ $# -eq 0 ]] && usage

case "$1" in
    validate) run_script "validate_context.py" ;;
    purge)    run_script "purge_journal.py" ;;
    sync)     run_script "sync_project.py" ;;
    all)
        run_script "validate_context.py"
        run_script "sync_project.py"
        run_script "purge_journal.py"
        echo "🎉 Full pipeline completed successfully."
        ;;
    help|--help|-h) usage ;;
    *) echo "❌ Unknown command: $1"; usage ;;
esac

```
CHUNK_END id=86bac54f32d7_c001
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=89 bytes=3753 mtime=2026-04-11T01:08:20.157384+00:00 sha1=7179930319fcc060058fbd50dcb63770bc05bc28
CHUNK_START id=4c6bbd05056e_c001 start_line=1 end_line=89
```python
import unittest
import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

class TestContextGovernance(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_root = self.test_dir
        self.context_dir = self.project_root / ".context"
        self.scripts_dir = self.context_dir / "_scripts"
        
        # Caminho real dos scripts
        self.repo_root = Path(__file__).parent.parent
        self.real_scripts_dir = self.repo_root / ".context" / "_scripts"
        
        # Cria estrutura de camadas
        for layer in ["brain", "maintenance", "monitoring", "_scripts"]:
            (self.context_dir / layer).mkdir(parents=True, exist_ok=True)
        (self.context_dir / "maintenance" / "_archive_context" / "journals").mkdir(parents=True, exist_ok=True)

        # Copia scripts reais para o sandbox
        for script in ["validate_context.py", "purge_journal.py", "sync_project.py"]:
            shutil.copy(self.real_scripts_dir / script, self.scripts_dir / script)

        # Cria arquivos base vazios
        for f in ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")
        
        for f in ["maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md", "maintenance/JOURNAL.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")

        self.python_cmd = sys.executable

    def tearDown(self):
        # Limpa sandbox
        shutil.rmtree(self.test_dir)

    def run_script(self, name):
        script_path = self.scripts_dir / name
        result = subprocess.run(
            [self.python_cmd, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=self.project_root
        )
        return result

    def test_validate_integrity(self):
        # Adiciona uma tabela válida em AGENT_REGISTRY para passar no check
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertIn("[SUCCESS]", res.stdout)

    def test_validate_missing_file(self):
        (self.context_dir / "brain/AGENT_REGISTRY.md").unlink()
        res = self.run_script("validate_context.py")
        self.assertIn("Arquivos ausentes", res.stdout)

    def test_purge_journal(self):
        journal = self.context_dir / "maintenance/JOURNAL.md"
        journal.write_text("## 📅 2024\nEntry 1\n\n## 📅 2024\nEntry 2", encoding="utf-8")
        res = self.run_script("purge_journal.py")
        self.assertIn("[OK] Purge concluido", res.stdout)
        
        # Verifica se arquivo foi criado no archive
        archive_files = list((self.context_dir / "maintenance/_archive_context/journals").glob("*.md"))
        self.assertGreaterEqual(len(archive_files), 1)

    def test_sync_project(self):
        # Simula package.json e schema.sql
        (self.project_root / "package.json").write_text('{"dependencies":{"test":"1.0"}}', encoding="utf-8")
        (self.context_dir / "maintenance/schema.sql").write_text("CREATE TABLE users (id INT);", encoding="utf-8")
        
        res = self.run_script("sync_project.py")
        self.assertIn("[OK] TECHNICAL_REQUIREMENTS.md sincronizado", res.stdout)
        
        req_content = (self.context_dir / "maintenance/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")
        self.assertIn("users", req_content)
        self.assertIn("test", req_content)

if __name__ == "__main__":
    unittest.main()

```
CHUNK_END id=4c6bbd05056e_c001
FILE_END id=file_4c6bbd05056e

````
CHUNK_END id=aa78525fb574_c019
FILE_END id=file_aa78525fb574

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=155 bytes=5469 mtime=2026-04-11T02:29:46.289656+00:00 sha1=18e30807c6ef1ce94e3619f19f8ec2bd93f77c52
CHUNK_START id=c59135753d26_c001 start_line=1 end_line=155
```bash
#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.2 Premium+)
# -----------------------------------------------------------------------------
# Versão Suprema: Fusão Antigravity + TLC Spec-Driven.
# Com detecção automática de gerenciador e motores de manutenção completos.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  command -v python3 >/dev/null 2>&1 || PYTHON="python3"
  command -v python >/dev/null 2>&1 || PYTHON="python"
  [ -z "${PYTHON:-}" ] && error "python3 ou python e obrigatorio."
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity AI-Ready Framework v2.2 Premium+..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop TLC..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança e integração TLC..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit + TLC Fusion)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT). O workshop \`.specs\` e o espaco de execucao efemera.

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo e handoffs.

````
CHUNK_END id=aa78525fb574_c027
CHUNK_START id=aa78525fb574_c028 start_line=8101 end_line=8400
````markdown
- .specs/: Workbench atômico (Regra de 48h/Max 3).

🔄 4. Gatilhos Operacionais
- "Inicie a fase de SPECIFY para o PRD #[ID]": IA cria spec atômica no .specs/.
- "Atualize contexto": Sincronizacao proativa via sync_project.py.
EOF

cat > .context/brain/TLC_INTEGRATION.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 🔗 TLC_INTEGRATION.md
Ponte entre Governança (.context/) e Execução Atômica (.specs/).

## 🔄 Ciclo de Vida Híbrido
1. INTENT -> PRD.md ativo define escopo.
2. SPECIFY -> IA cria .specs/features/[nome]/spec.md.
3. IMPLEMENT -> Geração de código baseada na spec.
4. VERIFY -> STATE.md marcado como ✅ PASSED.
5. SYNC -> Lições para o JOURNAL.md e limpeza da spec.
EOF

# (Injeção dos Motores Reais v2.2 Premium+)
cat > .context/_scripts/validate_context.py << 'EOF'
#!/usr/bin/env python3
import os, sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQUIRED = ["brain/RULES.md", "brain/PRD.md", "maintenance/JOURNAL.md"]
def check_specs():
    specs = CONTEXT_DIR.parent / ".specs/features"
    if not specs.exists(): return True
    return all((d / "STATE.md").exists() for d in specs.iterdir() if d.is_dir())
def validate():
    print("--- Validacao v2.2 Premium+ ---")
    missing = [f for f in REQUIRED if not (CONTEXT_DIR / f).exists()]
    if missing or not check_specs(): sys.exit(1)
    print("✅ Contexto e Workshop integros.")
if __name__ == "__main__": validate()
EOF

cat > .context/_scripts/cleanup_specs.py << 'EOF'
#!/usr/bin/env python3
import os, shutil, time
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
SPECS_DIR = SCRIPT_DIR.parent.parent / ".specs" / "features"
ARCHIVE_DIR = SCRIPT_DIR.parent / "maintenance" / "_archive_context" / "specs"
def cleanup():
    if not SPECS_DIR.exists(): return
    specs = sorted([d for d in SPECS_DIR.iterdir() if d.is_dir()], key=os.path.getmtime)
    while len(specs) > 3:
        shutil.move(str(specs.pop(0)), str(ARCHIVE_DIR))
    print("[OK] Manutencao de specs concluida.")
if __name__ == "__main__": cleanup()
EOF

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
const runner = '$PKG_MGR' === 'npm' ? 'npm run' : '$PKG_MGR';
Object.assign(pkg.scripts, {
  'context:validate': 'bash run_context.sh validate',
  'context:cleanup': 'bash run_context.sh cleanup',
  'context:all': runner + ' context:validate && ' + runner + ' context:cleanup',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:validate" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."

```
CHUNK_END id=c59135753d26_c001
FILE_END id=file_c59135753d26


````
CHUNK_END id=aa78525fb574_c035
CHUNK_START id=aa78525fb574_c036 start_line=10501 end_line=10800
````markdown
---
<a id="file_fa288d1472d2"></a>
FILE_START id=file_fa288d1472d2 path=package-lock.json domain=config lang=json lines=32 bytes=785 mtime=2026-04-11T01:12:03.334672+00:00 sha1=e8450c2eeca43eabd30597b19a6cb24ad70fcddb
CHUNK_START id=fa288d1472d2_c001 start_line=1 end_line=32
```json
{
  "name": "template-ai-context-governance",
  "version": "2.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "template-ai-context-governance",
      "version": "2.0.0",
      "license": "MIT",
      "devDependencies": {
        "husky": "^9.1.7"
      }
    },
    "node_modules/husky": {
      "version": "9.1.7",
      "resolved": "https://registry.npmjs.org/husky/-/husky-9.1.7.tgz",
      "integrity": "sha512-5gs5ytaNjBrh5Ow3zrvdUUY+0VxIuWVL4i9irt6friV+BqdCfmV11CQTWMiBYWHbXhco+J1kHfTOUkePhCDvMA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "husky": "bin.js"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/typicode"
      }
    }
  }
}

```
CHUNK_END id=fa288d1472d2_c001
FILE_END id=file_fa288d1472d2

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=27 bytes=824 mtime=2026-04-11T03:09:58.961110+00:00 sha1=cf2b6e50daab5aa1b974f11af667be601738252b
CHUNK_START id=7030d0b2f71b_c001 start_line=1 end_line=27
```json
{
  "name": "ai-context-governance-template",
  "version": "2.2.0",
  "description": "AI-Ready Template with Layered Context Governance & Spec-Driven Execution",
  "scripts": {
    "context:validate": "python run_context.py validate",
    "context:sync": "python run_context.py sync",
    "context:cleanup": "python run_context.py cleanup",
    "context:purge": "python run_context.py purge",
    "context:capture": "python captura_projeto.py --emit-symbol-index --emit-import-map",
    "context:all": "python run_context.py all",
    "context:test": "python tests/test_context.py",
    "prepare": "husky"
  },
  "keywords": [
    "ai",
    "context-governance",
    "spec-driven",
    "multi-agent",
    "automation"
  ],
  "author": "Tales Avancini",
  "license": "MIT",
  "devDependencies": {
    "husky": "^9.1.7"
  }
}

```
CHUNK_END id=7030d0b2f71b_c001
FILE_END id=file_7030d0b2f71b

---
<a id="file_a9422a4b7476"></a>
FILE_START id=file_a9422a4b7476 path=planos/implementation_plan.md domain=docs lang=markdown lines=77 bytes=3338 mtime=2026-04-10T23:15:28.184032+00:00 sha1=37ad3605aae584ee4398621d92edd7b76058413e
CHUNK_START id=a9422a4b7476_c001 start_line=1 end_line=77
```markdown
# 🏛️ Plano de Expansão: Context Governance Framework (v2.0)

Este plano detalha a transição do template de um sistema de documentação estática para um framework de governança ativa, focado em **escala**, **automação** e **prevenção de drift**.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Automação em Python e Escala de Contexto
- **Status:** Aguardando Aprovação

---

## 🧩 1. Estrutura de Arquivos Ampliada

Vamos expandir a pasta `.context/` para incluir novas camadas de inteligência:

### [NEW] Novos Documentos de Governança
- **`PROMPT_LIBRARY.md`**: Catálogo de personas e templates de prompts específicos para garantir consistência entre sessões.
- **`SESSION_MANAGER.md`**: Regras de gerenciamento de janela de tokens, limites de sessão e snapshots de resumo.
- **`CONTEXT_HEALTH.md`**: Dashboard de saúde do contexto (métricas de linhas, divergências e obsolescência).
- **`AGENT_REGISTRY.md`**: Definição de papéis (Expertises) e permissões de escrita/leitura nos arquivos do contexto.

---

## 📜 2. Atualização dos Protocolos (`RULES.md`)

Injetaremos novos protocolos de segurança e eficiência no arquivo de leis do agente:

### 🔹 Context Gate (Validação Pré-Voo)
O Agente deve realizar um "Checklist de Integridade" antes de gerar código, validando se o PRD e o Schema estão sincronizados.

### 🔹 Session Budget (Gestão de Tokens)
Definição de limites claros: ao atingir 80% da janela de contexto (estimada), o agente **deve** realizar um purge do `JOURNAL.md` (via script) e gerar um resumo semente.

---

## 🛠️ 3. Automação com Python (`.context/_scripts/`)

Criaremos scripts em Python para tornar a governança ativa e independente do ambiente da IDE.

### #### [NEW] `validate_context.py`
- Verifica se o `schema.sql` contém os campos referenciados no PRD atual.
- Valida o limite de linhas do `JOURNAL.md`.
- Gera um alerta visual se o status em qualquer arquivo for `Stale` ou `Deprecated`.

### #### [NEW] `purge_journal.py`
- Executa a lógica de arquivamento: move os primeiros 70% do log para `_archive_context/journals/`.
- Mantém os 30% finais e insere um resumo gerado pela IA no topo como conexão lógica.

### #### [NEW] `init_context.py`
- Script de bootstrap que inicializa a estrutura em novos projetos, gera os metadados de tempo reais e cria o `schema.sql` inicial.

---

## 📈 4. Monitoramento (`CONTEXT_HEALTH.md`)

Criação do dashboard dinâmico que será atualizado periodicamente pelos scripts ou manualmente pela IA.

| Métrica | Limite | Ação em caso de Falha |
| :--- | :--- | :--- |
| JOURNAL size | 600 linhas | Trigger `purge_journal.py` |
| PRD sync | 100% | Bloqueio de geração de UI |
| Token Window | 128k (80%) | Trigger Snapshot de Sessão |

---

## 🚦 Próximos Passos (Workflow)

1.  **Aprovação do Plano** (Você).
2.  **Criação dos Arquivos MD** com os templates propostos.
3.  **Geração do Código Python** para cada script de automação.
4.  **Atualização do `MASTER_FLOW.md` e `RULES.md`** para refletir a nova arquitetura.
5.  **Validação Final** da estrutura completa.

---

> [!IMPORTANT]
> A implementação será feita de forma **não invasiva** e **não executável** conforme solicitado, apenas preparando o repositório para ser exportado para o GitHub.

```
CHUNK_END id=a9422a4b7476_c001
FILE_END id=file_a9422a4b7476

---
<a id="file_32db3e3783df"></a>
FILE_START id=file_32db3e3783df path=planos/master_plan.md domain=docs lang=markdown lines=88 bytes=3620 mtime=2026-04-10T23:48:33.652301+00:00 sha1=9269f2e75a4300b61121c540eb8c3e57ba44329f
CHUNK_START id=32db3e3783df_c001 start_line=1 end_line=88
````markdown
# 🏛️ MASTER PLAN: Context Governance Framework (v2.0 + Multi-Agent)

Este plano consolida as estratégias de **Automação de Manutenção** e **Especialização Cognitiva (Multi-Agent)** em um único framework modular, pronto para escalar de pequenos MVPs a grandes sistemas.

## 🕒 Metadados
- **Versão:** 2.0 (Consolidada)
- **Foco:** Eficiência de Tokens, Governança Rígida e Automação Python
- **Status:** Aguardando Aprovação Final

---

## 🧩 1. Estrutura de Arquivos em Camadas (`.context/`)

A pasta será organizada em quatro camadas lógicas para isolamento operacional:

### 🧠 Camada Cognitiva (The Brain)
- **`MASTER_FLOW.md`**: Diretriz mestre de navegação.
- **`RULES.md`**: Protocolos de conduta ("A Lei").
- **`AGENT_REGISTRY.md`**: DNS de papéis, permissões e isolamento.
- **`PROMPT_LIBRARY.md`**: Biblioteca de templates de prompts.
- **`PRD.md`**: Requisito em execução (O "Norte").
- **`ROADMAP.md`**: Metas e fases (O Planejamento).

### 🛠️ Camada de Manutenção (The Housekeeper)
- **`JOURNAL.md`**: Log vivo (limite heurístico de tokens).
- **`TECHNICAL_REQUIREMENTS.md`**: Inventário técnico consolidado.
- **`rebuild_guide.md`**: Manual de setup e infra.
- **`schema.sql`**: Snapshot do banco de dados.
- **`ARCHITECTURE.md`**, `TESTS.md`, `rx-anatomy.md`, `rx-biology.md`.
- **`_archive_context/`**: Memória de longo prazo.

### 📊 Camada de Monitoramento (The Dashboard)
- **`CONTEXT_HEALTH.md`**: Status dashboard técnico e cognitivo.

### ⚙️ Camada de Automação (The Arms)
- **`_scripts/`**: Scripts Python com `#!/usr/bin/env python3`.

---

## 📜 2. Protocolos Integrados em `RULES.md`

1.  **🛡️ Checklist de Carga (Obrigatório):** Antes de codificar, validar carga de:

````
CHUNK_END id=aa78525fb574_c028
CHUNK_START id=aa78525fb574_c029 start_line=8401 end_line=8700
````markdown
    - [ ] Global (Rules, MasterFlow, Roadmap)
    - [ ] Role (Registry-defined)
    - [ ] Ephemeral (PRD ativo + Journal tail 30-50 lines)
2.  **🔒 Context Gate:** Verificação de integridade Schema vs PRD.
3.  **🤖 Active Role Declaration:** Início de tarefa com `🤖 Ativando @[role]`.
4.  **🔢 Heurística de Token (Session Budget):** Disparar alerta de reset/purge ao detectar:
    - `~15-20 trocas densas` OU `~50k caracteres no prompt`.
5.  **🤝 Handoff Protocol:** Registro estruturado no `JOURNAL.md` em trocas de domínio.

---

## 🐍 3. Automação Python (`.context/_scripts/`)

Scripts unificados que entendem a hierarquia de agentes:

- **`validate_context.py`**: Checa integridade de arquivos, conformidade de roles e saúde geral.
- **`purge_journal.py`**: Arquiva 70% do log e gera uma semente de contexto no topo do arquivo atual.
- **`sync_project.py`**: Atualiza `TECHNICAL_REQUIREMENTS.md` lendo o `package.json` e `schema.sql`.

---

## 📈 4. Dashboard de Saúde (`CONTEXT_HEALTH.md`)

```markdown
# 📊 Context Health Check
| Métrica | Status | Pilar |
| :--- | :--- | :--- |
| Journal Line Count | [ 412 / 600 ] | Manutenção |
| Active Role | @frontend-specialist | Cognitivo |
| Schema Consistency | ✅ Synchronized | DB-First |
| Token Window | ⚠️ 78k (80%) | Sessão |
```

---

## 🚦 Roadmap de Execução

1.  **Fase 1: Estrutura MD** (Criar Registry, Prompt Library e Health).
2.  **Fase 2: As Leis** (Atualizar Master Flow e Rules com a lógica Multi-Agent).
3.  **Fase 3: Os Braços** (Implementar scripts Python em `_scripts/`).
4.  **Fase 4: Finalização** (Git Commit + Walkthrough).

---

> [!IMPORTANT]
> Este plano prioriza a **independência**. O projeto pode ser operado em "Modo Solo" (Single Agent) usando a role `@fullstack-generalist`, ou em "Modo Escala" (Multi-Agent) conforme a necessidade.

````
CHUNK_END id=32db3e3783df_c001
FILE_END id=file_32db3e3783df

---
<a id="file_2a788cb45159"></a>
FILE_START id=file_2a788cb45159 path=planos/multi_agent_plan.md domain=docs lang=markdown lines=62 bytes=2824 mtime=2026-04-10T23:32:27.825062+00:00 sha1=71ea8355ff980c67c66959bec1e4782108bad081
CHUNK_START id=2a788cb45159_c001 start_line=1 end_line=62
```markdown
# 🤖 Plano de Implementação: Arquitetura Multi-Agent

Este plano detalha a especialização do template com foco em **Especialização de Papéis**, **Isolamento de Contexto** e **Protocolos de Handoff**. O objetivo é transformar o agente em um sistema de engenharia cognitiva coordenado.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Roles, Context Isolation & Token Efficiency
- **Status:** Aguardando Aprovação (Em Separado)

---

## 🧩 1. Novos Componentes de Estrutura

### [REFINED] `AGENT_REGISTRY.md`
- **Conceito:** DNS cognitivo e Manifesto de Especialidades.
- **Regra de Ouro:** "Não registrado = Não executado".
- **Conteúdo Robusto:** Tabela com Roles (`@db-architect`, `@frontend-specialist`, `@backend-engineer`, `@qa-validator`, `@devops-guardian`, `@context-keeper`, `@fullstack-generalist`), permissões granulares de escrita e gatilhos de ativação.
- **Human Insights:** Blocos de contexto explicando o "porquê" das decisões técnicas para futuras IAs.

### [NEW] `PROMPT_LIBRARY.md`
- **Função:** Catálogo de templates de prompts de alta performance.
- **Conteúdo:** Instruções estruturadas para tarefas repetitivas (ex: "Criação de Componente", "Análise de Bug Crítico", "Escrita de Documentação").

---

## 📑 2. Protocolos de Handoff & Isolamento

````
CHUNK_END id=aa78525fb574_c036
CHUNK_START id=aa78525fb574_c037 start_line=10801 end_line=11100
````markdown

### 🛡️ Camadas de Isolamento (Context Layering)
Implementação de carregamento por camadas no `RULES.md`:
1.  **🌍 Global (Sempre):** `RULES.md`, `MASTER_FLOW.md`, `ROADMAP.md`.
2.  **🎯 Role-Specific:** Definido no registry (ex: `@db` lê `schema.sql`).
3.  **📦 Task-Ephemeral:** `PRD.md` ativo e últimas 30-50 linhas do `JOURNAL.md`.
4.  **🗃️ Deep Archive:** Acesso apenas sob demanda explícita.

### 🤝 Protocolo de Handoff Estruturado
Tarefas cross-domain exigem registro de estado no `JOURNAL.md` antes da troca:
- **Formato:** `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [Checkpoint Técnico] | Próximo: [Ação]`

---

## 🛠️ 3. Integração com o Workflow Atual

### [MODIFY] `RULES.md`
- Adicionar a seção **3.1 Protocolo Multi-Agent**.
- Definir a obrigatoriedade da declaração de ativação: `🤖 Ativando @[role] | Tarefa: [X]`.

### [MODIFY] `MASTER_FLOW.md`
- Incluir `AGENT_REGISTRY.md` e `PROMPT_LIBRARY.md` no diagrama de árvore.
- Adicionar o ciclo de vida da sessão Multi-Agent.

---

## 🚦 Próximos Passos

1.  **Revisão do Plano** em paralelo com o plano de Automação (v2.0).
2.  **Criação dos arquivos MD** com os templates pré-definidos.
3.  **Simulação de Handoff** para testagem da lógica de semente (`Seed Context`).

---

> [!TIP]
> Esta arquitetura permite que o projeto escale para milhares de linhas de código sem que a IA perca o foco ou alucine por excesso de arquivos irrelevantes na janela de contexto.

```
CHUNK_END id=2a788cb45159_c001
FILE_END id=file_2a788cb45159

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=52 bytes=1722 mtime=2026-04-11T03:13:56.439267+00:00 sha1=7dd7ff3a9bf3b72409e48c7e7e770ef8985daba2
CHUNK_START id=350a79f8b829_c001 start_line=1 end_line=52
```python
#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto (v2.2.1 Premium)
Orquestrador multiplataforma para validacao, sincronia e limpeza.
"""
import sys
import subprocess
from pathlib import Path

# Configurações
BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"

def run_script(name):
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} nao encontrado em {SCRIPTS_DIR}")
        sys.exit(1)
    
    print(f"[RUN] Executando {name}...")
    try:
        # Usa o mesmo interpretador atual para garantir consistência
        subprocess.run([sys.executable, str(script_path)], check=True)
        print(f"[OK] Concluido: {name}\n")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Falha em {name}. Pipeline abortado.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("[USAGE] python run_context.py [validate|purge|sync|cleanup|all|help]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "validate": run_script("validate_context.py")
    elif cmd == "purge":  run_script("purge_journal.py")
    elif cmd == "sync":   run_script("sync_project.py")
    elif cmd == "cleanup": run_script("cleanup_specs.py")
    elif cmd == "all":
        run_script("validate_context.py")
        run_script("sync_project.py")
        run_script("cleanup_specs.py")
        print("[DONE] Pipeline completo finalizado (Validate -> Sync -> Cleanup).")
    elif cmd in ["help", "--help", "-h"]:
        print("Comandos: validate | purge | sync | cleanup | all")
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()

```
CHUNK_END id=350a79f8b829_c001
FILE_END id=file_350a79f8b829

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=38 bytes=1386 mtime=2026-04-11T02:57:36.569915+00:00 sha1=e6604f22108387e02990d6bc08fc703d62cb82f6
CHUNK_START id=86bac54f32d7_c001 start_line=1 end_line=38
```bash
#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - Orquestrador Universal de Contexto v2.2
# ---------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"

# 🔍 Detecção robusta de Python
if command -v python3 &>/dev/null; then PYTHON="python3"
elif command -v python &>/dev/null; then PYTHON="python"
else echo "❌ Erro: Python não encontrado no PATH."; exit 1; fi

run_script() {
  local script_name="$1"
  echo "▶️ Executando $script_name..."
  if ! $PYTHON "$SCRIPT_DIR/$script_name"; then
    echo "❌ Falha em $script_name. Pipeline abortado."; exit 1;
  fi
  echo -e "✅ Concluído: $script_name\n"
}

[[ $# -eq 0 ]] && { echo "🛠️ Uso: $0 [validate|purge|sync|cleanup|all|help]"; exit 1; }

case "$1" in
  validate) run_script "validate_context.py" ;;
  purge)    run_script "purge_journal.py" ;;
  sync)     run_script "sync_project.py" ;;
  cleanup)  run_script "cleanup_specs.py" ;;
  all)
    run_script "validate_context.py"
    run_script "sync_project.py"
    run_script "cleanup_specs.py"
    echo "🎉 Pipeline completo finalizado (Validate → Sync → Cleanup)."
    ;;
  help|--help|-h) echo "Comandos: validate | purge | sync | cleanup | all" ;;
  *) echo "❌ Comando desconhecido: $1"; exit 1 ;;
esac

```
CHUNK_END id=86bac54f32d7_c001
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=89 bytes=3753 mtime=2026-04-11T01:08:20.157384+00:00 sha1=7179930319fcc060058fbd50dcb63770bc05bc28
CHUNK_START id=4c6bbd05056e_c001 start_line=1 end_line=89
```python
import unittest
import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

class TestContextGovernance(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_root = self.test_dir
        self.context_dir = self.project_root / ".context"
        self.scripts_dir = self.context_dir / "_scripts"
        
        # Caminho real dos scripts
        self.repo_root = Path(__file__).parent.parent
        self.real_scripts_dir = self.repo_root / ".context" / "_scripts"
        
        # Cria estrutura de camadas
        for layer in ["brain", "maintenance", "monitoring", "_scripts"]:
            (self.context_dir / layer).mkdir(parents=True, exist_ok=True)
        (self.context_dir / "maintenance" / "_archive_context" / "journals").mkdir(parents=True, exist_ok=True)

        # Copia scripts reais para o sandbox
        for script in ["validate_context.py", "purge_journal.py", "sync_project.py"]:
            shutil.copy(self.real_scripts_dir / script, self.scripts_dir / script)

        # Cria arquivos base vazios
        for f in ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")
        
        for f in ["maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md", "maintenance/JOURNAL.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")

        self.python_cmd = sys.executable

    def tearDown(self):
        # Limpa sandbox
        shutil.rmtree(self.test_dir)

    def run_script(self, name):
        script_path = self.scripts_dir / name
        result = subprocess.run(
            [self.python_cmd, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=self.project_root
        )
        return result

    def test_validate_integrity(self):
        # Adiciona uma tabela válida em AGENT_REGISTRY para passar no check
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertIn("[SUCCESS]", res.stdout)

    def test_validate_missing_file(self):
        (self.context_dir / "brain/AGENT_REGISTRY.md").unlink()

````
CHUNK_END id=aa78525fb574_c029
CHUNK_START id=aa78525fb574_c030 start_line=8701 end_line=8731
````markdown
        res = self.run_script("validate_context.py")
        self.assertIn("Arquivos ausentes", res.stdout)

    def test_purge_journal(self):
        journal = self.context_dir / "maintenance/JOURNAL.md"
        journal.write_text("## 📅 2024\nEntry 1\n\n## 📅 2024\nEntry 2", encoding="utf-8")
        res = self.run_script("purge_journal.py")
        self.assertIn("[OK] Purge concluido", res.stdout)
        
        # Verifica se arquivo foi criado no archive
        archive_files = list((self.context_dir / "maintenance/_archive_context/journals").glob("*.md"))
        self.assertGreaterEqual(len(archive_files), 1)

    def test_sync_project(self):
        # Simula package.json e schema.sql
        (self.project_root / "package.json").write_text('{"dependencies":{"test":"1.0"}}', encoding="utf-8")
        (self.context_dir / "maintenance/schema.sql").write_text("CREATE TABLE users (id INT);", encoding="utf-8")
        
        res = self.run_script("sync_project.py")
        self.assertIn("[OK] TECHNICAL_REQUIREMENTS.md sincronizado", res.stdout)
        
        req_content = (self.context_dir / "maintenance/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")
        self.assertIn("users", req_content)
        self.assertIn("test", req_content)

if __name__ == "__main__":
    unittest.main()

```
CHUNK_END id=4c6bbd05056e_c001
FILE_END id=file_4c6bbd05056e

````
CHUNK_END id=aa78525fb574_c030
FILE_END id=file_aa78525fb574

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=155 bytes=5469 mtime=2026-04-11T02:29:46.289656+00:00 sha1=18e30807c6ef1ce94e3619f19f8ec2bd93f77c52
CHUNK_START id=c59135753d26_c001 start_line=1 end_line=155
```bash
#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.2 Premium+)
# -----------------------------------------------------------------------------
# Versão Suprema: Fusão Antigravity + TLC Spec-Driven.
# Com detecção automática de gerenciador e motores de manutenção completos.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  command -v python3 >/dev/null 2>&1 || PYTHON="python3"
  command -v python >/dev/null 2>&1 || PYTHON="python"
  [ -z "${PYTHON:-}" ] && error "python3 ou python e obrigatorio."
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi

````
CHUNK_END id=aa78525fb574_c037
CHUNK_START id=aa78525fb574_c038 start_line=11101 end_line=11400
````markdown
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity AI-Ready Framework v2.2 Premium+..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop TLC..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança e integração TLC..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit + TLC Fusion)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT). O workshop \`.specs\` e o espaco de execucao efemera.

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo e handoffs.
- .specs/: Workbench atômico (Regra de 48h/Max 3).

🔄 4. Gatilhos Operacionais
- "Inicie a fase de SPECIFY para o PRD #[ID]": IA cria spec atômica no .specs/.
- "Atualize contexto": Sincronizacao proativa via sync_project.py.
EOF

cat > .context/brain/TLC_INTEGRATION.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 🔗 TLC_INTEGRATION.md
Ponte entre Governança (.context/) e Execução Atômica (.specs/).

## 🔄 Ciclo de Vida Híbrido
1. INTENT -> PRD.md ativo define escopo.
2. SPECIFY -> IA cria .specs/features/[nome]/spec.md.
3. IMPLEMENT -> Geração de código baseada na spec.
4. VERIFY -> STATE.md marcado como ✅ PASSED.
5. SYNC -> Lições para o JOURNAL.md e limpeza da spec.
EOF

# (Injeção dos Motores Reais v2.2 Premium+)
cat > .context/_scripts/validate_context.py << 'EOF'
#!/usr/bin/env python3
import os, sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQUIRED = ["brain/RULES.md", "brain/PRD.md", "maintenance/JOURNAL.md"]
def check_specs():
    specs = CONTEXT_DIR.parent / ".specs/features"
    if not specs.exists(): return True
    return all((d / "STATE.md").exists() for d in specs.iterdir() if d.is_dir())
def validate():
    print("--- Validacao v2.2 Premium+ ---")
    missing = [f for f in REQUIRED if not (CONTEXT_DIR / f).exists()]
    if missing or not check_specs(): sys.exit(1)
    print("✅ Contexto e Workshop integros.")
if __name__ == "__main__": validate()
EOF

cat > .context/_scripts/cleanup_specs.py << 'EOF'
#!/usr/bin/env python3
import os, shutil, time
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
SPECS_DIR = SCRIPT_DIR.parent.parent / ".specs" / "features"
ARCHIVE_DIR = SCRIPT_DIR.parent / "maintenance" / "_archive_context" / "specs"
def cleanup():
    if not SPECS_DIR.exists(): return
    specs = sorted([d for d in SPECS_DIR.iterdir() if d.is_dir()], key=os.path.getmtime)
    while len(specs) > 3:
        shutil.move(str(specs.pop(0)), str(ARCHIVE_DIR))
    print("[OK] Manutencao de specs concluida.")
if __name__ == "__main__": cleanup()
EOF

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
const runner = '$PKG_MGR' === 'npm' ? 'npm run' : '$PKG_MGR';
Object.assign(pkg.scripts, {
  'context:validate': 'bash run_context.sh validate',
  'context:cleanup': 'bash run_context.sh cleanup',
  'context:all': runner + ' context:validate && ' + runner + ' context:cleanup',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:validate" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."

```
CHUNK_END id=c59135753d26_c001
FILE_END id=file_c59135753d26

---
<a id="file_fa288d1472d2"></a>
FILE_START id=file_fa288d1472d2 path=package-lock.json domain=config lang=json lines=32 bytes=785 mtime=2026-04-11T01:12:03.334672+00:00 sha1=e8450c2eeca43eabd30597b19a6cb24ad70fcddb
CHUNK_START id=fa288d1472d2_c001 start_line=1 end_line=32
```json
{
  "name": "template-ai-context-governance",
  "version": "2.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "template-ai-context-governance",
      "version": "2.0.0",
      "license": "MIT",
      "devDependencies": {
        "husky": "^9.1.7"
      }
    },
    "node_modules/husky": {
      "version": "9.1.7",
      "resolved": "https://registry.npmjs.org/husky/-/husky-9.1.7.tgz",
      "integrity": "sha512-5gs5ytaNjBrh5Ow3zrvdUUY+0VxIuWVL4i9irt6friV+BqdCfmV11CQTWMiBYWHbXhco+J1kHfTOUkePhCDvMA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "husky": "bin.js"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/typicode"
      }
    }
  }
}

```
CHUNK_END id=fa288d1472d2_c001
FILE_END id=file_fa288d1472d2

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=27 bytes=824 mtime=2026-04-11T03:09:58.961110+00:00 sha1=cf2b6e50daab5aa1b974f11af667be601738252b
CHUNK_START id=7030d0b2f71b_c001 start_line=1 end_line=27
```json
{
  "name": "ai-context-governance-template",
  "version": "2.2.0",
  "description": "AI-Ready Template with Layered Context Governance & Spec-Driven Execution",
  "scripts": {
    "context:validate": "python run_context.py validate",
    "context:sync": "python run_context.py sync",
    "context:cleanup": "python run_context.py cleanup",
    "context:purge": "python run_context.py purge",
    "context:capture": "python captura_projeto.py --emit-symbol-index --emit-import-map",
    "context:all": "python run_context.py all",
    "context:test": "python tests/test_context.py",
    "prepare": "husky"
  },
  "keywords": [
    "ai",
    "context-governance",
    "spec-driven",
    "multi-agent",
    "automation"
  ],
  "author": "Tales Avancini",
  "license": "MIT",
  "devDependencies": {
    "husky": "^9.1.7"
  }
}

```
CHUNK_END id=7030d0b2f71b_c001
FILE_END id=file_7030d0b2f71b

---
<a id="file_a9422a4b7476"></a>
FILE_START id=file_a9422a4b7476 path=planos/implementation_plan.md domain=docs lang=markdown lines=77 bytes=3338 mtime=2026-04-10T23:15:28.184032+00:00 sha1=37ad3605aae584ee4398621d92edd7b76058413e
CHUNK_START id=a9422a4b7476_c001 start_line=1 end_line=77
```markdown
# 🏛️ Plano de Expansão: Context Governance Framework (v2.0)

Este plano detalha a transição do template de um sistema de documentação estática para um framework de governança ativa, focado em **escala**, **automação** e **prevenção de drift**.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Automação em Python e Escala de Contexto
- **Status:** Aguardando Aprovação

---

## 🧩 1. Estrutura de Arquivos Ampliada

Vamos expandir a pasta `.context/` para incluir novas camadas de inteligência:

### [NEW] Novos Documentos de Governança
- **`PROMPT_LIBRARY.md`**: Catálogo de personas e templates de prompts específicos para garantir consistência entre sessões.
- **`SESSION_MANAGER.md`**: Regras de gerenciamento de janela de tokens, limites de sessão e snapshots de resumo.
- **`CONTEXT_HEALTH.md`**: Dashboard de saúde do contexto (métricas de linhas, divergências e obsolescência).
- **`AGENT_REGISTRY.md`**: Definição de papéis (Expertises) e permissões de escrita/leitura nos arquivos do contexto.

---

## 📜 2. Atualização dos Protocolos (`RULES.md`)

Injetaremos novos protocolos de segurança e eficiência no arquivo de leis do agente:

### 🔹 Context Gate (Validação Pré-Voo)
O Agente deve realizar um "Checklist de Integridade" antes de gerar código, validando se o PRD e o Schema estão sincronizados.

### 🔹 Session Budget (Gestão de Tokens)
Definição de limites claros: ao atingir 80% da janela de contexto (estimada), o agente **deve** realizar um purge do `JOURNAL.md` (via script) e gerar um resumo semente.

---

## 🛠️ 3. Automação com Python (`.context/_scripts/`)

Criaremos scripts em Python para tornar a governança ativa e independente do ambiente da IDE.

### #### [NEW] `validate_context.py`
- Verifica se o `schema.sql` contém os campos referenciados no PRD atual.
- Valida o limite de linhas do `JOURNAL.md`.
- Gera um alerta visual se o status em qualquer arquivo for `Stale` ou `Deprecated`.

### #### [NEW] `purge_journal.py`
- Executa a lógica de arquivamento: move os primeiros 70% do log para `_archive_context/journals/`.
- Mantém os 30% finais e insere um resumo gerado pela IA no topo como conexão lógica.

### #### [NEW] `init_context.py`
- Script de bootstrap que inicializa a estrutura em novos projetos, gera os metadados de tempo reais e cria o `schema.sql` inicial.

---

## 📈 4. Monitoramento (`CONTEXT_HEALTH.md`)

Criação do dashboard dinâmico que será atualizado periodicamente pelos scripts ou manualmente pela IA.

| Métrica | Limite | Ação em caso de Falha |
| :--- | :--- | :--- |
| JOURNAL size | 600 linhas | Trigger `purge_journal.py` |
| PRD sync | 100% | Bloqueio de geração de UI |
| Token Window | 128k (80%) | Trigger Snapshot de Sessão |

---

## 🚦 Próximos Passos (Workflow)

1.  **Aprovação do Plano** (Você).
2.  **Criação dos Arquivos MD** com os templates propostos.
3.  **Geração do Código Python** para cada script de automação.
4.  **Atualização do `MASTER_FLOW.md` e `RULES.md`** para refletir a nova arquitetura.
5.  **Validação Final** da estrutura completa.

---

> [!IMPORTANT]
> A implementação será feita de forma **não invasiva** e **não executável** conforme solicitado, apenas preparando o repositório para ser exportado para o GitHub.

```
CHUNK_END id=a9422a4b7476_c001
FILE_END id=file_a9422a4b7476

---
<a id="file_32db3e3783df"></a>
FILE_START id=file_32db3e3783df path=planos/master_plan.md domain=docs lang=markdown lines=88 bytes=3620 mtime=2026-04-10T23:48:33.652301+00:00 sha1=9269f2e75a4300b61121c540eb8c3e57ba44329f
CHUNK_START id=32db3e3783df_c001 start_line=1 end_line=88
````markdown
# 🏛️ MASTER PLAN: Context Governance Framework (v2.0 + Multi-Agent)

Este plano consolida as estratégias de **Automação de Manutenção** e **Especialização Cognitiva (Multi-Agent)** em um único framework modular, pronto para escalar de pequenos MVPs a grandes sistemas.

## 🕒 Metadados

````
CHUNK_END id=aa78525fb574_c038
CHUNK_START id=aa78525fb574_c039 start_line=11401 end_line=11700
````markdown
- **Versão:** 2.0 (Consolidada)
- **Foco:** Eficiência de Tokens, Governança Rígida e Automação Python
- **Status:** Aguardando Aprovação Final

---

## 🧩 1. Estrutura de Arquivos em Camadas (`.context/`)

A pasta será organizada em quatro camadas lógicas para isolamento operacional:

### 🧠 Camada Cognitiva (The Brain)
- **`MASTER_FLOW.md`**: Diretriz mestre de navegação.
- **`RULES.md`**: Protocolos de conduta ("A Lei").
- **`AGENT_REGISTRY.md`**: DNS de papéis, permissões e isolamento.
- **`PROMPT_LIBRARY.md`**: Biblioteca de templates de prompts.
- **`PRD.md`**: Requisito em execução (O "Norte").
- **`ROADMAP.md`**: Metas e fases (O Planejamento).

### 🛠️ Camada de Manutenção (The Housekeeper)
- **`JOURNAL.md`**: Log vivo (limite heurístico de tokens).
- **`TECHNICAL_REQUIREMENTS.md`**: Inventário técnico consolidado.
- **`rebuild_guide.md`**: Manual de setup e infra.
- **`schema.sql`**: Snapshot do banco de dados.
- **`ARCHITECTURE.md`**, `TESTS.md`, `rx-anatomy.md`, `rx-biology.md`.
- **`_archive_context/`**: Memória de longo prazo.

### 📊 Camada de Monitoramento (The Dashboard)
- **`CONTEXT_HEALTH.md`**: Status dashboard técnico e cognitivo.

### ⚙️ Camada de Automação (The Arms)
- **`_scripts/`**: Scripts Python com `#!/usr/bin/env python3`.

---

## 📜 2. Protocolos Integrados em `RULES.md`

1.  **🛡️ Checklist de Carga (Obrigatório):** Antes de codificar, validar carga de:
    - [ ] Global (Rules, MasterFlow, Roadmap)
    - [ ] Role (Registry-defined)
    - [ ] Ephemeral (PRD ativo + Journal tail 30-50 lines)
2.  **🔒 Context Gate:** Verificação de integridade Schema vs PRD.
3.  **🤖 Active Role Declaration:** Início de tarefa com `🤖 Ativando @[role]`.
4.  **🔢 Heurística de Token (Session Budget):** Disparar alerta de reset/purge ao detectar:
    - `~15-20 trocas densas` OU `~50k caracteres no prompt`.
5.  **🤝 Handoff Protocol:** Registro estruturado no `JOURNAL.md` em trocas de domínio.

---

## 🐍 3. Automação Python (`.context/_scripts/`)

Scripts unificados que entendem a hierarquia de agentes:

- **`validate_context.py`**: Checa integridade de arquivos, conformidade de roles e saúde geral.
- **`purge_journal.py`**: Arquiva 70% do log e gera uma semente de contexto no topo do arquivo atual.
- **`sync_project.py`**: Atualiza `TECHNICAL_REQUIREMENTS.md` lendo o `package.json` e `schema.sql`.

---

## 📈 4. Dashboard de Saúde (`CONTEXT_HEALTH.md`)

```markdown
# 📊 Context Health Check
| Métrica | Status | Pilar |
| :--- | :--- | :--- |
| Journal Line Count | [ 412 / 600 ] | Manutenção |
| Active Role | @frontend-specialist | Cognitivo |
| Schema Consistency | ✅ Synchronized | DB-First |
| Token Window | ⚠️ 78k (80%) | Sessão |
```

---

## 🚦 Roadmap de Execução

1.  **Fase 1: Estrutura MD** (Criar Registry, Prompt Library e Health).
2.  **Fase 2: As Leis** (Atualizar Master Flow e Rules com a lógica Multi-Agent).
3.  **Fase 3: Os Braços** (Implementar scripts Python em `_scripts/`).
4.  **Fase 4: Finalização** (Git Commit + Walkthrough).

---

> [!IMPORTANT]
> Este plano prioriza a **independência**. O projeto pode ser operado em "Modo Solo" (Single Agent) usando a role `@fullstack-generalist`, ou em "Modo Escala" (Multi-Agent) conforme a necessidade.

````
CHUNK_END id=32db3e3783df_c001
FILE_END id=file_32db3e3783df

---
<a id="file_2a788cb45159"></a>
FILE_START id=file_2a788cb45159 path=planos/multi_agent_plan.md domain=docs lang=markdown lines=62 bytes=2824 mtime=2026-04-10T23:32:27.825062+00:00 sha1=71ea8355ff980c67c66959bec1e4782108bad081
CHUNK_START id=2a788cb45159_c001 start_line=1 end_line=62
```markdown
# 🤖 Plano de Implementação: Arquitetura Multi-Agent

Este plano detalha a especialização do template com foco em **Especialização de Papéis**, **Isolamento de Contexto** e **Protocolos de Handoff**. O objetivo é transformar o agente em um sistema de engenharia cognitiva coordenado.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Roles, Context Isolation & Token Efficiency
- **Status:** Aguardando Aprovação (Em Separado)

---

## 🧩 1. Novos Componentes de Estrutura

### [REFINED] `AGENT_REGISTRY.md`
- **Conceito:** DNS cognitivo e Manifesto de Especialidades.
- **Regra de Ouro:** "Não registrado = Não executado".
- **Conteúdo Robusto:** Tabela com Roles (`@db-architect`, `@frontend-specialist`, `@backend-engineer`, `@qa-validator`, `@devops-guardian`, `@context-keeper`, `@fullstack-generalist`), permissões granulares de escrita e gatilhos de ativação.
- **Human Insights:** Blocos de contexto explicando o "porquê" das decisões técnicas para futuras IAs.

### [NEW] `PROMPT_LIBRARY.md`
- **Função:** Catálogo de templates de prompts de alta performance.
- **Conteúdo:** Instruções estruturadas para tarefas repetitivas (ex: "Criação de Componente", "Análise de Bug Crítico", "Escrita de Documentação").

---

## 📑 2. Protocolos de Handoff & Isolamento

### 🛡️ Camadas de Isolamento (Context Layering)
Implementação de carregamento por camadas no `RULES.md`:
1.  **🌍 Global (Sempre):** `RULES.md`, `MASTER_FLOW.md`, `ROADMAP.md`.
2.  **🎯 Role-Specific:** Definido no registry (ex: `@db` lê `schema.sql`).
3.  **📦 Task-Ephemeral:** `PRD.md` ativo e últimas 30-50 linhas do `JOURNAL.md`.
4.  **🗃️ Deep Archive:** Acesso apenas sob demanda explícita.

### 🤝 Protocolo de Handoff Estruturado
Tarefas cross-domain exigem registro de estado no `JOURNAL.md` antes da troca:
- **Formato:** `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [Checkpoint Técnico] | Próximo: [Ação]`

---

## 🛠️ 3. Integração com o Workflow Atual

### [MODIFY] `RULES.md`
- Adicionar a seção **3.1 Protocolo Multi-Agent**.
- Definir a obrigatoriedade da declaração de ativação: `🤖 Ativando @[role] | Tarefa: [X]`.

### [MODIFY] `MASTER_FLOW.md`
- Incluir `AGENT_REGISTRY.md` e `PROMPT_LIBRARY.md` no diagrama de árvore.
- Adicionar o ciclo de vida da sessão Multi-Agent.

---

## 🚦 Próximos Passos

1.  **Revisão do Plano** em paralelo com o plano de Automação (v2.0).
2.  **Criação dos arquivos MD** com os templates pré-definidos.
3.  **Simulação de Handoff** para testagem da lógica de semente (`Seed Context`).

---

> [!TIP]
> Esta arquitetura permite que o projeto escale para milhares de linhas de código sem que a IA perca o foco ou alucine por excesso de arquivos irrelevantes na janela de contexto.

```
CHUNK_END id=2a788cb45159_c001
FILE_END id=file_2a788cb45159

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=52 bytes=1722 mtime=2026-04-11T03:13:56.439267+00:00 sha1=7dd7ff3a9bf3b72409e48c7e7e770ef8985daba2
CHUNK_START id=350a79f8b829_c001 start_line=1 end_line=52
```python
#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto (v2.2.1 Premium)
Orquestrador multiplataforma para validacao, sincronia e limpeza.
"""
import sys
import subprocess
from pathlib import Path

# Configurações
BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"

def run_script(name):
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} nao encontrado em {SCRIPTS_DIR}")
        sys.exit(1)
    
    print(f"[RUN] Executando {name}...")
    try:
        # Usa o mesmo interpretador atual para garantir consistência
        subprocess.run([sys.executable, str(script_path)], check=True)
        print(f"[OK] Concluido: {name}\n")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Falha em {name}. Pipeline abortado.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("[USAGE] python run_context.py [validate|purge|sync|cleanup|all|help]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "validate": run_script("validate_context.py")
    elif cmd == "purge":  run_script("purge_journal.py")
    elif cmd == "sync":   run_script("sync_project.py")
    elif cmd == "cleanup": run_script("cleanup_specs.py")
    elif cmd == "all":
        run_script("validate_context.py")
        run_script("sync_project.py")
        run_script("cleanup_specs.py")
        print("[DONE] Pipeline completo finalizado (Validate -> Sync -> Cleanup).")
    elif cmd in ["help", "--help", "-h"]:
        print("Comandos: validate | purge | sync | cleanup | all")
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()

```
CHUNK_END id=350a79f8b829_c001
FILE_END id=file_350a79f8b829

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=38 bytes=1386 mtime=2026-04-11T02:57:36.569915+00:00 sha1=e6604f22108387e02990d6bc08fc703d62cb82f6
CHUNK_START id=86bac54f32d7_c001 start_line=1 end_line=38
```bash
#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - Orquestrador Universal de Contexto v2.2
# ---------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"

# 🔍 Detecção robusta de Python
if command -v python3 &>/dev/null; then PYTHON="python3"
elif command -v python &>/dev/null; then PYTHON="python"
else echo "❌ Erro: Python não encontrado no PATH."; exit 1; fi

run_script() {
  local script_name="$1"
  echo "▶️ Executando $script_name..."
  if ! $PYTHON "$SCRIPT_DIR/$script_name"; then
    echo "❌ Falha em $script_name. Pipeline abortado."; exit 1;
  fi
  echo -e "✅ Concluído: $script_name\n"
}

[[ $# -eq 0 ]] && { echo "🛠️ Uso: $0 [validate|purge|sync|cleanup|all|help]"; exit 1; }

case "$1" in
  validate) run_script "validate_context.py" ;;
  purge)    run_script "purge_journal.py" ;;
  sync)     run_script "sync_project.py" ;;
  cleanup)  run_script "cleanup_specs.py" ;;
  all)
    run_script "validate_context.py"
    run_script "sync_project.py"
    run_script "cleanup_specs.py"
    echo "🎉 Pipeline completo finalizado (Validate → Sync → Cleanup)."
    ;;
  help|--help|-h) echo "Comandos: validate | purge | sync | cleanup | all" ;;
  *) echo "❌ Comando desconhecido: $1"; exit 1 ;;
esac

```
CHUNK_END id=86bac54f32d7_c001
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=89 bytes=3753 mtime=2026-04-11T01:08:20.157384+00:00 sha1=7179930319fcc060058fbd50dcb63770bc05bc28
CHUNK_START id=4c6bbd05056e_c001 start_line=1 end_line=89
```python
import unittest
import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

class TestContextGovernance(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_root = self.test_dir
        self.context_dir = self.project_root / ".context"
        self.scripts_dir = self.context_dir / "_scripts"
        
        # Caminho real dos scripts
        self.repo_root = Path(__file__).parent.parent
        self.real_scripts_dir = self.repo_root / ".context" / "_scripts"
        
        # Cria estrutura de camadas
        for layer in ["brain", "maintenance", "monitoring", "_scripts"]:
            (self.context_dir / layer).mkdir(parents=True, exist_ok=True)
        (self.context_dir / "maintenance" / "_archive_context" / "journals").mkdir(parents=True, exist_ok=True)


````
CHUNK_END id=aa78525fb574_c039
CHUNK_START id=aa78525fb574_c040 start_line=11701 end_line=11768
````markdown
        # Copia scripts reais para o sandbox
        for script in ["validate_context.py", "purge_journal.py", "sync_project.py"]:
            shutil.copy(self.real_scripts_dir / script, self.scripts_dir / script)

        # Cria arquivos base vazios
        for f in ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")
        
        for f in ["maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md", "maintenance/JOURNAL.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")

        self.python_cmd = sys.executable

    def tearDown(self):
        # Limpa sandbox
        shutil.rmtree(self.test_dir)

    def run_script(self, name):
        script_path = self.scripts_dir / name
        result = subprocess.run(
            [self.python_cmd, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=self.project_root
        )
        return result

    def test_validate_integrity(self):
        # Adiciona uma tabela válida em AGENT_REGISTRY para passar no check
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertIn("[SUCCESS]", res.stdout)

    def test_validate_missing_file(self):
        (self.context_dir / "brain/AGENT_REGISTRY.md").unlink()
        res = self.run_script("validate_context.py")
        self.assertIn("Arquivos ausentes", res.stdout)

    def test_purge_journal(self):
        journal = self.context_dir / "maintenance/JOURNAL.md"
        journal.write_text("## 📅 2024\nEntry 1\n\n## 📅 2024\nEntry 2", encoding="utf-8")
        res = self.run_script("purge_journal.py")
        self.assertIn("[OK] Purge concluido", res.stdout)
        
        # Verifica se arquivo foi criado no archive
        archive_files = list((self.context_dir / "maintenance/_archive_context/journals").glob("*.md"))
        self.assertGreaterEqual(len(archive_files), 1)

    def test_sync_project(self):
        # Simula package.json e schema.sql
        (self.project_root / "package.json").write_text('{"dependencies":{"test":"1.0"}}', encoding="utf-8")
        (self.context_dir / "maintenance/schema.sql").write_text("CREATE TABLE users (id INT);", encoding="utf-8")
        
        res = self.run_script("sync_project.py")
        self.assertIn("[OK] TECHNICAL_REQUIREMENTS.md sincronizado", res.stdout)
        
        req_content = (self.context_dir / "maintenance/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")
        self.assertIn("users", req_content)
        self.assertIn("test", req_content)

if __name__ == "__main__":
    unittest.main()

```
CHUNK_END id=4c6bbd05056e_c001
FILE_END id=file_4c6bbd05056e

````
CHUNK_END id=aa78525fb574_c040
FILE_END id=file_aa78525fb574

---
<a id="file_9d2a5d7128b5"></a>
FILE_START id=file_9d2a5d7128b5 path=contexto_toc.md domain=docs lang=markdown lines=351 bytes=17009 mtime=2026-04-11T23:33:54.892099+00:00 sha1=2695ad4693da5bad3cf9c9b289aad3f0d8853417
CHUNK_START id=9d2a5d7128b5_c001 start_line=1 end_line=300
```markdown
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

```
CHUNK_END id=9d2a5d7128b5_c001
CHUNK_START id=9d2a5d7128b5_c002 start_line=301 end_line=351
```markdown
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

```
CHUNK_END id=9d2a5d7128b5_c002
FILE_END id=file_9d2a5d7128b5

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=155 bytes=5469 mtime=2026-04-11T02:29:46.289656+00:00 sha1=18e30807c6ef1ce94e3619f19f8ec2bd93f77c52
CHUNK_START id=c59135753d26_c001 start_line=1 end_line=155
```bash
#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.2 Premium+)
# -----------------------------------------------------------------------------
# Versão Suprema: Fusão Antigravity + TLC Spec-Driven.
# Com detecção automática de gerenciador e motores de manutenção completos.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  command -v python3 >/dev/null 2>&1 || PYTHON="python3"
  command -v python >/dev/null 2>&1 || PYTHON="python"
  [ -z "${PYTHON:-}" ] && error "python3 ou python e obrigatorio."
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity AI-Ready Framework v2.2 Premium+..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop TLC..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança e integração TLC..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit + TLC Fusion)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT). O workshop \`.specs\` e o espaco de execucao efemera.

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo e handoffs.
- .specs/: Workbench atômico (Regra de 48h/Max 3).

🔄 4. Gatilhos Operacionais
- "Inicie a fase de SPECIFY para o PRD #[ID]": IA cria spec atômica no .specs/.
- "Atualize contexto": Sincronizacao proativa via sync_project.py.
EOF

cat > .context/brain/TLC_INTEGRATION.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 🔗 TLC_INTEGRATION.md
Ponte entre Governança (.context/) e Execução Atômica (.specs/).

## 🔄 Ciclo de Vida Híbrido
1. INTENT -> PRD.md ativo define escopo.
2. SPECIFY -> IA cria .specs/features/[nome]/spec.md.
3. IMPLEMENT -> Geração de código baseada na spec.
4. VERIFY -> STATE.md marcado como ✅ PASSED.
5. SYNC -> Lições para o JOURNAL.md e limpeza da spec.
EOF

# (Injeção dos Motores Reais v2.2 Premium+)
cat > .context/_scripts/validate_context.py << 'EOF'
#!/usr/bin/env python3
import os, sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQUIRED = ["brain/RULES.md", "brain/PRD.md", "maintenance/JOURNAL.md"]
def check_specs():
    specs = CONTEXT_DIR.parent / ".specs/features"
    if not specs.exists(): return True
    return all((d / "STATE.md").exists() for d in specs.iterdir() if d.is_dir())
def validate():
    print("--- Validacao v2.2 Premium+ ---")
    missing = [f for f in REQUIRED if not (CONTEXT_DIR / f).exists()]
    if missing or not check_specs(): sys.exit(1)
    print("✅ Contexto e Workshop integros.")
if __name__ == "__main__": validate()
EOF

cat > .context/_scripts/cleanup_specs.py << 'EOF'
#!/usr/bin/env python3
import os, shutil, time
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
SPECS_DIR = SCRIPT_DIR.parent.parent / ".specs" / "features"
ARCHIVE_DIR = SCRIPT_DIR.parent / "maintenance" / "_archive_context" / "specs"
def cleanup():
    if not SPECS_DIR.exists(): return
    specs = sorted([d for d in SPECS_DIR.iterdir() if d.is_dir()], key=os.path.getmtime)
    while len(specs) > 3:
        shutil.move(str(specs.pop(0)), str(ARCHIVE_DIR))
    print("[OK] Manutencao de specs concluida.")
if __name__ == "__main__": cleanup()
EOF

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
const runner = '$PKG_MGR' === 'npm' ? 'npm run' : '$PKG_MGR';
Object.assign(pkg.scripts, {
  'context:validate': 'bash run_context.sh validate',
  'context:cleanup': 'bash run_context.sh cleanup',
  'context:all': runner + ' context:validate && ' + runner + ' context:cleanup',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:validate" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."

```
CHUNK_END id=c59135753d26_c001
FILE_END id=file_c59135753d26

---
<a id="file_fa288d1472d2"></a>
FILE_START id=file_fa288d1472d2 path=package-lock.json domain=config lang=json lines=32 bytes=785 mtime=2026-04-11T01:12:03.334672+00:00 sha1=e8450c2eeca43eabd30597b19a6cb24ad70fcddb
CHUNK_START id=fa288d1472d2_c001 start_line=1 end_line=32
```json
{
  "name": "template-ai-context-governance",
  "version": "2.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "template-ai-context-governance",
      "version": "2.0.0",
      "license": "MIT",
      "devDependencies": {
        "husky": "^9.1.7"
      }
    },
    "node_modules/husky": {
      "version": "9.1.7",
      "resolved": "https://registry.npmjs.org/husky/-/husky-9.1.7.tgz",
      "integrity": "sha512-5gs5ytaNjBrh5Ow3zrvdUUY+0VxIuWVL4i9irt6friV+BqdCfmV11CQTWMiBYWHbXhco+J1kHfTOUkePhCDvMA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "husky": "bin.js"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/typicode"
      }
    }
  }
}

```
CHUNK_END id=fa288d1472d2_c001
FILE_END id=file_fa288d1472d2

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=31 bytes=1038 mtime=2026-04-12T00:32:59.626503+00:00 sha1=6c784f371287b96b7551c37712e04c42e9270fbd
CHUNK_START id=7030d0b2f71b_c001 start_line=1 end_line=31
```json
{
  "name": "ai-context-governance-template",
  "version": "2.2.0",
  "description": "AI-Ready Template with Layered Context Governance & Spec-Driven Execution",
  "scripts": {
    "context:validate": "python run_context.py validate",
    "context:sync": "python run_context.py sync",
    "context:cleanup": "python run_context.py cleanup",
    "context:purge": "python run_context.py purge",
    "context:harness": "python run_context.py harness",
    "context:lint": "python run_context.py lint",
    "context:oracle": "python run_context.py oracle",
    "context:health": "python run_context.py health",
    "context:capture": "python captura_projeto.py --emit-symbol-index --emit-import-map",
    "context:all": "python run_context.py all",
    "context:test": "python tests/test_context.py",
    "prepare": "husky"
  },
  "keywords": [
    "ai",
    "context-governance",
    "spec-driven",
    "multi-agent",
    "automation"
  ],
  "author": "Tales Avancini",
  "license": "MIT",
  "devDependencies": {
    "husky": "^9.1.7"
  }
}

```
CHUNK_END id=7030d0b2f71b_c001
FILE_END id=file_7030d0b2f71b

---
<a id="file_a9422a4b7476"></a>
FILE_START id=file_a9422a4b7476 path=planos/implementation_plan.md domain=docs lang=markdown lines=77 bytes=3338 mtime=2026-04-10T23:15:28.184032+00:00 sha1=37ad3605aae584ee4398621d92edd7b76058413e
CHUNK_START id=a9422a4b7476_c001 start_line=1 end_line=77
```markdown
# 🏛️ Plano de Expansão: Context Governance Framework (v2.0)

Este plano detalha a transição do template de um sistema de documentação estática para um framework de governança ativa, focado em **escala**, **automação** e **prevenção de drift**.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Automação em Python e Escala de Contexto
- **Status:** Aguardando Aprovação

---

## 🧩 1. Estrutura de Arquivos Ampliada

Vamos expandir a pasta `.context/` para incluir novas camadas de inteligência:

### [NEW] Novos Documentos de Governança
- **`PROMPT_LIBRARY.md`**: Catálogo de personas e templates de prompts específicos para garantir consistência entre sessões.
- **`SESSION_MANAGER.md`**: Regras de gerenciamento de janela de tokens, limites de sessão e snapshots de resumo.
- **`CONTEXT_HEALTH.md`**: Dashboard de saúde do contexto (métricas de linhas, divergências e obsolescência).
- **`AGENT_REGISTRY.md`**: Definição de papéis (Expertises) e permissões de escrita/leitura nos arquivos do contexto.

---

## 📜 2. Atualização dos Protocolos (`RULES.md`)

Injetaremos novos protocolos de segurança e eficiência no arquivo de leis do agente:

### 🔹 Context Gate (Validação Pré-Voo)
O Agente deve realizar um "Checklist de Integridade" antes de gerar código, validando se o PRD e o Schema estão sincronizados.

### 🔹 Session Budget (Gestão de Tokens)
Definição de limites claros: ao atingir 80% da janela de contexto (estimada), o agente **deve** realizar um purge do `JOURNAL.md` (via script) e gerar um resumo semente.

---

## 🛠️ 3. Automação com Python (`.context/_scripts/`)

Criaremos scripts em Python para tornar a governança ativa e independente do ambiente da IDE.

### #### [NEW] `validate_context.py`
- Verifica se o `schema.sql` contém os campos referenciados no PRD atual.
- Valida o limite de linhas do `JOURNAL.md`.
- Gera um alerta visual se o status em qualquer arquivo for `Stale` ou `Deprecated`.

### #### [NEW] `purge_journal.py`
- Executa a lógica de arquivamento: move os primeiros 70% do log para `_archive_context/journals/`.
- Mantém os 30% finais e insere um resumo gerado pela IA no topo como conexão lógica.

### #### [NEW] `init_context.py`
- Script de bootstrap que inicializa a estrutura em novos projetos, gera os metadados de tempo reais e cria o `schema.sql` inicial.

---

## 📈 4. Monitoramento (`CONTEXT_HEALTH.md`)

Criação do dashboard dinâmico que será atualizado periodicamente pelos scripts ou manualmente pela IA.

| Métrica | Limite | Ação em caso de Falha |
| :--- | :--- | :--- |
| JOURNAL size | 600 linhas | Trigger `purge_journal.py` |
| PRD sync | 100% | Bloqueio de geração de UI |
| Token Window | 128k (80%) | Trigger Snapshot de Sessão |

---

## 🚦 Próximos Passos (Workflow)

1.  **Aprovação do Plano** (Você).
2.  **Criação dos Arquivos MD** com os templates propostos.
3.  **Geração do Código Python** para cada script de automação.
4.  **Atualização do `MASTER_FLOW.md` e `RULES.md`** para refletir a nova arquitetura.
5.  **Validação Final** da estrutura completa.

---

> [!IMPORTANT]
> A implementação será feita de forma **não invasiva** e **não executável** conforme solicitado, apenas preparando o repositório para ser exportado para o GitHub.

```
CHUNK_END id=a9422a4b7476_c001
FILE_END id=file_a9422a4b7476

---
<a id="file_32db3e3783df"></a>
FILE_START id=file_32db3e3783df path=planos/master_plan.md domain=docs lang=markdown lines=88 bytes=3620 mtime=2026-04-10T23:48:33.652301+00:00 sha1=9269f2e75a4300b61121c540eb8c3e57ba44329f
CHUNK_START id=32db3e3783df_c001 start_line=1 end_line=88
````markdown
# 🏛️ MASTER PLAN: Context Governance Framework (v2.0 + Multi-Agent)

Este plano consolida as estratégias de **Automação de Manutenção** e **Especialização Cognitiva (Multi-Agent)** em um único framework modular, pronto para escalar de pequenos MVPs a grandes sistemas.

## 🕒 Metadados
- **Versão:** 2.0 (Consolidada)
- **Foco:** Eficiência de Tokens, Governança Rígida e Automação Python
- **Status:** Aguardando Aprovação Final

---

## 🧩 1. Estrutura de Arquivos em Camadas (`.context/`)

A pasta será organizada em quatro camadas lógicas para isolamento operacional:

### 🧠 Camada Cognitiva (The Brain)
- **`MASTER_FLOW.md`**: Diretriz mestre de navegação.
- **`RULES.md`**: Protocolos de conduta ("A Lei").
- **`AGENT_REGISTRY.md`**: DNS de papéis, permissões e isolamento.
- **`PROMPT_LIBRARY.md`**: Biblioteca de templates de prompts.
- **`PRD.md`**: Requisito em execução (O "Norte").
- **`ROADMAP.md`**: Metas e fases (O Planejamento).

### 🛠️ Camada de Manutenção (The Housekeeper)
- **`JOURNAL.md`**: Log vivo (limite heurístico de tokens).
- **`TECHNICAL_REQUIREMENTS.md`**: Inventário técnico consolidado.
- **`rebuild_guide.md`**: Manual de setup e infra.
- **`schema.sql`**: Snapshot do banco de dados.
- **`ARCHITECTURE.md`**, `TESTS.md`, `rx-anatomy.md`, `rx-biology.md`.
- **`_archive_context/`**: Memória de longo prazo.

### 📊 Camada de Monitoramento (The Dashboard)
- **`CONTEXT_HEALTH.md`**: Status dashboard técnico e cognitivo.

### ⚙️ Camada de Automação (The Arms)
- **`_scripts/`**: Scripts Python com `#!/usr/bin/env python3`.

---

## 📜 2. Protocolos Integrados em `RULES.md`

1.  **🛡️ Checklist de Carga (Obrigatório):** Antes de codificar, validar carga de:
    - [ ] Global (Rules, MasterFlow, Roadmap)
    - [ ] Role (Registry-defined)
    - [ ] Ephemeral (PRD ativo + Journal tail 30-50 lines)
2.  **🔒 Context Gate:** Verificação de integridade Schema vs PRD.
3.  **🤖 Active Role Declaration:** Início de tarefa com `🤖 Ativando @[role]`.
4.  **🔢 Heurística de Token (Session Budget):** Disparar alerta de reset/purge ao detectar:
    - `~15-20 trocas densas` OU `~50k caracteres no prompt`.
5.  **🤝 Handoff Protocol:** Registro estruturado no `JOURNAL.md` em trocas de domínio.

---

## 🐍 3. Automação Python (`.context/_scripts/`)

Scripts unificados que entendem a hierarquia de agentes:

- **`validate_context.py`**: Checa integridade de arquivos, conformidade de roles e saúde geral.
- **`purge_journal.py`**: Arquiva 70% do log e gera uma semente de contexto no topo do arquivo atual.
- **`sync_project.py`**: Atualiza `TECHNICAL_REQUIREMENTS.md` lendo o `package.json` e `schema.sql`.

---

## 📈 4. Dashboard de Saúde (`CONTEXT_HEALTH.md`)

```markdown
# 📊 Context Health Check
| Métrica | Status | Pilar |
| :--- | :--- | :--- |
| Journal Line Count | [ 412 / 600 ] | Manutenção |
| Active Role | @frontend-specialist | Cognitivo |
| Schema Consistency | ✅ Synchronized | DB-First |
| Token Window | ⚠️ 78k (80%) | Sessão |
```

---

## 🚦 Roadmap de Execução

1.  **Fase 1: Estrutura MD** (Criar Registry, Prompt Library e Health).
2.  **Fase 2: As Leis** (Atualizar Master Flow e Rules com a lógica Multi-Agent).
3.  **Fase 3: Os Braços** (Implementar scripts Python em `_scripts/`).
4.  **Fase 4: Finalização** (Git Commit + Walkthrough).

---

> [!IMPORTANT]
> Este plano prioriza a **independência**. O projeto pode ser operado em "Modo Solo" (Single Agent) usando a role `@fullstack-generalist`, ou em "Modo Escala" (Multi-Agent) conforme a necessidade.

````
CHUNK_END id=32db3e3783df_c001
FILE_END id=file_32db3e3783df

---
<a id="file_2a788cb45159"></a>
FILE_START id=file_2a788cb45159 path=planos/multi_agent_plan.md domain=docs lang=markdown lines=62 bytes=2824 mtime=2026-04-10T23:32:27.825062+00:00 sha1=71ea8355ff980c67c66959bec1e4782108bad081
CHUNK_START id=2a788cb45159_c001 start_line=1 end_line=62
```markdown
# 🤖 Plano de Implementação: Arquitetura Multi-Agent

Este plano detalha a especialização do template com foco em **Especialização de Papéis**, **Isolamento de Contexto** e **Protocolos de Handoff**. O objetivo é transformar o agente em um sistema de engenharia cognitiva coordenado.

## 🕒 Metadados do Plano
- **Criado em:** 2026-04-10
- **Foco:** Roles, Context Isolation & Token Efficiency
- **Status:** Aguardando Aprovação (Em Separado)

---

## 🧩 1. Novos Componentes de Estrutura

### [REFINED] `AGENT_REGISTRY.md`
- **Conceito:** DNS cognitivo e Manifesto de Especialidades.
- **Regra de Ouro:** "Não registrado = Não executado".
- **Conteúdo Robusto:** Tabela com Roles (`@db-architect`, `@frontend-specialist`, `@backend-engineer`, `@qa-validator`, `@devops-guardian`, `@context-keeper`, `@fullstack-generalist`), permissões granulares de escrita e gatilhos de ativação.
- **Human Insights:** Blocos de contexto explicando o "porquê" das decisões técnicas para futuras IAs.

### [NEW] `PROMPT_LIBRARY.md`
- **Função:** Catálogo de templates de prompts de alta performance.
- **Conteúdo:** Instruções estruturadas para tarefas repetitivas (ex: "Criação de Componente", "Análise de Bug Crítico", "Escrita de Documentação").

---

## 📑 2. Protocolos de Handoff & Isolamento

### 🛡️ Camadas de Isolamento (Context Layering)
Implementação de carregamento por camadas no `RULES.md`:
1.  **🌍 Global (Sempre):** `RULES.md`, `MASTER_FLOW.md`, `ROADMAP.md`.
2.  **🎯 Role-Specific:** Definido no registry (ex: `@db` lê `schema.sql`).
3.  **📦 Task-Ephemeral:** `PRD.md` ativo e últimas 30-50 linhas do `JOURNAL.md`.
4.  **🗃️ Deep Archive:** Acesso apenas sob demanda explícita.

### 🤝 Protocolo de Handoff Estruturado
Tarefas cross-domain exigem registro de estado no `JOURNAL.md` antes da troca:
- **Formato:** `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [Checkpoint Técnico] | Próximo: [Ação]`

---

## 🛠️ 3. Integração com o Workflow Atual

### [MODIFY] `RULES.md`
- Adicionar a seção **3.1 Protocolo Multi-Agent**.
- Definir a obrigatoriedade da declaração de ativação: `🤖 Ativando @[role] | Tarefa: [X]`.

### [MODIFY] `MASTER_FLOW.md`
- Incluir `AGENT_REGISTRY.md` e `PROMPT_LIBRARY.md` no diagrama de árvore.
- Adicionar o ciclo de vida da sessão Multi-Agent.

---

## 🚦 Próximos Passos

1.  **Revisão do Plano** em paralelo com o plano de Automação (v2.0).
2.  **Criação dos arquivos MD** com os templates pré-definidos.
3.  **Simulação de Handoff** para testagem da lógica de semente (`Seed Context`).

---

> [!TIP]
> Esta arquitetura permite que o projeto escale para milhares de linhas de código sem que a IA perca o foco ou alucine por excesso de arquivos irrelevantes na janela de contexto.

```
CHUNK_END id=2a788cb45159_c001
FILE_END id=file_2a788cb45159

---
<a id="file_44c34e6237da"></a>
FILE_START id=file_44c34e6237da path=planos/roadmap_reactive_hok_v2_v3.md domain=docs lang=markdown lines=43 bytes=2070 mtime=2026-04-12T00:16:01.408542+00:00 sha1=bcab4c7525fa8c4ba078bf84d63965f3e60d3e23
CHUNK_START id=44c34e6237da_c001 start_line=1 end_line=43
```markdown
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

```
CHUNK_END id=44c34e6237da_c001
FILE_END id=file_44c34e6237da

---
<a id="file_6a4bd0586b20"></a>
FILE_START id=file_6a4bd0586b20 path=planos/walkthrough_hok_triad.md domain=docs lang=markdown lines=32 bytes=2243 mtime=2026-04-12T00:05:31.404227+00:00 sha1=0bbfa5d700f335f10599d185d0fa8e788cf93cac
CHUNK_START id=6a4bd0586b20_c001 start_line=1 end_line=32
```markdown
# 🚀 Walkthrough: Implantação da Tríade H.O.K (Governança Nível 3)

A semente transformou-se em um cérebro inteligente e reativo. Nós acabamos de entregar as 3 camadas do H.O.K (Harness, Oracle, Karpathy) de forma cirurgicamente perfeitamente integrada ao Orquestrador Python nativo que configuramos ontem. Nada de scripts quebrados no Windows ou vazamento de responsabilidades.

## 🛠️ O que foi construído nesta Sprint Atômica?

### 1. 🛡️ Harness (Validador de Contratos)
- Registramos o catálogo oficial no `.context/brain/HARNESS_REGISTRY.md`.
- Implementamos o `.context/_scripts/harness_runner.py` que entra para inspecionar, por exemplo, se a IA usou uma Spec que chama uma tabela SQL fantasma, barrando o fluxo antes do dano.

### 2. 🔍 Oracle (RAG Python Local)
- Demos à luz o `.context/_scripts/context_oracle.py`! Com ele, a IA tem a instrução de acionar `npm run context:oracle "meu problema"` caso identifique redundância, e assim o Oráculo retorna as melhores passagens das REGRAS em _std-lib_, com índice de `confidence` para ela analisar se está pisando em ovos.

### 3. 📖 Karpathy (Epistemologia Obrigatória)
- Criamos a pasta in-box inviolável `.context/maintenance/_archive_context/raw/` (via `.gitkeep`).
- Entregamos o `lint_wiki.py` no modo *Fase 1 (Warn-Only)*.
- Extra: o Regex foi isolado para evitar ser barulhento nos nossos Root Docs (como `RULES.md` e `MASTER_FLOW.md`).

## ⚙️ A Orquestração Central (run_context.py)

O script principal absorveu a tríade! Em vez de manchar o `package.json` com caminhos rígidos, nosso C-Level Handler (`run_context.py`) agora atende:
- `python run_context.py harness`
- `python run_context.py lint`
- `python run_context.py oracle`

Quando a validação dispara no prep-commit Husky, tudo gira nas engrenagens corretas no `npm run context:all`. 

---
> [!TIP]
> **Teste Agora Mesmo:** Escolha qualquer trecho sobre arquitetura em algum manual e peça pro oráculo responder. Execute `npm run context:oracle "O que é o TLC?"` e sinta o poder consultivo retornando sem nenhuma API adicional no meio.

**Status:** Missão e teste de pipeline finalizados sem um alerta sequer. O Cérebro Híbrido agora tem sistema imunológico. 🧬🦾

```
CHUNK_END id=6a4bd0586b20_c001
FILE_END id=file_6a4bd0586b20

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=66 bytes=2545 mtime=2026-04-12T00:32:50.142781+00:00 sha1=f5170093240fe60de348e136b6790ee461ae090e
CHUNK_START id=350a79f8b829_c001 start_line=1 end_line=66
```python
#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto (v2.2.1 Premium)
Orquestrador multiplataforma para validacao, sincronia e limpeza.
"""
import sys
import subprocess
from pathlib import Path

# Configurações
BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"

def run_script(name, args=None):
    if args is None:
        args = []
        
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} nao encontrado em {SCRIPTS_DIR}")
        sys.exit(1)
    
    print(f"[RUN] Executando {name}...")
    try:
        # Usa o mesmo interpretador atual para garantir consistência
        subprocess.run([sys.executable, str(script_path)] + args, check=True)
        print(f"[OK] Concluido: {name}\n")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Falha em {name}. Pipeline abortado.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("[USAGE] python run_context.py [validate|purge|sync|cleanup|all|help]")
        sys.exit(1)

    cmd = sys.argv[1]
    extra_args = sys.argv[2:]

    if cmd == "validate": run_script("validate_context.py", extra_args)
    elif cmd == "purge":  run_script("purge_journal.py", extra_args)
    elif cmd == "sync":   run_script("sync_project.py", extra_args)
    elif cmd == "cleanup": run_script("cleanup_specs.py", extra_args)
    elif cmd == "harness": run_script("harness_runner.py", extra_args)
    elif cmd == "lint":    run_script("lint_wiki.py", extra_args)
    elif cmd == "lint-strict": run_script("lint_wiki.py", ["--strict"] + extra_args)
    elif cmd == "oracle":  run_script("context_oracle.py", extra_args)
    elif cmd == "health":  run_script("health_sync.py", extra_args)
    elif cmd == "all":
        run_script("validate_context.py")
        run_script("sync_project.py")
        run_script("cleanup_specs.py")
        run_script("harness_runner.py")
        print("[RUN] Executando lint_wiki.py (Strict)...")
        run_script("lint_wiki.py", ["--strict"])
        print("[RUN] Sincronizando Health Dashboard...")
        run_script("health_sync.py")
        print("[DONE] Pipeline H.O.K. + Health completo (Validate -> Sync -> Cleanup -> Harness -> Lint-Strict -> Health).")
    elif cmd in ["help", "--help", "-h"]:
        print("Comandos: validate | purge | sync | cleanup | harness | lint | oracle | health | all")
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()

```
CHUNK_END id=350a79f8b829_c001
FILE_END id=file_350a79f8b829

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=38 bytes=1386 mtime=2026-04-11T02:57:36.569915+00:00 sha1=e6604f22108387e02990d6bc08fc703d62cb82f6
CHUNK_START id=86bac54f32d7_c001 start_line=1 end_line=38
```bash
#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - Orquestrador Universal de Contexto v2.2
# ---------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.context/_scripts"

# 🔍 Detecção robusta de Python
if command -v python3 &>/dev/null; then PYTHON="python3"
elif command -v python &>/dev/null; then PYTHON="python"
else echo "❌ Erro: Python não encontrado no PATH."; exit 1; fi

run_script() {
  local script_name="$1"
  echo "▶️ Executando $script_name..."
  if ! $PYTHON "$SCRIPT_DIR/$script_name"; then
    echo "❌ Falha em $script_name. Pipeline abortado."; exit 1;
  fi
  echo -e "✅ Concluído: $script_name\n"
}

[[ $# -eq 0 ]] && { echo "🛠️ Uso: $0 [validate|purge|sync|cleanup|all|help]"; exit 1; }

case "$1" in
  validate) run_script "validate_context.py" ;;
  purge)    run_script "purge_journal.py" ;;
  sync)     run_script "sync_project.py" ;;
  cleanup)  run_script "cleanup_specs.py" ;;
  all)
    run_script "validate_context.py"
    run_script "sync_project.py"
    run_script "cleanup_specs.py"
    echo "🎉 Pipeline completo finalizado (Validate → Sync → Cleanup)."
    ;;
  help|--help|-h) echo "Comandos: validate | purge | sync | cleanup | all" ;;
  *) echo "❌ Comando desconhecido: $1"; exit 1 ;;
esac

```
CHUNK_END id=86bac54f32d7_c001
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=89 bytes=3753 mtime=2026-04-11T01:08:20.157384+00:00 sha1=7179930319fcc060058fbd50dcb63770bc05bc28
CHUNK_START id=4c6bbd05056e_c001 start_line=1 end_line=89
```python
import unittest
import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

class TestContextGovernance(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_root = self.test_dir
        self.context_dir = self.project_root / ".context"
        self.scripts_dir = self.context_dir / "_scripts"
        
        # Caminho real dos scripts
        self.repo_root = Path(__file__).parent.parent
        self.real_scripts_dir = self.repo_root / ".context" / "_scripts"
        
        # Cria estrutura de camadas
        for layer in ["brain", "maintenance", "monitoring", "_scripts"]:
            (self.context_dir / layer).mkdir(parents=True, exist_ok=True)
        (self.context_dir / "maintenance" / "_archive_context" / "journals").mkdir(parents=True, exist_ok=True)

        # Copia scripts reais para o sandbox
        for script in ["validate_context.py", "purge_journal.py", "sync_project.py"]:
            shutil.copy(self.real_scripts_dir / script, self.scripts_dir / script)

        # Cria arquivos base vazios
        for f in ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")
        
        for f in ["maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md", "maintenance/JOURNAL.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")

        self.python_cmd = sys.executable

    def tearDown(self):
        # Limpa sandbox
        shutil.rmtree(self.test_dir)

    def run_script(self, name):
        script_path = self.scripts_dir / name
        result = subprocess.run(
            [self.python_cmd, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=self.project_root
        )
        return result

    def test_validate_integrity(self):
        # Adiciona uma tabela válida em AGENT_REGISTRY para passar no check
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertIn("[SUCCESS]", res.stdout)

    def test_validate_missing_file(self):
        (self.context_dir / "brain/AGENT_REGISTRY.md").unlink()
        res = self.run_script("validate_context.py")
        self.assertIn("Arquivos ausentes", res.stdout)

    def test_purge_journal(self):
        journal = self.context_dir / "maintenance/JOURNAL.md"
        journal.write_text("## 📅 2024\nEntry 1\n\n## 📅 2024\nEntry 2", encoding="utf-8")
        res = self.run_script("purge_journal.py")
        self.assertIn("[OK] Purge concluido", res.stdout)
        
        # Verifica se arquivo foi criado no archive
        archive_files = list((self.context_dir / "maintenance/_archive_context/journals").glob("*.md"))
        self.assertGreaterEqual(len(archive_files), 1)

    def test_sync_project(self):
        # Simula package.json e schema.sql
        (self.project_root / "package.json").write_text('{"dependencies":{"test":"1.0"}}', encoding="utf-8")
        (self.context_dir / "maintenance/schema.sql").write_text("CREATE TABLE users (id INT);", encoding="utf-8")
        
        res = self.run_script("sync_project.py")
        self.assertIn("[OK] TECHNICAL_REQUIREMENTS.md sincronizado", res.stdout)
        
        req_content = (self.context_dir / "maintenance/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")
        self.assertIn("users", req_content)
        self.assertIn("test", req_content)

if __name__ == "__main__":
    unittest.main()

```
CHUNK_END id=4c6bbd05056e_c001
FILE_END id=file_4c6bbd05056e
