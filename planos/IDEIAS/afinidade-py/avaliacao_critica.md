# Avaliação Crítica: `affinity_scanner.py` (Plano de 4 Eixos)

> Avaliador: Antigravity Agent (Claude Opus 4.6)
> Data: 2026-05-05
> Contexto: Avaliação técnica do plano descrito em `afinnity.md`, considerando o estado atual do ecossistema H.O.K Forge v2.6.2+ com SAM, journal-sync v2.0 e rx-communications.md (Seções 4 e 5).

---

## 1. Veredito Geral

**O plano é tecnicamente sólido e genuinamente útil.** A arquitetura de 4 eixos com fusão ponderada e detecção de drift é uma abordagem sofisticada que resolve um problema real: descobrir acoplamentos que a curadoria manual do `rx-communications.md` não consegue capturar.

A jóia do plano não está nos eixos individuais — está na **discordância entre eles** (Drift Detection). Quando os eixos discordam sobre um par de arquivos, isso revela insights que nenhuma análise isolada entrega.

---

## 2. Avaliação por Eixo

| Eixo | Score | Justificativa |
|---|---|---|
| **Referencial** | **9/10** | Determinístico. Detecta quem cita quem com precisão. Quase zero falsos positivos. O bônus de "verbos de obrigação" (DEVE, PROIBIDO) é um toque inteligente que eleva referências passivas vs. referências normativas. |
| **Temporal** | **9/10** | O insight mais original de todo o plano. Revela acoplamento *real* que nenhuma análise estática vê. Limitação: precisa de volume de commits para ser confiável (mínimo ~50 commits substanciais). Problema temporário para projetos jovens. |
| **Operacional** | **8/10** | Com a Seção 5 do `rx-communications.md` já estruturada, este eixo é essencialmente leitura de dados curados. Alta confiabilidade. A transitividade fraca (0.3) para arquivos co-consumidos é uma calibração sensata. |
| **Semântico (TF-IDF)** | **5/10** | O eixo mais fraco. Documentos de governança compartilham vocabulário demais ("commit", "journal", "regra", "governance", "spec"). O `max_df=0.95` não filtra esses termos porque eles aparecem em ~60-70% dos docs, não em 95%. Sem custom stop words agressivas, este eixo gera ruído que polui o score final. |
| **Fusão + Drift** | **10/10** | A verdadeira inteligência do sistema. A tabela de classificação de drift (Latente, Mecânico, Fantasma, Motor, Referência Morta) é actionable e cada tipo mapeia para uma ação concreta. Isso sozinho justifica a existência do scanner. |

---

## 3. Pontos Fortes

### 3.1 A Detecção de Drift é Irreplicável Manualmente
Nenhum humano ou IA, lendo documentos manualmente, vai perceber que `RULES.md` e `STATE.md` mudam juntos em 80% dos commits mas nenhum referencia o outro. Isso é um "Acoplamento Fantasma" que só a combinação Temporal × Referencial revela.

### 3.2 Arquivos Órfãos como Candidatos a Remoção
A detecção de arquivos sem afinidade > 0.3 é uma ferramenta de limpeza poderosa. Se um arquivo não é mencionado, não muda com ninguém, e nenhum script o consome — ele é peso morto.

### 3.3 O Output é Focado, Não É Uma Matriz Crua
O script gera Top-20 pares, Top-10 blast radius e uma lista de órfãos. Isso já é uma lista de adjacência focada, não uma NxN gigante para humanos lerem. A representação interna (numpy NxN) é um detalhe de implementação computacional — eficiente e invisível para o consumidor.

### 3.4 O Grafo Mermaid é Excelente para Onboarding
Um novo membro da equipe pode abrir o `rx-affinity.md`, ver o grafo, e em 30 segundos entender quais arquivos são os "hubs" do sistema.

---

## 4. Pontos Fracos e Riscos

### 4.1 O Eixo Semântico Precisa de Tuning Pesado
**Problema:** Em um ecossistema de governança, TODOS os documentos falam sobre os mesmos conceitos. O TF-IDF vai gerar alta similaridade entre pares que não são realmente acoplados.

**Mitigação sugerida:**
- Reduzir o peso do eixo semântico de 0.20 para **0.10** na fusão.
- Ou: Criar uma lista de stop words customizada com termos de governança (`commit`, `journal`, `rules`, `governance`, `spec`, `harness`, `pipeline`, `validation`, `context`).
- Ou: Implementá-lo por último e avaliar se agrega valor real antes de incluí-lo na fusão.

