---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo
---

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator`
**Gatilho:** Testes, validacao, edge cases, cobertura, mocks  
**Contexto Obrigatorio:** `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (criterios de aceite)
```text
🤖 Ativando @qa-validator | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{arquivo/feature a ser testada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{criar testes, validar edge cases ou aumentar cobertura}}
🚧 Restricoes:
- Seguir framework de testes definido em maintenance/TECHNICAL_REQUIREMENTS.md
- Mockar servicos externos; nao depender de rede real
- Cobrir happy path + 2 edge cases criticos no minimo
- Documentar falhas conhecidas no maintenance/JOURNAL.md se houver
📤 Saida Esperada:
1. Codigo dos testes (unitarios/integracao)
2. Matriz de cenarios cobertos
3. Recomendacoes de refatoracao se aplicavel
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧭 `@vision-architect`
**Gatilho:** Incepção, boundaries estratégicas, validação de mercado, análise de gaps  
**Contexto Obrigatório:** `brain/INCEPTION.md`, `market/SSOT_MAP.md`, `market/MARKET_INBOX.md`
🤖 Ativando @vision-architect | Tarefa: {{descrição_curta}}
📌 PROJECT_VIBE: {{resumo do sentimento}}
📌 MARKET_CONTEXT: {{gaps ou pesquisas alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{definir boundaries, validar fit ou resolver gaps}}
🚧 Restrições:
- Respeitar hierarquia do market/SSOT_MAP.md
- Citações explícitas em previsões (Regra Karpathy)
- Boundaries verificáveis apenas (formato: - NUNCA: X)
📤 Saída Esperada:
1. Proposta editada para INCEPTION.md
2. Novos itens para MARKET_INBOX.md se houver gaps
3. Verificação de alinhamento com PRD (se existir)

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada
2. spec.md com passos, contratos e critérios de verificação
3. STATE.md: draft → pronto para execução
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*
