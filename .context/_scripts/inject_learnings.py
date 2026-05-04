#!/usr/bin/env python3
"""
💉 inject_learnings.py (Injetor de Memória Inteligente)
Lê o LEARNINGS.md e cria o `.enriched.md` filtrando as scars 
mais relevantes para a spec atual.
"""
import sys
from pathlib import Path
import re

# Configurações de Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONTEXT_DIR = PROJECT_ROOT / ".context"
BRAIN_DIR = CONTEXT_DIR / "brain"
SPECS_DIR = PROJECT_ROOT / ".specs" / "features"

LEARNINGS_FILE = BRAIN_DIR / "LEARNINGS.md"

# Output encoding
stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
if callable(stdout_reconfigure):
    stdout_reconfigure(encoding="utf-8", errors="replace")

def get_active_features():
    """Retorna uma lista de diretórios de features que possuem spec.md."""
    if not SPECS_DIR.exists():
        return []
    
    features = []
    for d in SPECS_DIR.iterdir():
        if d.is_dir() and not d.name.startswith("_"):
            spec_file = d / "spec.md"
            if spec_file.exists():
                features.append(d)
    return features

def parse_learnings_md():
    """Lê o LEARNINGS.md e retorna lista de dicionários de scars."""
    scars = []
    if not LEARNINGS_FILE.exists():
        return scars
        
    content = LEARNINGS_FILE.read_text(encoding="utf-8", errors="replace")
    
    # Busca a seção de Scars
    blocks = re.split(r'### \[SCAR-\d+\]', content)
    for b in blocks[1:]:
        lines = b.strip().split('\n')
        if not lines: continue
        
        title_line = lines[0].strip()
        title_match = re.match(r'(.*) \(Score: (\d+)\)', title_line)
        
        if title_match:
            title = title_match.group(1)
            score = int(title_match.group(2))
            body = "\n".join(lines[1:]).strip()
            # Remove o delimitador de fim de bloco se houver
            body = body.split('\n---')[0].strip()
            
            scars.append({
                "title": title,
                "score": score,
                "body": body,
                "full_block": f"### {title_line}\n{body}"
            })
            
    return scars

def rank_scars_by_relevance(scars, spec_text):
    """Rankeia scars baseadas em palavras-chave da spec."""
    spec_text_lower = spec_text.lower()
    
    # Dicionário de termos técnicos para busca de contexto
    # Expandível conforme necessário
    keywords = re.findall(r'\b(git|regex|sam|harness|python|sql|database|context|journal|script|sprint|acceptance|migue|fraude|status)\b', spec_text_lower)
    keywords = set(keywords)
    
    for s in scars:
        relevance_bonus = 0
        scar_text = (s['title'] + " " + s['body']).lower()
        
        for kw in keywords:
            if kw in scar_text:
                relevance_bonus += 100 # Match de contexto dobra a importância
        
        s['_final_rank'] = s['score'] + relevance_bonus
        
    return sorted(scars, key=lambda x: x['_final_rank'], reverse=True)

def inject_to_feature(feature_dir, all_scars):
    """Gera/Atualiza o .enriched.md na feature com ranking de relevância."""
    spec_file = feature_dir / "spec.md"
    enriched_file = feature_dir / ".enriched.md"
    
    spec_content = spec_file.read_text(encoding="utf-8", errors="replace")
    
    # Rankeia as scars para esta spec específica
    ranked = rank_scars_by_relevance(all_scars, spec_content)
    
    # Pega as Top 3 mais relevantes (ou Top 3 geral se não houver scars específicas)
    top_scars = ranked[:3]
    
    scars_md = ""
    if not top_scars:
        scars_md = "*(Nenhuma memória estratégica relevante encontrada para esta feature)*"
    else:
        for s in top_scars:
            scars_md += s['full_block'] + "\n\n"
    
    enriched_md = f"""# 💉 Spec Enriquecida (MiMo v2.1)
> Este arquivo injeta memória estratégica contextualmente. O Agente DEVE priorizar as orientações abaixo.

## 🚨 MEMÓRIA ESTRATÉGICA RELEVANTE (CONTEXTUAL)
{scars_md}

---
## 📄 SPEC ORIGINAL
{spec_content}
"""
    
    enriched_file.write_text(enriched_md, encoding="utf-8")
    return enriched_file

def main():
    print("💉 [INJECTOR] Iniciando injeção de contexto inteligente (MiMo v2.1)...")
    
    features = get_active_features()
    if not features:
        print("[WARN] Nenhuma feature ativa encontrada.")
        sys.exit(0)
        
    all_scars = parse_learnings_md()
    if not all_scars:
        print("[WARN] Nenhuma scar encontrada no LEARNINGS.md.")
    
    for feature in features:
        inject_to_feature(feature, all_scars)
        print(f"[OK] Contexto rankeado para: {feature.name}/.enriched.md")
        
    print(f"✅ [SUCCESS] Contexto estratégico injetado com ranking de relevância.")

if __name__ == "__main__":
    main()
