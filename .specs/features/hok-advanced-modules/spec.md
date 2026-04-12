# 🚀 Spec: Automação Extrema H.O.K. (Security, Migrations, State Sync)

---

## 🎯 1. Objetivo (O Quê e Por Quê)
**Por Que:** O nível 3 de Governança (H.O.K.) precisa ser blindado contra vazamentos de tokens (Security), drift de dados (Migrations) e abandono de specs (State Sync).
**O Quê:** Implementar scanners de segredo, registro de migrações e atualização autônoma do `STATE.md`, roteando tudo nativamente pelo `run_context.py`.

## 📐 2. Escopo Técnico (Como)

### 2.1. Módulos Core
- `secrets_scanner.py`: Varredura via `git ls-files` para prevenir vazamentos na pipeline. Usa `.secrets-allowlist` para mitigar falsos positivos.
- `migration_registry.py`: Força a padronização de arquivos `.sql` e cruza a validação com `schema.sql`.
- `update_state_md`: Incorporado em `harness_runner.py`, muda interativamente o estado final da Spec.

### 2.2. Integração Orquestrador
- Modificar `run_context.py` para injetar `scan-secrets` e `check-migrations` no loop `all`.
- Ordem do pipeline: `validate → scan-secrets → sync → check-migrations → harness → lint → health`.

## 🧪 3. Critérios de Aceite (Done)
- [ ] O `secrets_scanner.py` usa `git ls-files` ou fallback estrito (`src`, `api`, `config`, `.context`).
- [ ] O `migration_registry.py` exige padrão `001_*.sql` e verifica contra `schema.sql`.
- [ ] O `harness_runner.py` escreve `✅ PASSED` ou `❌ FAILED` no `STATE.md` desta própria pasta local ao ser acionado.
- [ ] Todos os novos fluxos são orquestrados no `run_context.py` sem chamadas shell no `package.json`.
