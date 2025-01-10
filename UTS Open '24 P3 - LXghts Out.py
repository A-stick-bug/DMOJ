# https://dmoj.ca/problem/utso24p3
# How to flip odd length of 1: flip all odd index first, then even
# - 1111111 → 1010101 → 0000000
# - number of moves is equal to length of 1s
# How to flip even length of 1: create an extra 1 on either ends to make it odd
# - 011110 → 011111 → 010101 → 000000
# - number of moves is equal to length+2
#
# Split the string into blocks of 1s and keep track of the length of blocks
# Impossible case: 11011011 … 011
# Minimize number of flips
# - Turn as many even lengths into odd ones as possible
# - Reduce the odd lengths by 2 lights each time so they stay odd
# - Flip single lights


import sys


def compress(arr):
    groups = []
    cur = 1
    for i in range(1, N + 1):
        if arr[i] != arr[i - 1]:
            groups.append([arr[i - 1], cur])
            cur = 1
        else:
            cur += 1
    if cur != 0:
        groups.append([arr[-2], cur])
    if groups[-1][0] == 0:
        groups[-1][1] += 1
    else:
        groups.append([0, 1])
    return groups


N, K = map(int, input().split())
arr = [0] + list(map(int, input())) + [0]

groups = compress(arr)

# print(groups)
# odd group: flip normally
# even group: flip 1 on the side, then flip normally

total = 0

odds = [sz for val, sz in groups if val == 1 and sz % 2 == 1]
evens = [sz for val, sz in groups if val == 1 and sz % 2 == 0]

for i in range(1, len(groups) - 1):
    val, sz = groups[i]
    if val == 0:
        continue

    if sz % 2 == 1:  # odd group, turn all off immediately
        groups[i][0] = 0
        total += sz
    else:
        if sz != 2:  # even group of length >2, turn off at the cost of +2
            groups[i][0] = 0
            total += sz + 2

arr2 = []
for val, sz in groups:
    arr2.extend([val] * sz)
groups2 = compress(arr2)

# only has 2s -> impossible
if all(sz == 1 for val, sz in groups2 if val == 0) and K == 0:
    print(-1)
    sys.exit()

total += 4 * sum(val == 1 for val, sz in groups2)  # cost of 2s

# start reduction
if K <= len(evens):
    print(total - 3 * K)
else:
    total -= 3 * len(evens)  # reduced to odd
    K -= len(evens)
    odds += [i - 1 for i in evens]

    idx = 0
    while K >= 2 and idx < len(odds):  # by 2
        while odds[idx] > 1 and K >= 2:
            K -= 2
            odds[idx] -= 2
            total -= 2
        idx += 1

    idx = 0
    while K >= 1 and idx < len(odds):  # by 1
        while odds[idx] > 0 and K >= 1:
            K -= 1
            odds[idx] -= 1
            total -= 1
        idx += 1

    print(total)
