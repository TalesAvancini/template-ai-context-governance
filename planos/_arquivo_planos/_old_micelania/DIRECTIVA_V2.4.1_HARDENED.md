# Plano de Implementação: Antigravity Kit v2.4.1-Hardened

Este plano detalha a aplicação da **Diretiva de Implementação v2.4.1-Hardened**, focando em patches cirúrgicos, segurança fail-fast e ativação da governança estratégica (Inception/Market).

## 🗺️ Mapa Visual da Arquitetura

Para garantir o entendimento determinístico da ordem temporal e lógica, os diagramas abaixo regem o comportamento dos agentes.

### 1. Fluxo de Execução Fail-Fast (`run_context.py`)
*O pipeline é uma esteira crítica. Qualquer falha em segurança, sincronia ou contrato interrompe o fluxo imediatamente.*

```mermaid
graph TD
    Start([npm run context:all]) --> Validate[1. validate_context.py]
    Validate -->|FAIL| Error([❌ EXIT 1: Build Quebrado])
    Validate -->|Integrity OK| Secrets[2. secrets_scanner.py]
    Secrets -->|FAIL: Hits Found| Error
    Secrets -->|Clean| Sync[3. sync_project.py]
    Sync -->|FAIL| Error
    Sync -->|Updated| Migrations[4. migration_registry.py]
    Migrations -->|FAIL: Order Broken| Error
    Migrations -->|Order OK| Harness{5. harness_runner.py}
    
    Harness -->|FAIL: Strategy/Schema| Error
    Harness -->|PASS: All Contracts| Lint[6. lint_wiki.py --strict]
    
    Lint -->|FAIL: Missing Source| Error
    Lint -->|Citations OK| Health[7. health_sync.py]
    Health -->|Updated| Done([✅ DONE: Pipeline Sucesso])
```

### 2. A Máquina de Estados do Projeto (`RULES.md`)
*Define o modo operacional e os critérios de transição de maturidade.*

```mermaid
stateDiagram-v2
    [*] --> BOOTSTRAP
    
    BOOTSTRAP: [BOOTSTRAP]
    note right of BOOTSTRAP
      Foco: Estrutura, Scripts, 
      Inception e Market Setup.
      Regras: Validação de diretórios.
    end note
    
    BOOTSTRAP --> HARDENING: JOURNAL Entry + Context Pass + Harness Validated
    HARDENING: [HARDENING]
    note right of HARDENING
      Foco: Segurança, CI/CD, 
      Scanners e Estabilidade.
      Regras: Zero falhas no Harness Pipeline.
    end note
    
    HARDENING --> PRODUCTION: Zero falhas em N sessões + Baseline v2.4.1
    PRODUCTION: [PRODUCTION]
    note right of PRODUCTION
      Foco: Features Reais.
      Market/ vira fonte estratégica prioritária (SSOT_MAP).
    end note
```

### 3. O Rito do Spec Enricher (Concepção → Execução)
*Inclui o estado Exit 2 para pesquisa pendente e o fluxo de incepção estratégica.*

```mermaid
sequenceDiagram
    participant Human
    participant Vision as @vision-architect
    participant Inception as INCEPTION.md
    participant Market as MARKET/ Folders
    participant Enricher as @spec-enricher
    participant PRD as PRD.md

    Human->>Vision: "Tenho uma ideia para X"
    Vision->>Inception: Escreve [Boundaries] (- NUNCA: X)
    Enricher->>Inception: Lê INCEPTION.md e escaneia Entidades
    Enricher->>Market: Verifica compliance/ e research/
    
    alt Exit 2: Research Needed
        Market-->>Enricher: Incerteza técnica ou Gaps
        Enricher->>Market: Registra em MARKET_INBOX.md [TODO]
        Enricher->>Human: ❌ EXIT 2: Pesquisa necessária. Popule market/
        Human->>Market: Insere fontes (Karpathy Rule)
        Note over Enricher, Market: Reinicia ciclo Enrich
    else Fontes Presentes
        Market-->>Enricher: Documentos encontrados
        Enricher->>Enricher: Valida viabilidade vs Boundaries
        Enricher->>PRD: Gera PRD.md lastreado (> Fonte: market/...)
        Note right of PRD: Pronto para Handoff TLC
    end
```

