# https://dmoj.ca/problem/coci18c1p2
# Note: my current code is extremely weak and will probably break if new test cases are added
# Strategy:
# - assign values to variables that we are certain for (variable paired with a number)
# - assign values to variables that are paired with another variable with a value

import sys

n = int(input())
a1 = input().split()
a2 = input().split()

val = {}


def find_variables():
    for i, j in zip(a1, a2):
        if i in val:
            i = val[i]
        if j in val:
            j = val[j]

        if i == j:  # same thing, ignore
            continue

        if i.isnumeric() and j.isnumeric() and i != j:  # mismatched constant, can't do anything about it
            print("NE")
            sys.exit()
        elif i.isnumeric():  # assign variables
            if j in val and val[j] != i:
                print("NE")
                sys.exit()
            val[j] = i
        elif j.isnumeric():  # assign variables
            if i in val and val[i] != j:
                print("NE")
                sys.exit()
            val[i] = j


for _ in range(4):
    find_variables()
print("DA")
