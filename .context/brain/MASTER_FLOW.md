---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento define a organização da memória e governança do projeto. Seguimos uma arquitetura de camadas para garantir que a IA tenha foco máximo e o menor ruído possível.

---

## 📂 Estrutura do Diretório `.context/`

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
│   ├── JOURNAL.md                 # Log vivo (Máx ~50k char)
│   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e versões
│   ├── rebuild_guide.md           # Manual de setup e infra
│   ├── schema.sql                 # Snapshot do Banco de Dados
│   ├── ARCHITECTURE.md            # Blueprint técnico
│   ├── TESTS.md                   # Padrões de teste e TDDs
│   ├── rx-anatomy.md              # Raio-X de pastas
│   ├── rx-biology.md              # Raio-X de fluxos
│   └── _archive_context/          # Histórico imutável
│
├── 📊 monitoring/                  # CAMADA DE MONITORAMENTO (The Dashboard)
│   └── CONTEXT_HEALTH.md          # Dashboard de saúde técnica/cognitiva
│
└── ⚙️ _scripts/                    # CAMADA DE AUTOMAÇÃO (The Arms)
    ├── validate_context.py        # Validador de integridade
    ├── purge_journal.py           # Gerenciador de memória (Purge)
    └── sync_project.py            # Sincronizador de requisitos
```

---

## ⚙️ Diretrizes Operacionais

### 🔄 Ciclo de Vida do Contexto
1.  **Ativação:** O Agente declara sua Role via `AGENT_REGISTRY.md`.
2.  **Carga:** Verifica-se o `Checklist de Carga` no `RULES.md`.
3.  **Execução:** Trabalha-se no `PRD.md` atual, registrando decisões no `JOURNAL.md`.
4.  **Sincronização:** Scripts em `_scripts/` garantem que a documentação reflita o código.
5.  **Purge:** Ao atingir a heurística de tokens, o `JOURNAL.md` é limpo e arquivado.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*
