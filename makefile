build: src/pyprop/testing.py src/pyprop/basicGenerators.py pyproject.toml
	py -m build
	pip install dist/pyprop-0.0.1-py3-none-any.whl
