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
$ pip install -e . -r requirements.txt
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
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional & korean
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
