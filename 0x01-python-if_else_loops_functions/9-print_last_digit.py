#!/usr/bin/python3
def print_last_digit(number):
    if n > 0:
        ldigit = n % 10
    elif n < 0:
        ldigit = (-1 * n) % 10
    else:
        ldigit = 0
    print(ldigit,end='')
    return ldigit
