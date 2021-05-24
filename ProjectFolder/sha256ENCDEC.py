"""ask user to input a password user-passwordwith the format “uuudddd",
 where ‘u’ denotes upper-case letter and ‘d’ denotes a digit from 0-9;
 and output the hash value of SHA256(user-password) in hexadecimal form (1 pt)"""

import hashlib


def encrypt_string(userPassword):
    return hashlib.sha256(
        userPassword.encode()).hexdigest()


def decrypt_string(hash_from_encrypt):
    big_characters = 'ABCDEFGHIJKLMNOPQRSTUVQXYZ'
    numbers = '123456789'
    for u1 in big_characters:
        for u2 in big_characters:
            for u3 in big_characters:
                for d1 in numbers:
                    for d2 in numbers:
                        for d3 in numbers:
                            for d4 in numbers:
                                plainText = (u1 + u2 + u3 + d1 + d2 + d3 + d4)
                                plainTextToHash = encrypt_string(plainText)
                                if plainTextToHash == hash_from_encrypt:
                                    return "Your hash is " + plainTextToHash + " and the plaintext was " + plainText


hash_string = input("Input your string, and i will convert to hash \non the form SHA256 "
                    "please write\non the form: uuudddd: ")

# remove the hashtag under this statement to print out task 2B 1
# print(encrypt_string(hash_string))

# Remove the hashtag under this statement to print out task 2B 2
print(decrypt_string(encrypt_string(hash_string)))

