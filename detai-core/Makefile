.PHONY: bootstrap api lint format test

bootstrap:
	python -m pip install --quiet -r requirements.txt

api:
	uvicorn app.main:app --app-dir api --host 0.0.0.0 --port 8000 --reload

lint:
	python -m compileall api/app

format:
	python -m pip install --quiet ruff && ruff format api/app

test:
	python -m unittest tests/test_graph_api.py
