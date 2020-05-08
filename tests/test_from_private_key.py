#!/usr/bin/env python3

from eth_wallet.wallet import Wallet


PRIVATE_KEY = "656905e908b7349a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e"


def test_from_private_key():

    wallet = Wallet()
    wallet.from_private_key(private_key=PRIVATE_KEY)

    assert wallet.entropy() is None
    assert wallet.mnemonic() is None
    assert wallet.language() is None
    assert wallet.passphrase() is None
    assert wallet.seed() is None
    assert wallet.private_key() == "656905e908b7349a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e"
    assert wallet.public_key() == "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf"
    assert wallet.uncompressed() == \
        "d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf621eb61a050b753b6fb775e4a319aa15682df03d3" \
        "93ac3dc798c03f68a977355"
    assert wallet.compressed() == "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf"
    assert wallet.wallet_import_format() == "Kzcqd9d9jTzbeh7bNSjGkqQhNNFXnPT7gWopsLSuYbP3MEUAwwJC"
    assert wallet.finger_print() == "f91947eb"
    assert wallet.chain_code() is None
    assert wallet.path() is None
    assert wallet.address() == "0x9A610e8A2B40d010C9804451742233E182052851"

    assert wallet.extended_key(private_key=True, encoded=False) is None
    assert wallet.extended_key(private_key=False, encoded=False) is None
    assert wallet.extended_key(private_key=True, encoded=True) is None
    assert wallet.extended_key(private_key=False, encoded=True) is None

    assert wallet.dumps() == {
        "entropy": None,
        "mnemonic": None,
        "language": None,
        "passphrase": None,
        "seed": None,
        "root_private_key": None,
        "root_public_key": None,
        "uncompressed": "d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf621eb61a050b753b6fb775e4a319aa15682df03d393ac3dc798c03f68a977355",
        "compressed": "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf",
        "chain_code": None,
        "private_key": "656905e908b7349a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e",
        "public_key": "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf",
        "wif": "Kzcqd9d9jTzbeh7bNSjGkqQhNNFXnPT7gWopsLSuYbP3MEUAwwJC",
        "finger_print": "f91947eb",
        "path": None,
        "address": "0x9A610e8A2B40d010C9804451742233E182052851",
        "serialized": {
            "private_key_hex": None,
            "public_key_hex": None,
            "private_key_base58": None,
            "public_key_base58": None
        }
    }

    assert wallet.clean_derivation()
    assert wallet.path() is None
