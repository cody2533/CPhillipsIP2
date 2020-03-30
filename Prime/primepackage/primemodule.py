#primemodule.py
'''There are only two methods in this module.

'''


def is_prime(number):
    '''This method determines if a number is prime and returns true if it is and false if it isn't.

    Args:
        number (int): input int to be determined if it is prime
        prime_boolean (boolean): stopping condition if the input int is not prime

    Returns:
        prime_boolean (boolean): returns true for a prime number false for non prime

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

    Args:
        num (int): input number for length of list
        prime_list (list of ints): list of int that are all prime
        number (int): iterator starting at the first prime number
        i (int): iterator used for list index and stoping point for while loop

    Return:
        prime_list (list of int): list of prime int of num length

    Raises:
        NameError (Bad Number): this exception is raised if the input num is less than 1

    '''
    try:
        if num <= 0:
            raise NameError('Bad Number')
        prime_list = []
        number = 2
        i = 0
        while i < num:
            if is_prime(number):
                prime_list.append(number)
                i += 1
            number += 1
        return prime_list
    except NameError:
        print('Please choose a number greater than 0. Number chosen', num)
        raise
