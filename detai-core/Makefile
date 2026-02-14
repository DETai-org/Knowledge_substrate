.PHONY: bootstrap api api-dev lint format test

bootstrap:
	python -m pip install --quiet -r requirements.txt

api:
	uvicorn app.main:app --app-dir api --host 127.0.0.1 --port 9000

api-dev:
	uvicorn app.main:app --app-dir api --host 127.0.0.1 --port 9000 --reload

lint:
	python -m compileall api/app

format:
	python -m pip install --quiet ruff && ruff format api/app

test:
	python -m unittest tests/test_graph_api.py tests/test_graph_query_service.py
