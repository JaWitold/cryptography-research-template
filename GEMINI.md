# GEMINI.md

## Project Overview

The **Cryptography Research Template** is an academic-grade framework for implementing, evaluating, and demonstrating cryptographic protocols and primitives in Python. It is specifically designed to bridge the gap between theoretical cryptographic research and verifiable proof-of-concept implementations.

### Main Technologies
- **Language:** Python 3.14+
- **Dependency Management:** [Poetry](https://python-poetry.org/)
- **Core Cryptography:** `cryptography`, `PyNaCl`, and `py_ecc` (for BLS12-381 pairings).
- **Quality Assurance:** `pytest` (testing), `ruff` (linting/formatting), `mypy` (strict type checking).
- **Documentation & Analysis:** `pdoc` (API docs), `jupyter` (interactive notebooks).

### Architecture
- `src/`: Contains the core cryptographic implementations (e.g., `bls.py`).
- `tests/`: Houses the test suite, ensuring functional correctness and edge-case coverage.
- `notebooks/`: Provides interactive demonstrations of the protocols (e.g., `bls_usage.ipynb`).
- `docs/`: Stores generated API documentation.

## Building and Running

### Setup
Ensure you have Poetry installed, then run:
```bash
poetry install
```

### Execution & Testing
- **Run Tests:** `poetry run pytest` (includes coverage reporting).
- **Linting:** `poetry run ruff check .`
- **Formatting:** `poetry run ruff format .`
- **Type Checking:** `poetry run mypy src tests`
- **Generate Documentation:** `poetry run pdoc --output-dir docs/api src`
- **Launch Notebooks:** `poetry run jupyter notebook`

### CI/CD
A GitHub Actions pipeline is configured in `.github/workflows/ci.yml` to automatically run the quality control suite on every push and pull request.

## Development Conventions

### Coding Style
- **Compliance:** Strictly follows PEP 8 via Ruff.
- **Docstrings:** Uses **Google-style docstrings**.
- **Line Length:** Configured to **88 characters**.
- **Type Safety:** Employs **strict Mypy** checking. All functions should have type annotations.

### Testing Practices
- **Framework:** `pytest`.
- **Coverage:** Aim for high coverage on all core cryptographic logic (tracked via `pytest-cov`).
- **Mocks:** Use `unittest.mock` for simulating exceptions in third-party libraries.

### Security Guidelines
- **Academic Focus:** This is a research template. Implementations are **not** audited for production use.
- **Constant-Time:** Be mindful that standard Python is generally not constant-time; research code should clearly document timing assumptions.
- **Vulnerability Reporting:** Report issues via GitHub Issues, keeping the research context in mind.

## Citations
Researchers using this template for their publications can find the appropriate BibTeX entry in `CITATION.bib`.
