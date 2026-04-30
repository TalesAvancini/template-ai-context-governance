# 📜 PLANO DE IMPLEMENTAÇÃO: Spec Enricher (v2.4.1-Hardened)
*(Documento mestre para instalação do Módulo de Enriquecimento de Especificações)*

---

## 🎯 Objetivo & Visão
Instalar o **@spec-enricher** como role e ritual oficial, criando a ponte cognitiva entre a incepção estratégica e as especificações funcionais. O sistema deve impedir a geração de PRDs se houver gaps de mercado, forçando o ciclo **Research -> Valid -> Execute**.

---

## 🛠️ Arquitetura de Patches (Auditada)

### 🐍 scripts/enrich_context.py (Gap-Checker)
- **Logica:** Scan `INCEPTION.md` -> Busca restrita em `market/compliance` e `market/research` -> Validação de conteúdo (1000 chars) -> Update `MARKET_INBOX.md` (uma linha por entidade).
- **Exit Codes:** `0` (Ready), `2` (Research Needed), `1` (Error).

### 🛡️ scripts/harness_runner.py (Integrity Check)
- **Nova Funcionalidade:** `check_enrichment_integrity(prd_path)`.
- **Gatilhos Semânticos:** Monitora menções a integrações/compliance (integracao, compliance, integration, external api, etc.).
- **Contrato:** Exige seção `## 🚨 Critical Dependencies` com formato exato `- **{Entidade}** → Fonte: market/...`.

### 🐍 run_context.py (Dispatcher)
- **Integração:** Novo comando `enrich`.
- **Tratamento:** `subprocess.run(..., check=False)` + print do `[STRATEGIC BLOCK]`.
- **Help:** Atualizado para refletir o novo rito.

---

## 📋 Matriz de Roles & Prompts

| Role | Especialidade | Escrita | Leitura (Market) | Gátilho |
|------|---------------|---------|------------------|---------|
| `@spec-enricher` | Tradução estratégica, validação de gaps, PRDs lastreados | `PRD.md`, `MARKET_INBOX.md` | `compliance/`, `research/`, `INCEPTION.md` | `npm run context:enrich` |

---

## ✅ Plano de Verificação (H.O.K.)

### 1. Teste de Bloqueio (Exit 2)
1. Inserir entidade (ex: `LGPD`) no `INCEPTION.md`.
2. Certificar ausência do arquivo fonte em `market/`.
3. Rodar `npm run context:enrich`.
4. **Esperado:** Exit 2 + Mensagem de Strategic Block.

### 2. Teste de Sucesso (Exit 0)
1. Criar arquivo fonte `market/research/LGPD.md`.
2. Rodar `npm run context:enrich`.
3. **Esperado:** Exit 0 + Mensagem de Sucesso.

### 3. Teste de Validação (Harness)
1. Criar `PRD.md` com menção a integrações mas sem a seção de dependências.
2. Rodar `npm run context:harness`.
3. **Esperado:** Exit 1 + Erro de contrato de enriquecimento.

---

## 🔒 Handoff Final (Estado Pronto)
`@vision-architect` (Incepção) ⮕ `@spec-enricher` (Research & PRD) ⮕ `@spec-driver` (Specs)
