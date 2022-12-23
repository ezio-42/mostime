# Moscow time app

[![CI](https://github.com/ezio-42/mostime/actions/workflows/mostime.yml/badge.svg)](https://img.shields.io/github/actions/workflow/status/ezio-42/mostime/mostime.yml)
[![codecov](https://codecov.io/gh/ezio-42/mostime/branch/main/graph/badge.svg)](https://codecov.io/gh/ezio-42/mostime)
[![Python version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/ezio-42/mostime)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Description

Web application that displays current time in Moscow
and tracks page visits.

Endpoints:

1. ``/`` - displays current time in Moscow
2. ``/visits`` - displays visits to the page
3. ``/health`` - displays health status of the application

## Usage

### Manual running

1. Install dependencies

    For production run

    ``$ poetry install --no-dev``

    OR both dev tools and dependencies

    ``$ poetry install``

2. Run the application

    ``$ PYTHONPATH=src:tests python3 src/app/main.py``

3. Access <http://localhost:8080>

### Run app using Docker

1. Build docker image

    ``docker build -t mostime -f Dockerfile .``

2. Run docker image

    ``docker run -p 8080:8080 mostime``

3. Access <http://localhost:8080>

### Run app using Makefile

- #### With Docker

    1. Build docker image

        ``make build-docker``

    2. Run docker image

        ``make docker-run``

- #### Without Docker

    - ``make run``

- Access <http://localhost:8080>

## Tests

1. Install dependencies

    ``$ poetry install``

2. Run tests

    ``$ PYTHONPATH=src:tests pytest tests``

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

## License

The source code is licensed under the
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

See [LICENSE](LICENSE) for more information.

## Contribution

Fork repository, make changes, send us a pull request.
We will review your changes and apply them to the master branch shortly,
provided they don't violate our quality standards.
