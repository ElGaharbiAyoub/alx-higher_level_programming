#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for index in range(len(x)):
            if index < len(x) - 1:
                print("{:d}".format(x[index]), end=' ')
            else:
                print("{:d}".format(x[index]))
