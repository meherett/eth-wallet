#!/usr/bin/env python3

from eth_wallet import Wallet
from eth_wallet.utils import generate_mnemonic, check_mnemonic

import json

# 12 word mnemonic seed
MNEMONIC = "indicate warm sock mistake code spot acid ribbon sing over taxi toast"
# Or generate mnemonic
# MNEMONIC = generate_mnemonic(language="korean", strength=128)
# Secret passphrase
PASSPHRASE = None  # str("meherett")
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional & korean
LANGUAGE = "english"  # default is english

# Checking 12 word mnemonic seed
assert check_mnemonic(mnemonic=MNEMONIC, language=LANGUAGE), \
      "Invalid %s 12 word mnemonic seed." % LANGUAGE

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from mnemonic
wallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)

# Derivation from path
# wallet.from_path("m/44'/60'/0'/0/0")
# Derivation from index
wallet.from_index(44, harden=True)
wallet.from_index(60, harden=True)
wallet.from_index(0, harden=True)
wallet.from_index(0)
wallet.from_index(0, harden=True)

# Print all wallet information's
print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))

print("Entropy:", wallet.entropy())
print("Mnemonic:", wallet.mnemonic())
print("Language:", wallet.language())
print("Passphrase:", wallet.passphrase())
print("Seed:", wallet.seed())
print("Root Private Key:", wallet.root_private_key())
print("Root Public Key:", wallet.root_public_key())
print("Uncompressed:", wallet.uncompressed())
print("Compressed:", wallet.compressed())
print("Chain Code:", wallet.chain_code())
print("Private Key:", wallet.private_key())
print("Public Key:", wallet.public_key())
print("Wallet Import Format:", wallet.wallet_import_format())
print("Finger Print:", wallet.finger_print())
print("Path:", wallet.path())
print("Address:", wallet.address())

print("---- Serialized ----")

print("Private Key Hex:", wallet.extended_key(private_key=True, encoded=False))
print("Public Key Hex:", wallet.extended_key(private_key=False, encoded=False))
print("Private Key Base58:", wallet.extended_key(private_key=True, encoded=True))
print("Public Key Base58:", wallet.extended_key(private_key=False, encoded=True))
