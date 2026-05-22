#!/usr/bin/env python3
"""
blast_radius.py — Hybrid Blast Radius Calculator
Combines graphify structural edges with rx-communications
governance edges to produce prioritized propagation buckets.

Usage:
  python blast_radius.py --changed file1.py file2.md
"""
import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# ─── CONFIGURAÇÃO ───────────────────────────────────────
DEFAULT_GRAPH = "graphify-out/graph.json"
DEFAULT_RX = ".context/maintenance/rx-communications.md"
CROSS_FILE_RELATIONS = {
    "calls", "references", "implements",
    "rationale_for", "semantically_similar_to"
}


def load_graph_as_file_adjacency(graph_path: str) -> tuple:
    """
    Carrega graph.json e projeta um grafo FILE→FILE.
    Colapsa nós (funções, classes, conceitos) em seus
    source_files, criando edges diretas entre arquivos.
    """
    data = json.loads(
        Path(graph_path).read_text(encoding="utf-8")
    )

    # nodes é uma LISTA — pré-indexar
    id_to_file: dict[str, str] = {}
    for node in data.get("nodes", []):
        id_to_file[node["id"]] = node.get("source_file", "")

    # Projetar links em edges file→file
    file_adj: dict[str, set[str]] = defaultdict(set)
    for link in data.get("links", []):
        rel = link.get("relation", "")
        if rel not in CROSS_FILE_RELATIONS:
            continue
        src_file = id_to_file.get(link.get("source", ""), "")
        tgt_file = id_to_file.get(link.get("target", ""), "")
        if src_file and tgt_file and src_file != tgt_file:
            file_adj[src_file].add(tgt_file)
            file_adj[tgt_file].add(src_file)

    return dict(file_adj), data.get("built_at_commit", "")


def parse_rx_communications(rx_path: str) -> dict:
    """
    Parseia a Seção 4 do rx-communications.md.
    Extrai pares source → [targets] a partir das linhas
    'Afeta:' e 'Escreve em:'.
    """
    text = Path(rx_path).read_text(encoding="utf-8")
    adjacency: dict[str, set[str]] = defaultdict(set)
    current_file = None

    for line in text.splitlines():
        # Header de arquivo: **`FILENAME`** ou ### FILENAME
        header = re.search(
            r'\*\*`([^`]+)`\*\*|^###\s+.*?`([^`]+)`',
            line
        )
        if header:
            current_file = header.group(1) or header.group(2)
            current_file = Path(current_file).name
            continue

        if not current_file:
            continue

        # Linhas "Afeta:" ou "Escreve em:"
        afeta = re.search(
            r'(?:Afeta|Escreve em)\s*:\s*(.+)',
            line, re.IGNORECASE
        )
        if afeta:
            raw_targets = afeta.group(1).split(",")
            for t in raw_targets:
                # Limpar: remover [CRÍTICO], backticks, etc.
                clean = re.sub(
                    r'\[.*?\]\s*', '', t
                ).strip().strip('`').strip()
                if clean:
                    adjacency[current_file].add(
                        Path(clean).name
                    )

    return dict(adjacency)


def check_freshness(commit_hash: str) -> tuple:
    """Retorna (commits_behind, is_stale)."""
    if not commit_hash:
        return 999, True
    try:
        r = subprocess.run(
            ["git", "rev-list", "--count",
             f"{commit_hash[:8]}..HEAD"],
            capture_output=True, text=True, timeout=5
        )
        behind = int(r.stdout.strip())
        return behind, behind > 10
    except Exception:
        return 999, True


def normalize_seed(files: list) -> list:
    """Normaliza paths do seed."""
    result = []
    for f in files:
        p = Path(f)
        if p.is_absolute():
            try:
                p = p.relative_to(Path.cwd())
            except ValueError:
                pass
        result.append(str(p).replace("\\", "/"))
    return result


