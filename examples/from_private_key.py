#!/usr/bin/env python3

from eth_wallet import Wallet

import json

# Ethereum wallet private key
PRIVATE_KEY = "656905e908b7349a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e"

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from private key
wallet.from_private_key(private_key=PRIVATE_KEY)

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
