# 🗺️ Plano de Implementação: Automação Extrema H.O.K.

**Data:** 2026-04-11
**Versão:** v2.3.1-refinement
**Status:** Planejamento Aprovado / Pronto para Execução

Este plano detalha a injeção dos módulos H.O.K Avançados: Secret Scanner, SQL Migration Registry e Automação de STATE.md. Foca em performance O(N) Git Files, whitelists epistemológicas e validação atômica de DB-First.

---

## 🕵️ Avaliação Crítica do Especialista (@system-architect)

O plano aborda três lacunas críticas na governança atual:
1. **Segurança (Leak Prevention):** Scanner reativo no pré-commit para impedir o vazamento de chaves (Stripe, AWS, Supabase).
2. **Consistência de Dados (Migrations):** Registro e ordenação de arquivos SQL para evitar 'drift' entre o código e o banco.
3. **Sincronia Cognitiva (State Sync):** Atualização automática do `STATE.md` das specs via Harness, eliminando specs "zumbis" no workshop.

---

## 🛠️ Mudanças Propostas

### 🔐 1. Secrets Scanner (`secrets_scanner.py`)
- Implementação usando `git ls-files` para garantir processamento instantâneo.
- Suporte a `.secrets-allowlist` para ignorar falsos positivos em documentações e exemplos.
- Regex de detecção para: Stripe, Supabase, Google Services e Padrões de ENV Frontend.

### 🗂️ 2. Migration Registry (`migration_registry.py`)
- Verificação de ordem estrita (`001_`, `002_`, etc).
- Check de integridade entre as migrations localizadas em `.context/maintenance/migrations/` e o snapshot global `schema.sql`.

### 🤖 3. State Automation (`harness_runner.py`)
- Injeção da rotina `update_state_md()`.
- Lógica de detecção de Spec ativa via variável de ambiente `ACTIVE_SPEC` ou fallback por data de modificação.

---

## 🚀 Ordem de Execução no Pipeline `all`
A ordem foi otimizada para falhar o mais rápido possível (fail-fast) em caso de violação grave:
1. `validate` (Arquivos/Estrutura)
2. `scan-secrets` (Segurança) ⬅️ **Novo**
3. `sync` (Dependências)
4. `check-migrations` (Banco de Dados) ⬅️ **Novo**
5. `harness` (Contratos + STATE Update) ⬅️ **Evolução**
6. `lint` (Epistemologia)
7. `health` (Dashboard)

---

## 📈 Critérios de Sucesso
- Pipeline bloqueia commit se uma chave API real for detectada fora do `.env`.
- `STATE.md` da spec ativa muda automaticamente para `✅ PASSED` ou `❌ FAILED` sem intervenção humana.
- Erros de ordem em arquivos SQL são detectados antes do merge.

> 💡 **Nota:** Este plano prioriza a estabilidade e performance em sistemas Windows e Monorepos.
