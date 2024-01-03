# list all available commands
default:
  just --list

###############################################################################
# Basic project and env management

# clean all build, python, and lint files
clean:
	rm -fr dist
	rm -fr .eggs
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -fr .mypy_cache

# install with all deps
install:
    pip install -r requirements.txt

# lint, format, and check all files
lint:
	pre-commit run --all-files

###############################################################################
# Jupyter Slide Build

# store various dirs and filepaths
NOTEBOOKS_DIR := justfile_directory() + "/notebooks/"
BUILD_DIR := NOTEBOOKS_DIR + "_build/"

# remove build files
jupyter-clean:
	rm -fr {{BUILD_DIR}}

# build page
jupyter-build:
	jupyter nbconvert --to slides {{NOTEBOOKS_DIR}}*.ipynb --output-dir={{BUILD_DIR}} --execute

# render pages
jupyter-render:
    open -a /Applications/Firefox.app file://{{BUILD_DIR}}
