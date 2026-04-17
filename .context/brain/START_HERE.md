# 🚀 START_HERE: Seu Guia de Onboarding

Bem-vindo ao projeto! Este repositório utiliza o framework de governança **Antigravity v2.4.1**. Para começar de forma produtiva e garantir que a IA entenda seus objetivos, siga este fluxo:

## 🧭 O Ciclo de Vida da Descoberta

Para evitar "alucinações" e garantir que o código reflita sua intenção, seguimos o ciclo:

1. **Visão (Humano)**: Você escreve o que quer em linguagem natural.
2. **Inception (IA Proposta)**: A IA traduz sua visão em limites técnicos.
3. **Ativação (Ratificação)**: Você revisa e ativa a governança.

---

## 🛠️ Passo a Passo para Inicializar

### 1. Declare sua Visão
Crie um arquivo chamado `.context/brain/VISION.md`. 
*   **Dica**: Use o template `.context/brain/VISION.md.template` como base.
*   Escreva livremente: O que o projeto faz? Qual o problema resolve?

### 2. Solicite a Tradução Cognitiva
Peça para sua IA:
> "@spec-enricher detecte minha VISION.md e proponha o INCEPTION.md"

A IA gerará um arquivo `INCEPTION.proposed.md`.

### 3. Ratifique os Limites
Revise o arquivo proposto e, se estiver de acordo:
1. Renomeie `INCEPTION.proposed.md` para `INCEPTION.md`.
2. Altere o metadado `status: DRAFT` para `status: ACTIVE`.
3. Rode `npm run context:all` para confirmar a saúde do projeto.

---

## 📈 Comandos Úteis
*   `npm run context:validate`: Verifica se a documentação está íntegra.
*   `npm run context:enrich`: Sincroniza o contexto e detecta mudanças na visão.
*   `npm run context:all`: Executa a pipeline completa de governança.

> [!NOTE]
> Se você tentar escrever código em `src/` sem ter um `status: ACTIVE` no Inception, o sistema de segurança irá bloquear a execução para evitar desvio estratégico.
