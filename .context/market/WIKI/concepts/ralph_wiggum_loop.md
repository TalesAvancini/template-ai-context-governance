---
id: RALPH_WIGGUM_LOOP
type: concept
tags: [harness-engineering, agent-execution, context-management, ralph-wiggum]
aliases: [Atomic Loop, Clean Context Execution, O Loop de Ralph]
concept: Execução Atômica com Estado Limpo
entity: Antigravity Framework
source: market/RAW/ralph_wiggum_loop_dossier.md
last_updated: 2026-04-23
---

# Ralph Wiggum Loop

> Fonte: market/RAW/ralph_wiggum_loop_dossier.md

O **Ralph Wiggum Loop** é um padrão de execução para agentes de IA que prioriza a **sanidade cognitiva** do modelo através da aniquilação periódica da memória de chat. Inspirado na premissa de que o sistema de arquivos e o histórico do Git são memórias superiores à janela de contexto de um LLM, o método força a IA a "renascer" a cada tarefa, lendo apenas o estado atual necessário do disco.

O nome refere-se ao personagem Ralph Wiggum (*Os Simpsons*), simbolizando o foco na simplicidade determinística e na execução "cega" de especificações rígidas.

## Key Takeaways
*   **Aniquilação de Context Rot:** Impede que o histórico de tentativas falhas e conversas longas degrade a qualidade do raciocínio da IA.
*   **Cura da Context Anxiety:** Remove a ansiedade do modelo ao perceber a janela de tokens cheia, fornecendo uma "lousa em branco" a cada iteração.
*   **Maker vs. Checker:** Facilita a separação de papéis, pois o executor do loop foca apenas em cumprir a spec, enquanto o validador atua em um contexto separado.
*   **Backpressure Mecânico:** O loop só avança se passar por verificações determinísticas (testes, linters, compilers).

### ⚙️ Mecânica de Funcionamento (H.O.K. Integration)

No framework Antigravity (v2.5.2), o Ralph Wiggum Loop é implementado através da estrutura de **Specs Atômicas**:

1.  **Isolamento (Fresh Context):** Cada vez que um agente inicia o trabalho em uma spec (ex: `.specs/features/X`), ele não carrega o histórico de chats passados. O contexto é montado "just-in-time" usando apenas o `STATE.md` e os arquivos da Wiki necessários.
2.  **O Orquestrador:** O script `harness_runner.py` atua como o controlador do loop. Ele verifica o sinal de conclusão (`qa_signoff: true`) e as evidências de teste.
3.  **Persistência (A Memória):** O `JOURNAL.md` e o `STATE.md` são os arquivos onde a IA deposita o conhecimento adquirido, garantindo que o próximo agente que "nascer" saiba exatamente de onde continuar.

### 🛑 O Funil de Execução
O Ralph Wiggum Loop **nunca** deve ser usado para descoberta ou brainstorming. O fluxo obrigatório é:
1.  **Descoberta:** Conversa humana/IA (Vibe Coding permitido aqui).
2.  **Especificação:** Criação da Spec rígida (O Contrato).
3.  **Execução (O Loop):** Ativação da IA para cumprir a spec de forma determinística e autônoma.

## Related
*   [[harness_behavior]] (Cura do Leniency Bias)
*   [[karpathy_protocol]] (Linter Epistemológico)
*   [[context_isolation]] (Blindagem de Contexto)
