#!/usr/bin/env python3

from eth_wallet import Wallet

import json

# Ethereum wallet root private key
ROOT_PRIVATE_KEY = "d41f75ee8b3fd25bb696f1882f0d34a2a9b68dc20ba69b93a1e81b9413aac65100e8e6c" \
                   "ad6815767e839b5b86a954c11662cbcae94e8add8cd837842fd222312"

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from root private key
wallet.from_root_private_key(root_private_key=ROOT_PRIVATE_KEY)

# Derivation from path
# wallet.from_path("m/44'/60'/0'/0/0'")
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
