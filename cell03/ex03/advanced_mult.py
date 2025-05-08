#!/usr/bin/python3

import sys

argv = sys.argv

if len(argv) == 1:
    i = 0
    while(i < 11):
        print(f"Table de {i} : ", end="")
        j = 0
        while (j < 11):
            print(i*j, end=" ")
            j += 1
        i += 1
        print()
else:
    print("none")