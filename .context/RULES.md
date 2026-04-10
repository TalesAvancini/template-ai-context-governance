# 📜 RULES.md — Template Universal de Contexto & Governança

**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Antigravity Kit / Spec-Driven)

> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth) para o agente de IA. Se não está no contexto, não existe. O código deve ser o reflexo fiel do que está documentado aqui.

---

## 🧠 1. Protocolo de Manutenção do Contexto

A IA deve agir como o bibliotecário chefe do projeto. A consistência entre o Código e o Contexto é obrigatória.

### 📖 `JOURNAL.md` (O Diário de Bordo)
**O que é:** Memória de longo prazo de decisões de alto nível e resoluções de bugs complexos.
**Quando atualizar:**
- ✅ **Obrigatório:** Após corrigir um bug persistente ou alterar a lógica de negócio.
- ❌ **Proibido:** Não logar erros de sintaxe triviais ou mudanças de estilo (CSS/Indentação).
**Formato Padrão:**
```markdown
## 📅 Data/Hora
**Decisão/Bug:** [Descrição curta]
**Solução:** [O que foi feito]
**Implicação:** [Impacto no sistema]
```

### ⚙️ `TECHNICAL_REQUIREMENTS.md` (O Inventário Técnico)
**O que é:** Especificações estáticas do ecossistema (Stack, Schema, Keys).
**Quando atualizar:**
- ✅ **Obrigatório:** Sempre que houver mudança na `package.json` (novas libs).
- ✅ **Obrigatório:** Sempre que a estrutura do Banco de Dados for alterada (novas tabelas/colunas).
- ✅ **Obrigatório:** Ao integrar novos serviços externos (Stripe, Supabase, APIs de terceiros).
**Formato:** Listas concisas e tabelas. Sem narrativas.

### 🛠️ `rebuild_guide.md` (Manual de Reconstrução)
**O que é:** O guia "Pós-Mortem" para subir o projeto do zero em uma máquina limpa.
**Quando atualizar:**
- ✅ Ao descobrir "hacks" necessários para rodar o ambiente local.
- ✅ Ao configurar CI/CD ou variáveis de ambiente críticas.
- ✅ Se o deploy exigir passos manuais específicos (ex: "Rodar migration X antes do Y").

---

## 🗄️ 2. Protocolo Database-First (Anti-Alucinação)

É estritamente proibido construir código Frontend ou Lógica de Negócios baseada em suposições sobre a estrutura do Banco de Dados.

1.  **Verificação Obrigatória:** Antes de criar uma interface de usuário (UI) que dependa de dados, o Agente **DEVE** verificar o `schema.sql` ou o estado real do banco.
2.  **Aviso de Divergência:** Se a IA identificar que a UI exige um campo que não existe no DB, ela deve **parar a codificação** e avisar o usuário:
    > *"⚠️ Alerta: O Frontend exige a coluna 'user_avatar', mas ela não existe no Schema atual. Sugiro gerar a migration antes de prosseguir."*
3.  **Espelhamento Contínuo:** Toda alteração de estrutura feita diretamente no banco de produção deve ser imediatamente espelhada no arquivo `.context/schema.sql` ou na pasta de migrations.

---

## 🤖 3. Comportamento do Agente (Transparência)

Para garantir o controle total do gestor humano (Você), os Agentes não podem operar na "surdina".

1.  **Identificação:** Antes de iniciar uma tarefa complexa ou refatoração, a IA deve declarar qual skill ou agente está sendo ativado.
    *   *Exemplo:* `🤖 Ativando @frontend-specialist para refatorar o Header...`
2.  **Confirmação de Contexto:** Ao iniciar uma nova sessão ou tarefa grande, a IA deve ler os arquivos do `.context` antes de gerar código, para garantir que está usando as regras mais recentes.
3.  **Proatividade de Sincronização:**
    - Sempre que finalizar uma tarefa técnica relevante, a IA deve perguntar:
    > *"Essa alteração impacta a lógica de negócios ou banco de dados. Deseja que eu atualize o nosso contexto (JOURNAL ou Requirements) agora?"*

---

## 🔄 4. Gatilhos de Atualização Automática

O usuário pode forçar a sincronização usando os seguintes comandos ou equivalentes:

- *"Atualize o nosso contexto"* -> A IA sintetiza as mudanças recentes e atualiza o `JOURNAL.md` e verifica se o `TECHNICAL_REQUIREMENTS.md` está obsoleto.
- *"Qual o estado do projeto?"* -> A IA gera um relatório baseado no `JOURNAL.md` e no `ROADMAP.md` (se houver).

---

## 🚨 5. Regras de Segurança e Deploy

1.  **Segredos:** Variáveis sensíveis (`API_KEYS`, `TOKENS`) nunca devem ser escritas no código fonte. Elas devem ser referenciadas apenas como `[VARIABLE_NAME]` no contexto e geridas via `.env` ou painéis de Cloud.
2.  **Depreciação:** Se um arquivo ou função for removido do código, a menção a ele deve ser removida ou marcada como `[DEPRECATED]` no `ARCHITECTURE.md` para evitar que a IA sugira o uso de código morto.

---

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sua principal responsabilidade não é apenas gerar código funcional, mas garantir que a **documentação viva** do projeto permaneça intacta e confiável. Sem contexto atualizado, sua capacidade de longo prazo é nula.
