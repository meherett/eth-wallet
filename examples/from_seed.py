#!/usr/bin/env python3

from eth_wallet import Wallet

import json

# Wallet seed
SEED = "b3337a2fe409afbb257b504e4c09d36b57c32c452b71a0ed413298a5172f727a06bf6605488" \
       "723bc545a4bd51f5cd29a3e8bd1433bd1d26e6bf866ff53d1493f"

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from seed
wallet.from_seed(seed=SEED)

# Derivation from path
# wallet.from_path("m/44'/60'/0'/0/0")
# Derivation from index
wallet.from_index(44, harden=True)
wallet.from_index(60, harden=True)
wallet.from_index(0, harden=True)
wallet.from_index(0)
wallet.from_index(0, harden=True)

# Print all wallet information's
# print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))

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
