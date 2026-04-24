---
id: HARNESS_ARCHITECTURE
type: concept
tags: [harness-engineering, governanca, arquitetura, fitness-functions, design-de-software]
aliases: [Architecture Fitness Harness, Harness de Arquitetura]
concept: Manutenção de Fronteiras Modulares e Direção de Dependência
entity: Antigravity Framework
source: market/RAW/harness_engineering_manifesto.md
last_updated: 2026-04-23
---

# Architecture Fitness Harness (Harness de Arquitetura)

> Fonte: market/RAW/harness_engineering_manifesto.md

O **Architecture Fitness Harness** (Harness de Arquitetura) agrupa guias (*feedforward*) e sensores (*feedback*) projetados para definir e verificar as características arquiteturais de uma aplicação. Enquanto o *Maintainability Harness* se preocupa com a sintaxe e a higiene interna do código (como evitar duplicação), o *Architecture Harness* é o "leão de chácara" estrutural. Seu papel é garantir que agentes autônomos obedeçam aos limites de módulos, direções de dependência e padrões de design estabelecidos, impedindo que a Inteligência Artificial crie atalhos arquiteturais que destruiriam o sistema a longo prazo.

Na prática, este harness traduz princípios abstratos de arquitetura em **Fitness Functions** (Funções de Aptidão) executáveis que barram o código desalinhado.

## Key Takeaways
*   **Foco Principal:** Manter a estabilidade das estruturas de dados, fazer cumprir limites de módulos e garantir o fluxo correto das dependências do sistema.
*   **A "Física" do Repositório:** Transforma regras que normalmente ficariam apenas em documentos de design em barreiras mecânicas intransponíveis para a IA.
*   **Sensores Computacionais:** Linters customizados, testes estruturais (ex: *ArchUnit*) e validadores de schema.
*   **Guias Inferenciais:** *Skills* e prompts que instruem o agente sobre as convenções de observabilidade e arquitetura de domínio.

### 🏢 Exemplos Práticos na Indústria (Como as Big Techs fazem)

*   **A "Camisa de Força" Estrutural (OpenAI):** Divisão de domínios em camadas fixas com direção de dependência rigorosa (`Types → Config → Repo → Service → Runtime → UI`). Linters barram qualquer tentativa da UI de acessar o Repo diretamente.
*   **Fitness Functions de Performance (Thoughtworks):** Testes automatizados que atuam como sensores de feedback; se a IA introduzir código que degrade os SLOs (Service Level Objectives), o harness bloqueia a tarefa.

### ⚙️ Integração no Antigravity Kit (H.O.K. v2.5.2)

No nosso framework, o **Architecture Fitness Harness** é um dos pilares mais fortes e já opera de forma ativa no portão de commit:

1.  **O DB-First Registry (Sensor Computacional):** O script `harness_runner.py` atua como o juiz arquitetural definitivo. Ele lê a intenção da Spec e a compara fisicamente contra o `schema.sql`. Se o agente executor inventar uma coluna ou interagir com uma tabela inexistente, o harness bloqueia o avanço (Fail-Fast).
2.  **Check de Alinhamento Estratégico:** A função `check_strategic_alignment()` no harness compara ativamente o PRD gerado contra as regras rígidas (`- NUNCA:`) estabelecidas no `INCEPTION.md`. Isso garante que a arquitetura do produto não sofra *drift* em direção a soluções indesejadas pelo negócio.
3.  **Ação Recomendada (O Próximo Nível):** Implementar testes de *Dependency Graph* dentro do `validate_context.py` para impedir acoplamentos entre módulos que deveriam ser independentes.

## Related
*   [[harness_maintainability]] (Maintainability Harness)
*   [[harness_behavior]] (Behaviour Harness e Contratos de Sprint)
*   [[inception_strategy]] (A Camada 0: Inception e Alinhamento)
