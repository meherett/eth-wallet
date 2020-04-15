# eth-wallet

[![Build Status](https://travis-ci.org/meherett/eth-wallet.svg?branch=master)](https://travis-ci.org/meherett/eth-wallet)
![PyPI Version](https://img.shields.io/pypi/v/eth-wallet.svg?color=blue)
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
print(json.dumps(wallet.dumps(), indent=4))
```

<details>
  <summary>Output</summary><br/>

```json5
{
    "entropy": "8d7454bb99e8e68de6adfc5519cbee64",
    "mnemonic": "occasione pizzico coltivato cremoso odorare epilogo patacca salone fonia sfuso vispo selettivo",
    "language": "italian",
    "passphrase": null,
    "seed": "a0f734f68f800f1f43719473fbdcdb64b83a3d180add1d6f819ccbf5abbcb852c791d7e8249a62e1bbda60322de7ce0d0f3d5649e368431d058bbe6879ad2cd6",
    "private_key": "6fc58f27cec4b943e8a1f53bf7d54ecb0a22bd01c21e7d383870e99531b2ba24",
    "public_key": "024de8f3421dc1138c1d1ccd9bfe22d727d7639475eb852c54cc8b3fddd9c5e9e6",
    "uncompressed": "4de8f3421dc1138c1d1ccd9bfe22d727d7639475eb852c54cc8b3fddd9c5e9e66c153cd99d81f9db5985e5ba0ba4ca49d51086c8c89a7fdbc568c394fcfdfb3e",
    "wif": "KzxypdAu6Fyr4bu6KbBeWCARqSVsoUiQsi75LxwvHFU3Fq2QXeqy",
    "finger_print": "bc7c2a20",
    "chain_code": "c05e2d9fbbba549d39fb114a2501099912873c94c388d68b4623730e3c73b855",
    "path": "m/44'/60'/0'/0/0'",
    "address": "0x89f64dFE79777217BD16a278EE675DaE9c089729",
    "serialized": {
        "private_key_hex": "0488ade405c7b5aff680000000c05e2d9fbbba549d39fb114a2501099912873c94c388d68b4623730e3c73b855006fc58f27cec4b943e8a1f53bf7d54ecb0a22bd01c21e7d383870e99531b2ba24",
        "public_key_hex": "0488b21e05c7b5aff680000000c05e2d9fbbba549d39fb114a2501099912873c94c388d68b4623730e3c73b855006fc58f27cec4b943e8a1f53bf7d54ecb0a22bd01c21e7d383870e99531b2ba24",
        "private_key_base58": "xprvA3tptBgMHUbm7KFeMbPwWmj4DhyqfRHmsrUmBHvQsJgTi8RtiL8NZBVrHtpsmBxJXjzKybyGcidQuFJhjyU5YYF8wvm5gVTL6UcseQiKATz",
        "public_key_base58": "xpub6GtBHhDF7rA4KoL7TcvwsufnmjpL4t1dF5QMygL2ReDSavm3FsSd6ypL95y9rN6twUSKt46CHUNsWgrVddxdJPqJTw5TXpGP2LW7QU7sHju"
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
