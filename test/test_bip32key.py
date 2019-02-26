from bip32key import BIP32KEY, BIP32KEY_HARDEN
import binascii


entropy = binascii.hexlify(b"Meheret Tesfaye Batu")
# fromEntropy
master_key = BIP32KEY.fromEntropy(entropy=entropy)


# Testing fromPath and fromIndex are equaled.
def test_fromPath_and_fromIndex():
    # fromPath
    master_key_path = master_key.fromPath("m/44'/623'/1'/88/934")

    # fromIndex
    master_key_index = master_key.fromIndex(44 + BIP32KEY_HARDEN)
    master_key_index = master_key_index.fromIndex(623 + BIP32KEY_HARDEN)
    master_key_index = master_key_index.fromIndex(1 + BIP32KEY_HARDEN)
    master_key_index = master_key_index.fromIndex(88)
    master_key_index = master_key_index.fromIndex(934)

    assert master_key_path.address() == master_key_index.address()

    assert master_key_path.walletImportFormat() == master_key_index.walletImportFormat()

    assert master_key_path.chainCode() == master_key_index.chainCode()

    assert master_key_path.privateKey() == master_key_index.privateKey()

    assert len(master_key_path.privateKey().hex()) == 64

    assert master_key_path.publicKey() == master_key_index.publicKey()
