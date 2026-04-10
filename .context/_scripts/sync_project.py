#!/usr/bin/env python3
import os
import json

TECH_REQ_PATH = ".context/maintenance/TECHNICAL_REQUIREMENTS.md"
PKG_JSON_PATH = "package.json"

def sync_requirements():
    if not os.path.exists(PKG_JSON_PATH):
        print("[INFO] package.json não encontrado. Ignorando sync de dependências.")
        return

    with open(PKG_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    deps = data.get("dependencies", {})
    dev_deps = data.get("devDependencies", {})

    with open(TECH_REQ_PATH, 'r+', encoding='utf-8') as f:
        content = f.read()
        
        # Simplesmente anexa ao final se não houver seção
        f.write("\n\n## 📦 Auto-Synced Dependencies\n")
        for d, v in deps.items():
            f.write(f"- {d}: {v}\n")
        for d, v in dev_deps.items():
            f.write(f"- {d}: {v} (dev)\n")

    print(f"[OK] TECHNICAL_REQUIREMENTS.md atualizado com {len(deps) + len(dev_deps)} itens.")

if __name__ == "__main__":
    sync_requirements()
