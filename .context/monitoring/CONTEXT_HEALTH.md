---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

| Métrica | Valor Atual| Limite / Heurística | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Pilar de Manutenção** | | | | |
| JOURNAL.md (linhas) | 412 | 600 | Manutenção | ✅ OK |
| JOURNAL.md (tamanho) | ~12k char | 50k char | Manutenção | ✅ OK |
| **Pilar Cognitivo** | | | | |
| Role Ativa | @frontend-specialist | N/A | Cognitivo | ⚠️ Em Task |
| PRD Ativo | #14 - Auth Flows | 1 por vez | Cognitivo | ✅ OK |
| **Pilar de Consistência** | | | | |
| Schema vs PRD Sync | 0 divergências | 0 | DB-First | ✅ OK |
| Último Sincronismo | 2h atrás | < 24h | Governança | ✅ OK |
| **Pilar de Sessão** | | | | |
| Turns de Sessão | 8 trocas | 20 trocas | Sessão | ✅ OK |
| Token Window Est. | ~78k | 128k | Sessão | ⚠️ 80% |

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até que a migration seja documentada.
- **Se Turns > 18:** Propor Snapshot ou Reset de Sessão antes de iniciar próxima tarefa grande.

---

## 📅 Histórico de Saúde (Log de Purges)
| Data | Ação | Agente | Resultado |
| :--- | :--- | :--- | :--- |
| 2026-04-10 | Purge Completo | @context-keeper | Journal resetado para seed de 30 linhas. |
