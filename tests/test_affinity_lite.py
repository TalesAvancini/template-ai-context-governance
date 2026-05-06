import unittest
import re

def calculate_jaccard(set1, set2):
    """Calcula o índice de Jaccard entre dois conjuntos."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def find_references(content, filename_stem):
    """Busca referências ao nome do arquivo (stem) no conteúdo usando Word Boundaries."""
    # Escapa caracteres especiais no stem
    pattern = rf'\b{re.escape(filename_stem)}\b'
    matches = re.findall(pattern, content, re.IGNORECASE)
    return len(matches)

class TestAffinityLogic(unittest.TestCase):
    def test_jaccard_full_match(self):
        s1 = {"hash1", "hash2", "hash3"}
        s2 = {"hash1", "hash2", "hash3"}
        self.assertEqual(calculate_jaccard(s1, s2), 1.0)

    def test_jaccard_partial_match(self):
        s1 = {"h1", "h2"}
        s2 = {"h2", "h3"}
        # Intersection: {h2} (1), Union: {h1, h2, h3} (3) -> 1/3 = 0.333...
        self.assertAlmostEqual(calculate_jaccard(s1, s2), 0.3333333)

    def test_jaccard_no_match(self):
        s1 = {"h1"}
        s2 = {"h2"}
        self.assertEqual(calculate_jaccard(s1, s2), 0.0)

    def test_reference_found(self):
        content = "Este arquivo referencia RULES.md e STATE.md."
        self.assertEqual(find_references(content, "RULES"), 1)
        self.assertEqual(find_references(content, "STATE"), 1)

    def test_reference_word_boundary(self):
        content = "RULES_LEDGER.md não é o mesmo que RULES.md"
        # Deve achar apenas 'RULES' isolado, não dentro de 'RULES_LEDGER'
        self.assertEqual(find_references(content, "RULES"), 1)

    def test_reference_case_insensitive(self):
        content = "O arquivo rules.md foi alterado."
        self.assertEqual(find_references(content, "RULES"), 1)

if __name__ == "__main__":
    unittest.main()
