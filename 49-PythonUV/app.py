# https://docs.astral.sh/uv/



import uv


# uv -An extremely fast Python package and project manager, written in Rust.

# 01 uv init sample_project


# 02 uv venv - to create a virtual environment for the project, it will create a .venv folder in the project directory and it will also create a pyproject.toml file in the project directory to manage the dependencies of the project.
# 02.1 .venv\Scripts\activate - to activate the virtual environment, it will change the current working directory to the .venv folder and it will also change the prompt to indicate that the virtual environment is active.


# 03  uv run main.py

# 04  if want  - uv add numpy # package install

# 05 if want -  uv tree # show the dependency tree of the project

# 06 if want -  uv sync # to sync the dependencies of the project with the lockfile 

# if want add requirements.txt - uv add -r requirements.txt # to add the dependencies of the project from the requirements.txt file, it will read the dependencies from the requirements.txt file and it will add them to the pyproject.toml file with their versions.
# if want dependencies to requirements.txt file - uv export -r requirements.txt means to export the dependencies of the project to a requirements.txt file, it will create a requirements.txt file in the project directory and it will also add the dependencies of the project to the requirements.txt file with their versions.


# Highlights
# A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.
# 10-100x faster than pip.
# Provides comprehensive project management, with a universal lockfile.
# Runs scripts, with support for inline dependency metadata.
# Installs and manages Python versions.
# Runs and installs tools published as Python packages.
# Includes a pip-compatible interface for a performance boost with a familiar CLI.
# Supports Cargo-style workspaces for scalable projects.
# Disk-space efficient, with a global cache for dependency deduplication.
# Installable without Rust or Python via curl or pip.
# Supports macOS, Linux, and Windows.
# uv is backed by Astral, the creators of Ruff.

