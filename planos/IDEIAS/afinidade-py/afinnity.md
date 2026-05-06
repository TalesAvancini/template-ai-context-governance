# Plano Completo: Script de 4 Eixos — `affinity_scanner.py`

---

## Contexto: O que a atualização do `rx-communications.md` muda

A adição da **Seção 5 (Matriz de Acoplamento de Automação)** é a peça que faltava. Agora cada script tem declarado o que **lê** (depende de) e o que **escreve em** (afeta). Isso significa que o eixo operacional do script de 4 eixos não precisa mais fazer parsing de paths dentro dos `.py` — ele pode ler diretamente a Seção 5 como fonte estruturada.

Antes: os scripts eram invisíveis na matriz de acoplamento.
Agora: estão mapeados com direcionalidade (`Lê` → `Escreve em`).

Isso simplifica o eixo operacional de "regex em código Python" para "parsing da tabela do rx-communications".

---

## Visão Geral da Arquitetura

```
affinity_scanner.py
│
├── Eixo 1: Semântico    (TF-IDF cosine similarity)
├── Eixo 2: Referencial   (menções cruzadas entre arquivos)
├── Eixo 3: Operacional   (scripts como pontes entre arquivos)
├── Eixo 4: Temporal      (co-ocorrência no Git history)
│
├── Fusão ponderada → Matriz de Afinidade NxN
│
└── Saídas:
    ├── rx-affinity.md          (documento legível)
    ├── rx-affinity.json        (dados brutos para outros scripts)
    └── Seção atualizada no CONTEXT_HEALTH.md
```

---

## Especificação Detalhada por Eixo

### Eixo 1 — Semântico

**Objetivo:** Medir quão similares são dois arquivos em termos de vocabulário e tema.

**Algoritmo:** TF-IDF + Cosine Similarity

**Justificativa para TF-IDF (e não embeddings):**
- O framework já prioriza `stdlib` e dependências leves (`context_oracle.py` usa stdlib puro)
- `scikit-learn` é leve e roda offline
- Para 92 arquivos, TF-IDF é suficiente — embeddings de LLM seriam overkill e adicionariam latência/API key

**Implementação:**

```python
# === EIXO 1: SEMÂNTICO ===

import os
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calcular_eixo_semantico(arquivos: dict[str, str]) -> np.ndarray:
    """
    Recebe: dict {caminho_relativo: conteudo_texto}
    Retorna: matriz NxN de similaridade cosine (0.0 a 1.0)
    """
    caminhos = list(arquivos.keys())
    textos = list(arquivos.values())
    
    # TF-IDF com bigramas para capturar termos técnicos compostos
    # Ex: "fail closed", "blast radius", "token bloat"
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        stop_words=None,  # Não remover stop words — em governança, 
                           # conectivos importam ("nunca", "sempre", "deve")
        min_df=1,          # Aceitar termos que aparecem em 1+ arquivo
        max_df=0.95        # Ignorar termos em 95%+ dos arquivos (ruído)
    )
    
    tfidf_matrix = vectorizer.fit_transform(textos)
    cosine_matrix = cosine_similarity(tfidf_matrix)
    
    # Zerar diagonal (arquivo não é afim de si mesmo)
    np.fill_diagonal(cosine_matrix, 0.0)
    
    return cosine_matrix
```

**Tratamento de arquivos especiais:**
- Scripts Python (`.py`): incluir, mas com peso reduzido no eixo semântico (0.5x) porque o vocabulário técnico de código é diferente do vocabulário de governança
- Arquivos YAML/JSON: extrair apenas campos de texto (descrições, nomes) — ignorar estrutura sintática
- SQL: incluir apenas comentários e nomes de tabelas

**Normalização:** Cada score é dividido pelo valor máximo do eixo para ficar entre 0.0 e 1.0.

---

### Eixo 2 — Referencial

**Objetivo:** Capturar menções explícitas entre arquivos (um arquivo cita o nome de outro).

**Algoritmo:** Busca de substring com heurísticas de contexto.

**Implementação:**

