#!/usr/bin/env python3
"""
🛡️ workflow_journal_auditor.py — Sistema Anti-Migué (SAM)
Audita a coerência entre Promessa (Journal), Obrigação (Synapse) e Realidade (Git).
"""

import os, re, sys, json, subprocess
from pathlib import Path

# Configuração de encoding para Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
JOURNAL_PATH = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SYNAPSE_PATH = CONTEXT_DIR / "maintenance" / "JOURNAL_SYNAPSE.md"

def get_git_diff():
    """Retorna lista de arquivos modificados e novos (não comitados)."""
    try:
        # Arquivos modificados/staged
        res = subprocess.run(["git", "diff", "--name-only", "HEAD"], capture_output=True, text=True, check=True)
        files = set(res.stdout.splitlines())
        # Arquivos novos (untracked)
        res_untracked = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True, check=True)
        files.update(res_untracked.stdout.splitlines())
        return files
    except Exception as e:
        print(f"[ERROR] Falha ao ler Git: {e}")
        return set()

def get_synapse_rules():
    """Extrai JSON do JOURNAL_SYNAPSE.md."""
    if not SYNAPSE_PATH.exists():
        return {"rules": []}
    content = SYNAPSE_PATH.read_text(encoding="utf-8")
    match = re.search(r"<!-- SYNAPSE_JSON_START -->\s*(.*?)\s*<!-- SYNAPSE_JSON_END -->", content, re.DOTALL)
    if not match:
        print("[WARN] Bloco JSON não encontrado no Synapse. Usando regras vazias.")
        return {"rules": []}
    try:
        return json.loads(match.group(1))
    except Exception as e:
        print(f"[ERROR] Falha ao parsear JSON do Synapse: {e}")
        return {"rules": []}

def get_latest_journal_entry():
    """Extrai a última entrada (seção ## 📅) do JOURNAL.md."""
    if not JOURNAL_PATH.exists():
        return ""
    content = JOURNAL_PATH.read_text(encoding="utf-8")
    entries = re.split(r"(?=## 📅)", content)
    # Ignora o cabeçalho do arquivo
    valid_entries = [e for e in entries if "## 📅" in e]
    return valid_entries[0] if valid_entries else ""

def audit():
    print("🤖 Iniciando Auditoria Anti-Migué (SAM)...")
    
    diff_files = get_git_diff()
    synapse = get_synapse_rules()
    mode = synapse.get("mode", "assist")
    entry = get_latest_journal_entry()
    
    if not entry:
        print("[FAIL] Nenhuma entrada recente encontrada no JOURNAL.md.")
        return 1

    violations = []
    obligations_met = True

    for rule in synapse.get("rules", []):
        rule_id = rule.get("id")
        triggered = False
        
        # 1. Verifica se a regra foi disparada por arquivos alterados
        for pattern in rule.get("when_any_changed", []):
            if any(re.search(re.escape(pattern), f) for f in diff_files):
                triggered = True
                break
        
        # 2. Verifica se a regra foi disparada por novos caminhos
        if not triggered:
            for pattern in rule.get("when_new_path_under", []):
                if any(f.startswith(pattern) for f in diff_files):
                    triggered = True
                    break

        if triggered:
            print(f"[INFO] Regra '{rule_id}' disparada.")
            # Verificar tags no Journal
            for tag in rule.get("require_journal_tags", []):
                if tag.lower() not in entry.lower():
                    violations.append(f"Regra '{rule_id}': Tag '{tag}' ausente no Journal.")
            
            # Verificar arquivos que deveriam ser tocados (propagação)
            for req_file in rule.get("require_files_touched", []):
                # O arquivo deve estar no diff (foi alterado)
                if not any(f.endswith(req_file) for f in diff_files):
                    violations.append(f"Regra '{rule_id}': Arquivo '{req_file}' não foi propagado (ausente no diff).")
                
                # O checkbox correspondente deve estar marcado no Journal
                checkbox_pattern = rf"-\s*\[x\]\s*`?{re.escape(req_file)}`?"
                if not re.search(checkbox_pattern, entry, re.I):
                    violations.append(f"Regra '{rule_id}': Checkbox [x] para '{req_file}' ausente ou desmarcado no Journal.")

    # Validação de Segregação de Contexto (Modo Strict)
    if mode == "strict" or "### Contrato de Validacao" in entry:
        exec_id = re.search(r"executor_context_id:\s*`?(.*?)`?", entry, re.I)
        valid_id = re.search(r"validator_context_id:\s*`?(.*?)`?", entry, re.I)
        status_match = re.search(r"status:\s*`?(.*?)`?", entry, re.I)
        
        e_id = exec_id.group(1).strip() if exec_id else ""
        v_id = valid_id.group(1).strip() if valid_id else ""
        status = status_match.group(1).strip() if status_match else ""

        if not e_id or v_id in ["", "[PENDENTE]"]:
            violations.append("Contrato de Validação incompleto (IDs ausentes).")
        elif e_id == v_id:
            violations.append("Violação de Segregação: executor_context_id == validator_context_id.")
        
        if "READY TO COMMIT" not in status and "🟢" not in status:
            violations.append("Status de validação não é 'READY TO COMMIT'.")

    # Resultado Final
    if violations:
        print("\n❌ VIOLAÇÕES DETECTADAS:")
        for v in violations:
            print(f"  - {v}")
        
        if mode == "strict":
            print("\n[FATAL] Modo STRICT: Pipeline bloqueado.")
            return 1
        else:
            print("\n[WARN] Modo ASSIST: Pipeline prosseguindo com avisos.")
            return 0
    else:
        print("\n✅ AUDITORIA PASSOU: Reality Check coerente com a Promessa.")
        return 0

if __name__ == "__main__":
    sys.exit(audit())
