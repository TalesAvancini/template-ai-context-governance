# 🚀 Guia de Migração: Do Template para o Projeto Real

Este guia descreve como "descolar" este template do repositório de origem e iniciar seu novo projeto com a Governança Antigravity Kit v2.4.1.

---

## 🛠️ Passo a Passo via CLI

### 1. Clonar o Template
Escolha um nome para a pasta do seu novo projeto (Ex: `meu-novo-projeto`).
```powershell
git clone https://github.com/TalesAvancini/template-ai-context-governance.git meu-novo-projeto
cd meu-novo-projeto
```

### 2. Romper o vínculo com o Antigravity (Reset do Git)
Delete o histórico de commits do template para começar sua própria história do zero.
```powershell
# No Windows (PowerShell)
Remove-Item -Recurse -Force .git

# No Linux/Mac/WSL
rm -rf .git
```

### 3. Iniciar seu novo Repositório
```powershell
git init
git add .
git commit -m "chore: initial commit from Antigravity Kit v2.4.1"
```

### 4. Conectar ao seu NOVO repositório no GitHub
Crie um repositório vazio no seu GitHub e utilize a URL dele abaixo:
```powershell
git remote add origin https://github.com/SEU_USUARIO/SEU_NOVO_REPOSICTORIO.git
git branch -M main
git push -u origin main
```

### 5. Ativar o Motor de Governança
Garanta que os Hooks e dependências estejam prontos no novo ambiente.
```powershell
# Instalar dependências (Husky, etc)
npm install

# Rodar a validação completa pela primeira vez
npm run context:all
```

---

## 💡 Dicas de Manutenção
*   **package.json**: Edite os campos `name`, `version`, `author` e `description` para refletir a sua nova aplicação.
*   **README.md**: Atualize o título e a descrição principal do projeto, mantendo as seções de Operação de Contexto.
*   **Timezone**: Verifique se o arquivo `.env` do novo projeto possui a variável `CONTEXT_TIMEZONE` se você não estiver operando no fuso de Brasília.

---
> 🛸 **Antigravity Kit** | Governança não é burocracia, é a fundação da inteligência escalável.
