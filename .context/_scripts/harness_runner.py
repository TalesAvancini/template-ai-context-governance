#!/usr/bin/env python3
"""
🛡️ harness_runner.py — Validação reativa de contratos (Harness Layer)
Valida spec vs schema, PRD vs código, e integridade de handoffs.
"""
import os, re, sys, json
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(fmt)
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
JOURNAL = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SCHEMA = CONTEXT_DIR / "maintenance" / "schema.sql"
HARNESS_REG = CONTEXT_DIR / "brain" / "HARNESS_REGISTRY.md"
PRD = CONTEXT_DIR / "brain" / "PRD.md"
INCEPTION = CONTEXT_DIR / "brain" / "INCEPTION.md"

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

def check_strategic_alignment():
    if not INCEPTION.exists() or not PRD.exists():
        return True, "INCEPTION/PRD ausentes (skip estratégico)"
    prd_text = PRD.read_text(encoding="utf-8").lower()
    inception_text = INCEPTION.read_text(encoding="utf-8")
    boundaries = re.findall(r'^-\s*NUNCA:\s*(.+)$', inception_text, re.I | re.MULTILINE)
    violations = [b.strip() for b in boundaries if re.search(re.escape(b.strip().lower()), prd_text)]
    if violations: return False, f"PRD viola boundaries estrategicas: {violations}"
    return True, "Strategic alignment OK"

def check_enrichment_integrity(prd_path: Path):
    """Valida seção Critical Dependencies semanticamente (bullet + Fonte: + market/)."""
    if not prd_path.exists(): return True, "PRD ausente (skip)"
    text = prd_path.read_text(encoding="utf-8")
    text_lower = text.lower()

    # Só exige a seção se o PRD mencionar integrações, compliance ou APIs externas
    trigger_keywords = [
        "integração", "integracao", "integration", 
        "compliance", "api externa", "external api", 
        "stripe", "lgpd", "meta", "aws", "webhook"
    ]
    if not any(kw in text_lower for kw in trigger_keywords):
        return True, "Sem menção a integrações/compliance (skip)"

    section_match = re.search(r'^## 🚨 Critical Dependencies\s*\n(.*?)(?=\n## |\Z)', text, re.I | re.DOTALL | re.MULTILINE)
    if not section_match: 
        return False, "Seção Critical Dependencies obrigatória para PRDs com integrações/compliance"
    
    deps_text = section_match.group(1)
    missing = []
    for line in deps_text.splitlines():
        line = line.strip()
        if line.startswith("-"):
            # Validação semântica: deve conter "Fonte:" e "market/"
            if "fonte:" not in line.lower() or "market/" not in line.lower():
                missing.append(line[:60])
                
    if missing: return False, f"Dependencies sem lastro em market/: {missing}"
    return True, "Enrichment contract OK"

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

def update_state_md(spec_dir: Path, status: str, detail: str = ""):
    state = spec_dir / "STATE.md"
    if not state.exists(): return
    content = f"---\nstatus: {status}\nupdated: {format_ts()}\ndetail: {detail}\n---\n"
    tmp = state.with_suffix(".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(state)
    status_print = status.replace("✅", "[OK]").replace("❌", "[FAIL]")
    print(f"[STATE.md] -> {status_print} na spec {spec_dir.name}")

def get_inception_status():
    """Lê o status do Inception mestre."""
    if not INCEPTION.exists(): return "MISSING"
    try:
        content = INCEPTION.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("status:"):
                # Captura o valor antes de qualquer comentário #
                return line.split(":")[1].strip().split("#")[0].strip()
    except:
        return "ERROR"
    return "UNKNOWN"

def main():
    # 0. Verificação de Estado (Hybrid Discovery)
    status = get_inception_status()
    if status == "DRAFT":
        print("[BYPASS] Inception em DRAFT. Pulando validações rigorosas do Harness.")
        print("[INFO] Siga as instruções em START_HERE.md para ativar a governança completa.")
        sys.exit(0)

    # 1. Definindo a pasta spec ativa
    features_dir = CONTEXT_DIR.parent / ".specs" / "features"
    spec_dir_env = os.environ.get("ACTIVE_SPEC")
    
    if spec_dir_env and (features_dir / spec_dir_env).exists():
        spec_dir = features_dir / spec_dir_env
    else:
        # Fallback: spec modificada mais recentemente
        if features_dir.exists():
            active = sorted([d for d in features_dir.iterdir() if d.is_dir()], key=os.path.getmtime, reverse=True)
            spec_dir = active[0] if active else None
        else:
            spec_dir = None

    spec_name = spec_dir.name if spec_dir else "manual"
    spec_path = spec_dir / "spec.md" if spec_dir else Path("dummy")
    
    checks = {
        "schema": check_schema_contract(spec_path),
        "handoff": check_handoff_integrity(JOURNAL.read_text(encoding="utf-8") if JOURNAL.exists() else ""),
        "strategy": check_strategic_alignment(),
        "enrichment": check_enrichment_integrity(PRD)
    }
    
    fails = [f"{k}: {v[1]}" for k, v in checks.items() if not v[0]]
    if fails:
        detail = " | ".join(fails)
        log_harness("fail", detail, spec_name)
        if spec_dir: update_state_md(spec_dir, "❌ FAILED", detail)
        print(f"[ERROR] Harness fail: {detail}")
        sys.exit(1)
    
    log_harness("pass", "All contracts valid", spec_name)
    if spec_dir: update_state_md(spec_dir, "✅ PASSED", "All checks passed")
    print("[OK] Harness pass: Contracts validated.")
    sys.exit(0)

if __name__ == "__main__":
    main()
