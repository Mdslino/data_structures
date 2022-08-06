help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Remove cache files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

###
# Lint section
###
_flake8:
	@flake8 --show-source .

_isort:
	@isort --diff --check-only .

_black:
	@black --check .

_isort-fix:
	@isort .

_black_fix:
	@black .

_mypy:
	@mypy data_structures/

lint: _flake8 _isort _black _mypy  ## Check code lint
format-code: _isort-fix _black_fix ## Format code

###
# Tests section
###
test: clean ## Run tests
	@pytest tests/

test-coverage: clean ## Run tests with coverage output
	@pytest tests/ --cov data_structures/ --cov-report term-missing --cov-report xml --cov-report html
