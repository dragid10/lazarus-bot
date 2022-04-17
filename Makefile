# This is usually my first target so as soon as a developer clones
# a project and creates a virtualenv they can just run `make` to get things going.

setup:
	curl -sSL https://install.python-poetry.org | python3 - --preview
	. $$HOME/.poetry/env

install:
	  poetry install

update:
	  poetry update
