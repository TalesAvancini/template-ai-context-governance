---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 23:55
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança
**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)  
**PROJECT_MODE:** `[BOOTSTRAP]` *(Fases finitas: BOOTSTRAP, HARDENING, PRODUCTION)*

> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas para garantir escala, foco e rastreabilidade.

---

## 🏗️ 0. Máquina de Estados do Projeto (`PROJECT_MODE`)
O template governa a si mesmo e ao projeto através de três estados rígidos:
1. **`[BOOTSTRAP]`**: Focado na criação da infraestrutura do template, documentação core (RULES, AGENTS) e scripts de governança (INCEPTION/MARKET).
2. **`[HARDENING]`**: Ajustes em segurança (ci/cd, secret-scanners), estabilização e redução de dívida técnica antes de lançar o app.
3. **`[PRODUCTION]`**: Desenvolvimento maduro de features.
> ⚠️ **Regra de Transição:** Qualquer mudança de estado deve ser registrada no `JOURNAL.md` via `[handoff]` e validada com `npm run context:all`.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)
Antes de gerar código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:
1. **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`
2. **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
3. **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`

> ⚠️ **Bloqueio de Execução:** Se qualquer item estiver ausente ou desatualizado, a IA deve parar e solicitar a carga correta antes de prosseguir.

---

## 🔢 2. Session Budget & Heurísticas de Token
Para evitar alucinações por *Token Bloat* (excesso de memória na janela):
- **Gatilhos de Alerta:** ~50.000 caracteres acumulados OU ~15-20 trocas densas de desenvolvimento.
- **Ação ao atingir o limite:** Disparar: *"🔄 Contexto próximo do limite de foco. Deseja que eu execute o purge do JOURNAL, arquive o PRD atual ou inicie uma nova sessão limpa com snapshot de semente?"*

---

## 🧠 3. Protocolo de Manutenção do Contexto
A IA atua como bibliotecário chefe. Consistência entre Código e Contexto é obrigatória.
- **`maintenance/JOURNAL.md`:** Apenas decisões de arquitetura, resoluções de bugs complexos e mudanças de lógica. Proibido logar erros triviais. Ao atingir ~600 linhas ou 50k chars → acionar `_scripts/purge_journal.py`.
- **`maintenance/TECHNICAL_REQUIREMENTS.md`:** Atualizar sempre que houver mudança em `package.json`, alteração de Schema ou integração de novas APIs.
- **`maintenance/rebuild_guide.md`:** Atualizar com hacks de ambiente local, CI/CD ou passos manuais de deploy.
- **`.specs/` (Workshop Efêmero):** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/`. Decisões técnicas devem migrar para o `JOURNAL.md` antes da limpeza.

---

## 🗄️ 4. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.
1. **Verificação Obrigatória:** Antes de criar UI/lógica dependente de dados, validar `maintenance/schema.sql`.
2. **Aviso de Divergência:** Se o código exigir um campo inexistente, parar e avisar: *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro gerar a migration antes de prosseguir."*

---

## 🤖 5. Comportamento do Agente (Transparência & Roteamento)
- **Ativação:** Toda tarefa complexa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`
- **Isolamento:** Carregar APENAS `Global + Role-Specific + Task-Ephemeral`. Ignorar o resto.
- **Handoff:** Cruzar 2+ domínios? Pausar → registrar no `JOURNAL.md`:  
  `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo: [ação]`
- **Context Gate (Pré-Código):** Validar antes de gerar:  
  `[ ] PRD ativo` | `[ ] schema contém estruturas` | `[ ] JOURNAL < 550 linhas` | `[ ] zero secrets hardcoded`

---

## 🔄 6. Gatilhos de Interação (Para o Usuário)
- `"Atualize o contexto"` → IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- `"Qual o estado do projeto?"` → Relatório baseado no `JOURNAL.md` + `ROADMAP.md`.
- `"Roteie esta tarefa"` → Consulta `AGENT_REGISTRY.md`, inicia ativação/handoff.
- `"Use o prompt padrão"` → Seleciona template em `brain/PROMPT_LIBRARY.md`, preenche placeholders, solicita confirmação.
- `"Inicie SPECIFY para PRD #[ID]"` → Cria `.specs/features/`, gera `spec.md` alinhado ao PRD, inicia ciclo TLC.

---

## 🚨 7. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.
---

## 🔍 8. Protocolo Oracle (Consult-Before-Act)
- Se a spec ou PRD contiver ambiguidade técnica, execute: `npm run context:oracle "sua dúvida"`
- Se `confidence < 0.5` -> pause, registre `[oracle:uncertain]` no `JOURNAL.md` e solicite clarificação humana.
- Nunca assuma. Consulte!

## 📖 9. Regra Karpathy (Citação Obrigatória)
- Todo conteúdo/decisão de arquitetura sintetizado em `.context/` DEVE ser lastreado na realidade. Idealmente deve conter `> Fonte: raw/nome-arquivo`.
- `npm run context:lint` avalia (atualmente em modo Warn-Only) se há claims de arquitetura (`implementa X`, `segue padrão Y`) sem lastro de documentação originária.
## 📊 10. Dashboard Health Sync
- Antes de processar features complexas ou abrir Specs Atômicas, verifique o `.context/monitoring/CONTEXT_HEALTH.md` para assegurar que a janela de tokens e a saúde do Journal não exigem repouso ou manutenção prévia.

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.
