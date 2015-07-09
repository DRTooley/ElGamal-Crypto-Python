
import random
import ModularExponentiation

"""
primeFiner takes integer values n and t
n is the number of bits the desired prime number contains
t//2 (integer division so odd numbers are handled and simply truncated)  is the number of times to run the isComposite function
"""


def primeFinder(n, t):
    while True:  # until a prime is found
        p = random.randrange((2**n)+1, 2**(n+1), 2)  # select a random odd integer that is n bits long
        if millerRabinPrimalityTest(p, t):  # If the prime, p passes the primality test for t/2 iterations
            if millerRabinPrimalityTest(2*p+1, t):  # testing 2*p +1 for primality to give a higher probability that p is prime
                g = primitiveRoot(p)  # if both tests pass we must find a primitive root for the prime number, retuend into g
                return p, g  # p is the prime number, g is a primitive root of that prime number

"""
primitveRoot(p) finds a primitive root of the (assumed to be) prime number, p
"""


def primitiveRoot(p):
    while True:  # until a primitive root is found
        g = random.randint(2, p-1)  # take a random integer value 2 <= g <= p-1
        if ModularExponentiation.modExp(g, p-1, p) == 1:  # Test to see if g is a primitive root
            return g  # if it is a primitive root, return g

"""
isComposite tests to see if a number, n, is composite
a is a random integer 1 < a < n
k and m come from the equation (2^k)*m = n-1
many different a's should be tested to ensure a higher probability that n is in fact prime
"""


def isComposite(a, k, m, n):
        if ModularExponentiation.modExp(a, m, n) == 1:  # test to see if a^m mod n == 1, if so n is probably prime
            return False
        for i in range(k):
            # test to see if a^(m*(2^i)) mod n is -1, where 0 <= i < k
            # This covers the a^m mod n == -1 as well as all future increments by the power of 2
            # because a^(m*(2*i)) mod n = (a^m)^(2*i) mod n, where 0 <= i < k
            if ModularExponentiation.modExp(a, 2**i * m, n) == n-1:  # if this result is -1 then it is probably prime
                return False
        return True  # if the result was never -1 after k iterations, this number is composite

"""
millerRabinPrimalityTest
n is the potentially prime number being tested
t is the number of times (divided by two) that n will be tested to see if it's composite
The higher the t value to more likely that when the function returns true (implying the n is prime) that n is in fact prime
"""


def millerRabinPrimalityTest(n, t):

    if n % 2 == 0:  # if n is even it is not prime
        return False

    k = 0  # (2^k)*m = n-1, used to find the power of twos in n-1
    m = n-1  # will eventually hold an odd value m such that (2^k)*m = n-1
    while True:  # until you cannot divide out any more 2's
        q, r = divmod(m, 2)  # function that returns quotient, q, and remainder, r when m/2
        if r == 1:  # if m is odd, r will return as 1, thus the end result has been found and the loop is terminated
            break
        k += 1  # else m was even, increment k representing power of twos in n-1
        m = q  # m is the quotient to be divided on the next iteration of the loop until it is found to be odd
    assert(2**k*m == n-1)  # double checks the assumption behind finding k and m

    for i in range(t//2):  # test the primality t/2 times
        a = random.randrange(2, n)  # choose random integer 1 < a < n
        if isComposite(a, k, m, n):  # check to see if n is composite
            return False

    return True  # the number we found is prime with a very high probability