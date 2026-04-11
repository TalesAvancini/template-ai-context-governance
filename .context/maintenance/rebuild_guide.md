---
Criado em: 2026-04-10 21:44
Ultima Atualizacao: 2026-04-10 21:44
Status: Ativo
---

# 🛠️ Manual de Reconstrução & Automação

Este guia contém as instruções para subir o ambiente do zero e operar as ferramentas de governança de contexto.

---

## 🏗️ 1. Setup do Ambiente

### Requisitos Mínimos:
- **Python ≥ 3.8** (Para os scripts de automação)
- **Node.js** (Para os wrappers NPM)
- **Make** (Opcional, para orquestração Unix)
- **Bash** (Para Git Bash, WSL, Linux ou macOS)

---

## ⚙️ 2. Ferramentas de Automação

O projeto oferece três formas de gerenciar a saúde do contexto. Escolha a que melhor se adapta ao seu terminal:

### Opção A: Via NPM (Recomendado para Devs Web)
```bash
npm run context:validate  # Checa integridade e tokens
npm run context:sync      # Sincroniza deps e schema
npm run context:purge     # Limpa e arquiva o log vivo
```

### Opção B: Via Make (Recomendado para CI/CD e Unix)
```bash
make validate
make sync
make purge
make all       # Executa o pipeline completo: Valida -> Sync -> Purge
```

### Opção C: Via Bash (Resiliência Universal)
```bash
./run_context.sh validate
./run_context.sh all
```

---

## 🗃️ 3. Recuperação de Contexto (Archive)

Se precisar restaurar um Journal ou PRD antigo que foi arquivado:
1. Vá até `.context/maintenance/_archive_context/`.
2. Localize o arquivo pelo timestamp `YYYYMMDD_HHMMSS`.
3. Copie o conteúdo necessário de volta para a raiz da camada correspondente (`maintenance/` ou `brain/`).

---

## 🚨 4. Troubleshooting
- **Erro de Encoding (Windows):** Todos os scripts são forçados para UTF-8. Se vir caracteres estranhos, verifique se o seu terminal suporta Unicode.
- **Python não encontrado:** No Windows, o script tenta `python3` e faz fallback para `python`. Se falhar, certifique-se que o executável está no seu PATH.

> *Lembrete: Sem automação, a documentação morre. Use as ferramentas a cada nova funcionalidade iniciada no ROADMAP.md.*
