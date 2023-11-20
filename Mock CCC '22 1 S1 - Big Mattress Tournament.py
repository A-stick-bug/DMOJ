"""
https://dmoj.ca/problem/nccc9s1
Very annoying casework

special tilling case:
CBB
CCA

Regular tilling cases:
CA BB AA
CC BB BB
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    b %= 2

    if c > a:  # C MUST go with a
        print("NO")
        continue

    if b == 0:  # no extra B tile
        a -= c

    else:  # we have to deal with a leftover B tile
        if a == 0 and c == 0:  # nothing to combine with
            print("NO")
            continue
        a -= c  # combine C with A, we can fit a B in here as described in the special case above

    if a % 2 == 0:  # A goes in pairs
        print("YES")
    else:
        print("NO")
