# 🛠️ Guia de Estabilização: NotebookLM + Antigravity

Este guia contém a "receita do bolo" para resolver falhas de autenticação e conexão no servidor MCP do NotebookLM. Siga estes passos se a IA perder o acesso ao seu Save Point.

---

## 🚀 1. Preparação do Ambiente (Obrigatório)
Sempre que for rodar comandos de diagnóstico no PowerShell, rode este comando primeiro para evitar erros de caracteres especiais:

```powershell
$env:PYTHONUTF8=1
```

---

## 🛠️ 2. Correção de Dependências (O "Soro")
O Google detecta robôs facilmente. Para o login **persistir no disco**, o Python precisa destes três componentes:

1. **undetected-chromedriver**: Faz o navegador parecer humano.
2. **setuptools**: Necessário para versões modernas do Python (3.12+).

**Comando para reinstalar tudo se parar de funcionar:**
```powershell
uv pip install --python C:\Users\User\AppData\Roaming\uv\tools\notebooklm-mcp\Scripts\python.exe undetected-chromedriver setuptools
```

---

## 🔑 3. O Fluxo de Login Definitivo
Se a IA disser "Not Authenticated", siga este ritual:

1. Abra o arquivo `C:\Users\User\.gemini\antigravity\notebooklm-config.json`.
2. Mude `"headless": true` para **`false`**.
3. No terminal, rode: 
   `uv tool run notebooklm-mcp chat -n 8979de2f-a111-4856-8a71-197d6b9ec876`
4. **Logue manualmente** na janela que abrir.
5. Quando o notebook carregar, feche a janela e mude o config de volta para **`true`**.

---

## 🧠 4. Como o MCP funciona na prática?
Você **não** precisa dizer qual pasta eu devo ler. O sistema funciona por **ID de Notebook**:

*   **Vínculo:** O seu projeto local está vinculado ao Notebook **"Template-framework-HOK"** via ID.
*   **Ação:** Quando você me pede algo, eu uso o MCP para pesquisar nas **32 fontes** (PDFs, Docs, Planilhas) que você subiu lá no Google.
*   **Vantagem:** Você pode subir 1000 PDFs no NotebookLM e eu terei acesso a todo esse conhecimento sem "estourar" o limite de memória do nosso chat aqui.

---

> [!IMPORTANT]
> **Caminho do Perfil:** Suas senhas ficam salvas localmente em:
> `C:\Users\User\.gemini\antigravity\chrome_profile_notebooklm`
> **NUNCA** delete esta pasta, ou terá que logar novamente.

> [!TIP]
> **Notebook Errado?** Se quiser trocar de notebook, basta mudar o `default_notebook_id` no arquivo `notebooklm-config.json`.
