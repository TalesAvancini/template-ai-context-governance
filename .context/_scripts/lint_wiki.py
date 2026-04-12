#!/usr/bin/env python3
"""
📖 lint_wiki.py — Validacao Epistemologica (Karpathy Layer)
Fase 2: Modo Strict + Sugestao Automatica de Fonte.
"""
import sys
import re
import argparse
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "raw"
WIKI_DIRS = [CONTEXT_DIR / "brain", CONTEXT_DIR / "maintenance"]

# Regex refinado para capturar claims técnicos, ignorando headers e metadados
# Captura frases que parecem afirmações técnicas (ex: "O sistema usa X para Y.")
CLAIM_REGEX = re.compile(
    r'^(?![\s\-\*#>])'                      # Não começa com espaço, lista ou header
    r'([A-ZÁÉÍÓÚÂÊÎÔÛÃÕÇ][a-záéíóúâêîôûãõç\s,]{15,}'  # Começa com maiúscula + texto longo
    r'(?:utiliza|implementa|segue|requer|garante|valida|integra|usa|e|é)\s'  # Verbo técnico chave
    r'.+?\.)',                              # Termina com ponto
    re.MULTILINE
)

def find_raw_sources():
    """Lista arquivos na inbox raw para sugestão."""
    if not RAW_DIR.exists(): return []
    return [f.name for f in RAW_DIR.iterdir() if f.suffix == '.md']

def suggest_source(claim_text, raw_files):
    """Heurística simples: busca palavras-chave do claim nos nomes dos arquivos raw."""
    words = set(re.findall(r'\b\w{5,}\b', claim_text.lower()))
    # Palavras comuns de ignorar
    ignore = {'deve', 'como', 'para', 'sistema', 'projeto', 'este', 'esta', 'ser', 'com', 'sobre'}
    words -= ignore
    
    if not words: return None
    
    matches = []
    for raw_file in raw_files:
        file_lower = raw_file.lower()
        if any(w in file_lower for w in words):
            matches.append(f"raw/{raw_file}")
            
    return matches[0] if matches else None

def check_wiki(strict=False):
    """Varre a wiki em busca de claims sem citação."""
    raw_files = find_raw_sources()
    issues = []
    
    for d in WIKI_DIRS:
        if not d.exists(): continue
        for f in d.rglob("*.md"):
            # Ignora archive e o próprio lint report se existir
            if "_archive" in str(f) or "lint_report" in str(f): continue
            
            text = f.read_text(encoding="utf-8")
            
            # Pula arquivos raiz de documentação geral (opcional, mas recomendado)
            if f.name in ["README.md", "MASTER_FLOW.md", "RULES.md", "CONTEXT_HEALTH.md", "rebuild_guide.md"]: continue

            for match in CLAIM_REGEX.finditer(text):
                claim = match.group(0)
                # Verifica se há citação próxima (janela de -150 a +250 chars)
                start_idx = max(0, match.start() - 150)
                end_idx = min(len(text), match.start() + 250)
                context_window = text[start_idx:end_idx]
                citation_found = "> Fonte:" in context_window
                
                # Fallback: se não achou na janela, varre o arquivo inteiro (performance aceitável para .md)
                if not citation_found and "> Fonte:" in text:
                    citation_found = True

                if not citation_found and "SSOT" not in text:
                    suggestion = suggest_source(claim, raw_files)
                    
                    error_msg = f"[WARN] [{f.name}] Claim sem fonte: '{claim[:50]}...'"
                    if suggestion:
                        error_msg += f"\n   [DICA] Sugestao: Adicione '> Fonte: {suggestion}'"
                    else:
                        error_msg += f"\n   [DICA] Crie um arquivo em raw/ ou use '> Fonte: raw/novo.md'"
                    
                    issues.append(error_msg)

    if issues:
        print("\n[LINT] Wiki Report:")
        print("\n".join(issues))
        if strict:
            print("\n[FATAL] Commits bloqueados por falta de epistemologia. Resolva os claims acima.")
            sys.exit(1)
        else:
            print("\n[WARN] Warning: Verifique as citacoes para manter a qualidade documental.")
            sys.exit(0) # Não trava o pipeline em warn-mode
    else:
        print("[OK] Wiki limpa: Epistemologia em dia.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint de Citacoes e Epistemologia")
    parser.add_argument("--strict", action="store_true", help="Bloqueia o pipeline se houver erros")
    args = parser.parse_args()
    check_wiki(strict=args.strict)
