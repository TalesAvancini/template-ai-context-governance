---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📖 PROMPT_LIBRARY.md
> Catálogo de sementes e templates de prompts para garantir consistência e performance.

💡 *Insight Humano: Ter uma biblioteca de prompts evita que a IA tenha que "adivinhar" o formato de saída desejado. Isso economiza tempo e garante que o código siga os padrões de arquitetura do projeto.*

---

## 🏗️ Templates de Engenharia

### `@db-architect` | Criar nova Migration
```text
Role: @db-architect
Tarefa: Gerar migration SQL para [NOME_DA_TABELA]
📌 PRD_REF: [ID_REQUISITO]
📌 SCHEMA_SNAPSHOT: maintenance/schema.sql
🎯 Objetivo: Criar estrutura robusta seguindo [PADRÃO_SQL]
🚧 Restrições: Usar snake_case, incluir timestamps, chaves estrangeiras explicitas.
```

### `@frontend-specialist` | Criar Componente UI
```text
Role: @frontend-specialist
Tarefa: Desenvolver componente [NOME] em [FRAMEWORK]
📌 PRD_REF: [ID_REQUISITO]
📌 STYLE_REF: maintenance/rx-anatomy.md
🎯 Objetivo: Criar UI responsiva, acessível e performática.
🚧 Restrições: Usar design tokens do projeto, prop-types/Typescript, testes unitários.
```

### `@backend-engineer` | Criar Endpoint API
```text
Role: @backend-engineer
Tarefa: Implementar rota [MÉTODO] [PATH]
📌 BIOLOGY_REF: maintenance/rx-biology.md
📌 SCHEMA_REF: maintenance/schema.sql
🎯 Objetivo: Lógica de negócio isolada, tratamento de erros e validação.
🚧 Restrições: Seguir convenção REST, usar Joi/Zod para validação, logar erros complexos.
```

---

## 🛠️ Templates de Manutenção

### `@context-keeper` | Executar Purge de Sessão
```text
Role: @context-keeper
Tarefa: Sintetizar Journal e preparar semente de contexto.
📌 JOURNAL_SNAPSHOT: maintenance/journal.md
🎯 Objetivo: Reduzir Journal mantendo os pontos de decisão críticos.
📝 Instrução: Gere um resumo executivo de 5 itens e insira no topo após o purge.
```

---

## 🆕 Como adicionar novo template
1. Defina a **Role** responsável.
2. Identifique as **Referências** (arquivos do `.context`) necessárias.
3. Descreva o **Objetivo** e as **Restrições** fixas.
