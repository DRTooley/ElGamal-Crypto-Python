"""
modExp computes x^y mod N
"""


def modExp(x, y, N):
    # squaredValues stores all of the necessary powers that could be needed to calulate the final result. The starting
    # values are 0 (because X^0 = 1) and x % N (incase x >= N)
    squaredValues = [1, (x % N)]
    # currentPower is used as a loop counter of sorts, which keeps track of the current power of x^y mod N that is being
    # calculated. The 0th and 1st powers have already been stored in the squaredValues vector so it is initialized at 2
    currentPower = 2
    while(currentPower <= y):  # This continues until the current power is greater than the exponent that x is being raised by. This means all necessary values have been calculated and stored.
        # The below equation is squaring the last found exponential value mod N and storing that in temp to be saved in the squaredValues vector
        temp = squaredValues[len(squaredValues)-1]**2 % N
        squaredValues.append(temp)
        currentPower = currentPower * 2  # The currentPower has been calculated, move to the next square power. Increments loop counter

    i = len(squaredValues)-1 #index holder for while loop, finds last index in the squaredValues vector

    modValue = 1  # used to store the product of all powers that are stored in in squaredValues that will be used to calculate the modulare exponent
    while y > 0 and i >= 0:  # Checks that the exponent is still positive (meaning more values are needed from the squaredValues vector) and the index, i, of the vector does not go negative
        currentPower = currentPower/2  # Use the previous power.

        if currentPower <= y:
            y = y - int(currentPower)  # Subtract the current power from the total exponent, y if the power currently being checked is less than y.
            modValue = modValue * squaredValues[i] % N  # multiply to the current modValue

        i = i-1  # decrement the index holder

    return  modValue