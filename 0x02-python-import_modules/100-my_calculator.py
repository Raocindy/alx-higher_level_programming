#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def calculate(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        raise ValueError("Unknown operator. Available operators: +, -, *, /")

if __name__ == "__main__":
    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    try:
        result = calculate(a, operator, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    except ValueError as e:
        print(e)
        sys.exit(1)

