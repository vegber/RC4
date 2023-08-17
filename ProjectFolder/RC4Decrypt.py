import ConvertTextToBinary
from client import hashGen

"""
This is a RC4 Decryption program.
Author: Vegard Berge 


This program wil take the hexadecimal encryption you just made from RC4Encryption.py 
and convert it back to the original size and format

"""


def keyGen(key):
    key_length = len(key)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PseudoRandomStream(S, n):
    i = 0
    j = 0
    #    key = []
    key = bytearray(n)
    for l in range(0, n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key[l] = S[(S[i] + S[j]) % 256]

    return key


# this is the "key"
sharedSecret = hashGen(32)  # This is "hardCoded" becuase i lack the time to make it connected to server/client

plaintext = ConvertTextToBinary.DecryptStep("Ciphertext.txt")

BinaryLength = len(plaintext)


def Xor(plaintext, keystream):
    size = len(plaintext)
    result = bytearray(size)
    for k in range(0, size):
        result[k] = keystream[k] ^ plaintext[k]
        # print(result)
    return result


S = keyGen(sharedSecret)

keystream = PseudoRandomStream(S, BinaryLength)

ciffertext = Xor(plaintext, keystream)
# print(ciffertext)

"""
Denne delen skrive ut resultat til DecryptedIndex.html as W+. 
dvs at dersom brukar ikkje har dokument oppretta vil python 
lage den for deg. 
"""
outfile = open('DecryptedIndex.html', 'w+')
outfile.write(ciffertext.decode())  # dekode text
outfile.close()  # lukker fil
