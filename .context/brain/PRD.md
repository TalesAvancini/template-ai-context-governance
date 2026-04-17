---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 20:50
Status: Ativo
---

# 📦 Product Requirements Document (PRD)
> **TEMPLATE MESTRE**  
> Todas as funcionalidades descritas aqui SERÃO desmembradas em Specs Atômicas no The Workshop (`.specs/`). Nenhuma instrução contida neste PRD pode violar as restrições estratégicas estabelecidas no `INCEPTION.md`.

## 📌 1. Visão Geral
[Descreva o problema que o produto resolve, o público-alvo e o principal critério de sucesso do projeto. Seja direto.]

## 🚀 2. Requisitos Funcionais (Épicos)
*Descreva as entregas do ponto de vista do usuário final.*
- [ ] **Épico 1:** [Descrição breve].
  - História 1: "Como [ator], eu quero [ação] para que [valor]".

## 🛡️ 3. Critical Dependencies & Limites
> **Obrigatório:** Todas as dependências tecnológicas, de compliance ou integrações devem ter lastro ("Fonte: raw/...") validado na camada `market/`.

- **Integrações Externas:** [Nenhuma Detectada] → Fonte: *market/SSOT_MAP.md*
- **Compliance:** [Normal] → Fonte: *market/SSOT_MAP.md*

## 📓 4. Lógica de Negócio Categórica (Regras)
- [Regra de negócio inegociável]

---
💡 *Nota para Especialistas (Agentes):* Antes de decompor estas premissas usando o `@spec-driver`, ative o `npm run context:validate` para garantir que o projeto cumpriu a fase de **Hybrid Discovery** e está em `status: ACTIVE`.
