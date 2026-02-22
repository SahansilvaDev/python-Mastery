
# python-Mastery

A personal Python learning repo with small, focused scripts covering core language fundamentals through intermediate topics (OOP, exceptions, file handling, databases, multithreading, etc.). Most files are intended to be run directly and tweaked as you learn.

## Prerequisites

- Python 3.x installed (any modern 3.x should work)
- Windows: PowerShell or Command Prompt

## Quick start

Run any lesson/script from the repo root:

```bash
python 1-variables.py
```

On Windows you can also use the Python Launcher:

```bash
py -3 1-variables.py
```

## Optional: create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- PowerShell
	```powershell
	.\.venv\Scripts\Activate.ps1
	```
- CMD
	```bat
	.\.venv\Scripts\activate.bat
	```

## Repo map (high level)

The numbering is a rough learning order.

### Basics

- `1-variables.py`
- `2-dataTypes.py`
- `3-ArithmaticOperators.py`
- `4-conditionalStatements.py`
- `5-nestedStatements.py`
- `6-printFunction.py`
- `7-userInput.py`
- `8-string.py`

### Collections

- `9-ListsHandling.py`
- `10-TupleHandling.py`
- `11-SetHandling.py`
- `12-DectHandling.py`

### Control flow

- `13-WhileLoop.py`
- `14-ForLoop.py`
- `15-BreakandCont.py`

### Functions

- `16-BuitinFunct.py`
- `17-UserdefinedFunct.py`
- `26-LambdaFunction.py`
- `27-Decorators.py`

### OOP

- `18-OOP.py`
- `19-Encapsulation.py`
- `20-Inheritance.py`
- `29-Polymorphism.py`
- `36-Abstract.py`

### Common standard-library topics

- `22-DateTime.py`
- `38-RandomNumbers.py`
- `39-ZipFunction.py`
- `41-RegularExpressions.py`

### Recursion / algorithms / exercises

- `24-Factorial.py`
- `25-Recursion.py`
- `40-Pyramid.py`

### Errors and exceptions

- `30-Errors.py`
- `31-ExceptionHandling.py`

### Iteration + generators

- `33-Iterators.py`
- `34-Generators.py`

### Concurrency

- `35-MultiThreading.py`

### Working with modules, packages, and project layouts

- `21-CreateOwnModules/` (simple module import examples)
- `28-nameVariable/` (name/main variable demos)
- `43-init/` (package + `__init__.py` examples)

### File handling

- `37-FileHandling/FileHandling.py`
- `37-FileHandling/test.txt`

### Serialization

- `44-PickleModule/`

### Databases

- `46-DatabaseConnectivity/connectorSQLITE.py` (SQLite is built-in)
- `46-DatabaseConnectivity/connectorMYSQL.py` (may require extra dependency)

### Logging

- `47-Logging/`

### Secrets / env management

- `48-ManageSecretKeys/`
- `42-Venv.py`

### UV example project

- `49-PythonUV/sample_project/` (has its own `pyproject.toml` and README)

## Notes

- Some scripts may need third‑party packages (for example MySQL connectivity). If you hit an `ImportError`, install the missing package in your environment and re-run.
- A few modules (like `turtle`) rely on GUI support; on some systems that may require additional OS components.

## Contributing

This repo is primarily for learning. If you spot a bug or want to improve clarity, feel free to open a PR with a small, focused change.

