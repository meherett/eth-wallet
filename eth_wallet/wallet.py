#!/usr/bin/env python3

from ecdsa.curves import SECP256k1
from ecdsa.ecdsa import int_to_string, string_to_int
from binascii import hexlify, unhexlify
from mnemonic import Mnemonic
from hashlib import sha256

import hmac
import ecdsa
import struct
import sha3
import codecs
import hashlib

from eth_wallet.libs.base58 import checksum_encode, check_encode
from eth_wallet.utils import get_bytes, check_mnemonic, get_mnemonic_language

MIN_ENTROPY_LEN = 128
BIP32KEY_HARDEN = 0x80000000
CURVE_GEN = ecdsa.ecdsa.generator_secp256k1
CURVE_ORDER = CURVE_GEN.order()
FIELD_ORDER = SECP256k1.curve.p()
INFINITY = ecdsa.ellipticcurve.INFINITY
# extended
EXTEND_MAIN_PRIVATE = [
    codecs.decode("0488ade4", "hex")
]
EXTEND_MAIN_PUBLIC = [
    codecs.decode("0488b21e", "hex"),
    codecs.decode("049d7cb2", "hex")
]


class Wallet:

    def __init__(self):
        # Initialize core
        self.parent_fingerprint = b"\0\0\0\0"
        self._root_private_key, self._root_public_key = None, None
        self.secret, self.key, self.verified_key = None, None, None
        self.chain, self.depth, self.index = None, 0, 0
        # Wallet information's
        self._entropy, self._mnemonic, self._language, self._seed, \
            self._path, self._passphrase = None, None, None, None, "m", None

    def from_entropy(self, entropy,
                     passphrase=None, language="english"):

        if language not in ["english", "french", "italian", "japanese",
                            "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
            raise ValueError("Invalid language, use only this options english, french, "
                             "italian, spanish, chinese_simplified, chinese_traditional, japanese & korean.")

        self._entropy = entropy
        self._language = str(language)
        self._passphrase = str(passphrase) if passphrase else str()
        self._mnemonic = Mnemonic(language=self._language) \
            .to_mnemonic(data=unhexlify(self._entropy))
        self._seed = Mnemonic.to_seed(mnemonic=self._mnemonic, passphrase=self._passphrase)

        i = hmac.new(b"Bitcoin seed", get_bytes(
            self._seed), hashlib.sha512).digest()
        self._root_private_key = i
        il, ir = i[:32], i[32:]

        parse_il = int.from_bytes(il, "big")
        if parse_il == 0 or parse_il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        self.secret, self.chain = il, ir
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        self._root_public_key = self.verified_key.to_string()
        return self

    def from_mnemonic(self, mnemonic, passphrase=None, language=None):

        if language and language not in ["english", "french", "italian", "japanese",
                                         "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
            raise ValueError("Invalid language, use only this options english, french, "
                             "italian, spanish, chinese_simplified, chinese_traditional, japanese & korean.")

        if not check_mnemonic(mnemonic=mnemonic, language=language):
            raise ValueError("Invalid 12 word mnemonic.")

        self._mnemonic = mnemonic
        self._language = str(language) if language \
            else str(get_mnemonic_language(mnemonic=self._mnemonic))
        self._passphrase = str(passphrase) if passphrase else str()
        self._seed = Mnemonic.to_seed(mnemonic=self._mnemonic, passphrase=self._passphrase)

        i = hmac.new(b"Bitcoin seed", get_bytes(
            self._seed), hashlib.sha512).digest()
        self._root_private_key = i
        il, ir = i[:32], i[32:]

        parse_il = int.from_bytes(il, "big")
        if parse_il == 0 or parse_il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        self.secret, self.chain = il, ir
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        self._root_public_key = self.verified_key.to_string()
        return self

    def from_seed(self, seed):

        self._seed = unhexlify(seed)
        i = hmac.new(b"Bitcoin seed", get_bytes(
            seed), hashlib.sha512).digest()
        self._root_private_key = i
        il, ir = i[:32], i[32:]

        parse_il = int.from_bytes(il, "big")
        if parse_il == 0 or parse_il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        self.secret, self.chain = il, ir
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        self._root_public_key = self.verified_key.to_string()
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

    def from_root_private_key(self, root_private_key):
        self._root_private_key = unhexlify(root_private_key)
        self.secret, self.chain = self._root_private_key[:32], self._root_private_key[32:]
        self.key = ecdsa.SigningKey.from_string(self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        self._root_public_key = self.verified_key.to_string()
        return self

    def from_private_key(self, private_key):
        self.secret, self._path = unhexlify(private_key), None
        self.key = ecdsa.SigningKey.from_string(
            self.secret, curve=SECP256k1)
        self.verified_key = self.key.get_verifying_key()
        return self

    def root_private_key(self):
        return hexlify(self._root_private_key).decode() if self._root_private_key else None

    def root_public_key(self):
        return hexlify(self._root_public_key).decode() if self._root_public_key else None

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

    def uncompressed(self):
        return hexlify(self.verified_key.to_string()).decode()

    def compressed(self):
        padx = (b"\0" * 32 + int_to_string(
            self.verified_key.pubkey.point.x()))[-32:]
        if self.verified_key.pubkey.point.y() & 1:
            ck = b"\3" + padx
        else:
            ck = b"\2" + padx
        return hexlify(ck).decode()

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
        return self.compressed()

    def entropy(self):
        return str(self._entropy) \
            if self._entropy else None

    def mnemonic(self):
        return str(self._mnemonic) \
            if self._mnemonic else None

    def passphrase(self):
        return str(self._passphrase) \
            if self._passphrase else None

    def language(self):
        return str(self._language) \
            if self._language else None

    def seed(self):
        return hexlify(self._seed).decode() \
            if self._seed else None

    def path(self):
        return self._path \
            if not self._path == "m" else None

    def chain_code(self):
        return hexlify(self.chain).decode() if self.chain else None

    def identifier(self, private_key):
        return hashlib.new("ripemd160", sha256(
            unhexlify(self.public_key(private_key))).digest()).digest()

    def finger_print(self):
        return hexlify(self.identifier(
            self.private_key())[:4]).decode()

    def address(self):
        keccak_256 = sha3.keccak_256()
        keccak_256.update(self.verified_key.to_string())
        address = keccak_256.hexdigest()[24:]
        return checksum_encode(address)

    def wallet_import_format(self):
        raw = b"\x80" + self.key.to_string() + b"\x01"
        return check_encode(raw)

    def extended_key(self, private_key=True, encoded=True):
        version = EXTEND_MAIN_PRIVATE[0] \
            if private_key else EXTEND_MAIN_PUBLIC[0]
        depth = bytes(bytearray([self.depth]))
        parent_fingerprint = self.parent_fingerprint
        child = struct.pack(">L", self.index)
        chain = self.chain

        data = b"\x00" + unhexlify(self.private_key()) \
            if private_key else unhexlify(self.public_key())
        try:
            raw = (version + depth +
                   parent_fingerprint + child + chain + data)
            if encoded:
                return check_encode(raw)
            else:
                return raw.hex()
        except TypeError:
            return None

    def dumps(self):
        return dict(
            entropy=self.entropy(),
            mnemonic=self.mnemonic(),
            language=self.language(),
            passphrase=self.passphrase(),
            seed=self.seed(),
            root_private_key=self.root_private_key(),
            root_public_key=self.root_public_key(),
            uncompressed=self.uncompressed(),
            compressed=self.compressed(),
            chain_code=self.chain_code(),
            private_key=self.private_key(),
            public_key=self.public_key(),
            wif=self.wallet_import_format(),
            finger_print=self.finger_print(),
            path=self.path(),
            address=self.address(),
            serialized=dict(
                private_key_hex=self.extended_key(private_key=True, encoded=False),
                public_key_hex=self.extended_key(private_key=False, encoded=False),
                private_key_base58=self.extended_key(private_key=True, encoded=True),
                public_key_base58=self.extended_key(private_key=False, encoded=True),
            )
        )
