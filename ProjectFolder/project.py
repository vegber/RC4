import ConvertTextToBinary
from hashlib import sha256

class RC4:

    def __init__(self, P=187, g=2, S=32, privB=27):
        # Define constants
        self.sharedPrime = P
        self.generator = g
        self.BobsPrivKey = privB
        self.sharedSecret = self.hash_gen(S)  # hardCoded for now
        self.S = self.key_gen(self.sharedSecret)

    @staticmethod
    def hash_gen(some_number):
        return sha256(str(some_number).encode()).digest()

    def key_gen(self, key):
        key_length = len(key)
        S = list(range(256))
        j = 0

        for i in range(256):
            j = (j + S[i] + key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def pseudo_random_stream(self, n):
        S = self.S.copy()  # Make a copy to prevent mutation
        i = 0
        j = 0
        key = bytearray(n)
        for l in range(n):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            key[l] = S[(S[i] + S[j]) % 256]
        return key

    @staticmethod
    def xor(plaintext, keystream):
        size = len(plaintext)
        result = bytearray(size)
        for k in range(size):
            result[k] = keystream[k] ^ plaintext[k]
        return result

    def encrypt(self, plaintext):
        keystream = self.pseudo_random_stream(len(plaintext))
        return self.xor(plaintext, keystream)

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)  # RC4 encryption and decryption are the same operation

    def calculate_bobs_pub_key(self):
        return (self.generator ** self.BobsPrivKey) % self.sharedPrime

    def key_generator(self, PublicKeyAlice):
        return (PublicKeyAlice ** self.BobsPrivKey) % self.sharedPrime

# Utility functions
def write_to_file(filename, content, mode="w+"):
    with open(filename, mode) as file:
        file.write(content)

def main():
    rc4 = RC4()

    # Encrypt
    plaintext = ConvertTextToBinary.EncryptStep("plaintext.txt")
    ciphertext = rc4.encrypt(plaintext)
    write_to_file('Ciphertext.txt', ciphertext.hex())

    # Decrypt
    decrypted = rc4.decrypt(ciphertext)
    write_to_file('DecryptedIndex.html', decrypted.decode())

if __name__ == "__main__":
    main()
