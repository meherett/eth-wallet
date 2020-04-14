#!/usr/bin/env python3

try:
    from .wallet import Wallet
    modules = ["Wallet"]
except ModuleNotFoundError:
    modules = list()


# Author Information's
__version__ = "0.2.1"
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
