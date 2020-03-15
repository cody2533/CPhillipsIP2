# primeio.py
'''This module has two methods to read and write to a csv file.

'''

import csv


def write_primes(l, file_name):
    '''This method takes a list and name of a csv file and writes the list into the csv file
    
    '''
    with open(file_name, 'w') as csv_file:   
        primewriter = csv.writer(csv_file)
        primewriter.writerow(l)
    
    
def read_primes(file_name):
    '''This method takes a csv file and returns the contents as a list.
    
    '''
    primelist = []
    
    with open(file_name, 'r') as csv_file:
        primereader = csv.reader(csv_file, delimiter=',')            
        for row in primereader:
            primelist.append(row)
    
    return primelist


