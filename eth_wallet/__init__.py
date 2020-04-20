#!/usr/bin/env python3


# Information's
__version__ = "0.2.6"
__license__ = "GPL-3.0"
__author__ = "Meheret Tesfaye"
__email__ = "meherett@zoho.com"


# Wallet class
from .wallet import Wallet

modules = [
    "Wallet"
]


__all__ = [
    "__version__",
    "__license__",
    "__author__",
    "__email__",
    *modules
]