### 4.2 Histórico Git Jovem Limita o Eixo Temporal
**Problema:** Com poucos commits, o Jaccard será esparso e instável. Pares que co-ocorreram 2 vezes em 10 commits terão score alto mesmo que seja coincidência.

**Mitigação sugerida:**
- O script já prevê o advisory para < 50 commits. Manter essa guarda.
- Considerar um `min_commits` por arquivo: se um arquivo aparece em < 3 commits, excluí-lo do eixo temporal.

### 4.3 scikit-learn como Dependência
**Avaliação recalibrada:** Para um script de análise que roda sob demanda (`npm run context:affinity`), NÃO é a mesma coisa que uma dependência de CI/CD. O `validate_context.py` roda a cada commit e precisa ser stdlib puro. O affinity scanner rodaria semanal ou on-demand. Ter scikit-learn como dev dependency neste caso é **pragmatismo legítimo**, não violação de princípio.

**Alternativa se desejável:** TF-IDF pode ser implementado com `collections.Counter` e `math.sqrt` em ~40 linhas extras. Perda de performance desprezível para 92 arquivos.

---

## 5. Bugs Identificados no Código

| Localização | Bug | Correção |
|---|---|---|
| Eixo Temporal, `calcular_eixo_temporal()` | `matriz[j][j] = score` (linha do Jaccard simétrico) | Deveria ser `matriz[j][i] = score`. Está atribuindo à diagonal em vez do par simétrico. |
| Eixo Temporal, `_ambos_mudaram_recentemente()` | `max(intersecao)` em hashes SHA | O máximo lexicográfico de um SHA **não é** o commit mais recente. Precisa de `git log --format=%ct` para comparar timestamps reais. |
| Eixo Operacional, `_parsear_secao_5()` | Regex `\w+\.py` para detectar scripts | A Seção 5 agora inclui `journal-sync/SKILL.md` (não é `.py`). O regex precisa ser generalizado para capturar skills e outros automators. |

---

## 6. Ordem de Implementação Recomendada (ROI Máximo)

A ordem original do plano (Referencial → Semântico → Temporal → Fusão → Drift) não é ótima em termos de retorno sobre investimento. A ordem que entrega valor incremental máximo a cada fase:

| Prioridade | Eixo | Justificativa |
|---|---|---|
| **1º** | Temporal (Git) | Entrega o insight mais original e irreplicável. Mesmo sozinho, já revela Acoplamentos Fantasma. |
| **2º** | Referencial | Complementa o Temporal com dados determinísticos. Juntos permitem o primeiro Drift Detection. |
| **3º** | Operacional | Adiciona a camada de scripts/automação. Com a Seção 5 já estruturada, é parsing simples. |
| **4º** | Semântico | Só vale a pena se os 3 anteriores já estiverem calibrados. Pode ser experimental inicialmente. |

---

## 7. Relação com o Ecossistema Existente

| Ferramenta Atual | Papel | Relação com Affinity Scanner |
|---|---|---|
| `rx-communications.md` (manual) | Mapa de dependências curado pelo humano | O scanner **valida e complementa** o mapa manual. Detecta o que o humano esqueceu. |
| `journal-sync` v2.0 | Propagação baseada em `git status` + rx-communications | O scanner pode **alimentar** o journal-sync com novos pares que deveriam estar no rx-communications. |
| SAM (Auditor) | Verifica coerência entre Journal e Git | O scanner opera em camada diferente: não valida commits, mas **descobre relações estruturais**. São complementares. |

**Insight chave:** O affinity scanner não substitui nada do que existe. Ele é uma **ferramenta de descoberta** que alimenta as ferramentas de **enforcement** (SAM, journal-sync).

---

## 8. Conclusão

O plano é **aprovado com reservas técnicas**. A arquitetura é sólida, o conceito é valioso, e as saídas são bem desenhadas. As reservas são:

1. O Eixo Semântico precisa de calibração ou peso reduzido.
2. Corrigir os 3 bugs identificados antes de qualquer implementação.
3. Priorizar a ordem de implementação por ROI (Temporal → Referencial → Operacional → Semântico).

**A pergunta estratégica final:** *Quando* implementar? O ecossistema atual (SAM + journal-sync + rx-communications) já é funcional e blindado. O affinity scanner é uma evolução que agrega inteligência, não uma necessidade urgente. Pode ser implementado como um "Sprint de Maturidade" quando o repositório tiver massa crítica de commits (~100+) para o Eixo Temporal brilhar.
