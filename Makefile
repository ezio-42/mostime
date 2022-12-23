run:
	PYTHONPATH=src:tests CONFIG_FILE=config/local.json poetry run python3 src/app/main.py

test:
	PYTHONPATH=src:tests poetry run python3 -m pytest -rvs tests
	rm tests/visits.txt

pre-commit:
	pre-commit run -a

clean:
	rm -rf ./__pycache__
	rm -rf ./.mypy_cache
	rm -rf ./.pytest_cache
	rm -rf ./**/__pycache__
	rm -rf ./**/.mypy_cache
	rm -rf ./**/.pytest_cache

build-docker:
	docker build -t mostime -f Dockerfile .

run-in-docker:
	docker run -p 8080:8080 mostime
