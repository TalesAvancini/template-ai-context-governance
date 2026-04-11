import unittest
import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

class TestContextGovernance(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_root = self.test_dir
        self.context_dir = self.project_root / ".context"
        self.scripts_dir = self.context_dir / "_scripts"
        
        # Caminho real dos scripts
        self.repo_root = Path(__file__).parent.parent
        self.real_scripts_dir = self.repo_root / ".context" / "_scripts"
        
        # Cria estrutura de camadas
        for layer in ["brain", "maintenance", "monitoring", "_scripts"]:
            (self.context_dir / layer).mkdir(parents=True, exist_ok=True)
        (self.context_dir / "maintenance" / "_archive_context" / "journals").mkdir(parents=True, exist_ok=True)

        # Copia scripts reais para o sandbox
        for script in ["validate_context.py", "purge_journal.py", "sync_project.py"]:
            shutil.copy(self.real_scripts_dir / script, self.scripts_dir / script)

        # Cria arquivos base vazios
        for f in ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")
        
        for f in ["maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md", "maintenance/JOURNAL.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")

        self.python_cmd = sys.executable

    def tearDown(self):
        # Limpa sandbox
        shutil.rmtree(self.test_dir)

    def run_script(self, name):
        script_path = self.scripts_dir / name
        result = subprocess.run(
            [self.python_cmd, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=self.project_root
        )
        return result

    def test_validate_integrity(self):
        # Adiciona uma tabela válida em AGENT_REGISTRY para passar no check
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertIn("[SUCCESS]", res.stdout)

    def test_validate_missing_file(self):
        (self.context_dir / "brain/AGENT_REGISTRY.md").unlink()
        res = self.run_script("validate_context.py")
        self.assertIn("Arquivos ausentes", res.stdout)

    def test_purge_journal(self):
        journal = self.context_dir / "maintenance/JOURNAL.md"
        journal.write_text("## 📅 2024\nEntry 1\n\n## 📅 2024\nEntry 2", encoding="utf-8")
        res = self.run_script("purge_journal.py")
        self.assertIn("[OK] Purge concluido", res.stdout)
        
        # Verifica se arquivo foi criado no archive
        archive_files = list((self.context_dir / "maintenance/_archive_context/journals").glob("*.md"))
        self.assertGreaterEqual(len(archive_files), 1)

    def test_sync_project(self):
        # Simula package.json e schema.sql
        (self.project_root / "package.json").write_text('{"dependencies":{"test":"1.0"}}', encoding="utf-8")
        (self.context_dir / "maintenance/schema.sql").write_text("CREATE TABLE users (id INT);", encoding="utf-8")
        
        res = self.run_script("sync_project.py")
        self.assertIn("[OK] TECHNICAL_REQUIREMENTS.md sincronizado", res.stdout)
        
        req_content = (self.context_dir / "maintenance/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")
        self.assertIn("users", req_content)
        self.assertIn("test", req_content)

if __name__ == "__main__":
    unittest.main()
