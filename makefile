build: src/pyproptest/testing.py src/pyproptest/basicGenerators.py pyproject.toml
	py -m build
	pip install dist/pyproptest-0.0.1-py3-none-any.whl
