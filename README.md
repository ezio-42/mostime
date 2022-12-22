# Moscow time app

## Description

Web application that displays current time in Moscow
and tracks page visits.

Endpoints:

1. ``/`` - displays current time in Moscow
2. ``/visits`` - displays visits to the page
3. ``/health`` - displays health status of the application

## Usage

1. Install dependencies

    For production run

    ``$ poetry install --no-dev``

    OR both dev tools and dependencies

    ``$ poetry install``

2. Run the application

    ``$ PYTHONPATH=src python3 src/app/main.py``

3. Access <http://localhost:8080>

## Tests

1. Install dependencies

    ``$ poetry install``

2. Run tests

    ``$ PYTHONPATH=src pytest tests``

## Quality Checks

1. Install pre-commit, linters, and formatters

    ```bash
        poetry add -D black flake8 isort mypy pre-commit

        pre-commit install
    ```

2. Run linters and formatters

    ```bash
        black .

        flake8 --verbose --max-line-length=80 --ignore="E203,W503"

        isort .

        mypy .

        pre-commit run -a markdownlint-fix

        pre-commit run -a hadolint-docker
    ```
