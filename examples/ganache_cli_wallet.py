#!/usr/bin/env python3

from eth_wallet import Wallet
from eth_wallet.utils import generate_entropy

# 128 strength entropy
ENTROPY = generate_entropy(strength=128)
# Secret passphrase
PASSPHRASE = None  # str("meherett")
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese & korean
LANGUAGE = "japanese"  # default is english

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from entropy
wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)

print("Mnemonic:", wallet.mnemonic())
print("Base HD Path:  m/44'/60'/0'/0/{account_index}", "\n")

# Get wallet information's from account index
for account_index in range(10):
    # Derivation from path
    # wallet.from_path(f"m/44'/60'/0'/0/{account_index}")
    # Derivation from index
    wallet.from_index(44, harden=True)
    wallet.from_index(60, harden=True)
    wallet.from_index(0, harden=True)
    wallet.from_index(0)
    wallet.from_index(account_index)
    # Print account_index, address and private_key like ganache-cli/testrpc
    print(f"({account_index}) {wallet.path()} {wallet.address()} 0x{wallet.private_key()}")
    # Clean derivation
    wallet.clean_derivation()
