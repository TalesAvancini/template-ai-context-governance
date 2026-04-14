#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade.
Retorna exit 1 se houver qualquer alerta ou erro.
"""
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

REQUIRED_FILES = [
    "brain/RULES.md", 
    "brain/MASTER_FLOW.md", 
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md", 
    "maintenance/JOURNAL.md", 
    "maintenance/schema.sql", 
    "maintenance/TECHNICAL_REQUIREMENTS.md"
]

OPTIONAL_FILES = [
    "brain/INCEPTION.md"
]


JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000

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
    if "| Role | " not in content and "| Role " not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"

def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists(): return True, "Workshop inativo (OK)"
    features_dir = specs_dir / "features"
    if not features_dir.exists(): return False, "Diretorio features ausente no .specs"
    active_specs = [d for d in features_dir.iterdir() if d.is_dir()]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
    return True, f"OK ({len(active_specs)} specs ativas)"

def validate():
    print("--- Iniciando validação de contexto (v2.4 Hardened) ---")
    issues = []

    missing = check_files()
    if missing: issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else: print("[OK] Todos os arquivos obrigatórios presentes.")

    # Verifica camada estratégica (opcional)
    inception = CONTEXT_DIR / "brain/INCEPTION.md"
    if inception.exists(): print("[OK] INCEPTION.md presente (Camada Estratégica Ativa)")
    else: print("[INFO] INCEPTION.md ausente (Modo execução direta)")

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok: issues.append(f"[WARN] .specs/: {spec_msg}")
    else: print(f"[OK] .specs/: {spec_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok: issues.append(f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}")
    else: print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, token_ok = estimate_tokens()
    est_tokens = total_chars // 4
    if not token_ok: issues.append(f"[WARN] Contexto estimado alto: ~{est_tokens}k tokens. Execute purge.")
    else: print(f"[OK] Estimativa de contexto segura: ~{est_tokens}k tokens")

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok: issues.append(f"[WARN] AGENT_REGISTRY.md: {reg_msg}")
    else: print("[OK] AGENT_REGISTRY.md estrutura válida.")

    print("\n--- Relatório Final ---")
    if not issues:
        print("[SUCCESS] Contexto íntegro. Pronto para execução.")
        sys.exit(0)
    else:
        for issue in issues: print(issue)
        print("[FATAL] Resolva os alertas antes de gerar código.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        sys.exit(1)
