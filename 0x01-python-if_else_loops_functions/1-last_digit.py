#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

message = "Last digit of {0} is {1} and it is {2}".format(number, last_digit)

if last_digit == 0:
    print("{0} and is 0".format(message))
elif last_digit > 5 and last_digit % 10 != 0:
    print("{0} and is greater than 5".format(message))
else:
    print("{0} and is less than 6 and not 0".format(message))
