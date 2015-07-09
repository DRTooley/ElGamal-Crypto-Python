__author__ = 'David'
import ModularExponentiation

"""
Decrpy assumes that there are two files in the same folder.
K2 is the private key
Cipher is the cipher text to be decrypted using the private key found in K2
"""


def Decrypt():
    PrivateKeyFile = open('K2', 'r')  # opens the private key

    prime = int(PrivateKeyFile.readline())  # reads in the prime number
    PrimitiveRoot = int(PrivateKeyFile.readline())
    x = int(PrivateKeyFile.readline())  # The random number value 1 <= x <= p-1 used to calculate h in the public key

    PrivateKeyFile.close()

    CiphertextFile = open('Cipher', 'r')
    text = []  # vector to hold each character as the ascii value is calculated from Cipher
    for line in CiphertextFile:  # line is a variable holding one line of the Cipher, this will be a string that contains two numbers, r and t, separated by a single space
        rt = line.split()  # splits the line by white space. storing all strings of consecutive characters in the vector rt

        r = int(rt[0])  # the first value in rt is the encryption r value
        t = int(rt[1])  # the second value in rt is the encryption t value
        s = ModularExponentiation.modExp(r, x, prime)  # calculates r^x mod prime
        letter = ModularExponentiation.modExp(s, prime-2, prime) * t % prime  # calculates (s^(prime-2) mod prime) * t mod prime, this will result in the original ascii value for the encrypted character
        text.append(letter)  # add the decrypted ascii value to the vector

    CiphertextFile.close()
    plaintext = ''  # The values in text will be converted from ascii to character and concatenated into this string
    for letter in text:  # for each ascii value in the text vector
        plaintext += chr(letter)  # convert to char and concat to the plaintext string

    PlaintextFile = open('Plaintext', 'w')  # open file named 'Plaintext' for writing
    PlaintextFile.write(plaintext)  # write the decrypted message to the file
    PlaintextFile.close()


