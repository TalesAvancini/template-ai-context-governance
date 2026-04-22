#!/usr/bin/env python3
"""Verifica consistencia de versao via SSOT (VERSION.md) e matriz declarativa."""

import json
import re
import sys
from pathlib import Path

# .../.context/_scripts/check_version_consistency.py -> raiz em parents[2]
ROOT = Path(__file__).resolve().parents[2]
VERSION_FILE = ROOT / "VERSION.md"
TARGETS_FILE = ROOT / ".context" / "maintenance" / "version_targets.json"


def get_ssot_version():
    if not VERSION_FILE.exists():
        return None
    text = VERSION_FILE.read_text(encoding="utf-8")
    # Aceita vX.Y ou vX.Y.Z e normaliza para X.Y.Z
    match = re.search(r"^\s*v?(\d+)\.(\d+)(?:\.(\d+))?\s*$", text, re.MULTILINE)
    if not match:
        return None
    major, minor, patch = match.group(1), match.group(2), match.group(3) or "0"
    return f"{major}.{minor}.{patch}"


def normalize_version(value):
    value = value.strip()
    m = re.match(r"^(\d+)\.(\d+)(?:\.(\d+))?$", value)
    if not m:
        return value
    return f"{m.group(1)}.{m.group(2)}.{m.group(3) or '0'}"


def validate_targets(version):
    if not TARGETS_FILE.exists():
        return [".context/maintenance/version_targets.json (ausente)"]

    data = json.loads(TARGETS_FILE.read_text(encoding="utf-8"))
    targets = data.get("targets", [])
    mismatches = []

    for target in targets:
        rel_path = target["path"]
        fpath = ROOT / rel_path
        if not fpath.exists():
            mismatches.append(f"{rel_path} (ausente)")
            continue

        content = fpath.read_text(encoding="utf-8")
        flags = re.MULTILINE if target.get("multiline") else 0
        m = re.search(target["pattern"], content, flags)

        if not m:
            mismatches.append(f"{rel_path} (padrao nao encontrado)")
            continue

        found = normalize_version(m.group(1))
        if found != version:
            mismatches.append(f"{rel_path} (esperado {version}, achado {found})")

    return mismatches


if __name__ == "__main__":
    ssot_version = get_ssot_version()
    if not ssot_version:
        print("[FATAL] VERSION.md invalido ou ausente.")
        sys.exit(1)

    errors = validate_targets(ssot_version)
    if errors:
        print(f"\n[ERROR] Drift de versao detectado (SSOT: v{ssot_version}):")
        for err in errors:
            print(f"  - {err}")
        print("\n[FATAL] Corrija manualmente os arquivos-alvo e rode novamente.")
        sys.exit(1)

    print(f"[OK] Versao consistente: v{ssot_version}")
    sys.exit(0)
