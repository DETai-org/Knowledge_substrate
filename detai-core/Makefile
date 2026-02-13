.PHONY: api lint format

api:
	uvicorn app.main:app --app-dir api --host 0.0.0.0 --port 8000 --reload

lint:
	python -m compileall api/app

format:
	python -m pip install --quiet ruff && ruff format api/app