def classify(
    seed: list,
    structural: dict[str, set[str]],
    governance: dict[str, set[str]]
) -> dict:
    """Classifica em 3 buckets."""
    seed_basenames = {Path(s).name for s in seed}

    # Structural → basenames
    struct_set: set[str] = set()
    for s in seed:
        basename = Path(s).name
        neighbors = (
            structural.get(s, set()) |
            structural.get(basename, set())
        )
        struct_set.update(neighbors)
    struct_set -= seed_basenames

    # Governance → basenames
    gov_set: set[str] = set()
    for s in seed:
        basename = Path(s).name
        neighbors = governance.get(basename, set())
        gov_set.update(neighbors)
    gov_set -= seed_basenames

    # Classificar
    must = struct_set & gov_set
    likely = struct_set - gov_set
    declared = gov_set - struct_set

    return {
        "must_update": sorted(must),
        "likely_update": sorted(likely),
        "declared_only": sorted(declared),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Hybrid Blast Radius Calculator"
    )
    parser.add_argument(
        "--changed", nargs="+", required=True,
        help="Files in the propagation seed"
    )
    parser.add_argument(
        "--graph", default=DEFAULT_GRAPH,
        help="Path to graphify graph.json"
    )
    parser.add_argument(
        "--rx", default=DEFAULT_RX,
        help="Path to rx-communications.md"
    )
    parser.add_argument(
        "--format", choices=["json", "text"],
        default="json",
        help="Output format"
    )
    args = parser.parse_args()

    seed = normalize_seed(args.changed)
    if not seed:
        print("Error: --changed is empty",
              file=sys.stderr)
        sys.exit(2)

    warnings: list[str] = []
    structural: dict[str, set[str]] = {}
    governance: dict[str, set[str]] = {}
    graph_commit = ""

    # ── Graph ──
    graph_path = Path(args.graph)
    if graph_path.exists():
        try:
            structural, graph_commit = \
                load_graph_as_file_adjacency(
                    str(graph_path)
                )
            behind, stale = check_freshness(graph_commit)
            if stale:
                warnings.append(
                    f"graph_stale_{behind}_commits"
                )
        except Exception as e:
            warnings.append(f"graph_load_error: {e}")
    else:
        warnings.append("graph_unavailable")

    # ── Governance ──
    rx_path = Path(args.rx)
    if rx_path.exists():
        try:
            governance = parse_rx_communications(
                str(rx_path)
            )
        except Exception as e:
            warnings.append(f"rx_parse_error: {e}")
    else:
        warnings.append("governance_unavailable")

    # ── Nenhuma fonte ──
    if not structural and not governance:
        print(json.dumps({
            "error": "No data sources available",
            "recovery": [
                "Run: graphify extract . "
                "&& graphify update .",
                "Verify: .context/maintenance/"
                "rx-communications.md exists"
            ]
        }, indent=2))
        sys.exit(4)

    # ── Classificação ──
    buckets = classify(seed, structural, governance)

    output = {
        "seed": seed,
        **buckets,
        "meta": {
            "graph_available": bool(structural),
            "governance_available": bool(governance),
            "graph_commit": (
                graph_commit[:8]
                if graph_commit else None
            ),
            "warnings": warnings,
        },
    }

    if args.format == "json":
        print(json.dumps(
            output, indent=2, ensure_ascii=False
        ))
    else:
        print("═" * 50)
        print("  BLAST RADIUS")
        print("═" * 50)
        print(f"Seed: {', '.join(seed)}")
        print()
        for bucket, emoji in [
            ("must_update", "🔴"),
            ("likely_update", "🟡"),
            ("declared_only", "🔵"),
        ]:
            items = buckets[bucket]
            print(
                f"{emoji} {bucket.upper()} ({len(items)})"
            )
            for f in items:
                print(f"   {f}")
            if not items:
                print("   (none)")
            print()
        if warnings:
            print(
                f"⚠ WARNINGS: {', '.join(warnings)}"
            )

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Internal error: {e}", file=sys.stderr)
        sys.exit(5)
