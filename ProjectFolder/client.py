from hashlib import sha256

sharedPrime = 187
generator = 2
BobsPrivKey = 27


# This function calculates Bob´s public key
def CalculateBobsPubKey():
    return (generator ** BobsPrivKey) % sharedPrime


# This keyGenerator takes Alice´s shared public key as input
# Notice that this Kab is the same as Alice´s keyGen
def Keygenerator(PublicKeyAlice):
    return (PublicKeyAlice ** BobsPrivKey) % sharedPrime


# This generates a hash to the RC4 system
def hashGen(TheirsharedKey):
    return sha256(str(TheirsharedKey).encode()).digest()


def HashgeneratorForSharedSecret(SharedSecret):
    return sha256(str(SharedSecret).encode()).hexdigest()


def hashGenerator(someNumber):
    return sha256(someNumber.encode()).hexdigest()


def decrypter(hash):
    numbers = '123456789'
    for first in numbers:
        for second in numbers:
            plaintext = first + second
            plainTextToHash = hashGenerator(plaintext)
            if plainTextToHash == hash:
                return plaintext
