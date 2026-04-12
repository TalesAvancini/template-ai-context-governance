# 🛸 Antigravity Kit v2.3 Premium+ (H.O.K. Enabled)
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

## 🚀 Instalação Ultra-Rapida (One-Click Setup)

Se voce quer inicializar este framework em um novo projeto do zero, basta rodar o nosso bootstrapper supremo:

```bash
# 1. Torne o script executavel
chmod +x init_ai_project.sh

# 2. Execute
./init_ai_project.sh
```

O script ira criar automaticamente toda a estrutura de camadas, os workshops de execução, os motores de manutenção v2.2+, e configurar a blindagem Husky.

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. PRD v2.0, Rules, Registry e a Ponte de Integração TLC.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação (v2.3)
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

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*
