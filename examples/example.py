from bip32key import BIP32KEY, BIP32KEY_HARDEN
import binascii

master_key = BIP32KEY.fromEntropy(binascii.hexlify(b"Meheret Tesfaye Batu"))

master_key = master_key.fromIndex(44 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(60 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(0 + BIP32KEY_HARDEN)
master_key = master_key.fromIndex(0)
master_key = master_key.fromIndex(0)

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