```python
import re
from pathlib import Path

def calcular_eixo_referencial(arquivos: dict[str, str]) -> np.ndarray:
    """
    Para cada par (A, B), verifica se A menciona o nome de B
    em seu conteúdo. Retorna matriz NxN com scores ponderados.
    """
    caminhos = list(arquivos.keys())
    n = len(caminhos)
    matriz = np.zeros((n, n))
    
    # Pré-computar nomes "buscáveis" de cada arquivo
    # Ex: "brain/RULES.md" → ["RULES.md", "RULES", "rules"]
    nomes_busca = {}
    for caminho in caminhos:
        stem = Path(caminho).stem           # "RULES"
        fname = Path(caminho).name          # "RULES.md"
        nomes_busca[caminho] = {
            'stem': stem,
            'filename': fname,
            'pattern': re.compile(
                rf'\b{re.escape(stem)}\b',  # Busca com word boundary
                re.IGNORECASE
            )
        }
    
    for i, caminho_a in enumerate(caminhos):
        conteudo_a = arquivos[caminho_a]
        for j, caminho_b in enumerate(caminhos):
            if i == j:
                continue
            
            info_b = nomes_busca[caminho_b]
            matches = info_b['pattern'].findall(conteudo_a)
            
            if not matches:
                continue
            
            # Score base: log do número de menções (diminui retornos)
            import math
            score_bruto = math.log(1 + len(matches))
            
            # Bônus de contexto: se a menção aparece em cabeçalho YAML
            # (Affects, Affected-By), o acoplamento é DECLARADO → peso maior
            if _mencao_em_frontmatter(conteudo_a, info_b['stem']):
                score_bruto *= 2.0
            
            # Bônus: se a menção aparece junto de verbos de obrigação
            # ("DEVE", "OBRIGATÓRIO", "PROIBIDO", "EXIGE")
            if _mencao_com_obrigacao(conteudo_a, info_b['stem']):
                score_bruto *= 1.5
            
            matriz[i][j] = score_bruto
    
    # Normalizar para 0.0 - 1.0
    max_val = matriz.max()
    if max_val > 0:
        matriz = matriz / max_val
    
    return matriz

def _mencao_em_frontmatter(conteudo: str, nome: str) -> bool:
    """Verifica se a menção está dentro do bloco YAML (--- ... ---)"""
    match = re.match(r'^---\n(.*?)\n---', conteudo, re.DOTALL)
    if not match:
        return False
    frontmatter = match.group(1)
    return nome in frontmatter

def _mencao_com_obrigacao(conteudo: str, nome: str) -> bool:
    """Verifica se o nome aparece perto de verbos de obrigação"""
    padroes = [
        rf'(?:DEVE|OBRIGATÓRIO|PROIBIDO|EXIGE|NECESSITA).*?{re.escape(nome)}',
        rf'{re.escape(nome)}.*?(?:DEVE|OBRIGATÓRIO|PROIBIDO|EXIGE|NECESSITA)',
    ]
    return any(re.search(p, conteudo, re.IGNORECASE | re.DOTALL) for p in padroes)
```

**Edge cases tratados:**
- `JOURNAL.md` menciona centenas de arquivos → o `log(1 + n)` impita que 100 menções não sejam 100x mais fortes que 1 menção
- Nomes ambíguos (`STATE` pode aparecer em texto genérico) → o `\b` (word boundary) reduz falsos positivos
- Arquivos com nomes muito curtos (`PRD`) → adicionar verificação de que não é substring de outra palavra

---

### Eixo 3 — Operacional

**Objetivo:** Capturar acoplamento via scripts que consomem múltiplos arquivos (ponte operacional).

**Algoritmo:** Dois passos — parsing da Seção 5 do `rx-communications.md` + inferência de transitividade.

**Implementação:**

