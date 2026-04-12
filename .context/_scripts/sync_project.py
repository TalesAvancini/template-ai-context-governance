#!/usr/bin/env python3
"""
🔄 sync_project.py
Sincroniza TECH_REQUIREMENTS.md com package.json e schema.sql.
Usa marcadores <!-- AUTO-SYNC START/END --> para preservar edicoes humanas.
"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(fmt)
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

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
    now = format_ts()

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
