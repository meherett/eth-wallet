#!/usr/bin/env python3

from eth_wallet import Wallet
from eth_wallet.utils import generate_entropy

import json

# 128 strength entropy
ENTROPY = "50f002376c81c96e430b48f1fe71df57"
# Or generate entropy
# ENTROPY = generate_entropy(strength=128)
# Secret passphrase
PASSPHRASE = None  # str("meherett")
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional & korean
LANGUAGE = "korean"  # default is english

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from entropy
wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)

# Derivation from path
# wallet.from_path("m/44'/60'/0'/0/0'")
# Derivation from index
wallet.from_index(44, harden=True)
wallet.from_index(60, harden=True)
wallet.from_index(0, harden=True)
wallet.from_index(0)
wallet.from_index(0, harden=True)

# Print all wallet information's
# print(json.dumps(wallet.dumps(), indent=4))

# Get Entropy
print("Entropy:", wallet.entropy())
# Get Mnemonic
print("Mnemonic:", wallet.mnemonic())
# Get Language
print("Language:", wallet.language())
# Get Passphrase
print("Passphrase:", wallet.passphrase())
# Get Seed
print("Seed:", wallet.seed())
# Get Private Key
print("Private Key:", wallet.private_key())
# Get Public Key
print("Public Key:", wallet.public_key())
# Get Uncompressed Public Key
print("Uncompressed:", wallet.uncompressed())
# Get Wallet Import Format
print("Wallet Import Format:", wallet.wallet_import_format())
# Get Finger Print
print("Finger Print:", wallet.finger_print())
# Get Chain Code
print("Chain Code:", wallet.chain_code())
# Get Derivation Path
print("Derivation Path:", wallet.path())
# Get Address
print("Address:", wallet.address())

# ---- Serialized ----
print("---- Serialized ----")

# Get Private Key Hex
print("Private Key Hex:",
      wallet.extended_key(private_key=True, encoded=False))
# Get Public Key Hex
print("Public Key Hex:",
      wallet.extended_key(private_key=False, encoded=False))
# Get Private Key Base58
print("Private Key Base58:",
      wallet.extended_key(private_key=True, encoded=True))
# Get XPublic Key Base58
print("Public Key Base58:",
      wallet.extended_key(private_key=False, encoded=True))
