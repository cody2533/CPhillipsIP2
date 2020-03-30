# primeio.py
'''This module has two methods to read and write to a csv file.

'''

import csv

def write_primes(primelist, file_name):
    '''This method takes a list and name of a csv file and writes the list into the csv file

    Args:
        primelist (list of ints): input list of integers
        file_name (str): input file name to be written to
        csvwriter: writer for the csv file

    Raises:
        OSError: file not found 

    Example:
        write_primes(list, 'file.csv')

    '''
    try:
        with open(file_name, 'w', newline='') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(primelist)
    except OSError as err:
        print(err)

def read_primes(file_name):
    '''This method takes a csv file and returns the contents as a list.

    Args:
        file_name (str): input file name to be read from
        primelist (list of int): list that stores the integers from the file
        i (int): iterator for position in the csv file
        csvreader: reader for the file

    Returns:
        primelist: the list of prime numbers

    Raises:
        OSError: file not found

    Example:
        primelist = read_primes('file.csv')

    '''
    primelist = []
    i = 0
    try:
        with open(file_name, newline='') as csv_file:
            csvreader = csv.reader(csv_file)
            for row in csvreader:
                while i < len(row):
                    primelist.append(int(row[i]))
                    i += 1
        return primelist
    except OSError as err:
        print(err)
