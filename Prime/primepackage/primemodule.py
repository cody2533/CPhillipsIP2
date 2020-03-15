#primemodule.py
'''There are only two methods in this module.

The first method determines if a number is prime and returns true or false.

The second method uses the first method to compile a list of prime numbers up to the input and returns the list.

'''


def isPrime(n):
    '''This method determines if a number is prime and returns true if it is and false if it isn't.
    
    '''
    primeBoolean = True
    for i in range(2, round(n/2) + 1):
        if n % i == 0:
            primeBoolean = False
            break;

    return primeBoolean
    
def getNPrime(num):
    '''This method compiles a list of prime numbers of the input length and returns the list.
    
    This method uses isPrime to determine if a number is prime.
    
    '''
    primeList = []
    n = 2
    i = 0
    while i < num:
        if isPrime(n):
            primeList.append(n)
            i += 1
        n += 1
    return primeList

