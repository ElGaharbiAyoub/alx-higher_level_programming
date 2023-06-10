#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for index, y in enumerate(x):
            if index < len(x) - 1:
                print("{:d}".format(y), end=' ')
            else:
                print("{:d}".format(y))
            # print("{:d}".format(y), end=' ' if index != (len(x) - 1) else "\n")
