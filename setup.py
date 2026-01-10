"""
Setup script for dlrsp-requirements.

This is a metadata-only package that helps GitHub track usage
of the DLRSP requirements repository.
"""

from setuptools import setup

# Read requirements from dev.in to include in install_requires
# This allows GitHub to track dependencies
try:
    with open("dev.in", "r") as f:
        requirements = [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]
except FileNotFoundError:
    requirements = []

setup(
    name="dlrsp-requirements",
    version="1.0.5",
    description="Common Python requirements for DLRSP organization projects",
    long_description=open("README.md").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/DLRSP/requirements",
    author="DLRSP",
    author_email="dlrsp-dev@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    # Include dependencies so GitHub can track them
    install_requires=requirements,
    # This is a metadata-only package
    packages=[],
    zip_safe=False,
)
