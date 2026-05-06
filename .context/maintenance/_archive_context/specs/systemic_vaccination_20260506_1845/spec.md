# Spec: Vacinação Sistêmica & Formalização de Ritos H.O.K

## 1. Visão Geral
**Status:** CLOSED
**Contexto:** Erros recentes (como a Síndrome da Mosca e a Fraude Narrativa causada por leitura de cache/passado) demonstraram que as diretrizes do `hok-governor` sofrem de "Drift de Atenção" durante execuções longas. Precisamos injetar essas "vacinas" físicas no `LEARNINGS.md` (Córtex Estratégico) e forçar a validação tática no `journal-sync` (força imperativa).

## 2. Objetivos da Sprint (Sprint 01)
- **Córtex Estratégico:** Injetar as regras [SCAR-007] (Formatação Estrita YAML x Markdown) e [SCAR-008] (A Síndrome da Mosca na Janela) no arquivo `LEARNINGS.md`.
- **Bússola Comportamental:** Executar a poda cirúrgica do `hok-governor/SKILL.md` (Cortar Lei 4 - KBuM e Lei 8 - Espelhamento de Metadados).
- **Rito de Sincronia:** Adicionar restrição inviolável de `PLAIN TEXT` para os campos do contrato no `journal-sync/SKILL.md`.

## 3. Restrições e Escopo Negativo (CONSTRAINTS)
- **NÃO** alterar scripts Python do sistema de governança (`.context/_scripts/`).
- **NÃO** deletar o conteúdo histórico do `LEARNINGS.md` (utilizar técnica de append/inserção cuidadosa).
- **NÃO** realizar commits automáticos.
- **NÃO** iniciar a escrita sem antes validar a leitura do `.enriched.md` (Rito do Córtex).

## 4. Allow List (Gatekeeper Permissions)
Esta lista tranca o escopo físico da feature. O Gatekeeper bloqueará alterações fora destes arquivos:
- `.context/brain/LEARNINGS.md`
- `.agent/skills/journal-sync/SKILL.md`
- `.agent/skills/hok-governor/SKILL.md`

## 5. Contract
- contract_mode: sprint_based
- current_sprint: sprint_01
- sprint_01:
  - [x] Injeção de SCARs no Córtex
  - [x] Poda do HOK Governor
  - [x] Endurecimento do Journal Sync

## 6. QA Sign-Off
- **Auditor:** @qa-validator (Antigravity AI)
- **Verdict:** APPROVED
- **Evidence:**
  - [x] SCAR-007 e SCAR-008 validados fisicamente no `LEARNINGS.md`.
  - [x] Poda das Leis 4 e 8 confirmada no `hok-governor/SKILL.md`.
  - [x] Cláusula de Castidade (Plain Text) confirmada no `journal-sync/SKILL.md`.
  - [x] Reality Check: `JOURNAL.md` em sincronia com o estado físico do Git.
- **Timestamp:** 2026-05-06 21:30

