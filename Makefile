PYTHON ?= python3
VENV := .venv
PYTHON_BIN := $(VENV)/bin/python
PIP_BIN := $(VENV)/bin/pip
PYTEST_BIN := $(VENV)/bin/pytest
RUFF_BIN := $(VENV)/bin/ruff

.PHONY: install test lint run clean

install:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt

test:
	. $(VENV)/bin/activate && $(PYTHON_BIN) -m pytest -q

lint:
	. $(VENV)/bin/activate && $(PYTHON_BIN) -m ruff check src tests

run:
	. $(VENV)/bin/activate && $(PYTHON_BIN) -m src.main

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
