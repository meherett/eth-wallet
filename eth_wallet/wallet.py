#!/usr/bin/env python3

"""
AUTHOR: Meheret Tesfaye
EMAIL: meherett@zoho.com
GITHUB: https://github.com/meherett
"""

from ecdsa.curves import SECP256k1
from ecdsa.ecdsa import int_to_string, string_to_int
from binascii import hexlify, unhexlify

import hmac
import ecdsa
import struct
import codecs
import hashlib
import binascii

from eth_wallet.utils.base58 import *
from eth_wallet.utils.utils import *


MiN_ENTROPY_LEN = 128
BIP32KEY_HARDEN = 0x80000000
CURVE_GEN = ecdsa.ecdsa.generator_secp256k1
CURVE_ORDER = CURVE_GEN.order()
FiELD_ORDER = SECP256k1.curve.p()
INFINITY = ecdsa.ellipticcurve.INFINITY
EX_MAIN_PRIVATE = [
    codecs.decode("0488ade4", "hex")
]
EX_MAIN_PUBLiC = [
    codecs.decode("0488b21e", "hex"),
    codecs.decode("049d7cb2", "hex")
]


class Wallet:

    def __init__(self):

        self.secret = None
        self.parent_fingerprint = b"\0\0\0\0"

        self.key = None
        self.verified_key = None

        self.chain = None
        self.depth = 0
        self.index = 0

        self.mnemonic = None
        self.seed = None
        self._path = "m"

    def from_entropy(self, entropy,
                     passphrase=str(), language="english"):

        self.mnemonic = Mnemonic(language=language) \
            .to_mnemonic(entropy.encode())

        i = hmac.new(b"Bitcoin seed", get_bytes(
            Mnemonic.to_seed(self.mnemonic, passphrase)), hashlib.sha512).digest()
        il, ir = i[:32], i[32:]

        parse_il = int.from_bytes(il, "big")
        if parse_il == 0 or parse_il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        self.secret, self.chain = il, ir
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        return self

    def from_mnemonic(self, mnemonic, passphrase=str()):

        if not check_mnemonic(mnemonic):
            raise ValueError("Invalid 12 word mnemonic!")

        self.mnemonic = mnemonic
        i = hmac.new(b"Bitcoin seed", get_bytes(
            Mnemonic.to_seed(self.mnemonic, passphrase)), hashlib.sha512).digest()
        il, ir = i[:32], i[32:]

        parse_il = int.from_bytes(il, "big")
        if parse_il == 0 or parse_il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        self.secret, self.chain = il, ir
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        return self

    def from_seed(self, seed):

        self.seed = seed
        i = hmac.new(b"Bitcoin seed", get_bytes(seed), hashlib.sha512).digest()
        il, ir = i[:32], i[32:]

        parse_il = int.from_bytes(il, "big")
        if parse_il == 0 or parse_il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        self.secret, self.chain = il, ir
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        return self

    def hmac(self, data):
        i = hmac.new(self.chain, data, hashlib.sha512).digest()
        return i[:32], i[32:]

    def derive_private_key(self, index):

        i_str = struct.pack(">L", index)
        if index & BIP32KEY_HARDEN:
            data = b"\0" + self.key.to_string() + i_str
        else:
            data = unhexlify(self.public_key()) + i_str
        il, ir = self.hmac(data)

        il_int = string_to_int(il)
        if il_int > CURVE_ORDER:
            return None
        pvt_int = string_to_int(self.key.to_string())
        k_int = (il_int + pvt_int) % CURVE_ORDER
        if k_int == 0:
            return None
        secret = (b"\0" * 32 + int_to_string(k_int))[-32:]

        self.secret, self.chain, self.depth, self.index, self.parent_fingerprint = \
            secret, ir, (self.depth + 1), index, unhexlify(self.finger_print())
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        return self

    def from_path(self, path):
        if str(path)[0:2] != "m/":
            raise ValueError("Bad path, please insert like this type of path \"m/0'/0\"! ")

        self._path = path
        for index in self._path.lstrip("m/").split("/"):
            if "'" in index:
                self.derive_private_key(int(index[:-1]) + BIP32KEY_HARDEN)
            else:
                self.derive_private_key(int(index))
        return self

    def from_index(self, index, harden=False):
        if not isinstance(index, int):
            raise ValueError("Bad index, Please import only integer number!")

        if harden:
            self._path = self._path + ("/%d'" % index)
            self.derive_private_key(index + BIP32KEY_HARDEN)
        else:
            self._path = self._path + ("/%d" % index)
            return self.derive_private_key(index)

    def private_key(self):
        return hexlify(self.key.to_string()).decode()

    def public_key(self, private_key=None):
        if private_key:
            key = ecdsa.SigningKey.from_string(
                unhexlify(private_key), curve=SECP256k1)
            verified_key = key.get_verifying_key()
            padx = (b"\0" * 32 + int_to_string(
                verified_key.pubkey.point.x()))[-32:]
            if verified_key.pubkey.point.y() & 1:
                ck = b"\3" + padx
            else:
                ck = b"\2" + padx
            return hexlify(ck).decode()
        padx = (b"\0" * 32 + int_to_string(
            self.verified_key.pubkey.point.x()))[-32:]
        if self.verified_key.pubkey.point.y() & 1:
            ck = b"\3" + padx
        else:
            ck = b"\2" + padx
        return hexlify(ck).decode()

    def path(self):
        return str(self._path)

    def uncompressed(self, private_key=None):
        if private_key:
            private_key = binascii.unhexlify(private_key)
            key = ecdsa.SigningKey.from_string(bytes(private_key), curve=SECP256k1)
            verified_key = key.get_verifying_key()
            return hexlify(verified_key.to_string()).decode()
        return hexlify(self.verified_key.to_string()).decode()

    def chain_code(self):
        return self.chain.hex()

    def identifier(self, private_key=None):
        if private_key is None:
            return hashlib.new("ripemd160", sha256(
                unhexlify(self.public_key(self.private_key()))).digest()).digest()
        return hashlib.new("ripemd160", sha256(
            unhexlify(self.public_key(private_key))).digest()).digest()

    def finger_print(self, private_key=None):
        if private_key is None:
            return hexlify(self.identifier(
                self.private_key())[:4]).decode()
        return hexlify(self.identifier(private_key)[:4]).decode()

    def address(self, private_key=None):
        keccak_256 = sha3.keccak_256()
        if private_key:
            key = ecdsa.SigningKey.from_string(
                unhexlify(private_key), curve=SECP256k1)
            verified_key = key.get_verifying_key()
            keccak_256.update(verified_key.to_string())
            address = keccak_256.hexdigest()[24:]
            return checksum_encode(address)
        keccak_256.update(self.verified_key.to_string())
        address = keccak_256.hexdigest()[24:]
        return checksum_encode(address)

    def wallet_import_format(self, private_key=None):
        if private_key:
            key = ecdsa.SigningKey.from_string(
                unhexlify(private_key), curve=SECP256k1)
            raw = b"\x80" + key.to_string() + b"\x01"
            return check_encode(raw)
        raw = b"\x80" + self.key.to_string() + b"\x01"
        return check_encode(raw)

    def extended_key(self, private_key=True, encoded=True):
        version = EX_MAIN_PRIVATE[0] if private_key else EX_MAIN_PUBLiC[0]
        depth = bytes(bytearray([self.depth]))
        parent_fingerprint = self.parent_fingerprint
        child = struct.pack(">L", self.index)
        chain = self.chain

        data = b"\x00" + unhexlify(self.private_key())
        raw = (version + depth +
               parent_fingerprint + child + chain + data)
        if not encoded:
            return raw.hex()
        else:
            return check_encode(raw)

    def dumps(self):
        return {
            "private_key": self.private_key(),
            "public_key": self.public_key(),
            "uncompressed": self.uncompressed(),
            "wif": self.wallet_import_format(),
            "finger_print": self.finger_print(),
            "chain_code": self.chain_code(),
            "path": self.path(),
            "address": self.address(),
            "serialized": {
                "private_key_hex": self.extended_key(private_key=True, encoded=False),
                "public_key_hex": self.extended_key(private_key=False, encoded=False),
                "xprivate_key_base58": self.extended_key(private_key=True, encoded=True),
                "xpublic_key_base58": self.extended_key(private_key=False, encoded=True),
            }
        }
