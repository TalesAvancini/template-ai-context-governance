---
Criado em: 2026-04-14 11:50
Status: Ativo
---

# ⚖️ SSOT_MAP: Hierarquia de Verdade (v2.4.1 Hardened)

> Este mapa define a precedência absoluta de informações. Em caso de conflito, a camada superior anula a inferior.

1.  ⚖️ **Market Compliance** (`market/compliance/*.md`): Restrições legais, jurisdição e termos de terceiros (Stripe, Apple, LGPD). **BLOQUEANTE**.
2.  🧭 **Inception Layer** (`brain/INCEPTION.md`): Boundaries estratégicos e Vibe do produto. **BLOQUEANTE**.
3.  📜 **Rules of Engagement** (`brain/RULES.md`): Protocolos de IA e Máquina de Estados.
4.  🎯 **Execution Context** (`brain/PRD.md` + `maintenance/schema.sql`): O contrato técnico atual.
5.  🕒 **Operational History** (`maintenance/JOURNAL.md`): Memória de curto prazo das sessões.

---
> ⚠️ **Harness Gate**: O `harness_runner.py` valida automaticamente se o PRD viola os boundaries definidos no `INCEPTION.md` (regras `- NUNCA:`).
