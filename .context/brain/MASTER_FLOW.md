---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura do Diretório `.context/`

```text
.context/
├── 🧠 brain/                       # CAMADA COGNITIVA (The Brain)
│   ├── MASTER_FLOW.md             # Este documento
│   ├── RULES.md                   # Protocolos e "A Lei"
│   ├── AGENT_REGISTRY.md          # DNS de Roles e Permissões
│   ├── PROMPT_LIBRARY.md          # Catálogo de templates de prompts
│   ├── PRD.md                     # Requisito em execução (O Norte)
│   └── ROADMAP.md                 # Metas e fases (O Planejamento)
│
├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
│   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Curta)
│   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e versões (Inventário)
│   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
│   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
│   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
│   ├── TESTS.md                   # Ledger de padrões e TDDs
│   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
│   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
│   └── _archive_context/          # Histórico imutável (A Biblioteca)
│
├── 📊 monitoring/                  # CAMADA DE MONITORAMENTO (The Dashboard)
│   └── CONTEXT_HEALTH.md          # Status dashboard técnico e cognitivo
│
└── ⚙️ _scripts/                    # CAMADA DE AUTOMAÇÃO (The Arms)
    ├── validate_context.py        # Validador de integridade
    ├── purge_journal.py           # Gerenciador de memória (Purge)
    └── sync_project.py            # Sincronizador de requisitos
```

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*
