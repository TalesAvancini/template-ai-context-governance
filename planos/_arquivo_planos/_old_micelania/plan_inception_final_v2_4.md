# Implementation Plan: Inception + Market v2.4.0 (Fase 1 & 2)

O objetivo central deste plano é criar a fundação estratégica do projeto antes que qualquer código ou PRD rígido seja emitido. Com as críticas refinadas do especialista, a arquitetura agora possui rastreabilidade estratégica e premissas fortes sem engessar os projetos legados. 

Tudo será feito via **Dogfooding** utilizando `.specs/features/meta-inception/`.

## User Review Required
> [!NOTE]
> A implementação será rigorosa. O `validate_context.py` acomodará o `INCEPTION.md` como opcional para não quebrar compatibilidade reversa com projetos legados.

---

## 🏗️ Fase 0: Dogfooding (Abertura de Contexto)
Emulando nosso fluxo, abriremos uma feature spec para justificar as mudanças:

### [System Spec]
#### [NEW] [.specs/features/meta-inception/spec.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.specs/features/meta-inception/spec.md)
#### [NEW] [.specs/features/meta-inception/STATE.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.specs/features/meta-inception/STATE.md)

---

## 📁 Fase 1: Fundação Documental 

Criaremos a estrutura de Market e atualizaremos a Árvore Mestre do sistema.

#### [MODIFY] [.context/brain/MASTER_FLOW.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/MASTER_FLOW.md)
- Inserir a documentação da nova camada `🌐 market/` contendo Restrições externas, economia, compliance.

#### [NEW] [.context/brain/INCEPTION.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/INCEPTION.md)
- Template com seções: `[Vibe]`, `[Boundaries]` (ex: `- NUNCA: <regra>`), `[Gaps]`, `[Assumptions]` e log de tomada de decisão.

#### [NEW] [.context/market/SSOT_MAP.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/SSOT_MAP.md)
- Define a hierarquia explícita de verdade: `compliance > inception > prd > journal`.

#### [NEW] [.context/market/MARKET_INBOX.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/MARKET_INBOX.md)
- Lista de gaps em formato de tabela com colunas (Gap, Fonte, Prioridade, Status) obedecendo à Regra Karpathy de citações raw.

#### [NEW] [.context/market/economics.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/economics.md)
#### [NEW] [.context/market/compliance/.gitkeep](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/compliance/.gitkeep)
#### [NEW] [.context/market/research/.gitkeep](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/research/.gitkeep)

---

## 🤖 Fase 2: Governança de Agentes & Harness

Integrar regras de Market dentro do orquestrador sistêmico.

#### [MODIFY] [.context/brain/AGENT_REGISTRY.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/AGENT_REGISTRY.md)
- Inserir a role `@vision-architect`.  
- *Escopo Restritivo*: Escrita em `INCEPTION.md`, leitura em `market/`. Tarefas: definir boundaries, validar gaps de mercado.

#### [MODIFY] [.context/brain/PROMPT_LIBRARY.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/PROMPT_LIBRARY.md)
- Adicionar o bloco de personalidade/prompt para roteamento para o `@vision-architect`.

#### [MODIFY] [.context/brain/RULES.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md)
- Checklist de carga opcional para permitir que a camada Market seja consumida.

#### [MODIFY] [.context/_scripts/validate_context.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/validate_context.py)
- Não exigir `INCEPTION.md` na lista fixa (backward compatibility), mas alertar `[OK] INCEPTION.md presente` se estiver lá.

#### [MODIFY] [.context/_scripts/context_oracle.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/context_oracle.py)
- Adicionar `brain/INCEPTION.md` e `market/SSOT_MAP.md` à indexação caso existam.

#### [MODIFY] [.context/_scripts/harness_runner.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/harness_runner.py)
- Implementar a rotina isolada `check_strategic_alignment(prd_path, inception_path)`.
- Buscar no `INCEPTION.md` ocorrências do bloco `Boundaries` (`- NUNCA:`).
- Procurar no `PRD.md` se há a ocorrência proibida e setar Exit 1 se houver match.

---

## 🧪 Verification Plan (Dogfood)

1. Abrir e documentar a Spec `meta-inception`.
2. Rodar a montagem (Fases 1 e 2).
3. Teste Negativo (Fail-Fast): 
   - Criaremos temporariamente `- NUNCA: usar mongoDB` no Inception;
   - Registraremos `usar mongoDB` no PRD;
   - Executar `python .context/_scripts/harness_runner.py` e constatar que ele impede a transição quebrando o build.
4. Fechar logando o sucesso no `JOURNAL.md` e limpando os arquivos de teste negativo.
