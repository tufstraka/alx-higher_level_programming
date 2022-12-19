#!/usr/bin/python3

def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
        print("Inside result: {}".format(quotient))
    except(TypeError, ZeroDivisionError):
        print("Inside result: {}".format(quotient))
    finally:
        return quotient
