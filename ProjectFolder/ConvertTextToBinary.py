def EncryptStep():
    f = open('plaintext.txt', 'r')
    file = f.read().encode()
    return file


def DecryptStep():
    f = open('Ciphertext.txt', 'r')
    file = f.read()
    x = bytes.fromhex(file)
    return x


