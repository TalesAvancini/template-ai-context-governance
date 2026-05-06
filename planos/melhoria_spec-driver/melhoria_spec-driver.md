# Implementation Plan: Otimização Spec-Driven V3 (Cura de Dores do Executor)

### Goal
Otimizar os artefatos de governança do **Spec-Driven V3** (Templates, Prompts de Agente e Regras Globais) para blindar o `spec-driver` contra "Deriva de Atenção", "Estagnação de Shell" e "Falhas de Regex/Escopo", reduzindo a fricção com o SAM e o Gatekeeper.

### Assumptions
- A governança dura (Fail-Closed) é inegociável. A solução é "educar" a IA através do prompt e dos templates, não desativar os validadores Python.
- Alterações em `.agent/subagents/spec-driver.md` têm impacto imediato na próxima execução do subagente.
- A máquina hospedeira do repositório opera primariamente em Windows (PowerShell).

---

### Plan

#### 1. Injeção Atômica (Prevenção de Deriva de Atenção)
- **Files:** `.agent/templates/spec_v3.md`, `.specs/features/SSD_PLAYBOOK.md`
- **Change:** 
  - Adicionar a seção `5. Raw Payloads (Injeção Atômica)` no template `spec_v3.md`.
  - No `SSD_PLAYBOOK.md` (Fase A), instituir a regra de que buscas cegas por "IDs ou Referências Externas" são proibidas se o payload não estiver na Spec.
- **Verify:** `git diff .agent/templates/spec_v3.md`

#### 2. Sync Prévio (Mitigação de Scope Block)
- **Files:** `.agent/subagents/spec-driver.md`
- **Change:** 
  - Na instrução da **SKILL 5 (scope-guard)**, adicionar a diretiva: *"Validate physical path existence. Before entering Phase C, you MUST run a physical check (`dir` or equivalent) on all `allow_list` targets. If a path is invalid/global vs local, [HANDOFF: ESCALATION] immediately."*
- **Verify:** `git diff .agent/subagents/spec-driver.md`

#### 3. Protocolo Rígido de Tier (Prevenção de Anti-Loop)
- **Files:** `.agent/templates/AGENT_SCRATCHPAD.md`
- **Change:** 
  - Adicionar à seção `💡 Known Traps`: **[BLOCKED] Falta de Justificativa de Tier:** "Se o Validador travar na Skill 6 com erro de Tier 2/3, não tente de novo. Atualize o `STATE.md` com a chave `tier_justification:` no log da tarefa e tente novamente."
- **Verify:** `git diff .agent/templates/AGENT_SCRATCHPAD.md`

#### 4. Estagnação de Shell (Adaptação Cross-Platform)
- **Files:** `.context/brain/RULES.md`, `.agent/templates/AGENT_SCRATCHPAD.md`
- **Change:** 
  - Adicionar regra de ouro no `RULES.md`: "OS Baseline: Assuma Windows (PowerShell). Proibido o uso de operadores bash-only como `&&` para encadeamento. Prefira comandos linha a linha."
- **Verify:** `git diff .context/brain/RULES.md`

#### 5. Surgical Edits (Resiliência de Parser e Regex)
- **Files:** `.specs/features/SSD_ERRORS_LEDGER.md`, `.agent/templates/AGENT_SCRATCHPAD.md`
- **Change:** 
  - Registrar a cicatriz **Scar #006 — Sensibilidade de Whitespace (Regex)** no Ledger.
  - Adicionar a "Vacina" no `AGENT_SCRATCHPAD.md` (Known Traps): **Falha no TargetContent:** "Se a substituição falhar por causa de indentação (ex: no STATE.md), quebre a edição em blocos (Surgical Edits) menores de 1-3 linhas."
- **Verify:** `git diff .specs/features/SSD_ERRORS_LEDGER.md`

---

### Risks & mitigations
- **Risco:** O aumento das instruções no `spec-driver.md` e `AGENT_SCRATCHPAD.md` pode estourar o "attention limit" do modelo.
- **Mitigação:** As edições serão pílulas de texto curto (bullet points diretos) sem longas explicações.

### Rollback plan
- Confirmar integridade com `git diff` após cada substituição. Se alguma Regex falhar, reverter via `git checkout -- <file>`.
