# __init__.py
'''This module imports the methods to be used in another folder.

'''

__all__ = ['write_primes', 'read_primes', 'isPrime', 'getNPrime']
from primepackage.primeio import write_primes, read_primes
from primepackage.primemodule import isPrime, getNPrime

