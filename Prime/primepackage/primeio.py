# primeio.py
'''This module has two methods to read and write to a csv file.

'''

import csv

def write_primes(primelist, file_name):
    '''This method takes a list and name of a csv file and writes the list into the csv file

    '''
    with open(file_name, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(primelist)

def read_primes(file_name):
    '''This method takes a csv file and returns the contents as a list.

    '''
    primelist = []
    i = 0
    with open(file_name, newline='') as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            while i < 100:
                primelist.append(int(row[i]))
                i += 1
    return primelist
