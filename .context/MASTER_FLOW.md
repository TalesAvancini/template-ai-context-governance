# 🏛️ MASTER_FLOW: Template Universal de Gestão de Contexto

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma estrutura de memória persistente que garante foco, rastreabilidade e alta performance para agentes de IA e humanos.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo no `.context` deve conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Última Atualização: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura do Diretório `.context/`

```text
.context/
├── MASTER_FLOW.md              # Este documento (diretriz mestra)
├── RULES.md                    # Protocolo de conduta da IA (A Lei)
├── ROADMAP.md                  # Metas e fases ativas (O Norte)
├── PRD.md                      # Requisito em execução (1 por vez)
├── JOURNAL.md                  # Log vivo (Máx 600 linhas - Memória Curta)
├── ARCHITECTURE.md             # Blueprint técnico evolutivo (O DNA)
├── TECHNICAL_REQUIREMENTS.md   # Stack, limites e versões
├── schema.sql                  # Estado atual do banco (Snapshot real)
├── TESTS.md                    # Ledger de padrões e TDDs vitoriosos
├── rx-anatomy.md               # Raio-X de pastas (Anatomia do Repositório)
├── rx-biology.md               # Raio-X de fluxos (Biologia do Negócio)
└── _archive_context/           # Histórico imutável (A Biblioteca)
    ├── prds/                   # Ciclos de funcionalidades concluídas
    ├── schemas/                # Evolução das tabelas (v1, v2...)
    ├── journals/               # Purges do log vivo (Memória Longa)
    ├── post-mortems/           # Lições aprendidas (ex: rebuild_guide)
    └── rx-snapshots/           # Versões antigas de anatomia/fluxo
```

---

## ⚙️ 3. Regras de Manutenção

### 🔄 Ciclo de Vida do PRD e Schema
1.  **Upgrade:** Antes de alterar o `PRD.md` ou `schema.sql`, uma cópia fiel do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz deve representar sempre o estado **em execução** ou **em produção**.

### 📝 Gestão do JOURNAL.md
*   **Limite de 600 linhas:** Para evitar saturação de tokens e dispersão da IA.
*   **O Purge:** Ao atingir o limite, os 70% mais antigos são movidos para `_archive_context/journals/` e os 30% mais novos permanecem como semente para o novo ciclo.

### 🔍 Visão de RX (Raio-X)
*   **rx-anatomy**: Mantém a IA ciente de onde as coisas devem ser criadas.
*   **rx-biology**: Mantém a IA ciente de como o dinheiro/dados fluem no negócio.

---

> *Este template é a fundação de um projeto saudável. Se a estrutura for seguida, a IA nunca sofrerá de alucinação por falta de contexto.*
