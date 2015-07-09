import KeyGeneration
import Encryption
import Decryption

import random
import string

"""
This is the file the I used to test the entire program. It creates 50 random strings of varying lengths ( 1 <= length <= 10000)
and writes these to a file 'TestFile'
Then this file is opened and each line is read, encrypted, decrypted, and then the original line read from
TestFile is compared against the decrypted message stored inside of the file 'Plaintext'
"""


if __name__ == '__main__':
    TestFile = open("TestFile", 'w')
    for j in range(50):
        charInLine = random.randint(1, 10000)
        TestFile.write(''.join(random.choice(string.ascii_letters + string.digits)for i in range(charInLine)) + '\n')
    TestFile.close()
    with open('TestFile') as File:
        for TestLine in File:
            print(TestLine)
            PublicKey, PrivateKey = KeyGeneration.KeyGenerator(200, 100)
            publicFile = open("K1", 'w')
            PublicFileText = str(PublicKey[0]) + '\n' + str(PublicKey[1]) + '\n' + str(PublicKey[2])
            publicFile.write(PublicFileText)

            publicFile.close()
            privateFile = open("K2", 'w')
            PrivateFileText = str(PrivateKey[0]) + '\n' + str(PrivateKey[1]) + '\n' + str(PrivateKey[2])
            privateFile.write(PrivateFileText)
            privateFile.close()
            #message = "You can trust some of the people all of the time. You can trust all of the people some of the time. But you can't trust all of the people all of the time."
            Encryption.Encrypt(TestLine)

            Decryption.Decrypt()

            PlaintextFile = open('Plaintext', 'r')
            FileLine = PlaintextFile.read()
            if(FileLine != TestLine):
                print('Error occured!!')
                print("File Line: ", FileLine, end='')
                print("Test Line: ", TestLine, end='')
                print()
            PlaintextFile.close()

        print('Completed!')


