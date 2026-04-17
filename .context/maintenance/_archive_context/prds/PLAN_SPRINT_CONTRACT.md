# Implantação: Contratos de Sprint

Abaixo documentamos as alterações que faremos no framewok base de governança do H.O.K para erradicar o viés de autoavaliação em Agentes, forçando o acordo do formato final de validação (`Definition of Done`) entre Geração e Code Review.

## Resumo das Modificações (v2.5 Integration)

### 1. Template de Contrato Enxuto e Atômico
#### `spec.md` (Frontmatter)
Ao criar `.specs/features/[slug]/spec.md`, o YAML Frontmatter embute o contrato diretamente via variáveis `definition_of_done`, `qa_signoff` e `signed_by`. Isso elimina a necessidade de um arquivo extra e isola o contrato cirurgicamente por Spec.

### 2. Higiene de Roles
#### `AGENT_REGISTRY.md` 
Em vez de inchar o roteador com entidades novas, apenas estendemos a capacidade das originais:
- `@spec-driver` (Responsável pelo Output do YAML com `qa_signoff: false`)
- `@qa-validator` (Verifica a compatibilidade e injeta a validação `qa_signoff: true`). 

### 3. Governança Teórica
#### `RULES.md` 
Adicionada a cláusula `1.1 Regra de Contrato de Sprint (Research-First)` determinando dependência mecânica da aprovação antes da codificação. As saídas de PROMPT_LIBRARY.md também ditam as novas restrições.

### 4. Backpressure Mecânico Leve (Harness Layer)
#### `harness_runner.py` 
A injeção do check `check_sprint_contract()` lê diretamente via Parser Stdlib o YAML entre os metadados `---` da Spec na fase de CI/CD. Retorna Falha Letal (Exit 1) se não detectar `qa_signoff: true` ou o campo estrito `signed_by` não estiver atribuído.
