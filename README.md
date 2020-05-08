# eth-wallet

[![Build Status](https://travis-ci.org/meherett/eth-wallet.svg?branch=master)](https://travis-ci.org/meherett/eth-wallet)
[![PyPI Version](https://img.shields.io/pypi/v/eth-wallet.svg?color=blue)](https://pypi.org/project/eth-wallet)
[![Coverage Status](https://coveralls.io/repos/github/meherett/eth-wallet/badge.svg?branch=master)](https://coveralls.io/github/meherett/eth-wallet?branch=master)

The implementation of Hierarchical Deterministic (HD) wallets generator for Ethereum protocol.

### Installation

```
$ pip install eth-wallet
```

Or clone it locally, and run:

```
$ pip install -e .[tests] -r requirements.txt
```

### Quick Usage

```python
#!/usr/bin/env python3

from eth_wallet import Wallet
from eth_wallet.utils import generate_entropy

import json

# 128 strength entropy
ENTROPY = generate_entropy(strength=128)
# Secret passphrase
PASSPHRASE = None  # str("meherett")
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese & korean
LANGUAGE = "italian"  # default is english

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from entropy
wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)

# Derivation from path
# wallet.from_path("m/44'/60'/0'/0/0'")
# Or derivation from index
wallet.from_index(44, harden=True)
wallet.from_index(60, harden=True)
wallet.from_index(0, harden=True)
wallet.from_index(0)
wallet.from_index(0, harden=True)

# Print all wallet information's
print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))
```

<details>
  <summary>Output</summary><br/>

```json5
{
    "entropy": "dd1bd1610ad21cc7378b33a2fb0780ba",
    "mnemonic": "stizzoso succoso fuggente austria buca icona stufo impiego planare spedire svedese luppolo",
    "language": "italian",
    "passphrase": null,
    "seed": "030cfa72163e50ab30b7b777a740cf9b81132db32dbe5586db300929d44883c600cfbba441e91b7acbf43d2efa743e6e28eef6af8da5313a4cc2efc702471697",
    "root_private_key": "ca1b05291e99e4f8a4dbd1c694b983a5f37c90737481ac0357492a2d7fb6c4a62546aad67bc9e963d659c49114f64cdb56b9ff69800daa4c6add97665613b697",
    "root_public_key": "64fb2d43d9b3cebe7833ef08b642e135642f67aced2afcb9bf2a2f2e0d089ddbca8f5daf77fa501bb5b046f1c2e1399b72a5fb53d10baa8701deee2200da81c0",
    "uncompressed": "711c954c41932b8ee6743d3370e1457be654c2a3e9ad2fb73edb36c5ec40fa299a0b3cf5e44c985097dfcd0bd0051781262a6cb7997c5b8c5aed1b9be8765d05",
    "compressed": "03711c954c41932b8ee6743d3370e1457be654c2a3e9ad2fb73edb36c5ec40fa29",
    "chain_code": "bc93dd52faeed3c7f254dabb87f8d6f021f1ea7eaf2819769799cc473314f031",
    "private_key": "7a5c1e516c339b88e3b37209cbaada31bc6dde3eef5590b6cab952be13722671",
    "public_key": "03711c954c41932b8ee6743d3370e1457be654c2a3e9ad2fb73edb36c5ec40fa29",
    "wif": "L1KZaDq2uRkYrX1f9aLLn5MCwrp5FNjyGAUkXz3detCet2PbfCmL",
    "finger_print": "619eed36",
    "path": "m/44'/60'/0'/0/0'",
    "address": "0x093e9Fc7e162B097bAea14a4a63B0F3D35530494",
    "serialized": {
        "private_key_hex": "0488ade405afd9d7d180000000bc93dd52faeed3c7f254dabb87f8d6f021f1ea7eaf2819769799cc473314f031007a5c1e516c339b88e3b37209cbaada31bc6dde3eef5590b6cab952be13722671",
        "public_key_hex": "0488b21e05afd9d7d180000000bc93dd52faeed3c7f254dabb87f8d6f021f1ea7eaf2819769799cc473314f03103711c954c41932b8ee6743d3370e1457be654c2a3e9ad2fb73edb36c5ec40fa29",
        "private_key_base58": "xprvA3iex88bZnGj3xL5FLCGRxDER6zU7opAcpBmeaSghX3HW5fTwM1iGVenooA91TvwiWDaztbVQKGVJDQuaeoJyW7agqzJpoTyg7jYkokvTet",
        "public_key_base58": "xpub6Gi1MdfVQ9q2GSQYMMjGo69xy8pxXGY1z37NSxrJFraGNszcUtKxpHyGf64aPrRhtRsumxod1ygu2xmSkSFby1VSaAohJseCsEss4mWutYi"
    }
}
```
</details>

ganache-cli/testrpc wallet

```python
#!/usr/bin/env python3

from eth_wallet import Wallet
from eth_wallet.utils import generate_mnemonic

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from entropy
wallet.from_mnemonic(mnemonic=generate_mnemonic(language="spanish"), passphrase=None)

print("Mnemonic:", wallet.mnemonic())
print("Base HD Path:  m/44'/60'/0'/0/{account_index}", "\n")

# Get wallet information's from account index
for account_index in range(10):
    # Derivation from path
    wallet.from_path(f"m/44'/60'/0'/0/{account_index}")
    # Print account_index, address and private_key like ganache-cli/testrpc
    print(f"({account_index}) {wallet.address()} 0x{wallet.private_key()}")
    # Clean derivation
    wallet.clean_derivation()
```

<details>
  <summary>Output</summary><br/>

```shell script
Mnemonic: barro fresa ocre glaciar peldaño juzgar líquido fuente fatiga empate revés careta
Base HD Path:  m/44'/60'/0'/0/{account_index} 

(0) 0x7E323A9081B3dF1883DDc41C2104Ff1294721131 0xa1d9d231285a47de647664ee85628d26a59d78f6a386a25b0e203a98a3119ba1
(1) 0x7D62e231Cc747f92b8E759e4d55907B3cA288cC5 0x9d23fd86d51c64aa6c9fa78ec0d54bb95189ad20514615f43576d64dc5df6a08
(2) 0x339887398877CE42f9a01849F6a30021969B9833 0x8e788633678a171f766efcb365a4673861909a59fb6096e2bbc135a9f8de0fee
(3) 0x264a8E2A745af7548d0052f9e16C61F0D900c0E4 0x99085cf6e11b87231368e411a92d1f7215b54dfb775615135fe9ced38e1b0a2e
(4) 0xC2806f4A4055417C816Ae417ffD2Ba1beb0751fc 0xea9feb763c3f494e9664b7548c58c85a307aaf7f5862f79a78f90707e4936451
(5) 0x01Ed66b394b9c177E7E4fBbD698bedDc639C5B31 0xf544dba64b769086b1987fb642a2f09793e869b304979c033f3c90284c7384fc
(6) 0xF483edE8f1d8243Bb74931f15e89Fd0Bb040D18E 0xc47fcc8c526b48c541d414f52907e0c5b6a1e96bed9625de88b203213c3ebde6
(7) 0xf7de9d4b01E21AfF7509420D4C3eC9A14f280511 0x87c4d50bf10f0fa7729c632056b41ecd3b3b4f203f675ff9094e4de12aff3fd8
(8) 0xb4c74eC460be14B18865C0b2eddD1F63B4cBCF03 0xab1976c54014f65c28c9976c9f2d6c71d9c848ea9620927c162e12fa8d5686e3
(9) 0x095d5E698407b67270d24589CF0Af5458Ca783b0 0x24ff1176fd9c18c1a36efb6c15474567ffe2d71251876739fe787395092cd895
```
</details>

[Click this to see more examples](https://github.com/meherett/eth-wallet/blob/master/examples).

### Testing

You can run the tests with:

```
$ pytest
```

Or use `tox` to run the complete suite against the full set of build targets, or pytest to run specific 
tests against a specific version of Python.

### License

Distributed under the [GPL-3.0](https://github.com/meherett/eth-wallet/blob/master/LICENSE) license. See ``LICENSE`` for more information.
