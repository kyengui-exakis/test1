NAME := __PROJECT_NAME__
POETRY := $(shell command -v poetry 2> /dev/null)

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install     		install packages and prepare environment"
	@echo "  lint        		run the code linters"
	@echo "  format      		reformat code"
	@echo "  tests        		run all the tests"
	@echo "  tests-with-coverage	run all the tests with coverage results"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

install: pyproject.toml poetry.lock
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install

.PHONY: lint
lint:
	$(POETRY) run nox --session="lint"

.PHONY: format
format:
	$(POETRY) run nox --session="format"

.PHONY: tests
tests:
	$(POETRY) run nox --session="tests"

.PHONY: tests-with-coverage
tests-with-coverage:
	$(POETRY) run nox --session="tests_with_coverage"
