#!/usr/bin/env python3

from mnemonic import Mnemonic
from binascii import hexlify

import os


def get_bytes(string):
    if isinstance(string, bytes):
        byte = string
    elif isinstance(string, str):
        byte = bytes.fromhex(string)
    else:
        raise TypeError("agreement must be either 'bytes' or 'string'!")
    return byte


def generate_mnemonic(language="english", strength=128):
    return Mnemonic(language=language).generate(strength=strength)


def generate_entropy(strength=128):
    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError(
            "Strength should be one of the following "
            "[128, 160, 192, 224, 256], but it is not (%d)."
            % strength
        )
    return hexlify(os.urandom(strength // 8)).decode()


def check_mnemonic(mnemonic, language):
    try:
        return Mnemonic(language=language).check(mnemonic)
    except:
        return False
