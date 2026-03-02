# Contributing to the Cryptography Research Template

Thank you for your interest in improving this research template. Contributions that enhance the robustness, clarity, or performance of the cryptographic primitives or the research environment are welcome.

## Workflow

1.  **Environment Management:** All development must be conducted via [Poetry](https://python-poetry.org/).
2.  **Quality Control:** Contributions must pass the project's quality control suite:
    - **Linting:** `poetry run ruff check .`
    - **Formatting:** `poetry run ruff format .`
    - **Type Checking:** `poetry run mypy src`
3.  **Testing:** Every contribution must be accompanied by relevant unit or property-based tests. All tests must pass:
    ```bash
    poetry run pytest
    ```
4.  **Pull Requests:** When submitting a PR, clearly explain the improvement in the context of research efficiency, cryptographic correctness, or protocol scalability.
