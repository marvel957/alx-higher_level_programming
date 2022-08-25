#!/usr/bin/python3
from sys import argv
argv_length = len(argv)
num = 0
if argv_length == 1:
    print("0")
    for i in range(1, argv_length):
        num = num + int(argv[i])
    print("{}".format(num))
