# __init__.py
'''This module imports the methods to be used in another folder.

'''

__all__ = ['write_primes', 'read_primes', 'is_prime', 'get_n_prime']
from primepackage.primeio import write_primes, read_primes
from primepackage.primemodule import is_prime, get_n_prime
