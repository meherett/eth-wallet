#!/usr/bin/env python3

from eth_wallet import Wallet

import json

# Ethereum wallet private key
PRIVATE_KEY = "b9d3f312b38951361597219c8979e177d99349fd0213bac55508c8469d02064f"

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from private key
wallet.from_private_key(private_key=PRIVATE_KEY)

# Print all wallet information's
# print(json.dumps(wallet.dumps(), indent=4))

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
# Get Address
print("Address:", wallet.address())
