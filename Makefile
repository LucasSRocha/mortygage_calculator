.PHONY: help
help:  ## This help
	@awk 'BEGIN {FS = ":.?## "} /^[a-zA-Z_-]+:.?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '_pycache_' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

set-path:
    export PYTHONPATH=.

###
# Dependencies section
###
.PHONY: _base_pip
_base_pip:
	@pip install -U pip poetry

.PHONY: dev-dependencies
dev-dependencies: _base_pip
	@poetry install

.PHONY: dependencies
dependencies: _base_pip ## Install dependencies
	@poetry install --no-root --only main

.PHONY: ci-dependencies
ci-dependencies: _base_pip
	@poetry export --without-hashes --dev -f requirements.txt > requirements.txt
	@pip install -r requirements.txt

.PHONY: outdated
outdated: ## Show outdated packages
	@poetry show --outdated


###
# Lint section
###
_flake8:
	@flake8 .

_black:
	@black --check .

_isort:
	@isort --diff --check-only .

_isort-fix:
	@isort .

_black_fix:
	@black .

.PHONY: lint
lint: _flake8 _isort _black   ## Check code lint

.PHONY: format-code
format-code: _isort-fix _black_fix ## Format code

run: ## Run server with uvicorn
	@uvicorn main:app

run-local: ## Run server with reload option
	@poetry run uvicorn main:app --reload


###
# Tests section
###
test: ## Run tests
	@poetry run pytest

.PHONY: test-coverage
test-coverage: clean ## Run tests with coverage output
	@poetry run pytest . --cov . --cov-report term-missing --cov-report xml --cov-report html

test-debug: clean ## Run tests with active pdb
	poetry run pytest --pdb
