#!/usr/bin/env python3

from eth_wallet.wallet import Wallet


MNEMONIC = "indicate warm sock mistake code spot acid ribbon sing over taxi toast"
PASSPHRASE = None
LANGUAGE = "english"


def test_from_mnemonic():

    wallet = Wallet()
    wallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)

    wallet.from_index(44, harden=True)
    wallet.from_index(60, harden=True)
    wallet.from_index(0, harden=True)
    wallet.from_index(0)
    wallet.from_index(0, harden=True)

    assert wallet.private_key() == "678d12447649cc9eeede87562069c2ff1524f31df025f521be255d4a6c8eaed0"
    assert wallet.public_key() == "03df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f"
    assert wallet.uncompressed() == "df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f1e4f78a8cae1d" \
                                    "af5dd1a716a96475b16dcfb455e7d97fe75dd8f1f8ea5cc0a41"
    assert wallet.wallet_import_format() == "KzgzzJkyzqcy8bLJDPLwXV5VmJER3f35q9zyAgSdMLn6aqMovQ66"
    assert wallet.finger_print() == "2004e94c"
    assert wallet.chain_code() == "67a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93def287754"
    assert wallet.path() == "m/44'/60'/0'/0/0'"
    assert wallet.address() == "0xAaB4E88BCa0d7C1e40CE540b9642558d6f9a3a05"

    assert wallet.extended_key(private_key=True, encoded=False) == "0488ade405f450d7af8000000067a537696eecbfdd5755" \
                                                                   "734eee16dca622e62bb3c98f66db89cad93def28775400" \
                                                                   "678d12447649cc9eeede87562069c2ff1524f31df025f5" \
                                                                   "21be255d4a6c8eaed0"
    assert wallet.extended_key(private_key=False, encoded=False) == "0488b21e05f450d7af8000000067a537696eecbfdd575" \
                                                                    "5734eee16dca622e62bb3c98f66db89cad93def287754" \
                                                                    "00678d12447649cc9eeede87562069c2ff1524f31df02" \
                                                                    "5f521be255d4a6c8eaed0"
    assert wallet.extended_key(private_key=True, encoded=True) == "xprvA4Dqp8w5LcQejoog9rci7sadBJetitNj1wvbG7uHLLk" \
                                                                  "SxoFhkzVnZ7A8Z6Kz4VRMpFSJ2Kct9KFf8uVpuWiqU9vBrk" \
                                                                  "h9w6dVfThmF4RUxHV"
    assert wallet.extended_key(private_key=False, encoded=True) == "xpub6HDCDeTyAyxwxHt9Ft9iV1XMjLVP8M6aPArC4WJttg" \
                                                                   "HRqbarJXp36uUcQHUG9fZxDytHvmjop517kM3coBDPE1WM" \
                                                                   "Nm1XnRSYbKb117iqsNg"

    assert wallet.dumps() == {
        "entropy": None,
        "mnemonic": "indicate warm sock mistake code spot acid ribbon sing over taxi toast",
        "language": "english",
        "passphrase": None,
        "seed": "baff3e1fe60e1f2a2d840d304acc98d1818140c79354a353b400fb019bfb256bc392d7aa9047adff1f14bce0342e14605"
                "c6743a6c08e02150588375eb2eb7d49", 
        "private_key": "678d12447649cc9eeede87562069c2ff1524f31df025f521be255d4a6c8eaed0",
        "public_key": "03df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f", 
        "uncompressed": "df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f1e4f78a8cae1daf5dd1a716a9"
                        "6475b16dcfb455e7d97fe75dd8f1f8ea5cc0a41",
        "wif": "KzgzzJkyzqcy8bLJDPLwXV5VmJER3f35q9zyAgSdMLn6aqMovQ66",
        "finger_print": "2004e94c",
        "chain_code": "67a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93def287754",
        "path": "m/44'/60'/0'/0/0'",
        "address": "0xAaB4E88BCa0d7C1e40CE540b9642558d6f9a3a05", 
        "serialized": {
            "private_key_hex": "0488ade405f450d7af8000000067a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93d"
                               "ef28775400678d12447649cc9eeede87562069c2ff1524f31df025f521be255d4a6c8eaed0",
            "public_key_hex": "0488b21e05f450d7af8000000067a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93de"
                              "f28775400678d12447649cc9eeede87562069c2ff1524f31df025f521be255d4a6c8eaed0",
            "private_key_base58": "xprvA4Dqp8w5LcQejoog9rci7sadBJetitNj1wvbG7uHLLkSxoFhkzVnZ7A8Z6Kz4VRMpFSJ2Kct9KF"
                                  "f8uVpuWiqU9vBrkh9w6dVfThmF4RUxHV",
            "public_key_base58": "xpub6HDCDeTyAyxwxHt9Ft9iV1XMjLVP8M6aPArC4WJttgHRqbarJXp36uUcQHUG9fZxDytHvmjop517"
                                 "kM3coBDPE1WMNm1XnRSYbKb117iqsNg"}
    }
