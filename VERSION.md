# 🛸 Antigravity Kit Versioning
v2.5.2
Dash: [Antigravity Kit v2.5.2 - Independent QA Segregation]
Audit Status: ✅ PASSED
Release Date: 2026-04-23

📜 Changelog:
- **[Segregação QA]** Specs `type: standard` exigem `executor_context_id != validator_context_id` no harness.
- **[Contrato de Sprint]** Template oficial `.specs/_template.md` atualizado com campos de proveniência e assinatura.
- **[Hook Estável]** Pre-commit em modo read-only (`check-version`, `validate`, `scan-secrets`) para evitar drift automático em cadeia.
