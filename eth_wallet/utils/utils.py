#!/usr/bin/env python3

from mnemonic import Mnemonic

import random


def generate_entropy(strength=128):

    if strength % 32 != 0:
        raise ValueError("strength must be a multiple of 32")
    if strength < 128 or strength > 256:
        raise ValueError("strength should be >= 128 and <= 256")

    return random.randint(0, 2 ** strength - 1) \
        .to_bytes(16, byteorder="big")


def get_bytes(string):
    if isinstance(string, bytes):
        byte = string
    elif isinstance(string, str):
        byte = bytes.fromhex(string)
    else:
        raise TypeError("agreement must be either 'bytes' or 'string'!")
    return byte


def check_mnemonic(mnemonic, language="english"):
    try:
        return Mnemonic(language=language).check(mnemonic)
    except:
        return False
