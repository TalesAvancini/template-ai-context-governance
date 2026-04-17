---
version: 2.4.1
mode: STRATEGIC
status: ACTIVE  # [DRAFT | ACTIVE | TRANSLATION_LOCK]
---

# 🧭 INCEPTION - Fronteiras Estratégicas (SSOT)

*Ratificado a partir da tradução cognitiva do `VISION.md`.*

## 🎯 Visão Mestra
O Antigravity Kit (H.O.K Forge v2.4.1) é uma solução de **Harness Engineering** projetada para PMEs e Tech Leads. Seu objetivo é controlar o "AI Slop" e governar as IA geradoras de código através de uma arquitetura determinística implacável, reduzindo confabulações e inchaço de contexto sem depender de infraestruturas MLOps complexas. A equação fundamental é **Agente = Modelo + Harness**.

## 🛑 NUNCA (Boundaries)
> *Limites inegociáveis. Se a IA tentar cruzar estas linhas, o Harness aplicará o fail-fast.*

- **NUNCA** utilizar infraestruturas de MLOps de grande porte ou bancos vetoriais pesados. A indexação deve permanecer leve, rápida e focada na realidade financeira do projeto.
- **NUNCA** confiar apenas na aprovação sintética da IA (Leniency Bias). Nenhuma linha é final sem passar pelo sensor computacional rígido do Harness de Contratos (`harness_runner.py`).
- **NUNCA** introduzir complexidade tecnológica desnecessária no banco de estados; o repositório **deve** usar apenas `.md`, `.json` e `.sql` como SSOT (Single Source of Truth).
- **NUNCA** permitir confabulação de dados. Afirmações técnicas sem citação explícita (`> Fonte: raw/...`) do Linter Epistemológico (Karpathy rule) serão sumariamente rejeitadas.
- **NUNCA** trabalhar com contexto infinito. As execuções devem usar o *Ralph Wiggum Loop*, quebrando o desenvolvimento em Specs Atômicas com aniquilação periódica de memória.

## 🟢 SEMPRE (Restrições de Processo)
> *Processos que a IA deve invocar obrigatoriamente durante o ciclo de vida.*

- **SEMPRE** utilizar bibliotecas padrão (`stdlib-only`) para os scripts do Oráculo, garantindo execução local independente de contêineres e dependências pesadas.
- **SEMPRE** aplicar a "Divulgação Progressiva". O conhecimento deve ser roteado *just-in-time*, entregando ao modelo apenas o que ele precisa saber para a task efêmera, evitando Context Bloat.
- **SEMPRE** validar os limites técnicos usando o `schema.sql` antes de qualquer ação generativa de UI ou banco.
- **SEMPRE** utilizar a pasta `market/` para populacionar lacunas tecnológicas via "Spec Enricher" antes de compilar Documentos de Requisitos finais (PRDs).