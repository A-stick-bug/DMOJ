# https://dmoj.ca/problem/negativeones
# Solve in reverse (go a/b to -1)
# the moves become +1, *-1, ^-1

import sys

a, b = map(int, input().split())
if a == 0:
    print(2)
    print("*+")
    sys.exit()

moves = []
if a > 0:
    moves.append("*")
a = abs(a)

while a != 1 or b != 1:
    if a > b:
        moves.append("+")
        a -= b
    else:
        moves.append("^")
        a, b = b, a

print(len(moves))
print("".join(moves[::-1]))
