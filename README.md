# atumanyire-ange-calc

A simple arithmetic and statistical utility package, built for the
"Create & Publish a Python Package" lab (Software Engineering & Python
Development Lab).

- **Install name (pip / TestPyPI):** `atumanyire-ange-calc`
- **Import name (in Python code):** `atumanyire_ange_calc`
- **Source code:** https://github.com/ATUMANYIRE/AtumanyireAnge-Calc
- **TestPyPI:** https://test.pypi.org/project/atumanyire-ange-calc/

## Quick start

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ atumanyire-ange-calc
```

```python
from atumanyire_ange_calc import operations

operations.add(10, 25)                  # 35
operations.multiply(3, 4)               # 12
operations.average([10, 20, 30, 40])    # 25.0
```

The functions can also be imported directly:

```python
from atumanyire_ange_calc import add, multiply, average
```

## API

| Function | Description | Example |
|---|---|---|
| `add(a, b)` | Sum of two numbers | `add(2, 3)` → `5` |
| `multiply(a, b)` | Product of two numbers | `multiply(3, 4)` → `12` |
| `average(numbers)` | Arithmetic mean of a list; returns `0.0` for an empty list | `average([1, 2, 3])` → `2.0` |

---

# Step-by-step guide: how this package was built and published

The rest of this README walks through the full lab workflow, from an empty
folder to a package installed from TestPyPI. Commands are for Windows
PowerShell. On macOS/Linux, use `source test_env/bin/activate` instead of
`test_env\Scripts\activate`.

## Step 1: Install the tools

You need Python 3.8 or newer. Then install the packaging tools:

```powershell
python -m pip install --upgrade pip build twine
```

- `build` turns the source code into distribution files.
- `twine` uploads those files to TestPyPI / PyPI.

Create accounts on both registries (they are separate):

- TestPyPI (sandbox for practice): https://test.pypi.org/account/register/
- PyPI (the real index): https://pypi.org/account/register/

## Step 2: Create the project layout

```
atumanyire-calcutils/                  <- project root (git repo)
├── LICENSE                            <- MIT license text
├── README.md                          <- this file (also shown on TestPyPI)
├── pyproject.toml                     <- package metadata and build config
├── .gitignore                         <- keeps build output out of git
├── atumanyire_ange.py                 <- demo script that uses the package
└── src/
    └── atumanyire_ange_calc/          <- the importable package
        ├── __init__.py                <- public API and version
        └── operations.py              <- the actual functions
