"""Tests for blast_radius.py — 6 core scenarios."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / \
    ".context" / "_scripts" / "blast_radius.py"
SCRIPT_DIR = SCRIPT.parent

sys.path.insert(0, str(SCRIPT_DIR))

from blast_radius import classify


class TestClassifyBuckets:

    def test_both_agree_gives_must_update(self):
        """Arquivo em ambos → must_update."""
        seed = ["fileA.py"]
        structural = {"fileA.py": {"shared.md"}}
        governance = {"fileA.py": {"shared.md"}}
        result = classify(seed, structural, governance)
        assert "shared.md" in result["must_update"]
        assert "shared.md" not in result["likely_update"]
        assert "shared.md" not in result["declared_only"]

    def test_structural_only_gives_likely(self):
        """Só no graph → likely_update."""
        seed = ["fileA.py"]
        structural = {"fileA.py": {"only_graph.md"}}
        governance = {}
        result = classify(seed, structural, governance)
        assert "only_graph.md" in result["likely_update"]
        assert "only_graph.md" not in result["must_update"]

    def test_governance_only_gives_declared(self):
        """Só na governance → declared_only."""
        seed = ["fileA.py"]
        structural = {}
        governance = {"fileA.py": {"only_gov.md"}}
        result = classify(seed, structural, governance)
        assert "only_gov.md" in result["declared_only"]
        assert "only_gov.md" not in result["must_update"]

    def test_no_matches_gives_empty_buckets(self):
        """Seed sem edges → buckets vazios."""
        seed = ["unknown.py"]
        structural = {"other.py": {"x.md"}}
        governance = {"other.py": {"y.md"}}
        result = classify(seed, structural, governance)
        assert result["must_update"] == []
        assert result["likely_update"] == []
        assert result["declared_only"] == []

    def test_seed_excluded_from_buckets(self):
        """Seed não aparece nos buckets."""
        seed = ["fileA.py"]
        structural = {"fileA.py": {"fileA.py", "fileB.py"}}
        governance = {"fileA.py": {"fileA.py", "fileB.py"}}
        result = classify(seed, structural, governance)
        assert "fileA.py" not in result["must_update"]
        assert "fileB.py" in result["must_update"]


class TestDegradation:

    def test_both_unavailable_exits_4(self):
        """Sem nenhuma fonte → exit 4."""
        no_exist = Path(tempfile.gettempdir()) / \
            "__blast_radius_test_no_exist"
        result = subprocess.run(
            [
                sys.executable, str(SCRIPT),
                "--changed", "nonexistent.py",
                "--graph", str(no_exist / "graph.json"),
                "--rx", str(no_exist / "rx.md"),
            ],
            capture_output=True, text=True,
        )
        assert result.returncode == 4
        output = json.loads(result.stdout)
        assert "error" in output
