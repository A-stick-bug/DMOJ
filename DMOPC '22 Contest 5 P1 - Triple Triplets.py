# https://dmoj.ca/problem/dmopc22c5p1
# Possible constructions:
# - only use 1 and 2 (somehow correct first guess lol)

import sys

n = int(input())

if n <= 2:
    print(0)
    sys.exit()

best = 0
for twos in range(1, n // 2 + 1):
    ones = n - 2 * twos
    ones_pairs = ones * (ones - 1) // 2  # number of ways to choose 2 ones
    best = max(best, ones_pairs * twos)
print(best)
