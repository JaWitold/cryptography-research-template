# Welcome to the Cryptography Research Template

This template provides a standardized, professional environment for implementing and evaluating cryptographic protocols and primitives in Python.

## Core Research & Development Workflows

### 1. Functional Verification (Testing)

The project utilizes `pytest` for functional tests and `Hypothesis` for property-based verification of mathematical invariants.

- **Full Suite:** `poetry run pytest`
- **With Coverage:** `poetry run pytest --cov=src`
- **Invariants Only:** `poetry run pytest tests/test_invariants.py`

### 2. Quality Assurance & Static Analysis

Maintain high academic and software engineering standards with integrated static analysis tools.

- **Linting & Formatting:** `poetry run ruff check .`
- **Type Safety (Strict):** `poetry run mypy src tests`
- **Pre-commit:** `poetry run pre-commit install`

### 3. Performance Evaluation (Benchmarking)

Performance metrics are essential for academic evaluation. Use the benchmarking suite to collect data for your research.

- **Direct Run:** `PYTHONPATH=. poetry run python benchmarks/benchmark_bls.py`
- **Docker (Reproducible):**
  ```bash
  docker build -t crypto-research-bench .
  docker run --rm crypto-research-bench
  ```

### 4. Interactive Analysis (Jupyter)

Use Jupyter Notebooks for visual demonstrations and interactive protocol prototyping.

- **Launch:** `poetry run jupyter notebook notebooks/bls_usage.ipynb`

### 5. Documentation Management

The template supports both low-level API references and high-level research documentation.

- **Generate API Reference:** `poetry run pdoc --output-dir docs/api src`
- **Serve Site Locally:** `poetry run mkdocs serve`

## Next Steps

- Consult the [Mathematical Context](math.md) for formal definitions.
- Review the [Security Policy](security.md) regarding implementation limitations.
- Explore the `src/` directory for protocol implementation patterns.
