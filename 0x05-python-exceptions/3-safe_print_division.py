#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        solution = a / b
    except (ZeroDivisionError, FloatingPointError):
        solution = None
    finally:
        print("Inside result: {}".format(answer))
    return (solution)