## User Review Required

> [!IMPORTANT]
> **Regra de Patch Rígida:** Não substituiremos arquivos inteiros. Faremos edições apenas nos blocos indicados para preservar a integridade das funções auxiliares.
> **Estado Atual:** Muitos componentes já possuem a lógica da v2.4.1 instalada. Este plano irá **formalizar, corrigir discrepâncias de string (acentuação, logs) e garantir a presença dos novos arquivos** da camada Market.

## Proposed Changes

### 📂 FASE 1: Scripts Core (Hardening)

#### [MODIFY] [run_context.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/run_context.py)
- Sincronizar o bloco `elif cmd == "all":` para incluir o print de sincronização e a string final com acentuação correta conforme a diretiva.

#### [MODIFY] [validate_context.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/validate_context.py)
- Garantir a verificação da camada opcional `INCEPTION.md`.
- Assegurar que `sys.exit(1)` seja chamado se houver `issues`.

#### [MODIFY] [context_oracle.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/context_oracle.py)
- Revisar regex Unicode para garantir compatibilidade PT-BR (`\b\w{3,}\b`).
- Confirmar indexação de `brain/INCEPTION.md` e `market/SSOT_MAP.md`.

#### [MODIFY] [harness_runner.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/harness_runner.py)
- Sincronizar a função `check_strategic_alignment()` e o dicionário de `checks` no `main()`.

#### [MODIFY] [secrets_scanner.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/secrets_scanner.py)
- Validar `JSON_ALLOWLIST` e a lógica de scan que ignora MDs e imagens, mas escaneia JSONs fora da allowlist.

---

### 📂 FASE 2: Governança & Registry

#### [MODIFY] [RULES.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md)
- Inserir/Sincronizar a seção `## 🏗️ 0. Máquina de Estados (PROJECT_MODE)` com o texto exato da diretiva.

#### [MODIFY] [AGENT_REGISTRY.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/AGENT_REGISTRY.md)
- Adicionar/Sincronizar a role `@vision-architect` e a camada `Strategic` na tabela de isolamento.

#### [MODIFY] [MASTER_FLOW.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/MASTER_FLOW.md)
- Atualizar árvore de diretórios para incluir explicitamente a camada `🌐 market/`.

#### [MODIFY] [PROMPT_LIBRARY.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/PROMPT_LIBRARY.md)
- Sincronizar o prompt do `@vision-architect` com os gatilhos e restrições H.O.K.

---

### 📂 FASE 3: Camada Inception + Market

#### [NEW] [INCEPTION.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/INCEPTION.md)
- Criar template mestre com boundaries `- NUNCA:`.

#### [NEW] [SSOT_MAP.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/SSOT_MAP.md)
- Definir hierarquia da verdade.

#### [NEW] [MARKET_INBOX.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/MARKET_INBOX.md) e [economics.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/economics.md)
- Criar arquivos com frontmatter padrão.

#### [NEW] .gitkeeps
- Criar em `market/compliance/` e `market/research/`.

---

### 📂 FASE 4: Isolamento & Bundle

#### [MODIFY] [captura_projeto.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/captura_projeto.py)
- Aplicar o filtro **path-scoped** para ignorar `compliance/` e `research/` no bundle.

#### [MODIFY] [JOURNAL.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/maintenance/JOURNAL.md)
- Registrar a entrada de conclusão do hardening.

---

## Verification Plan

### Automated Tests
1. **Pipeline Completo:** `npm run context:all` (Saída esperada: `[DONE] ... concluído com sucesso.`)
2. **Isolamento Market:** Comando python para verificar se `market/compliance` e `market/research` NÃO estão no bundle.
3. **Oracle Unicode:** Consultar termos com acento e verificar confidence.
4. **Harness Fail-Fast:** Inserir boundary proibida no `INCEPTION.md` e violar no `PRD.md`, verificando se o Harness bloqueia com exit 1.

### Manual Verification
- Revisão visual dos arquivos `.md` gerados na camada `market/`.
- Verificação do frontmatter YAML em todos os novos arquivos.
