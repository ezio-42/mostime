# Moscow time app

## Overview

Web application that displays current time in Moscow.

## Usage

### Install dependencies

#### Only dependencies (for production run)

    poetry install --no-dev

#### Both dev tools and dependencies

    poetry install

### Run

    python3 main.py

## Development

### Install pre-commit, linters, and formatters

    ```bash
        poetry add -D black flake8 isort mypy pre-commit

        pre-commit install
    ```

### Run linters and formatters

    ```bash
        black .

        flake8 --verbose --max-line-length=80 --ignore="E203,W503"

        isort .

        mypy .

        pre-commit run -a markdownlint-fix

        pre-commit run -a hadolint-docker
    ```
