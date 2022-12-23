env:
	export PYTHONPATH=src:tests

run:
	poetry run python3 src/app/main.py

test:
	poetry run python3 -m pytest -rvs tests

pre-commit:
	pre-commit run -a

clean:
	rm -rf ./__pycache__
	rm -rf ./.mypy_cache
	rm -rf ./.pytest_cache
	rm -rf ./**/__pycache__
	rm -rf ./**/.mypy_cache
	rm -rf ./**/.pytest_cache
