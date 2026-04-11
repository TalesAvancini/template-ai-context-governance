---
Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-10 23:27
Status: Ativo
---

# 🧬 rx-anatomy.md (Raio-X de Anatomia)
> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Arquivos de decisão e regras
│   ├── maintenance/        # Logs, db schema e inventários
│   └── monitoring/         # Dashboard de saúde
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.sh          # Orquestrador universal Bash
├── init_ai_project.sh      # Bootstrapper supremo
└── package.json            # Gerenciamento de libs e scripts context:*

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `_archive_context/specs/`
- **Não é fonte da verdade.** O `.context/` permanece como SSOT.
