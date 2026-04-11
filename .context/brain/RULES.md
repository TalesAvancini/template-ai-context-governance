---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança

**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)

> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas (Cognitiva, Manutenção, Monitoramento e Automação) para garantir escala e foco operacional.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)

Antes de gerar qualquer código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:

1.  **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`.
2.  **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
3.  **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`.

> ⚠️ **Bloqueio de Execução:** Se qualquer um dos itens acima não estiver carregado ou visível, a IA deve parar e solicitar a carga antes de prosseguir.

---

## 🔢 2. Session Budget & Heurísticas de Token

Para evitar alucinações por "Token Bloat" (excesso de memória na janela), adotamos limites práticos:

### 🚩 Gatilhos de Reset/Purge
A IA deve monitorar o estado da sessão e sugerir uma limpeza ou snapshot quando detectar:
- **Volume:** Aprox. **50.000 caracteres** acumulados no buffer de prompt/repost.
- **Duração:** Aprox. **15 a 20 trocas (mensagens)** densas de desenvolvimento.

### 🔄 Ação ao atingir o limite:
A IA deve disparar a seguinte mensagem ao usuário:
> *"🔄 Contexto próximo do limite de foco (~20 trocas). Deseja que eu execute o purge do JOURNAL, arquive o PRD atual ou inicie uma nova sessão limpa com um snapshot de semente?"*

---

## 🧠 1. Protocolo de Manutenção do Contexto
A IA deve agir como o "bibliotecário chefe". A consistência entre Código e Contexto é obrigatória.

### 📖 `maintenance/JOURNAL.md` (O Diário de Bordo)
- **O que logar:** Decisões de arquitetura, resoluções de bugs complexos e mudanças em lógica de negócio.
- **Proibido:** Erros de sintaxe triviais, mudanças de estilo (CSS) ou indentação.
- **O Purge:** Ao atingir o limite heurístico (~50k char), acionar `_scripts/purge_journal.py` para arquivar 70% e gerar semente de contexto.

### ⚙️ `maintenance/TECHNICAL_REQUIREMENTS.md`
- **Atualização Obrigatória:** Mudanças no `package.json`, alteração de Schema ou integração de novas APIs/Serviços.

### 🛠️ `maintenance/rebuild_guide.md` (Manual de Reconstrução)
- **Atualização Obrigatória:** Descoberta de hacks de ambiente local, configurações críticas de CI/CD ou passos manuais de deploy.

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e o `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões tomadas na spec devem ser transferidas para o `JOURNAL.md` no momento do merge.

---

## 🗄️ 2. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.

1.  **Verificação Obrigatória:** Antes de criar UI ou lógica que dependa de dados, o Agente DEVE verificar `maintenance/schema.sql`.
2.  **Aviso de Divergência:** Se a IA identificar que o código exige um campo inexistente no DB, ela deve parar e avisar: 
    *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro a migration antes de prosseguir."*

---

## 🤖 3. Comportamento do Agente (Transparência & Roteamento)

### 📋 3.1 Registro & Ativação
- **DNS de Roles:** `brain/AGENT_REGISTRY.md` é a única fonte oficial de papéis.
- **Identificação:** Toda tarefa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`.
- **Isolamento de Contexto:** Carregar apenas: Global (`brain/` base) + Role-Specific + Task-Ephemeral (`brain/PRD.md` + tail de `maintenance/JOURNAL.md`).

### 🤝 3.2 Handoff & Cruzamento de Domínios
Se uma tarefa exigir 2+ especialidades, o agente atual deve pausar e registrar:
- `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado Tecnico: [Resumo] | Próximo Passo: [Ação]`
O próximo agente inicia com contexto limpo + estado transferido.

### ⚖️ 3.3 Validação Pré-Código (Context Gate)
Antes de gerar código de produção, validar mentalmente ou via script:
- [ ] `brain/PRD.md` ativo e alinhado.
- [ ] `maintenance/schema.sql` contém as estruturas referenciadas.
- [ ] `maintenance/JOURNAL.md` < 550 linhas.
- [ ] Nenhuma variável sensível hardcoded.

---

## 🔢 4. Session Budget & Heurísticas de Token
- **Volume:** Aprox. **50.000 caracteres** ou **15-20 trocas** densas.
- **Alerta:** Ao detectar o limite, propor purge ou reset de sessão imediatamente.

---

## 🔄 5. Gatilhos de Interação (Para o Usuário)
- **"Atualize o contexto":** IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- **"Qual o estado do projeto?":** IA gera relatório baseado no `JOURNAL.md` e `ROADMAP.md`.
- **"Roteie esta tarefa":** IA consulta `AGENT_REGISTRY.md` e inicia o fluxo de ativação/handoff.
- **"Use o prompt padrão":** IA seleciona o template no `brain/PROMPT_LIBRARY.md`, preenche placeholders e solicita confirmação.
- **"Novo PRD":** IA deve usar o template v2.0 (`brain/PRD.md`), preencher metadados, validar Context Gate e registrar no `ROADMAP.md`.
- **"Inicie a fase de SPECIFY para o PRD #[ID]":** A IA cria a estrutura em `.specs/features/`, gera o `spec.md` alinhado ao PRD e inicia o ciclo TLC.

---

## 🚨 6. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se uma função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.

---

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.
