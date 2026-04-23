# 🛸 Antigravity Kit v2.5.2 Hardened (H.O.K. Enabled)
> **O ecossistema definitivo para engenharia AI-Ready: Governança Macro + Execução Atômica + Controle Ativo.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação. Ele unifica o **Antigravity Kit** com o **TLC Spec-Driven** e eleva a governança ao **Nível 3 (H.O.K.)**, garantindo que Propósito → Execução → Validação operem em loop fechado e autônomo.

---

## 🛡️ A Tríade H.O.K. (Governança Nível 3)
O kit evoluiu de validação passiva para **controle ativo e reativo**:
| Pilar | Função | Script | Gatilho |
|-------|--------|--------|---------|
| 🛡️ **Harness** | Bloqueia specs que violam contratos (Schema vs PRD, Handoffs incompletos) | `harness_runner.py` | `npm run context:all` / `pre-commit` |
| 🔍 **Oracle**  | RAG local `stdlib` que resolve ambiguidades antes da geração de código | `context_oracle.py` | `npm run context:oracle "dúvida"` |
| 📖 **Karpathy**| Linter epistemológico: exige `> Fonte: raw/...` em claims técnicos | `lint_wiki.py` | `npm run context:lint` (Strict no commit) |

> 💡 **Regra de Ouro:** `Se não está no .context, não existe. Se não tem fonte, é alucinação. Se não passa no Harness, não vai pro repositório.`

---

## 🚀 Instalação e Onboarding

### Cenário 1: Repositório Novo (Template)
Se você apenas clonou este repositório base, você já possui todo o ecossistema Antigravity. Apenas execute:
```bash
npm install
npm run prepare # ativa os hooks do Husky
```

### Cenário 2: Aplicando a projetos existentes (Bootstrapper)
Se você quer governar um projeto pré-existente, copie os arquivos `.context/_scripts/`, `run_context.py` e execute o integrador via Bash:
```bash
# O ambiente precisa de um bash real compatível (Linux/Mac/WSL/Git Bash)
bash init_ai_project.sh
```
> ⚠️ **Aviso Operacional:** O `init_ai_project.sh` cria as pastas estruturais de regras e injeta NPM Scripts cross-platform. Ele **não** gera os motores internos e aborta se a pasta `.context/` estruturada já existir. Certifique-se de copiar os `.py` desta raiz se estiver instalando manualmente!

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. Regras, Fronteiras (VISION/INCEPTON) e PRD-Template.
- **`market/`**: Camada Estratégica. Restrições do mundo real, dependências externas e compliance.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.
- **`_scripts/`**: Validação ativa (Harness e Oracle) escrita na biblioteca Padrão do Python (Seguro Cross-Platform).

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação (v2.5.2)
| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Checa integridade, estrutura e estimativa de tokens |
| `npm run context:harness`  | Valida contratos ativos e handoffs (`harness_runner.py`) |
| `npm run context:oracle`   | Roteia consulta proativa ao Oráculo local (com confidence) |
| `npm run context:lint`     | Fiscaliza citações epistemológicas e claims sem fonte |
| `npm run context:all`      | 🟢 Pipeline C-Level: Validate → Sync → Cleanup → Harness → Lint(Strict) |

---

## 🤝 Protocolo de Ativação Híbrida

Para iniciar uma tarefa com poder total, use o prompt mestre:
> *"Inicie a fase de SPECIFY para o PRD #[ID] usando o modo Híbrido TLC."*

Isso ativará a role `@spec-driver` e iniciará o ciclo atômico no `.specs/` alinhado à governança do `.context/`.

---

## 🕐 Configuração de Fuso Horário
Por padrão, o kit usa **America/Sao_Paulo (Brasília)** (-3h fixo). Para alterar globalmente:

```bash
# No terminal (temporário)
export CONTEXT_TIMEZONE="America/New_York"
npm run context:all

# Ou no .env do projeto (permanente)
echo "CONTEXT_TIMEZONE=Europe/London" >> .env
```

*Nota: Usa apenas Python stdlib (sem dependência do módulo 'pytz') para máxima compatibilidade cruzada.*

---

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*
