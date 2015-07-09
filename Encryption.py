__author__ = 'David'
import random
import ModularExponentiation

"""
Encrypt takes a string message and encrypts the message using the public key given in the file 'K1'
Assumes K1 is a valid file

In this function I treated each character in the message as it's ascii value when using the encryption function
"""

def Encrypt(message):
    PublicKeyFile = open('K1', 'r')

    prime = int(PublicKeyFile.readline())  # the prime number
    PrimitiveRoot = int(PublicKeyFile.readline())  # the primitve root of the prime
    h = int(PublicKeyFile.readline())  # PrimitiveRoot^x mod prime    Where x is the random number in the private key

    PublicKeyFile.close()

    CiphertextFile = open('Cipher', 'w')
    for character in message:  # for every ascii character that is in the string message
        k = random.randint(0, prime-1)  # Find a random number, k, where 0 <= k <= p-1
        r = ModularExponentiation.modExp(PrimitiveRoot, k, prime)  # Compute r, where r = PrimitiveRoot^k mod prime
        t = ModularExponentiation.modExp(h, k, prime)*ord(character) % prime  # Compute t, where t = (h^k mod prime) * [ascii value of character] mod prime
        CiphertextFile.write(str(r)+' '+str(t)+'\n')  # writes these values to the file named 'Cipher'

    CiphertextFile.close()




