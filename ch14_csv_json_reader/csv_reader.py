#!/usr/bin/python

import csv

def csv_reader(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        #read_data(reader)
        read_data_loop(reader)

def read_data(reader):
    '''This will read all data once in memory and print the data at once'''
    data = list(reader)
    print data
    print "First column of first row: (1st cell of excel): ", data[0][0]

def read_data_loop(reader):
    '''This will read data one by one line instead of loading data in memory once'''
    for row in reader:
        print('Row #' + str(reader.line_num) + ' ' + str(row))


def csv_writer(path):
    '''This will append data in existing file'''
    with open(path, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([3,'Madhya Pradesh', 'Bhopal'])
        writer.writerow([4,'Punjab, Haryana', 'Chandigarh'])
#        The writerow() method for Writer objects takes a list argument. Each value in the list is placed in its own cell in the output CSV file. The return value of writerow() is the number of characters written to the file for that row (including newline characters).

def csv_writer_delimiter_lineterminator(path):
    '''This will append data in existing file'''
    with open(path, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
        writer.writerow([5, 'Maharastra', 'Mumbai'])
        writer.writerow([6, 'Goa', 'panji'])
#        The writerow() method for Writer objects takes a list argument. Each value in the list is placed in its own cell in the output CSV file. The return value of writerow() is the number of characters written to the file for that row (including newline characters).


if __name__ == "__main__":
    reader = csv_reader('test.csv')
    print "\nAppending data in file"
    writer = csv_writer('test.csv')
    writer = csv_writer_delimiter_lineterminator('test.csv')
    print "\nprinting new  data in file"
    reader = csv_reader('test.csv')
