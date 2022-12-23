.PHONY: run clean

SHELL=/bin/bash

install:
	echo "Installing..."
	make install-poetry
	make setup-environment-variables
	poetry shell
	make install-pre-commit

setup-environment-variables:
	export PYTHONPATH=src:tests

install-poetry:
	echo "Installing poetry..."
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - --version 1.1.13
	$(eval include ${HOME}/.poetry/env)

install-pre-commit:
	pip install pre-commit
	pre-commit install

run:
	poetry run python3 src/app/main.py

test:
	poetry run python3 -m pytest -rvs tests

pre-commit:
	pre-commit run -a

clean:
	rm -rf __pycache__
