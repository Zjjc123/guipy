rm -rf ./docs/_build
poetry run sphinx-build -b html docs docs/_build
