# Requirements Repository Usage Example

This example project demonstrates how to use the `DLRSP/requirements` repository in a Python project.

## 📋 Description

This example shows how to:
1. Install dependencies from the requirements repository
2. Configure GitHub Actions to use the requirements
3. Run automated tests

## 🚀 Setup

### Local Installation

```bash
# Clone the repository
git clone https://github.com/DLRSP/example-usage.git
cd example-usage

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies from the requirements repository
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt

# Or, if you have already downloaded the requirements locally
pip install -r ../requirements/py310-dev.txt
```

## 🧪 Running Tests

```bash
# Run tests with pytest
pytest

# With coverage
coverage run -m pytest
coverage report
```

## 📝 Project Structure

```
example-usage/
├── README.md
├── .github/
│   └── workflows/
│       └── ci.yaml          # CI workflow that uses the requirements
├── tests/
│   └── test_example.py      # Example tests
└── src/
    └── example.py            # Example code
```

## 🔧 GitHub Actions Configuration

The `.github/workflows/ci.yaml` workflow shows how to use the requirements in GitHub Actions:

```yaml
- name: Install dependencies
  run: |
    pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt
```

## ✅ Verification

This project should:
- ✅ Correctly install all dependencies from the requirements repository
- ✅ Automatically run tests on GitHub Actions
- ✅ Work with different Python versions (3.9, 3.10, 3.11, 3.12)