```

This is the **src layout**: the package lives under `src/` so you can't
accidentally import the local folder instead of the installed package when
testing.

## Step 3: Write the code

`src/atumanyire_ange_calc/operations.py` holds the functions:

```python
from typing import List


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def average(numbers: List[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)
```

`List[float]` from `typing` is used rather than `list[float]` because the
latter only works on Python 3.9+, and the package supports 3.8.

`src/atumanyire_ange_calc/__init__.py` defines what users can import:

```python
__version__ = "0.1.0"

from . import operations
from .operations import add, multiply, average

__all__ = ["operations", "add", "multiply", "average"]
```

Listing `operations` in `__all__` matters: IDEs like PyCharm use `__all__`
to resolve `from atumanyire_ange_calc import operations`.

## Step 4: Configure `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=77.0.0"]
build-backend = "setuptools.build_meta"

[project]
name = "atumanyire-ange-calc"
version = "0.1.0"
description = "A simple arithmetic and statistical utility package"
readme = "README.md"
authors = [
    { name = "ATUMANYIRE" }
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
license = "MIT"
license-files = ["LICENSE"]
requires-python = ">=3.8"
dependencies = []

[project.urls]
Homepage = "https://github.com/ATUMANYIRE/AtumanyireAnge-Calc"

[tool.setuptools.packages.find]
where = ["src"]
```

Key points:

- **`name`** must be unique across the whole registry. If the upload says the
  name is taken, choose another.
- **`version`** must change for every upload. TestPyPI/PyPI never accept the
  same version twice, even after deleting it.
- **`license = "MIT"`** is the modern SPDX form. The older
  `License :: OSI Approved :: MIT License` classifier is deprecated and
  triggers a warning with recent setuptools.
- **`[tool.setuptools.packages.find] where = ["src"]`** tells setuptools where
  the package lives.

## Step 5: Build the distributions

From the project root (the folder containing `pyproject.toml`):

```powershell
python -m build
```

This creates `dist/` with two files:

- `atumanyire_ange_calc-0.1.0.tar.gz`: source distribution
- `atumanyire_ange_calc-0.1.0-py3-none-any.whl`: wheel (built distribution)

Check that they are valid before uploading:

```powershell
python -m twine check dist/*
```

Both should say `PASSED`.

## Step 6: Publish to TestPyPI

1. Log in at https://test.pypi.org/ and go to **Account settings → API tokens
   → Add API token**. Copy the token (it starts with `pypi-`).
2. Upload:

   ```powershell
   python -m twine upload --repository testpypi dist/*
   ```

3. When prompted:
   - **Username:** `__token__`
   - **Password:** paste the token (nothing appears as you type; that's
     normal).

On success twine prints a link like
`https://test.pypi.org/project/atumanyire-ange-calc/0.1.0/`.

> **Keep your token secret.** Never paste it into chats, code, or git. If it
> leaks, delete it in Account settings and create a new one.

## Step 7: Install from TestPyPI and test

Use a fresh virtual environment so you're testing the published package, not
your local files:

```powershell
python -m venv test_env
test_env\Scripts\activate
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ atumanyire-ange-calc
```

`--extra-index-url` lets pip fetch any dependencies from the real PyPI, since
TestPyPI doesn't host everything.

Then run the demo script:

```powershell
python atumanyire_ange.py
```

Expected output:

```
atumanyire_ange_calc version: 0.1.0
add(10, 25)               = 35
multiply(3, 4)            = 12
average([10, 20, 30, 40]) = 25.0
```

Or test interactively:

```
python
>>> from atumanyire_ange_calc import operations
>>> operations.add(10, 25)
35
>>> operations.average([10, 20, 30, 40])
25.0
>>> exit()
```

## Step 8: Push the source to GitHub

```powershell
git init -b main
git add .
git commit -m "Add atumanyire-ange-calc package"
git remote add origin https://github.com/ATUMANYIRE/AtumanyireAnge-Calc.git
git push -u origin main
```

`.gitignore` keeps `dist/`, `build/`, `*.egg-info/`, `__pycache__/` and
`test_env/` out of the repository. Make the repository **public** (Settings →
Danger Zone → Change visibility) so your instructor can view it.

## Step 9: Releasing a new version

1. Change the code.
2. Bump the version in **both** `pyproject.toml` (`version = "0.1.1"`) and
   `src/atumanyire_ange_calc/__init__.py` (`__version__ = "0.1.1"`).
3. Delete the old build output, rebuild, check and upload:

   ```powershell
   Remove-Item -Recurse -Force dist, build -ErrorAction SilentlyContinue
   python -m build
   python -m twine check dist/*
   python -m twine upload --repository testpypi dist/*
   ```

4. Upgrade the installed copy:

   ```powershell
   pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ atumanyire-ange-calc
   ```

## Step 10: Publishing to the real PyPI (optional)

The workflow is the same. Create an API token on https://pypi.org and drop
`--repository testpypi`:

```powershell
python -m twine upload dist/*
```

Users can then install with a plain `pip install atumanyire-ange-calc`.

## Troubleshooting

| Problem | Cause and fix |
|---|---|
| `File already exists` on upload | That version is already on the index. Bump the version and rebuild (Step 9). |
| `403 Forbidden` / invalid credentials | The username must be exactly `__token__`, and the token must include the `pypi-` prefix. TestPyPI and PyPI tokens aren't interchangeable. |
| `The name ... is too similar to an existing project` | Pick a more unique `name` in `pyproject.toml`. |
| `No matching distribution found` right after upload | The index can take a minute to update. Wait and retry. |
| `ModuleNotFoundError: atumanyire_ange_calc` | The virtual environment where the package is installed isn't active. Run `test_env\Scripts\activate` first, or install into the environment you're using. |
| PyCharm: "Cannot find reference 'operations'" | PyCharm is using an interpreter where the package isn't installed, or where a different package with the same name is installed. Check File → Settings → Project → Python Interpreter, install the package there, then File → Invalidate Caches if the warning remains. |
| `TypeError: 'type' object is not subscriptable` on Python 3.8 | Use `typing.List[float]` instead of `list[float]`. |

## Lab submission checklist

1. GitHub repository: https://github.com/ATUMANYIRE/AtumanyireAnge-Calc
2. TestPyPI page: https://test.pypi.org/project/atumanyire-ange-calc/
3. Screenshot of Step 7: the `pip install` and `python atumanyire_ange.py` output.

## License

MIT. See [LICENSE](LICENSE).
