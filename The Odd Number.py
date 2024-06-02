# Trick: if we xor every number, the one with even frequencies cancel out
# Also use some cursed optimization tricks
# 1. reading input directly from stdin
# 2. put code in function optimization

from sys import stdin


def solve():
    stdin.readline()  # we don't need to know what n is
    num = 0
    for x in stdin:
        num ^= int(x)
    print(num)


solve()
