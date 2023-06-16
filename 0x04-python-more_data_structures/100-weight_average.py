#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list):
        total = 0
        weight = 0
        for x in my_list:
            total += x[0] * x[1]
            weight += x[1]
        return total / weight
    else:
        return 0
