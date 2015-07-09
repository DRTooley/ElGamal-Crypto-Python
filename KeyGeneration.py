__author__ = 'David'

import PrimeNumber as PN
import ModularExponentiation as ME
import random
"""
KeyGeneration is a function that will take in an int value for n, which is the number of bits that the prime will be,
and for t and these will be passed on to the primeFinder function. primeFinder returns variable p, which is an n bit prime
number and g, which is a primitive root of p. Then x is found where x is a random integer value 1 <= x <= p-1
"""
def KeyGenerator(n=200, t=100):
    p, g = PN.primeFinder(n, t)  # Find prime, p, and primitive root, g.
    x = random.randint(1, p-1)  # a random integer value 1 <= x <= p-1
    h = ME.modExp(g, x, p)  # Calculates g^x mod p
    PublicKey = [p, g, h]  # Sets the public key to [n bit prime, primitive root of n bit prime, g^x mod p]
    PrivateKey = [p, g, x]  # Sets the private key to [n bit prime, primitive root of n bit prime, random integer value 1 <= x <= p-1]
    return PublicKey, PrivateKey