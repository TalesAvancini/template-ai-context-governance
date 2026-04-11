---
Criado em: 2026-04-10 22:30
Ultima Atualizacao: 2026-04-10 22:30
Status: Ativo (EM EXECUCAO)
---

# 📦 PRD #15: Checkout com Integração Stripe

## 🎯 Objetivo
Implementar um fluxo de pagamento seguro e resiliente usando Stripe Elements e Webhooks.

## 🛠️ Requisitos
- [ ] UI: Form de pagamento customizado (Elements).
- [ ] Backend: Gerar `PaymentIntent` e processar Webhooks.
- [ ] DB: Salvar estado em `orders` (pending, success, failed).

## 🚨 Criterios de Aceite
1. O usuario nao pode fechar o checkout sem um Order ID gerado.
2. Webhooks devem ser idempotentes.
3. Tratamento de erro claro para "Card Declined".