```python
import re
from collections import defaultdict

def calcular_eixo_operacional(
    arquivos: dict[str, str],
    rx_communications_path: str
) -> np.ndarray:
    """
    Se A é lido pelo script X, e X escreve em B,
    então A e B têm afinidade operacional via X.
    
    Exemplo:
      harness_runner.py LÊ spec.md
      harness_runner.py ESCREVE em HARNESS_LOG.md
      → spec.md e HARNESS_LOG.md têm afinidade operacional
    """
    caminhos = list(arquivos.keys())
    n = len(caminhos)
    matriz = np.zeros((n, n))
    
    # Passo 1: Extrair relações Lê/Escreve da Seção 5
    grafo_scripts = _parsear_secao_5(rx_communications_path)
    # Resultado: {
    #   "harness_runner.py": {
    #       "le": ["spec.md", ".specs/features/"],
    #       "escreve": ["HARNESS_LOG.md"]
    #   },
    #   ...
    # }
    
    # Passo 2: Para cada script, conectar tudo que ele lê
    #          com tudo que ele escreve
    for script, relacoes in grafo_scripts.items():
        fontes = relacoes['le']
        destinos = relacoes['escreve']
        
        for fonte in fontes:
            for destino in destinos:
                i = _encontrar_indice(fonte, caminhos)
                j = _encontrar_indice(destino, caminhos)
                if i is not None and j is not None:
                    # Afinidade bidirecional mas assimétrica:
                    # fonte → destino tem score mais alto
                    # (a fonte alimenta o destino)
                    matriz[i][j] = max(matriz[i][j], 0.8)
                    matriz[j][i] = max(matriz[j][i], 0.5)
    
    # Passo 3: Transitividade fraca
    # Se script X lê A e B (sem escrever em nenhum),
    # A e B têm afinidade fraca (consomidos pelo mesmo motor)
    for script, relacoes in grafo_scripts.items():
        fontes = relacoes['le']
        if len(fontes) > 1 and not relacoes['escreve']:
            for idx_a, fa in enumerate(fontes):
                for fb in fontes[idx_a + 1:]:
                    i = _encontrar_indice(fa, caminhos)
                    j = _encontrar_indice(fb, caminhos)
                    if i is not None and j is not None:
                        matriz[i][j] = max(matriz[i][j], 0.3)
                        matriz[j][i] = max(matriz[j][i], 0.3)
    
    return matriz

def _parsear_secao_5(rx_path: str) -> dict:
    """
    Faz parsing da Seção 5 do rx-communications.md.
    Procura padrões como:
      - **Lê (Depende de):** `arquivo1.md`, `arquivo2.md`
      - **Escreve em (Afeta):** `arquivo3.md`
    """
    with open(rx_path) as f:
        conteudo = f.read()
    
    # Encontrar a Seção 5
    inicio = conteudo.find('## ⚙️ 5. Matriz de Acoplamento de Automação')
    if inicio == -1:
        return {}
    
    secao = conteudo[inicio:]
    scripts = {}
    script_atual = None
    
    for linha in secao.split('\n'):
        # Detectar nome do script: **`nome_script.py`**
        match_script = re.search(r'\*\*`(\w+\.py)`\*\*', linha)
        if match_script:
            script_atual = match_script.group(1)
            scripts[script_atual] = {'le': [], 'escreve': []}
            continue
        
        if not script_atual:
            continue
        
        # Detectar "Lê (Depende de):"
        match_le = re.search(r'Lê.*?:\s*(.*)', linha)
        if match_le:
            refs = re.findall(r'`([^`]+)`', match_le.group(1))
            scripts[script_atual]['le'].extend(refs)
        
        # Detectar "Escreve em (Afeta):"
        match_escreve = re.search(r'Escreve em.*?:\s*(.*)', linha)
        if match_escreve:
            refs = re.findall(r'`([^`]+)`', match_escreve.group(1))
            scripts[script_atual]['escreve'].extend(refs)
    
    return scripts

def _encontrar_indice(nome_parcial: str, caminhos: list) -> int | None:
    """
    Encontra o índice de um arquivo pelo nome parcial.
    Ex: "RULES.md" encontra ".context/brain/RULES.md"
    """
    for idx, caminho in enumerate(caminhos):
        if caminho.endswith(nome_parcial) or nome_parcial in caminho:
            return idx
    return None
```

**Por que a transitividade é "fraca" (0.3)?**
Porque dois arquivos consumidos pelo mesmo script não necessariamente se afetam mutuamente — eles apenas "coexistem" no mesmo motor. O score baixo reflete isso.

---

### Eixo 4 — Temporal

**Objetivo:** Medir co-ocorrência real de mudanças no histórico Git.

**Algoritmo:** Contagem de commits onde dois arquivos mudaram juntos.

**Implementação:**

```python
import subprocess
from collections import defaultdict

def calcular_eixo_temporal(
    arquivos: dict[str, str],
    repo_path: str = ".",
    max_commits: int = 500
) -> np.ndarray:
    """
    Para cada par (A, B), calcula a frequência com que
    aparecem juntos no mesmo commit.
    
    Fórmula: Jaccard modificado
      co_ocorrencia(A, B) = commits_com_ambos / commits_com_A_ou_B
    """
    caminhos = list(arquivos.keys())
    n = len(caminhos)
    
    # Passo 1: Coletar commits por arquivo
    # arquivo → set de commit hashes
    commits_por_arquivo = _coletar_commits_por_arquivo(
        repo_path, caminhos, max_commits
    )
    
    # Passo 2: Calcular Jaccard para cada par
    matriz = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i + 1, n):
            commits_a = commits_por_arquivo.get(caminhos[i], set())
            commits_b = commits_por_arquivo.get(caminhos[j], set())
            
            if not commits_a or not commits_b:
                continue
            
            intersecao = len(commits_a & commits_b)
            uniao = len(commits_a | commits_b)
            
            if uniao == 0:
                continue
            
            # Jaccard index
            score = intersecao / uniao
            
            # Bônus: se co-ocorrência é alta E ambos mudaram recentemente
            # (últimos 30 dias), o acoplamento é mais relevante
            if _ambos_mudaram_recentemente(
                commits_a, commits_b, repo_path, dias=30
            ):
                score *= 1.3
            
            matriz[i][j] = score
            matriz[j][j] = score  # Simétrico por natureza
    
    # Normalizar
    max_val = matriz.max()
    if max_val > 0:
        matriz = matriz / max_val
    
    return matriz

def _coletar_commits_por_arquivo(
    repo_path: str,
    caminhos: list[str],
    max_commits: int
) -> dict[str, set[str]]:
    """
    Para cada arquivo, roda:
      git log --pretty=format:%H -<max_commits> -- <arquivo>
    e retorna o set de hashes.
    """
    resultado = {}
    for caminho in caminhos:
        try:
            proc = subprocess.run(
                ['git', 'log', '--pretty=format:%H', f'-{max_commits}',
                 '--', caminho],
                capture_output=True, text=True, cwd=repo_path
            )
            if proc.returncode == 0 and proc.stdout.strip():
                hashes = set(proc.stdout.strip().split('\n'))
                resultado[caminho] = hashes
        except FileNotFoundError:
            pass  # Git não disponível
    return resultado

def _ambos_mudaram_recentemente(
    commits_a: set, commits_b: set, 
    repo_path: str, dias: int = 30
) -> bool:
    """Verifica se a interseção mais recente é dentro de N dias"""
    intersecao = commits_a & commits_b
    if not intersecao:
        return False
    # Pega o commit mais recente da intersecao
    mais_recente = max(intersecao)  # Hash lexicográfico é aproximação
    try:
        proc = subprocess.run(
            ['git', 'log', '-1', '--format=%ct', mais_recente],
            capture_output=True, text=True, cwd=repo_path
        )
        if proc.returncode == 0:
            import time
            timestamp = int(proc.stdout.strip())
            dias_desde = (time.time() - timestamp) / 86400
            return dias_desde <= dias
    except:
        pass
    return False
```

**Limitação importante:** Se o repositório tem poucos commits (< 50), o eixo temporal terá dados esparsos. O script deve detectar isso e emitir um aviso: `[ADVISORY] Histórico Git com menos de 50 commits — scores temporais podem ser imprecisos.`

---

## Fusão Ponderada

```python
def calcular_matriz_afinidade(
    eixo_semantico: np.ndarray,
    eixo_referencial: np.ndarray,
    eixo_operacional: np.ndarray,
    eixo_temporal: np.ndarray,
    pesos: dict = None
) -> np.ndarray:
    """
    Fusão ponderada dos 4 eixos em uma matriz final.
    """
    if pesos is None:
        pesos = {
            'semantico': 0.20,
            'referencial': 0.35,
            'operacional': 0.25,
            'temporal': 0.20
        }
    
    matriz_final = (
        pesos['semantico'] * eixo_semantico +
        pesos['referencial'] * eixo_referencial +
        pesos['operacional'] * eixo_operacional +
        pesos['temporal'] * eixo_temporal
    )
    
    return matriz_final
```

**Os pesos são configuráveis** via `version_targets.json` ou um novo campo no `package.json`:

```json
{
  "affinity_weights": {
    "semantic": 0.20,
    "referential": 0.35,
    "operational": 0.25,
    "temporal": 0.20
  }
}
```

Isso permite ajustar sem alterar o script.

---

## Saídas

### Saída 1: `rx-affinity.md`

```python
def gerar_rx_affinity(
    matriz: np.ndarray,
    caminhos: list[str],
    eixos: dict[str, np.ndarray],
    drifts: list[dict]
) -> str:
    """Gera o documento rx-affinity.md"""
    
    md = []
    md.append("# 📊 RX-AFFINITY: Matriz de Afinidade Automática")
    md.append(f"> Gerado por `affinity_scanner.py` em {datetime.now()}")
    md.append("")
    
    # === SEÇÃO 1: Top Afinidades ===
    md.append("## 🔥 Top 20 Pares Mais Afins")
    md.append("| Rank | Arquivo A | Arquivo B | Score | Eixo Dominante |")
    md.append("|------|-----------|-----------|-------|----------------|")
    
    pares = _extrair_top_pares(matriz, caminhos, top=20)
    for rank, (a, b, score, eixo_dominante) in enumerate(pares, 1):
        md.append(f"| {rank} | `{a}` | `{b}` | {score:.3f} | {eixo_dominante} |")
    
    # === SEÇÃO 2: Blast Radius por Arquivo ===
    md.append("")
    md.append("## 💥 Blast Radius (Top 10 Arquivos Mais Conectados)")
    md.append("| Arquivo | Conexões Fortes (>0.5) | Conexões Médias (0.2-0.5) | Grau Total |")
    md.append("|---------|----------------------|--------------------------|------------")
    
    blast_radius = _calcular_blast_radius(matriz, caminhos, threshold_forte=0.5)
    for arquivo, fortes, medias, grau in blast_radius[:10]:
        md.append(f"| `{arquivo}` | {fortes} | {medias} | {grau:.2f} |")
    
    # === SEÇÃO 3: Arquivos Órfãos (Sem Afinidade) ===
    md.append("")
    md.append("## 🏝️ Arquivos Órfãos (Nenhuma afinidade > 0.3)")
    orfaos = _encontrar_orfaos(matriz, caminhos, threshold=0.3)
    for arquivo in orfaos:
        md.append(f"- `{arquivo}` — possível candidato a remoção ou integração")
    
    # === SEÇÃO 4: Drift entre Eixos ===
    md.append("")
    md.append("## ⚠️ Drift Entre Eixos")
    md.append("> Pares onde os eixos discordam fortemente (ex: alto semântico, baixo temporal)")
    md.append("| Arquivo A | Arquivo B | Semântico | Referencial | Operacional | Temporal | Interpretação |")
    md.append("|-----------|-----------|-----------|-------------|-------------|----------|---------------|")
    
    drifts_detectados = _detectar_drift_entre_eixos(eixos, caminhos)
    for drift in drifts_detectados[:15]:
        md.append(
            f"| `{drift['a']}` | `{drift['b']}` | "
            f"{drift['sem']:.2f} | {drift['ref']:.2f} | "
            f"{drift['ope']:.2f} | {drift['tmp']:.2f} | "
            f"{drift['interpretacao']} |"
        )
    
    # === SEÇÃO 5: Grafo Mermaid ===
    md.append("")
    md.append("## 🕸️ Grafo de Afinidade (Mermaid)")
    md.append("```mermaid")
    md.append(_gerar_mermaid(matriz, caminhos, threshold=0.3))
    md.append("```")
    
    return '\n'.join(md)
```

### Saída 2: `rx-affinity.json`

```python
def gerar_rx_affinity_json(
    matriz: np.ndarray,
    caminhos: list[str],
    eixos: dict[str, np.ndarray]
) -> dict:
    """JSON estruturado para consumo por outros scripts"""
    
    pares = []
    n = len(caminhos)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] > 0.1:  # Threshold mínimo
                pares.append({
                    "arquivo_a": caminhos[i],
                    "arquivo_b": caminhos[j],
                    "score_total": round(matriz[i][j], 4),
                    "eixos": {
                        "semantico": round(eixos['semantico'][i][j], 4),
                        "referencial": round(eixos['referencial'][i][j], 4),
                        "operacional": round(eixos['operacional'][i][j], 4),
                        "temporal": round(eixos['temporal'][i][j], 4)
                    }
                })
    
    return {
        "gerado_em": datetime.now().isoformat(),
        "total_arquivos": n,
        "total_pares_relevantes": len(pares),
        "pesos": PESOS_DEFAULT,
        "pares": sorted(pares, key=lambda x: -x['score_total'])
    }
