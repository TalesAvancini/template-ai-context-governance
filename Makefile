.PHONY: help validate purge sync all

# No Windows, pode ser necessário rodar como: make PYTHON=python validate
PYTHON ?= python3

help:
	@echo "🛠️ Context Management Commands (v2.4.1+)"
	@echo "  make validate  - Check .context integrity via H.O.K"
	@echo "  make purge     - Archive oldest journal entries"
	@echo "  make sync      - Sync TECH_REQUIREMENTS.md with environment"
	@echo "  make test      - Run automated infrastructure tests"
	@echo "  make all       - [BREAKING] Run FULL H.O.K pipeline (validate, sync, purge, harness, lint)"
	@echo "  make help      - Show this message"

validate:
	@echo "🔍 Delegating to run_context.py..."
	@$(PYTHON) run_context.py validate

purge:
	@echo "🗜️ Delegating to run_context.py..."
	@$(PYTHON) run_context.py purge

sync:
	@echo "🔄 Delegating to run_context.py..."
	@$(PYTHON) run_context.py sync

test:
	@echo "🧪 Running infrastructure tests..."
	@$(PYTHON) tests/test_context.py

all:
	@echo "🚀 Delegating full pipeline to run_context.py..."
	@$(PYTHON) run_context.py all
