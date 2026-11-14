# Contributing to `mlops-python-package`

## Pull Request Policy
- Never push directly to `main`.
- All changes must go through an isolated feature branch and pull request.
- Ensure all CI checks pass before requesting review.

## Quality Checks (Python Profile)
```bash
ruff check . && ruff format --check . && mypy . && pytest
```
