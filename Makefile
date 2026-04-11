.PHONY: help validate purge sync all

CONTEXT_SCRIPTS := .context/_scripts
# No Windows, pode ser necessário rodar como: make PYTHON=python validate
PYTHON ?= python3

help:
	@echo "🛠️ Context Management Commands"
	@echo "  make validate  - Check .context integrity & estimate tokens"
	@echo "  make purge     - Archive 70% of oldest journal entries"
	@echo "  make sync      - Sync TECH_REQUIREMENTS.md with package.json & schema.sql"
	@echo "  make test      - Run automated infrastructure tests"
	@echo "  make all       - Run full pipeline: validate -> sync -> purge"
	@echo "  make help      - Show this message"

validate:
	@echo "🔍 Running context validation..."
	@$(PYTHON) $(CONTEXT_SCRIPTS)/validate_context.py

purge:
	@echo "🗜️ Running journal purge..."
	@$(PYTHON) $(CONTEXT_SCRIPTS)/purge_journal.py

sync:
	@echo "🔄 Running project sync..."
	@$(PYTHON) $(CONTEXT_SCRIPTS)/sync_project.py

test:
	@echo "🧪 Running infrastructure tests..."
	@$(PYTHON) tests/test_context.py

all: validate sync purge
	@echo "🎉 Full context pipeline completed successfully."
