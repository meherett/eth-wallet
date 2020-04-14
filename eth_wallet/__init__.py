#!/usr/bin/env python3

try:
    from .wallet import Wallet
    from .utils import utils, base58
    modules = [
        "Wallet",
        "utils",
        "base58"
    ]
except ModuleNotFoundError:
    modules = []


# ETH-Wallet Information's
__version__ = "0.2.0"
__license__ = "GPL-3.0"
__author__ = "Meheret Tesfaye"
__email__ = "meherett@zoho.com"


__all__ = [
    "__version__",
    "__license__",
    "__author__",
    "__email__",
    *modules
]
