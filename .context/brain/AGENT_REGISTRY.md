---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Testes unitários/E2E, edge cases, cobertura, mocks, TDD | `tests/`, `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (apenas leitura para bugs) | `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (critérios de aceite) | "testar", "validar", "cobertura", "mock", "edge case", "TDD", "bug" |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@spec-driver` | Criação e orquestração de specs atômicas | `.specs/` (leitura/gravação temporária) | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (tail 30) | "inicie specify", "crie spec", "modo híbrido" |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |

💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Carregar APENAS: Global + Role-Specific + Task-Ephemeral
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*
