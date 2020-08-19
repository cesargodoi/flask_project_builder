clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

install:
	pip install -e .

install-dev:
	pip install -e .['dev']

init-db:
	FLASK_APP=flask_project_builder/app.py flask create-db
	FLASK_APP=flask_project_builder/app.py flask db upgrade

test:
	FLASK_ENV=test pytest tests/ -v --cov=flask_project_builder

format:
	isort **/*.py
	black -l 79 **/*.py