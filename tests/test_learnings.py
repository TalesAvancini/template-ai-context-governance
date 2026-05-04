import unittest
import sys
from pathlib import Path
import re

# Adiciona o diretório de scripts ao path para importação
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / ".context" / "_scripts"
sys.path.append(str(SCRIPTS_DIR))

# Mock de dependências se necessário ou import direto
try:
    import learnings_aggregator as agg
    import inject_learnings as inj
except ImportError:
    print("[ERROR] Não foi possível importar os scripts de memória para teste.")

class TestMiMoMemory(unittest.TestCase):

    def test_decay_logic(self):
        """Valida se o decaimento temporal altera o score corretamente."""
        from datetime import datetime, timedelta
        
        # Simula uma scar de ontem (sem decay)
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        scar_new = {"data": yesterday}
        score_new = agg.calculate_score(scar_new, {})
        
        # Simula uma scar de 40 dias atrás (50% decay)
        old_date = (datetime.now() - timedelta(days=40)).strftime("%Y-%m-%d")
        scar_old = {"data": old_date}
        score_old = agg.calculate_score(scar_old, {})
        
        self.assertGreater(score_new, score_old, "Scars novas devem ter score maior que antigas.")
        self.assertEqual(score_old, 50, "Score antigo com decay de 50% deveria ser 50 (base 100).")

    def test_harness_frequency_bonus(self):
        """Valida se falhas no harness aumentam o score."""
        scar = {"feature": "test_feat", "data": "2026-05-01"}
        
        # Sem falhas
        score_base = agg.calculate_score(scar, {})
        
        # Com 5 falhas (+50 pts)
        score_high = agg.calculate_score(scar, {"test_feat": 5})
        
        self.assertEqual(score_high, score_base + 50)

    def test_relevance_ranking(self):
        """Valida se o injetor prioriza scars com palavras-chave da spec."""
        scars = [
            {"title": "Erro de SQL", "score": 100, "body": "Falha na query", "full_block": "B1"},
            {"title": "Erro de Git", "score": 100, "body": "Conflito de merge", "full_block": "B2"}
        ]
        spec_text = "Estamos trabalhando com banco de dados e SQL."
        
        ranked = inj.rank_scars_by_relevance(scars, spec_text)
        
        self.assertEqual(ranked[0]['title'], "Erro de SQL", "A scar de SQL deveria estar em primeiro para esta spec.")
        self.assertGreater(ranked[0]['_final_rank'], ranked[1]['_final_rank'])

if __name__ == "__main__":
    unittest.main()
