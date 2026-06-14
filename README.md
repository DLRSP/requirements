# Requirements

Centralized repository for managing common Python dependencies used in DLRSP organization projects.

## Description

This repository contains compiled Python requirements files for different Python versions. These files are **CI and development only** — they are not bundled in PyPI wheels and are not used for production deploy of django-* modules.

## Available Files

### Development Requirements (CI/dev only)
- `py39-dev.txt` through `py314-dev.txt` — tox, pytest, coverage, pip-tools, etc.

### CI Test Requirements (CI only)
- `py39-test.txt` through `py314-test.txt` — coveralls, django-jenkins, and transitive deps for module tox/CI

### Documentation Requirements
- `py310-docs.txt`, `py311-docs.txt` — MkDocs and related tooling

### Source Files
- `dev.in` — development and tox tooling
- `test.in` — CI-only test tooling (coveralls, django-jenkins)
- `requirements/docs.in` — documentation generation

## Usage

Install from a tagged release in module tox or CI workflows:

```bash
# Dev tooling (Python 3.11 example)
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/v1.0.9/py311-dev.txt

# CI test tooling
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/v1.0.9/py311-test.txt
```

In GitHub Actions, pin the workflows `requirements-ref` input to a semver tag (e.g. `v1.0.9`).

## Updating Requirements

The `.txt` files are generated from `.in` files using `pip-compile`:

```bash
pip-compile --allow-unsafe --generate-hashes --output-file=py311-dev.txt dev.in
pip-compile --allow-unsafe --generate-hashes --output-file=py311-test.txt test.in
```

The `upgrade-common-dependency` workflow recompiles all `.in` files on schedule and opens PRs when dependencies change.

## Included Dependencies

### Development (`dev.in`)
- `pip`, `setuptools`, `wheel` — base tools
- `tox`, `tox-py` — test automation
- `coverage`, `pytest`, `pytest-django`, `pytest-randomly` — testing

### CI test (`test.in`)
- `coveralls` — coverage reporting in CI
- `django-jenkins` — Jenkins integration for django-* module CI

### Documentation (`requirements/docs.in`)
- `mkdocs`, `mkdocs-material`, revision-date plugin

## Automated Workflows

This repository uses centralized workflows from `DLRSP/workflows`:
- **Verify Requirements** — compile check + install dry-run for dev, test, docs, and django matrix locks
- **Upgrade Common Dependencies** — weekly dependency upgrades via PR
- **Release Requirements** — semver tag on merge to main

## Notes

- Requirements files use `--generate-hashes` for reproducibility
- `dev.in` and `test.in` are **not** shipped in PyPI module wheels; runtime locks live per-module under `requirements/py*-django*.txt`
- This repository is not an installable Python package

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — see [LICENSE](LICENSE).
