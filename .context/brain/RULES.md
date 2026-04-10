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

## 🧠 3. Protocolo de Manutenção do Contexto

### 📖 `maintenance/JOURNAL.md` (O Diário de Bordo)
- **Quando atualizar:** Após corrigir bugs persistentes ou alterar lógica de negócio.
- **O Purge:** Ao atingir o limite heurístico, acionar `_scripts/purge_journal.py` para arquivar 70% e gerar semente.

### 🤖 4. Protocolo Multi-Agent (Especialização)

1.  **Declaração de Ativação:** Toda tarefa deve iniciar com: `🤖 Ativando @[role] | Tarefa: [Descrição]`.
2.  **Handoff Obrigatório:** Cruzamento de domínios exige registro de estado no `JOURNAL.md`:
    - `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [Checkpoint] | Próximo: [Ação]`

---

## 🗄️ 5. Protocolo Database-First (Anti-Alucinação)

1.  **Verificação Obrigatória:** Antes de criar UI, verificar `maintenance/schema.sql`.
2.  **Aviso de Divergência:** Se o Schema não bate com o PRD, pare e peça a migration.

---

> **Nota Final para a IA:** Você é o guardião da integridade deste projeto. Sua eficiência depende de quão limpo e focado é o seu contexto atual. Sem contexto blindado, você alucina; com contexto em camadas, você escala.
