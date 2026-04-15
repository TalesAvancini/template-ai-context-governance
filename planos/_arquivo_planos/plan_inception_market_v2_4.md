# 🧭 Plano: Expansão Estratégica INCEPTION + MARKET (v2.4.0)

Este plano detalha a implementação da camada de concepção pré-PRD, permitindo que o caos criativo seja filtrado e validado por dados externos antes de entrar na governança rígida de execução.

## Avaliação dos Especialistas

> [!NOTE]
> **Veredito:** Arquitetura altamente recomendada para projetos que exigem conformidade (LGPD, Stripe, Meta) ou pesquisa profunda.

**Pontos Fortes:**
- **Anti-Token-Bloat:** A biblioteca `MARKET/` não é carregada no bundle principal; ela vive apenas no índice do Oráculo.
- **Rastreabilidade:** Força o `Karpathy Script` a exigir fontes de mercado para decisões de negócio.
- **Separação de Preocupações:** `@vision-architect` cuida do "O Quê" e "Por Quê", enquanto o restante do H.O.K. cuida do "Como".

**Riscos Identificados:**
- **Ruído Semântico:** Se o `INCEPTION.md` ficar muito poluído, o Oráculo pode trazer referências obsoletas.
- **Drift de Visão:** O PRD pode se desviar da Inception. Precisamos do Harness para validar isso.

---

## Proposta de Melhoramentos (Refinamentos Antigravity)

### 1. Camada de Concepção (`.context/market/`)
- Criar a estrutura física:
  - `compliance/`: Regras de ouro (ex: "Stripe Guidelines").
  - `research/`: Fatos brutos (NotebookLM outputs).
  - `economics.md`: Tabela de custos de infra e tokens.
- **Refinamento Antigravity:** Adicionar um `SSOT_MAP.md` dentro de `market/` para o Oráculo saber quais arquivos têm prioridade em termos de conformidade.

### 2. O Útero Criativo (`.context/brain/INCEPTION.md`)
- Novo blueprint com seções:
  - `[Vibe]`: Descrição subjetiva do desejo humano.
  - `[Boundaries]`: O que NÃO faremos (vital para o Harness).
  - `[Gaps]`: Termos ou tecnologias marcados com `??` que exigem research.

### 3. Automação e "Oráculo 2.0"
- **Update `context_oracle.py`**: Adicionar suporte a caminhos dinâmicos para incluir `.context/market/`.
- **New Script `identify_gaps.py`**: Automatizar a leitura do `INCEPTION.md` em busca de incertezas e gerar uma lista de "Shopping de Conhecimento" em `MARKET_INBOX.md`.
- **Update `harness_runner.py`**: Adicionar o check `STRATEGIC_ALIGNMENT` (valida PRD vs Inception Boundaries).

---

## Proposed Changes

### [Component Name]

#### [NEW] [INCEPTION_TEMPLATE.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/INCEPTION.md)
#### [NEW] [Market Directory Structure](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/)
#### [MODIFY] [context_oracle.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/context_oracle.py)
#### [MODIFY] [AGENT_REGISTRY.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/AGENT_REGISTRY.md)

---

## Próximos Passos (Workflow proposto)

1. **Aprovação deste Plano.**
2. **Setup da Estrutura**: Criar as pastas e o arquivo `INCEPTION.md`.
3. **Registro da Role**: Adicionar `@vision-architect` ao registry.
4. **Upgrade do Oráculo**: Permitir a indexação da camada Market.
5. **Teste de Stress**: Rodar um brainstorm simulado e ver o Oráculo buscar no `market/`.

## Open Questions

- Qual o formato preferencial para as saídas do NotebookLM? Recomendo **Markdown com citações em linha** para facilitar o trabalho do Karpathy.
- Deseja que o `captura_projeto.py` ignore a pasta `market/` explicitamente (forçando o uso do Oráculo) ou que leve apenas o `SSOT_MAP.md`? (Recomendo ignorar tudo e usar só Oráculo).
