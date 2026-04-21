---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-21
Status: Ativo
---

# 🏗️ ARCHITECTURE: Pipeline de Classes & Fluxos
> 🤖 [SYSTEM HOOK] NÃO preencha antes de `schema.sql` existir. Siga DB-First.
> 📐 Formato: [Componente] → [Responsabilidade] → [Dependência] → [Endpoint/Route]
> ⚠️ REGRA DE MOCK: Se DB não estiver disponível, mockar em `src/__mocks__/` com o EXATO formato do `schema.sql`. Proibido inventar campos não declarados.

## 📦 Estrutura Atual (Exemplo)
| Camada | Arquivo/Dir | Função | SSOT Vinculado |
|--------|-------------|--------|----------------|
| DB | `maintenance/schema.sql` | Verdade estrutural | `run_context.py sync` |
| API | `src/api/` | Rotas, validação, auth | `schema.sql` + `PRD.md` |
| UI | `src/components/` | Interface, estado | `rx-anatomy.md` |
