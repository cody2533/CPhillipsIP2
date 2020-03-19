#primemodule.py
'''There are only two methods in this module.

'''


def is_prime(number):
    '''This method determines if a number is prime and returns true if it is and false if it isn't.

    '''
    prime_boolean = True
    for i in range(2, round(number/2) + 1):
        if number % i == 0:
            prime_boolean = False
            break

    return prime_boolean

def get_n_prime(num):
    '''This method compiles a list of prime numbers of the input length and returns the list.

    This method uses isPrime to determine if a number is prime.

    '''
    prime_list = []
    number = 2
    i = 0
    while i < num:
        if is_prime(number):
            prime_list.append(number)
            i += 1
        number += 1
    return prime_list
