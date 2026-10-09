# My Calculator (`my_calculator`)

This project is an example of creating a modern **Python Package** using PEP 517/518/621 standards (`pyproject.toml`) and the `src-layout` structure, distributed directly via a **Git Repository** (GitHub) without needing to publish to PyPI.

The implementation and usage test code can be found in the [`examplepackagetest`](../examplepackagetest) directory.

---

## Table of Contents

1. [Architecture & Project Structure](#architecture--project-structure)
2. [Technical Breakdown of Package Components](#technical-breakdown-of-package-components)
3. [Distribution via Git Mechanism](#distribution-via-git-mechanism)
4. [Implementation Guide (`examplepackagetest`)](#implementation-guide-examplepackagetest)
5. [Code Example & Output](#code-example--output)
6. [Local Development Workflow](#local-development-workflow)

---

## Architecture & Project Structure

The structure of the repository and test consumer project is organized as follows:

```text
pythonpackage/
│
├── my-calculator/                      # Python Package Git Repository
│   ├── .git/                           # Git Version Control
│   ├── pyproject.toml                  # Build configuration & package metadata (PEP 621)
│   ├── README.md                       # Technical package documentation
│   └── src/                            # Source code directory (src-layout)
│       └── my_calculator/              # Main package
│           ├── __init__.py             # Package entry point (exposes public API)
│           └── core.py                 # Mathematical function implementations
│
└── examplepackagetest/                 # Consumer / implementation directory
    ├── requirements.txt                # Project dependencies (referencing the Git repo)
    └── main.py                         # Test & demonstration script
```

### Why Use `src-layout`?

The `src/my_calculator/` layout is recommended by the [Python Packaging Authority (PyPA)](https://packaging.python.org/) because:

- **Prevents Import Parity Bugs**: Prevents Python from accidentally importing modules directly from the current working directory (CWD) during testing, ensuring that tests only run against the package as actually installed.
- **Clean File Separation**: Separates application source code from root-level configuration files, test runners, and documentation.

---

## Technical Breakdown of Package Components

### 1. Build Configuration: [`pyproject.toml`](./pyproject.toml)

This file replaces traditional `setup.py` and `setup.cfg` configurations, adhering to modern Python packaging specifications:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_calculator"
version = "1.0.0"
description = "Modul kalkulator sederhana untuk example repositori"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Alfin", email = "halovinaofficial@gmail.com" }
]

[tool.setuptools.packages.find]
where = ["src"]
```

- **`build-system`**: Specifies the build frontend and backend tools (`setuptools`).
- **`project`**: Declares package metadata including name, version, description, minimum Python version, and authors.
- **`tool.setuptools.packages.find`**: Directs `setuptools` to discover Python modules inside the `src/` directory.

### 2. Core Logic: [`core.py`](./src/my_calculator/core.py)

Provides fundamental arithmetic functions with type hinting and error handling:

- `add(a, b)`: Adds two numbers.
- `subtract(a, b)`: Subtracts two numbers.
- `multiply(a, b)`: Multiplies two numbers.
- `divide(a, b)`: Divides two numbers, raising `ValueError("Tidak dapat membagi dengan nol.")` if the divisor is `0`.

### 3. Exposing Public API: [`__init__.py`](./src/my_calculator/__init__.py)

```python
from .core import add, subtract, multiply, divide
```

By re-exporting the functions from `.core` in `__init__.py`, consumers can import and invoke functions directly:

```python
import my_calculator

my_calculator.add(5, 3)
```

without needing to reach into internal modules such as `my_calculator.core.add(5, 3)`.

---

## Distribution via Git Mechanism

This package is distributed directly from a GitHub repository without requiring publication to PyPI. `pip` natively supports installation via VCS (Version Control System) protocols.

Git URL format for `pip`:

```text
git+https://github.com/<username>/<repository-name>[@<commit_or_tag_or_branch>]
```

Installation options:

- **Default (latest default branch commit)**:
  ```bash
  pip install git+https://github.com/halovina/my-calculator
  ```

- **Specific Tag / Release**:
  ```bash
  pip install git+https://github.com/halovina/my-calculator@v1.0.0
  ```

- **Specific Branch**:
  ```bash
  pip install git+https://github.com/halovina/my-calculator@main
  ```

- **Specific Commit Hash**:
  ```bash
  pip install git+https://github.com/halovina/my-calculator@a1b2c3d
  ```

---

## Implementation Guide (`examplepackagetest`)

The [`examplepackagetest`](../examplepackagetest) directory acts as a client project that consumes the `my_calculator` package.

### 1. Declaring Dependencies ([`requirements.txt`](../examplepackagetest/requirements.txt))

Contents of `requirements.txt`:

```text
git+https://github.com/halovina/my-calculator
```

### 2. Installing Dependencies

Run the following command in your terminal (preferably inside an active virtual environment):

```bash
cd examplepackagetest
pip install -r requirements.txt
```

> `pip` automatically clones the repository, reads `pyproject.toml`, builds the package, and installs it into your Python environment.

### 3. Executing Code ([`main.py`](../examplepackagetest/main.py))

`main.py` demonstrates calling the addition and division functions, including handling the zero-division error:

```python
# main.py
import my_calculator

try:
    # Using the addition function
    hasil_tambah = my_calculator.add(10, 5)
    print(f"Hasil 10 + 5 = {hasil_tambah}")

    # Using the division function
    hasil_bagi = my_calculator.divide(20, 4)
    print(f"Hasil 20 / 4 = {hasil_bagi}")
    
    # Testing division by zero
    my_calculator.divide(10, 0)

except ValueError as e:
    print(f"Error terdeteksi: {e}")
```

Run the script:

```bash
python main.py
```

---

## Code Example & Output

Terminal output when running `main.py`:

```text
Hasil 10 + 5 = 15
Hasil 20 / 4 = 5.0
Error terdeteksi: Tidak dapat membagi dengan nol.
```

---

## Local Development Workflow

To make local changes to `my-calculator` and immediately test them in `examplepackagetest` without committing and pushing to GitHub every time:

1. **Install in Editable Mode (`-e`)**:
   ```bash
   pip install -e /path/to/my-calculator
   ```
   Or from within the `examplepackagetest` directory:
   ```bash
   pip install -e ../my-calculator
   ```

2. **Git Commit & Push Workflow**:
   Once your local changes are verified:
   ```bash
   cd my-calculator
   git add .
   git commit -m "feat: add new feature"
   git push origin main
   ```

3. **Updating the Package in Client Projects**:
   To update an existing installation to the latest remote commit:
   ```bash
   pip install --upgrade --force-reinstall git+https://github.com/halovina/my-calculator
   ```