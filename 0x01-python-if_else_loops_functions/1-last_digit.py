#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit *= -1

print(f"Last digit of {number} is ", end='')
if lastdigit == 0:
    print(f"{lastdigit} and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print(f"{lastdigit} and is less than 6 and not 0")
else:
    print(f"{lastdigit} and is greater than 5")
