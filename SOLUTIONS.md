# Solutions to Identified Problems

## 🔍 Identified Problems

1. **Blocked or incomplete PRs** due to dependencies
2. **GitHub does not track usage** of the requirements repository by other projects
3. **Lack of documentation** on how to use this repository

## ✅ Proposed Solutions

### 1. Resolving Dependency Issues in PRs

#### Problem
PRs in DLRSP repositories get blocked or don't complete correctly due to dependency issues.

#### Solutions

**A. Use GitHub raw URLs with specific tags**

Instead of using the `main` branch, use versioned tags to ensure stability:

```yaml
# ❌ Don't do this (uses main branch, which can change)
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt

# ✅ Do this (uses versioned tags)
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/v1.0.0/py310-dev.txt
```

**B. Add fallback for missing dependencies**

In GitHub Actions workflows, add error handling:

```yaml
- name: Install dependencies
  run: |
    pip install --upgrade pip setuptools wheel || true
    pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt || pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt --no-deps
```

**C. Verify that requirements files are always up to date**

Add a workflow that periodically verifies that requirements are synchronized:

```yaml
# .github/workflows/verify-requirements.yaml
name: Verify Requirements
on:
  schedule:
    - cron: '0 0 * * 1'  # Every Monday
  workflow_dispatch:

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Verify requirements can be installed
        run: |
          pip install pip-tools
          pip-compile --check dev.in
```

### 2. Making GitHub Track Repository Usage

#### Problem
GitHub doesn't show that this repository is used by other projects because:
- It's not a Python package published on PyPI
- Files are referenced via raw URLs, which GitHub doesn't automatically track
- There's no recognized "dependency" mechanism from GitHub

#### Solutions

**A. Publish as Python Package (Recommended)**

Create a minimal Python package that can be installed from PyPI or GitHub:

1. **Create `setup.py` or `pyproject.toml`:**

```python
# setup.py
from setuptools import setup

setup(
    name="dlrsp-requirements",
    version="1.0.0",
    description="Common Python requirements for DLRSP projects",
    url="https://github.com/DLRSP/requirements",
    packages=[],  # No packages, only metadata
    install_requires=[
        # List of dependencies from dev.in
    ],
    python_requires=">=3.9",
)
```

2. **Publish to PyPI or GitHub Packages:**

```bash
# Publish to GitHub Packages
python -m build
python -m twine upload --repository github dist/*
```

3. **Usage in projects:**

```bash
pip install dlrsp-requirements
# or
pip install git+https://github.com/DLRSP/requirements.git
```

**B. Use GitHub Dependency Graph (Alternative)**

GitHub automatically tracks dependencies if:
- Projects use `requirements.txt` or `pyproject.toml` that reference this repository
- The repository is referenced as a Git submodule

**Example with submodule:**

```bash
# In projects that use requirements
git submodule add https://github.com/DLRSP/requirements.git requirements-common
```

Then in workflows:

```yaml
- name: Checkout with submodules
  uses: actions/checkout@v4
  with:
    submodules: recursive

- name: Install dependencies
  run: |
    pip install -r requirements-common/py310-dev.txt
```

**C. Use GitHub Actions Reusable Workflows**

Create a reusable workflow that other repositories can call:

```yaml
# .github/workflows/install-requirements.yaml
name: Install Requirements
on:
  workflow_call:
    inputs:
      python-version:
        required: true
        type: string

jobs:
  install:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          repository: DLRSP/requirements
          path: requirements
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
      - name: Install
        run: |
          pip install -r requirements/py310-dev.txt
```

**Usage in other repositories:**

```yaml
jobs:
  test:
    uses: DLRSP/requirements/.github/workflows/install-requirements.yaml@main
    with:
      python-version: "3.10"
```

**D. Add Metadata to Repository**

Add files that GitHub can recognize:

1. **Create `.github/FUNDING.yml`** (optional, for support)
2. **Add topic tags** to the repository: `python`, `requirements`, `dependencies`, `dlrsp`
3. **Create `package.json` for npm** (if applicable) or other recognized formats

### 3. Improve Documentation

#### Implemented Solutions

✅ **README.md** - Complete documentation on how to use the repository
✅ **example-usage/** - Working example project
✅ **SOLUTIONS.md** - This document with solutions

#### Additional Suggested Improvements

1. **Add badges to README:**

```markdown
![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
```

2. **Add "Used By" section to README:**

```markdown
## 📦 Projects Using This Repository

- [django-errors](https://github.com/DLRSP/django-errors)
- [django-sp](https://github.com/DLRSP/django-sp)
- [django-iubenda](https://github.com/DLRSP/django-iubenda)
```

3. **Create GitHub Pages** with detailed documentation

### 4. Automate Updates

#### Workflow for Automatic Updates

Add a workflow that:
- Automatically updates requirements when dependencies change
- Creates automatic PRs in repositories that use this repository
- Verifies that requirements are installable

## 🎯 Recommended Implementation Plan

### Phase 1: Stabilization (Immediate)
1. ✅ Create README.md with documentation
2. ✅ Create example project
3. ⏳ Add requirements verification workflow
4. ⏳ Create versioned tags for stability

### Phase 2: GitHub Tracking (Short term)
1. ⏳ Publish as Python package on GitHub Packages
2. ⏳ Add submodule support
3. ⏳ Create reusable workflow

### Phase 3: Automation (Medium term)
1. ⏳ Automate requirements updates
2. ⏳ Create bot to update dependent repositories
3. ⏳ Add monitoring and alerting

## 📚 Useful Resources

- [GitHub Dependency Graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph)
- [GitHub Packages](https://docs.github.com/en/packages)
- [Reusable Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [pip-compile documentation](https://pip-tools.readthedocs.io/)
