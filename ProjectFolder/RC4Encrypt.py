import ConvertTextToBinary
from client import hashGen

"""
This is a RC4 encryption program. 
Author: Vegard Berge 
"""

"""
NOTE: 
This program will take index.html and encrypt it by rc4. 
The output of this conversion vil be in hexa and is outputted in 
CipherText.txt 
After you "Run" this program, you should get a hex string. 
This string can be decrypted by running RC4Decrypt. The output 
of that program wil be placed in DecryptedIndex.html

"""


def keyGen(key):
    key_length = len(key)  # finner lengden av hash
    S = list(range(256))  # lage liste på 256
    j = 0  # lager tom variabel

    for i in range(256):  # iterer over lkjasda sdfj
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
sharedSecret = hashGen(32)  # # This is "hardCoded" becuase i lack the time to make it connected to server/client

plaintext = ConvertTextToBinary.EncryptStep()  # Henter text fra ConvertTextToBinary (altså index.html)

BinaryLength = len(plaintext)  # Finner lengda til plaintext


def Xor(plaintext, keystream):
    size = len(plaintext)
    result = bytearray(size)
    for k in range(0, size):
        result[k] = keystream[k] ^ plaintext[k]
        # print(result)
    return result


S = keyGen(sharedSecret)  # lagre resultat frå keygen i variabel S

keystream = PseudoRandomStream(S, BinaryLength)

ciphertext = Xor(plaintext, keystream)

"""
Denne delen opnar Ciphertext og leser den.
"""

outfile = open('Ciphertext.txt', 'w+')
outfile.write(ciphertext.hex())

outfile.close()  # lukker fil
