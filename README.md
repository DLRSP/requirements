# Requirements

Centralized repository for managing common Python dependencies used in DLRSP organization projects.

## 📋 Description

This repository contains compiled Python requirements files for different Python versions, used as common dependencies across all organization projects.

## 📦 Available Files

### Development Requirements
- `py38-dev.txt` - Python 3.8
- `py39-dev.txt` - Python 3.9
- `py310-dev.txt` - Python 3.10
- `py311-dev.txt` - Python 3.11

### Documentation Requirements
- `py-docs.txt` - Dependencies for documentation generation (MkDocs)

### Source Files
- `dev.in` - Source file for development requirements
- `docs.in` - Source file for documentation requirements

## 🚀 Usage

### Installation via GitHub URL

To use these requirements in a project, you can install them directly from GitHub:

```bash
# For Python 3.10
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt

# For Python 3.11
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py311-dev.txt

# For documentation
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py-docs.txt
```

### Usage in GitHub Actions

Example usage in a GitHub Actions workflow:

```yaml
- name: Install dependencies
  run: |
    pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt
```

### Usage with Tags/Versions

To use a specific version, you can reference a tag:

```bash
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/v1.0.0/py310-dev.txt
```

## 🔄 Updating Requirements

The `.txt` files are automatically generated from `.in` files using `pip-compile`:

```bash
# For Python 3.10
pip-compile --allow-unsafe --generate-hashes --output-file=py310-dev.txt dev.in

# For Python 3.11
pip-compile --allow-unsafe --generate-hashes --output-file=py311-dev.txt dev.in

# For documentation
pip-compile --allow-unsafe --generate-hashes --output-file=py-docs.txt docs.in
```

## 📝 Included Dependencies

### Development Requirements (`dev.in`)
- `pip`, `setuptools`, `wheel` - Base tools
- `tox`, `tox-py` - Testing and automation
- `coverage` - Code coverage
- `pytest`, `pytest-django`, `pytest-randomly` - Testing frameworks

### Documentation Requirements (`docs.in`)
- `mkdocs`, `mkdocs-material` - Documentation generation
- `mkdocs-git-revision-date-plugin` - Plugin for revision dates

## 🔧 Automated Workflows

This repository uses centralized workflows from `DLRSP/workflows`:
- **CI/CD**: Runs automated tests on push and PR
- **Upgrade Dependencies**: Automatically updates common dependencies
- **PR Rebase**: Automatically rebases PRs when push is made to main

## 📚 Notes

- Requirements files are generated with `--generate-hashes` to ensure security and reproducibility
- The `pip`, `setuptools` and `wheel` packages are marked as `--allow-unsafe` as they are necessary for installation
- This repository is not an installable Python package, but a repository of requirements files

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.
