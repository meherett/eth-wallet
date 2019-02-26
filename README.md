<p align="start">		
  <img src="https://raw.githubusercontent.com/meherett/bip32key/master/bip32key.png">		
</p>

# bip32key

*The implementation of Hierarchical Deterministic (HD) wallets generator for Ethereum blockchain*

![GitHub](https://img.shields.io/github/license/meherett/bip32key.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bip32key.svg)

## Installation

Install bip32key

```
pip install bip32key
```

## Usage

##### Import entropy
```
from bip32key import BIP32KEY, BIP32KEY_HARDEN
import binascii

# Import entropy
entropy = binascii.hexlify(b"Meheret Tesfaye Batu")
master_key = BIP32KEY.fromEntropy(entropy)
```

##### Import Path
```
# Added master key path
master_key = master_key.fromPath("m/44'/69'/12'/5/0")
```

##### Or Import Index 
```
# This is same with fromPath
master_key = master_key.fromIndex(44 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(69 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(12 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(5)
master_key = master_key.fromIndex(0)
```

##### Get All
```
# Get All Information
print(master_key.print())

# Get Address
print(master_key.address())
# Get Wallet Import Format
print(master_key.walletImportFormat())
# Get Finger Print
print(master_key.fingerPrint().hex())
# Get Chain Code
print(master_key.chainCode())
# Get Private Key
print(master_key.privateKey().hex())
# Get Public Key
print(master_key.publicKey().hex())

##### Serialized #####

# Get Private Key Hex
print(master_key.extendedKey(private=True, encoded=False).hex())
# Get Public Key Hex
print(master_key.extendedKey(private=False, encoded=False).hex())
# Get XPrivate Key Base58
print(master_key.extendedKey(private=True, encoded=True))
# Get XPublic Key Base58
print(master_key.extendedKey(private=False, encoded=True))
```

## Example

###### Metamask and MyEtherWallet uses this path/index
```
master_key = master_key.fromPath("m/44'/60'/0'/0/0")
```
```
master_key = master_key.fromIndex(44 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(60 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(0 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(0)
master_key = master_key.fromIndex(0)
```

## Author
##### # Meheret Tesfaye [@meherett](http://github.com/meherett).
