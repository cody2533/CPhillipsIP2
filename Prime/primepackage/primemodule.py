#primemodule.py
'''There are only two methods in this module.

The first method determines if a number is prime and returns true or false.

The second method uses the first method to compile a list of prime numbers up to the input and returns the list.

'''


def isPrime(n):
    primeBoolean = True
    for i in range(2, round(n/2) + 1):
        if n % i == 0:
            primeBoolean = False
            break;

    return primeBoolean
    
def getNPrime(num):
    primeList = []
    n = 2
    while n <= num:
        if isPrime(n):
            primeList.append(n)
        n += 1
    return primeList

