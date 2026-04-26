---
Criado em: 2026-04-26
Ultima Atualizacao: 2026-04-26
Status: Ativo (v2.5.2)
---

# 🔬 RX: Raio-X do Repositório `Antigravity-Template` (v2.5.2)

> Mapeamento funcional e arquitetural do ecossistema de governança. Este documento serve como bússola para humanos e IAs navegarem na estrutura Autobuilder.

---

## 1) Visão Geral Rápida

*   **O Produto:** Este repositório é um **Framework de Governança**. O "produto" é a automação da integridade do contexto.
*   **Camada de Comando:** Centralizada no `run_context.py` e mapeada via `package.json`.
*   **Memória:** Distribuída entre `.context/` (Sempre Ativo) e `.specs/` (Efêmero/Execução).
*   **Fase Atual:** **Autobuilder**. O sistema está em constante auto-aperfeiçoamento e saneamento.

---

## 2) Mapa das Pastas da Raiz

| Pasta / Arquivo | Função no Projeto | Status | Evidências-chave |
| :--- | :--- | :--- | :--- |
| **`.context/`** | Memória de longo prazo, regras de arquitetura e logs de manutenção. | **Ativo e Crítico** | `brain/`, `maintenance/`, `monitoring/` |
| **`.specs/`** | Bancada de execução (Workshop). Onde os contratos de código nascem. | **Ativo (Workshop)** | `features/`, `_template.md` |
| **`.husky/`** | Cão de guarda. Bloqueia commits que violam a governança. | **Ativo (Gatekeeper)** | `pre-commit` |
| **`planos/`** | Área de rascunhos, pesquisas e ideias fora do contexto core. | **Suporte (Lab)** | `_arquivo_planos/` |
| **`tests/`** | Testes de integridade da própria infraestrutura de governança. | **Ativo (QA)** | `test_context.py` |
| **`captura_projeto/`** | Ferramentas de bundling e ingestão de contexto para LLMs. | **Suporte (Ingestão)** | `captura_projeto.py` |
| **`_modoLight/`** | Versão simplificada do framework para ambientes de baixo recurso. | **Opcional** | Scripts simplificados |
| **`run_context.py`** | O "Maestro". Orquestra todos os scripts Python do framework. | **Ativo (Core)** | `all`, `validate`, `harness` |
| **`package.json`** | Painel de controle NPM e registro de versões. | **Ativo (Config)** | `scripts`, `version: 2.5.2` |

---

## 3) Detalhamento das Pastas Críticas

### 🧠 `.context/` (Governança e Memória)
Esta é a "Caixa Preta" e o "Cérebro" do projeto.
*   **`brain/`**: Contém a **Constituição** (`RULES.md`), a **Visão** (`VISION.md`) e o **Registro de Agentes**. É o que define o comportamento da IA.
*   **`maintenance/`**: Contém o **Diário** (`JOURNAL.md`), a **Anatomia** e a **Biologia**. É o registro dos fatos e da saúde técnica.
*   **`monitoring/`**: Focado em dashboards em tempo real (`CONTEXT_HEALTH.md`).
*   **`_scripts/`**: O motor lógico. Contém os scripts Python que fazem o "trabalho sujo" de validação e sincronia.

### 🧪 `.specs/` (Workshop de Execução)
Onde o trabalho real acontece.
*   **`features/`**: Cada subpasta aqui é uma tarefa atômica. Contém o `spec.md` (o contrato) e o `STATE.md` (o progresso).
*   **`_template.md`**: O molde para criar novas tarefas sem erro.

---

## 4) Pontos de Atenção e Diagnóstico

*   **Saneamento Recente:** As pastas `.context/specs` e `.context/planos` foram **eliminadas** para reduzir o ruído cognitivo. O histórico foi movido para `planos/_arquivo_planos/` na raiz.
*   **Regra de Ouro:** Nunca edite arquivos em `.context/` sem atualizar o `JOURNAL.md`. O sistema SAM (Anti-Migué) está ativo e bloqueia o commit se você tentar "pular etapas".
*   **Fuso Horário:** O sistema opera nativamente em **Brasília (-3h)**. Registros de data fora desse padrão podem gerar alertas de inconsistência.

---

## 5) Leitura Funcional do Repositório

O repositório está organizado em uma **Hierarquia de Verdade**:
1.  **Nível 0 (Leis):** `RULES.md`, `INCEPTION.md`.
2.  **Nível 1 (Planos):** `PRD.md`, `ROADMAP.md`.
3.  **Nível 2 (Ação):** `.specs/features/`.
4.  **Nível 3 (Evidência):** `JOURNAL.md`, `HARNESS_LOG.md`.

**Veredito:** O repositório está em estado **Hardened (Endurecido)**. Toda mudança é rastreável, cada linha de código tem um contrato e a IA é mantida sob rédea curta por scripts de validação contínua.

---
**Gerado por:** `@antigravity-agent`
**Inspirado em:** `aline-insta/Rx_pastas.md`
