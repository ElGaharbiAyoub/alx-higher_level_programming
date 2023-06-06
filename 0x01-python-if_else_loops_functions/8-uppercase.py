#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            toUpper = ord(letter) - 32
        else:
            toUpper = ord(letter)
        print("{:c}".format(toUpper), end='')
    print('')