```

### Saída 3: Integração com `CONTEXT_HEALTH.md`

O `health_sync.py` existente pode incluir um resumo:

```markdown
## 📡 Afinidade (último scan: 2026-05-05)
- **Pares fortes (>0.5):** 14
- **Arquivos órfãos:** 3 (`economics.md`, `GUIA_ESTABILIZACAO.md`, `test_oracle.py`)
- **Drifts entre eixos:** 2 (ver `rx-affinity.md` §4)
```

---

## Detecção de Drift Entre Eixos (O Insight Mais Valioso)

Aqui está o verdadeiro diferencial do script. Quando os 4 eixos **discordam** sobre um par de arquivos, isso revela algo que nenhum eixo isolado consegue:

```python
def _detectar_drift_entre_eixos(
    eixos: dict[str, np.ndarray],
    caminhos: list[str],
    threshold_discrepancia: float = 0.4
) -> list[dict]:
    """
    Detecta pares onde os eixos discordam fortemente.
    """
    drifts = []
    n = len(caminhos)
    
    for i in range(n):
        for j in range(i + 1, n):
            scores = {
                'sem': eixos['semantico'][i][j],
                'ref': eixos['referencial'][i][j],
                'ope': eixos['operacional'][i][j],
                'tmp': eixos['temporal'][i][j]
            }
            
            max_score = max(scores.values())
            min_score = min(scores.values())
            discrepancia = max_score - min_score
            
            if discrepancia < threshold_discrepancia:
                continue
            
            # Classificar o tipo de drift
            interpretacao = _classificar_drift(scores)
            
            drifts.append({
                'a': caminhos[i],
                'b': caminhos[j],
                **scores,
                'discrepancia': discrepancia,
                'interpretacao': interpretacao
            })
    
    return sorted(drifts, key=lambda x: -x['discrepancia'])

