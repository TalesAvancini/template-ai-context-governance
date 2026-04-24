# 🧠 JOURNAL_SYNAPSE.md (Matriz de Gatilhos)

Este arquivo define as regras determinísticas de propagação de contexto. 
O Agente Executor deve cumprir as promessas geradas por estas regras para liberar o commit.

<!-- SYNAPSE_JSON_START -->
{
  "version": 1,
  "mode": "assist",
  "rules": [
    {
      "id": "sql_change",
      "when_any_changed": [".context/maintenance/schema.sql"],
      "require_journal_tags": ["SQL", "Schema"],
      "require_files_touched": [".context/maintenance/TECHNICAL_REQUIREMENTS.md"],
      "severity": "critical"
    },
    {
      "id": "new_context_path",
      "when_new_path_under": [".context/"],
      "require_files_touched": [".context/maintenance/rx-anatomy.md"],
      "severity": "critical"
    },
    {
      "id": "rules_change",
      "when_any_changed": [".context/brain/RULES.md"],
      "require_journal_tags": ["Governança", "Regras"],
      "require_metadata_bump": ["VERSION.md"],
      "severity": "critical"
    },
    {
      "id": "market_change",
      "when_any_changed": [".context/market/SSOT_MAP.md"],
      "require_journal_tags": ["Market", "Roteamento"],
      "severity": "warning"
    }
  ]
}
<!-- SYNAPSE_JSON_END -->

## 📋 Tabela de Referência Humana

| ID | Se mudar... | Exige atualização em... | Gravidade |
| :--- | :--- | :--- | :--- |
| `sql_change` | `schema.sql` | `TECHNICAL_REQUIREMENTS.md` | 🔴 CRITICAL |
| `new_context_path` | `.context/*` (novo) | `rx-anatomy.md` | 🔴 CRITICAL |
| `rules_change` | `RULES.md` | Journal + `VERSION.md` | 🔴 CRITICAL |
| `market_change` | `SSOT_MAP.md` | Tags de Market no Journal | 🟡 WARNING |

---
*Gerado via Antigravity Kit v2.5.2 | Protocolo SAM*
