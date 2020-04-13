#!/usr/bin/env python3

from setuptools import setup, find_packages

import eth_wallet

# README.md
with open("README.md", "r") as readme:
    long_description = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="eth-wallet",
    version=eth_wallet.__version__,
    description="The implementation of Hierarchical Deterministic (HD) wallets generator for Ethereum protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=eth_wallet.__license__,
    author=eth_wallet.__author__,
    author_email=eth_wallet.__email__,
    url="https://github.com/mehetett/bip32key",
    keywords=["ethereum-wallet", "eth", "wallet"],
    python_requires=">=3.6,<4",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest>=5.4.1,<6",
            "pytest-cov>=2.8.1,<3"
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]
)
