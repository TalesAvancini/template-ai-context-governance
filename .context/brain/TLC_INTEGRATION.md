---
Criado em: 2026-04-10 23:29
Ultima Atualizacao: 2026-04-10 23:29
Status: Ativo
---

# 🔗 TLC_INTEGRATION.md
> Ponte entre Governança de Longo Prazo (`.context/`) e Execução Atômica (`.specs/`).  
> 💡 *Insight Humano: O PRD diz O QUÊ e POR QUÊ. A SPEC diz COMO e QUANDO. O TLC orquestra a transição.*

## 🔄 Ciclo de Vida Híbrido
1. **INTENT** → `PRD.md` ativo define escopo e critérios de aceite.
2. **SPECIFY** → IA cria `.specs/features/[nome]/spec.md` com passos atômicos, contratos de API/DB e testes.
3. **IMPLEMENT** → Geração de código baseada na spec. Handoffs registrados no `JOURNAL.md`.
4. **VERIFY** → Testes passam → `STATE.md` marcado como `✅ PASSED`.
5. **SYNC** → Decisões arquiteturais e lições → `JOURNAL.md`. Spec arquivada ou deletada.

## 📏 Regras de Ouro
- 🔒 **Soberania do Contexto:** `.specs/` nunca sobrescreve `.context/`. Apenas alimenta a memória de longo prazo.
- 🧹 **Efemeridade:** Spec inativa >48h ou pós-merge → mover para `_archive_context/specs/` ou deletar.
- 🤝 **Handoff:** Handoff obrigatório no `JOURNAL.md` se a spec cruzar domínios (ex: `@backend` → `@qa`).
- ⚠️ **Divergência:** Se `spec.md` divergir de `schema.sql` ou `PRD.md` → parar e solicitar correção de contexto.

## 🤖 Fluxo de Ativação
`"Inicie a fase de SPECIFY para o PRD #[ID]"` → 
1. IA lê `PRD.md` + `schema.sql` + `JOURNAL.md` (últimas 30).
2. Cria `.specs/features/[nome]/` com `spec.md` e `STATE.md: draft`.
3. Executa passos atômicos → atualiza `STATE.md`.
4. Ao concluir: `✅ Spec passed. Deseja arquivar a spec e sincronizar o JOURNAL.md?`

---
> *Este documento garante que o "Cérebro" (Contexto) e o "Músculo" (TLC) operem em harmonia.*
