#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        ldigit = number % 10
    elif n < 0:
        ldigit = ((-1 * number) % 10) * -1
    else:
        ldigit = 0
    print(ldigit,end='')
    return ldigit
