# primeio.py
'''There are only two methods in this module.

The first method takes a list and name of a csv file and writes the list into the file.

The second method takes a csv file and returns the contents as a list.

'''

import csv


def write_primes(l, file_name):
    with open(file_name, 'w') as csv_file:   
        primewriter = csv.writer(csv_file)
        primewriter.writerow(l)
    
    
def read_primes(file_name):
    primelist = []
    
    with open(file_name, 'r') as csv_file:
        primereader = csv.reader(csv_file, delimiter=',')            
        for row in primereader:
            primelist.append(row)
    
    return primelist