def _classificar_drift(scores: dict) -> str:
    """Interpreta o padrão de scores entre eixos"""
    
    if scores['sem'] > 0.5 and scores['tmp'] < 0.1:
        return "🔍 Acoplamento Latente — falam do mesmo assunto mas nunca mudam juntos"
    
    if scores['ref'] > 0.5 and scores['sem'] < 0.2:
        return "🔗 Acoplamento Mecânico — um referencia o outro mas vocabulário diverge"
    
    if scores['tmp'] > 0.5 and scores['ref'] < 0.2:
        return "👻 Acoplamento Fantasma — mudam juntos mas nenhum referencia o outro"
    
    if scores['ope'] > 0.5 and scores['ref'] < 0.2:
        return "⚙️ Acoplamento de Motor — script conecta silenciosamente"
    
    if scores['ref'] > 0.5 and scores['tmp'] < 0.1 and scores['ope'] < 0.1:
        return "📝 Referência Morta — citado mas nunca impactado operacionalmente"
    
    return "⚠️ Drift Geral — eixos em conflito, investigar manualmente"
```

**Cada tipo de drift é uma ação diferente:**

| Tipo de Drift | Significado | Ação |
|---|---|---|
| Acoplamento Latente | Falam do mesmo tema mas nunca mudam juntos | Considerar fusão ou consolidação |
| Acoplamento Mecânico | Referência sem vocabulário compartilhado | Verificar se a referência é viva ou morta |
| Acoplamento Fantasma | Mudam juntos sem referência explícita | Adicionar tag `Affects` para formalizar |
| Acoplamento de Motor | Script conecta sem que os documentos saibam | Documentar no `rx-communications.md` Seção 5 |
| Referência Morta | Citado mas sem impacto real | Remover referência ou promover a acoplamento real |

---

## Integração com o Framework Existente

| Ponto de Integração | Modificação | Linhas |
|---|---|---|
| `package.json` | Adicionar `"context:affinity": "python .context/_scripts/affinity_scanner.py"` | 1 |
| `SCRIPT_GLOSSARY.md` | Entrara nova na tabela "Motores Epistemológicos" | 1 entrada |
| `health_sync.py` | Chamar `affinity_scanner` e incluir resumo no CONTEXT_HEALTH | ~15 |
| `rx-communications.md` | Adicionar referência ao `rx-affinity.md` no rodapé | 3 |
| `.github/workflows/context-health.yml` | Rodar `context:affinity` semanalmente | 2 |

---

## Dependências e Restrições

```python
# requirements implícitos (todos leves)
# scikit-learn — TF-IDF + cosine similarity
# numpy — manipulação de matrizes (já vem com scikit-learn)
# subprocess — chamadas Git (stdlib)
# re, json, math, pathlib — stdlib puro
```

**Se quiser ZERO dependências externas**, o TF-IDF pode ser implementado manualmente (~40 linhas extras) usando `collections.Counter` e cálculo de cosseno via `math.sqrt`. Mas `scikit-learn` é a escolha pragmática.

---

## Cronograma de Implementação Sugerido

| Fase | O quê | Esforço |
|---|---|---|
| **Fase 1** | Eixo Referencial + Eixo Operacional (parsing Seção 5) | 1 dia |
| **Fase 2** | Eixo Semântico (TF-IDF) | 0.5 dia |
| **Fase 3** | Eixo Temporal (Git) | 0.5 dia |
| **Fase 4** | Fusão + Saídas (rx-affinity.md, JSON) | 1 dia |
| **Fase 5** | Detecção de Drift + Integração com framework | 1 dia |
| **Total** | | **4 dias** |

A Fase 1 pode ser entregue isoladamente e já gera valor — a tabela de referências cruzadas e operacionais sozinha já revela acoplamentos ocultos.

---

## Resumo Final

| Aspecto | Detalhe |
|---|---|
| **Nome do script** | `affinity_scanner.py` |
| **Localização** | `.context/_scripts/affinity_scanner.py` |
| **Comando** | `npm run context:affinity` |
| **Entrada** | Todos os `.md` + `.py` do projeto + `rx-communications.md` Seção 5 + Git history |
| **Saída 1** | `rx-affinity.md` (documento legível com top pares, blast radius, órfãos, drifts, Mermaid) |
| **Saída 2** | `rx-affinity.json` (dados brutos para consumo por outros scripts) |
| **Saída 3** | Resumo no `CONTEXT_HEALTH.md` |
| **Dependências** | `scikit-learn` + stdlib |
| **Esforço** | ~4 dias |
| **O que automatiza** | Descoberta de acoplamentos — o que o Coupling Matrix (Níveis 1-3) não fazia |