#!/usr/bin/env python3

from eth_wallet import Wallet

# 12 word seeds
MNEMONIC = "indicate warm sock mistake code spot acid ribbon sing over taxi toast"

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from mnemonic
wallet.from_mnemonic(mnemonic=MNEMONIC)

# Derivation from path
# wallet.from_path("m/44'/60'/0'/0/0")
# Derivation from index
wallet.from_index(44, harden=True)
wallet.from_index(60, harden=True)
wallet.from_index(0, harden=True)
wallet.from_index(0)
wallet.from_index(0, harden=True)

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
print("BIP32 Derivation Path:", wallet.path())
# Get Address
print("Address:", wallet.address())

# #### Serialized #####

# Get Private Key Hex
print("BIP32 Extended Private Key Encoded:",
      wallet.extended_key(private_key=True, encoded=False))
# Get Public Key Hex
print("BIP32 Extended Public Key Encoded:",
      wallet.extended_key(private_key=False, encoded=False))
# Get XPrivate Key Base58
print("BIP32 Extended Private Key:",
      wallet.extended_key(private_key=True, encoded=True))
# Get XPublic Key Base58
print("BIP32 Extended Public Key:",
      wallet.extended_key(private_key=False, encoded=True))
