---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-05-27 20:08
Status: Ativo
---

# 🏛️ MASTER_FLOW: O Roteador Global e Código Civil

> **ESCOPO DE EXISTÊNCIA:** Este documento é o "Mapa Mundi" do ecossistema H.O.K Forge. Ele **NÃO** ensina a executar tarefas táticas (isso é papel das Skills e Subagentes). A função deste arquivo é estritamente apontar onde as coisas estão (Root Tree), quem é responsável por cada etapa do ciclo de vida, e listar as **Leis Macro-Operacionais** (Arquivamento, Purge e Fricção) que não pertencem a nenhum fluxo específico.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) deve obrigatoriamente conter este cabeçalho para garantir a integridade do índice:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura de Governança (Context & Specs)

O repositório é segregado em camadas de cognição:

```text
/ (Root do Projeto)
├── AGENTS.md               # 🛡️ MANIFESTO DE GOVERNANÇA (Root Rulebook)
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── .context/               # 🏛️ GOVERNO E MEMÓRIA DE LONGO PRAZO
    ├── 🧠 brain/           # Leis, Subagentes, Regras, Master Flows
    ├── 🌐 market/          # Compliance, SSOT Map, Dores de Mercado
    ├── 🛠️ maintenance/     # O Motor Vivo (Journal, Logs, Rx-Communications, Schema)
    ├── monitoring/         # O Radar (Project Index, Health)
    └── _scripts/           # A Força Física Bruta (Harness, Purge, Auditores)
```

---

## 🔄 3. O Ciclo Macro do TLC (Ponteiros de Execução)

O ciclo de vida completo de uma funcionalidade vai muito além da codificação. Para executar cada fase, você **NÃO DEVE** tentar agir sozinho. Use o Roteamento abaixo para acionar a Skill ou Subagente correto:

| Ato do TLC | Objetivo | Orquestrador/Responsável |
| :--- | :--- | :--- |
| **1. Incepção (Semente)** | Traduzir `INCEPTION.md` e gaps de mercado em um `PRD.md` lastreado. | Delegue ao Subagente: `@spec-enricher` |
| **2. Planejamento SDD** | Quebrar o PRD em Specs atômicas e assinar o contrato. | Use a Skill: `sdd-orchestrator` |
| **3. Ingestão de Wiki** | Validar arquivos RAW e internalizá-los como conhecimento estático. | *(Pendente: Futura Skill de Base de Conhecimento)* |
| **4. Vacinação e Execução** | Injetar cicatrizes, codificar e validar via SAM. | Use a Skill: `sdd-orchestrator` (que aciona o `@spec-driver`) |
| **5. Ritos de Fechamento** | Auditoria final do SAM, Commit, Cleanup e Archival. | Use a Skill: `sdd-orchestrator` |

> ➡️ *Para detalhes técnicos sobre como o SDD funciona internamente (Atos 2, 4 e 5), consulte o arquivo `FLOW_SDD.md`.*

---

## 🛡️ 4. As Leis de Macro-Manutenção

Estas leis transcendem os fluxos de Spec e afetam a vida útil do repositório inteiro.

### 4.1. O Gatilho de Fricção Operacional `[GOVERNANCE-FRICTION]`
Sempre que uma regra *advisory* for violada no dia a dia (ex: quebra da cronologia do Journal, Metadata desatualizado, ou lixo não detectado pelo SAM), o Agente **deve** registrar o evento no `.context/maintenance/HARNESS_LOG.md`:
- `[GOVERNANCE-FRICTION] <data> | <arquivo> | <descrição do desvio>`
- *Nota:* Este log não bloqueia o commit, mas serve para auditar a "Dívida de Governança" da equipe/IA.

### 4.2. Arquivamento e Imutabilidade (PRD e Schema)
- **Upgrade:** Antes de sobrepor o `brain/PRD.md` ou o `maintenance/schema.sql` com uma nova versão radical, uma cópia do estado atual DEVE ser movida para a respectiva subpasta no `_archive_context/`.
- Nunca apague a história das decisões do Banco de Dados ou da Estratégia do Produto.

### 4.3. A Regra do Purge (JOURNAL.md)
O `.context/maintenance/JOURNAL.md` é a memória contínua, mas é fisicamente limitado:
- **Limite Máximo:** 600 linhas.
- **Acionamento:** Quando o limite é atingido, o script `purge_journal.py` deve ser acionado.
- **O Rito:** Ele enviará os 70% mais antigos da memória para um arquivo datado em `_archive_context/` e manterá os 30% mais novos como a "semente" da próxima iteração.

### 4.4. Efemeridade do Workshop (.specs/)
- As Specs são rascunhos de execução, não documentação permanente. 
- Pós-merge, ou caso fiquem >48h inativas, elas devem ser expurgadas usando o `npm run context:cleanup` (se o Orquestrador não o fez).
- As decisões arquiteturais que ocorreram dentro da Spec devem ser migradas para o `JOURNAL.md` **antes** da destruição da Spec.
