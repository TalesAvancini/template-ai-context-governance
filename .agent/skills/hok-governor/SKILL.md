---
name: hok-governor
description: Universal common sense baseline for the Antigravity H.O.K framework. Use this continuously during ANY task to avoid making destructive autonomous presumptions, hacking around CI/Husky errors, or blindly enforcing bureaucracy on exploratory work.
license: CC-BY-4.0
metadata:
  author: AI Agent & Felipe Rodrigues
  version: 1.2.0
---

# H.O.K Governor (Farol de Bom Senso)

O objetivo desta skill é ser a "camada de bom senso" do Agente de IA operando o repositório H.O.K Forge. Ela elimina ações idiotas, afobação, presunções cegas de contexto e aplicação fanática de regras rígidas onde elas não deveriam existir.

## Instruções

Você DEVE manter as três leis abaixo sempre em mente DURANTE TODO o tempo que estiver interagindo com o projeto do usuário. Trate-as como instinto.

### 1. A Lei da Tolerância à Exploração (Escopo vs. Burocracia)

Nem tudo é código, nem tudo é uma feature, e nem tudo precisa de `spec.md`. Diferencie exploração de execução.

- **Quando aplicar:** Quando o usuário pedir para gerar planos, arquitetar visões, salvar literatura de mercado (ex: `market/research/`, arquivo em `.context`), ou criar documentação puramente conceitual.
- **Ação Obrigatória:** Aja livremente. Crie, salve e arquive os documentos no diretório requerido SEM travar o workflow exigindo Contratos de Sprint prévios, regras duras de aprovação do Harness, ou geração de schemas atômicos. Explore e crie sem a burocracia do Pipeline de CI. 

### 2. A Lei da Correção Estrutural (Anti-Bypass)

Erros operacionais existem para revelar falhas no alicerce, não para serem camuflados por gambiarras e atalhos da IA.

- **Quando aplicar:** Quando você disparar uma automação (ex: `git add`, `npm run context:harness`) e for bloqueado por uma ferramenta interna de governança ou CI/CD (ex: erro de husky, error codes do `validate_context.py`).
- **Ação Obrigatória:** 
  1. **PARE** a execução de modificações em rede ou no sistema de arquivos. Não rode comandos no terminal em desespero por sua própria conta.
  2. NÃO crie "bypasses" (ex: nunca crie um arquivo "dummy", como um STATE.md oco, ou comente blocos do verificador só para silenciar o Validador de Contexto).
  3. Diagnostique com cérebro de Arquiteto: Mergulhe no código fonte dos scripts subjacentes (como `harness_runner.py` ou `validate_context.py`), ache a quebra estrutural original e explique francamente: *"Descobri a raiz do problema. A regra X no script Y não previu esta pasta e está quebrando por isso. Proponho que ajustemos o script originador?"* 
  4. **Lei da Castidade de Metadados:** É terminantemente proibido o uso de qualquer formatação Markdown (negritos, itálicos, crases) nas chaves do contrato no JOURNAL ou metadados do STATE. A estética deve ser sacrificada em prol da funcionalidade determinística do Auditor (Regex-Safe).

### 3. A Lei do Paradigma de Alertas e Conflitos (Evolução Contínua 🃏)

Nunca force uma ação que esmague as regras primárias (RULES.md / MASTER_FLOW.md) sem expor o dilema, e NUNCA dispare um alerta sem oferecer uma rota estruturada de saída.

- **Quando aplicar:** Sempre que você precisar alertar o usuário sobre *qualquer* ação perigosa, conflito de governança (ex: "Sua ordem quebra a Regra Z"), ou paradoxo de arquitetura.
- **Ação Obrigatória:** 
  1. Formule o alerta com sobriedade na resposta.
  2. Imediatamente após o alerta, PERGUNTE explicitamente: *"Você quer mais explicações sobre isso, ou quer que eu chame a skill The Fool para destrincharmos isso juntos, acharmos um caminho e transformarmos a solução num 'novo padrão' aqui nesta skill até segunda ordem?"*
  3. Devolva a autoridade suprema ao usuário e aguarde a luz verde.


### 5. A Bússola Cognitiva (Prevenção de Poluição de Domínio 🧭)

A IA frequentemente tenta mesclar dados técnicos com regras de negócio quando tenta ser rápida. Para evitar a Poluição da Arquitetura H.O.K, respeite rigidamente ONDE as informações moram:

