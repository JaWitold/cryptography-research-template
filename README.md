# Cryptography Research Template

## Overview

This repository provides a standardized, academic-grade template for implementing and evaluating cryptographic protocols and primitives. It is designed to streamline the transition from theoretical research to verifiable proof-of-concept implementations, ensuring high standards for code quality, type safety, and automated testing.

The template is pre-configured for pairing-based cryptography, signature schemes, and zero-knowledge primitives, but it remains general enough for any Python-based cryptographic research.

## Project Structure

- `src/`: Core protocol implementations.
- `tests/`: Comprehensive test suite including functional verification and edge-case analysis.
- `notebooks/`: Jupyter notebooks for protocol demonstrations and visual analysis.
- `docs/`: Automated API documentation and research notes.

## Tech Stack

- **Language:** Python 3.10+
- **Dependency Management:** [Poetry](https://python-poetry.org/)
- **Cryptographic Primitives:**
  - `cryptography`: General-purpose primitives (AES, RSA, SHA).
  - `PyNaCl`: Networking and Cryptography (NaCl) library.
  - `py_ecc`: BLS12-381 pairing-friendly elliptic curve implementation.
- **Quality Control:**
  - `pytest`: Testing and coverage reporting.
  - `ruff`: High-performance linting and formatting.
  - `mypy`: Static type checking.
  - `pdoc`: Documentation generation.

## Usage Guide

### 1. Installation & Setup

Ensure you have [Poetry](https://python-poetry.org/) installed. Clone the repository and initialize the environment:

```bash
git clone <repository-url>
cd cryptography-research-template
poetry install
```

### 2. Automated Testing

The project uses `pytest` for functional verification and `Hypothesis` for property-based testing of mathematical invariants.

```bash
# Run all tests
poetry run pytest

# Run tests with terminal coverage report
poetry run pytest --cov=src

# Run property-based invariant tests only
poetry run pytest tests/test_invariants.py
```

### 3. Quality Assurance & Static Analysis

Maintain high code standards using the integrated linting and typing suite.

```bash
# Comprehensive linting and formatting check
poetry run ruff check .
poetry run ruff format --check .

# Strict static type analysis
poetry run mypy src tests

# Install pre-commit hooks for automated checks
poetry run pre-commit install
```

### 4. Performance Benchmarking

Evaluate protocol efficiency using the benchmarking suite. Results are critical for academic performance analysis.

**Local Execution:**
```bash
PYTHONPATH=. poetry run python benchmarks/benchmark_bls.py
```

**Reproducible Execution (Docker):**
To ensure consistent results across different environments, use the provided Docker configuration:
```bash
docker build -t crypto-research-bench .
docker run --rm crypto-research-bench
```

### 5. Interactive Research (Jupyter)

For protocol prototyping and visual analysis, use the pre-configured Jupyter environment.

```bash
poetry run jupyter notebook notebooks/bls_usage.ipynb
```

### 6. Documentation Generation

The project supports two layers of documentation: automated API references via `pdoc` and a structured research site via `MkDocs`.

```bash
# Generate API docs
poetry run pdoc --output-dir docs/api src

# Serve the research site locally
poetry run mkdocs serve
```

## Security Assumptions

Implementations within this framework typically operate under specific cryptographic models (e.g., Random Oracle Model). Researchers using this template are encouraged to document their assumptions within the protocol-specific modules.
