__author__ = 'David'

import ModularExponentiation as ME
import random

"""
This module is used to ensure the correctness of the Modular Exponentiation module.
Python has a built in modular exponentiation function so this test is very simple.
The current setting has this testing 10000 random values x, y, n where x^y mod n is calculated
by both the pow function and my modular exponentiation function. If they differ increment the error
counter and alert the tester
"""

if __name__ == '__main__':
    ErrorCount = 0
    for i in range(10000):
        x = random.randint(2, 10000)
        y = random.randint(2, 10000)
        n = random.randint(1000, 20000)
        powVale = pow(x, y, n)
        ModExpVal = ME.modExp(x, y, n)
        if(ModExpVal != powVale):
            print('Error! PowVal = ', powVale, 'ModExpVal = ', ModExpVal)
            ErrorCount += 1
    print(ErrorCount)