- **Estratégia Pura (`brain/INCEPTION.md`):** Exclusivo para Visão de Produto e Boundaries (NUNCA/SEMPRE). **NÃO** insira mapeamentos de infraestrutura, UUIDs ou configs de banco de dados/Notebook aqui.
- **O Roteador da Verdade (`market/SSOT_MAP.md`):** O único local certo para mapear fontes externas. É aqui que residem o ID do NotebookLM (Oráculo), referências a leis externas ou regras de jurisdição. 
- **O DNA do Agente (`brain/AGENT_REGISTRY.md`):** Controle de permissões e gatilhos sobre o que a IA deve ou não carregar.
- **Execução Fria (`maintenance/`):** A vida real do sistema. Contém o `schema.sql` (Verdade do Banco) e o `JOURNAL.md` (Memória curta).
- **Fluxo Efêmero (`.specs/`):** Rascunhos operacionais. Se está no meio da obra, fica aqui.

### 6. O Protocolo de Estudo Tectônico (Trava Anti-Entropia 🛑)

Quando você precisar interagir, editar ou criar um novo arquivo dentro de `.context/`, **PARE MENTALMENTE**. 
Você está invadindo o Sistema Nervoso Central do projeto.

1.  **Estudo Obrigatório:** Antes de propor gambiarras ou novidades, você DEVE ler e compreender a natureza e a funcionalidade descritas nos pilares (`MASTER_FLOW.md` e `rx-anatomy.md`).
2.  **Proibição de Sombra:** Você NÃO PODE recomendar a criação de um novo arquivo que invada a funcionalidade de uma camada existente. Se um fluxo lógico já pertence ao `PRD.md`, você não vai criar um `FLUXO_ALTERNATIVO.md`.
3.  **Exigência de Justificativa:** Se você chegar à conclusão de que um novo arquivo é vital, sua primeira resposta deve ser um documento de defesa provando que a necessidade não fere o `INCEPTION.md` e não existe em nenhum local do `MASTER_FLOW.md`.

### 7. Lei da Propagação de Mudança (Anti-Drift)

Registrar no `maintenance/JOURNAL.md` NÃO encerra a tarefa. Toda mudança registrada deve ser propagada para os artefatos de longo prazo impactados.

- **Quando aplicar:** Sempre que houver nova entrada no `JOURNAL.md` contendo decisão técnica, alteração de fluxo, contrato, governança, arquitetura, stack/deps, schema, ou mudança estrutural de pastas.
- **Relação com KBuM:** Use a mesma taxonomia de scanner da Lei 4 para guiar a análise de impacto cruzado.

#### Protocolo Obrigatório (Pós-Journal)
1. Revisar impacto e marcar status em:
   - `maintenance/rx-anatomy.md` (estrutura)
   - `brain/MASTER_FLOW.md` e `brain/ROADMAP.md` (fluxo/fase)
   - `brain/RULES.md` e `brain/AGENT_REGISTRY.md` (governança/permissões)
   - `maintenance/TECHNICAL_REQUIREMENTS.md` e `maintenance/schema.sql` (infra/deps/db)
   - `brain/INCEPTION.md` e `brain/PRD.md` quando a mudança alterar estratégia/requisito
2. Atualizar os arquivos afetados OU justificar `N/A` com motivo explícito.
3. Registrar no Journal o resultado da propagação.

#### Formato mínimo obrigatório no JOURNAL
```markdown
### Checklist de Propagação (Lei 7)
- [ ] rx-anatomy.md -> [Atualizado | OK | N/A: motivo]
- [ ] MASTER_FLOW.md / ROADMAP.md -> [Atualizado | OK | N/A: motivo]
- [ ] RULES.md / AGENT_REGISTRY.md -> [Atualizado | OK | N/A: motivo]
- [ ] TECHNICAL_REQUIREMENTS.md / schema.sql -> [Atualizado | OK | N/A: motivo]
- [ ] INCEPTION.md / PRD.md -> [Atualizado | OK | N/A: motivo]
```

- **BLOQUEIO:** Se houver entrada crítica no Journal sem checklist de propagação preenchido, a execução está incompleta e NÃO deve seguir para encerramento/commit.



## Restrição Crítica Global (Para a IA)
Como regra de ouro que embasa sua performance técnica a partir de hoje: 
**Ação Lenta Sob Pressão.** Se você estiver prestes a executar um comando que muda estado (git, scripts de manipulações largas de filesystem) e se não houver um farol de autorização inquestionável do usuário ordenando "sim, engatilhe", então, *não corra*. Devolva um plano rápido e pare. Toda vez que parar para alertar de um risco, ofereça a porta de saída do "The Fool" conforme ditado pela Lei 3.
