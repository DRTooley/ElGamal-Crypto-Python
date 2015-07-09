
import KeyGeneration
import Encryption
import Decryption

"""
This is the main ElGamal run file where individual tests are run. Firs the public and private keys are created and then
stored into their respective files. The message variable is the message that you would like to be encrypted and then
subsequently decrypted. For these runs the Public Key is saved to the file 'K1', the Private Key is saved to the file
'K2', the encryption function writes the r and t value pairs to the file named 'Cipher'. The Cipher file is read by the
decryption function and then decrypted to find the original message which is then saved to the file 'Plaintext'.
"""

if __name__ == '__main__':
    #PublicKey is a vector of length 3 that has the values of p, g, h
    #PrivateKey is a vector of length 3 that has the values of p, g, x
    print("Generating Keys...")
    PublicKey, PrivateKey = KeyGeneration.KeyGenerator(200, 100)

    publicFile = open("K1", 'w')  # Opening file to write the public key to
    PublicFileText = str(PublicKey[0]) + '\n' + str(PublicKey[1]) + '\n' + str(PublicKey[2])  # The text value that is to be written into the public key file
    publicFile.write(PublicFileText)  # Write public key into file
    publicFile.close()

    privateFile = open("K2", 'w')  # Opening file to write the private key to
    PrivateFileText = str(PrivateKey[0]) + '\n' + str(PrivateKey[1]) + '\n' + str(PrivateKey[2])  # the text that is to be written into the private key file
    privateFile.write(PrivateFileText)  # Write private key into file
    privateFile.close()

    # message is the message the user wants to have encrypted and then subsequently decrypted
    message = "You can trust some of the people all of the time. You can trust all of the people some of the time. But you can't trust all of the people all of the time."
    print("Encrypting Message: ", message)
    # Begin the Encryption process
    Encryption.Encrypt(message)

    print("Decrypting message...")
    # Begin the Decryption Process
    Decryption.Decrypt()

    print("Finished!")






