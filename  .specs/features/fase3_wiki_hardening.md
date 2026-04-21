---
Criado em: 2026-04-21
Ultima Atualizacao: 2026-04-21
Status: Arquivado
---

# 🛠️ SPEC: Implementação Karpathy Wiki (Fase 3 H.O.K)

**Origem:** Plano aprovado `.context/planos/PHASE_3_KARPATHY_WIKI.md`
**Executor:** @spec-driver (Gemini Flash)
**Auditor Final:** @vision-architect (Gemini Pro)

## 🎯 Objetivo
Transformar a camada `market/` em uma arquitetura determinística de "Zero RAG" usando o padrão Karpathy. Isso impedirá o bloqueio de tokens da IA operacional e unificará a governança de conhecimento.

## 📋 Tasks Atômicas (Para o Gemini Flash)

- [x] **1. Estrutura Física**
  - Criar o diretório `.context/market/RAW/` com arquivo `.gitkeep` contendo comentário: `# RAW: Dossiês Brutos (Ignorado pela IA)`.
  - Criar o diretório `.context/market/WIKI/` com arquivo `.gitkeep`.
  - Criar arquivo `.context/market/WIKI/_template.md` com YAML estruturado (`entity`, `concept`, `tags`, `source`) exigindo a declaração `> Fonte: RAW/...`.

- [x] **2. Oráculo (Privileged Isolation)**
  - Fazer patch em `.context/_scripts/context_oracle.py`:
    - Restringir leitura apenas para `WIKI` e `compliance`.
    - Implementar "Triple-Match Heuristic" (Tags > Nome > Frontmatter).
    - Mudar retorno para despejar **o arquivo inteiro** se der "match", em vez de snippets picados.
    - Injetar o `[INFO] Fallback` se não achar na WIKI e a palavra pesquisada parecer de domínio interno.

- [x] **3. Governança Automática**
  - Fazer patch em `.context/_scripts/lint_wiki.py` para bloquear commit se um arquivo em `WIKI/` não possuir o marcador `> Fonte: RAW/...` ou `> Fonte: market/RAW/...`.
  - Atualizar `.context/brain/RULES.md` adicionando o `Protocolo de Destilação (RAW → WIKI)`.
  - Validar que `.context/_scripts/captura_projeto.py` (se existir) está ignorando o diretório `market/RAW/`.

- [x] **4. Teste Clínico**
  - Criar `RAW/dossie_teste.md` e `WIKI/conceito_teste.md` referenciando a fonte.
  - Testar a execução do `context_oracle.py "conceito"`.
  - Verificar se o Lint falha se criarmos um `WIKI/fail_teste.md` sem fonte.

---

> **Resultado Final:** Implementação concluída. Oráculo validado com `confidence: 1.0` e retorno integral do arquivo. Linter Karpathy ativo.
