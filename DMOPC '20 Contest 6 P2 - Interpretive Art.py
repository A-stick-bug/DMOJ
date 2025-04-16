# https://dmoj.ca/problem/dmopc20c6p2
# Implementation problem
# Turn binary string A into B by sorting subarrays, find min moves w/ reconstruction
# Observations:
# - 0 can only move left
# - think of pulling groups of 0s to the left

import sys

n = int(input())
A = [0] + list(map(int, input().split())) + [1]  # padding
B = [0] + list(map(int, input().split())) + [1]
n += 2

one_A = [i for i in range(n) if A[i]]
one_B = [i for i in range(n) if B[i]]

if A == B:
    print(0)
    sys.exit()

if sum(A) != sum(B) or not all(i <= j for i, j in zip(one_A, one_B)):  # different frequencies: impossible
    print(-1)
    sys.exit()

moves = []
b_idx = 0
a_idx = 0
while b_idx != n - 1:
    while B[b_idx] == 1 and b_idx != n - 1:  # clear leading 1s
        b_idx += 1
    if b_idx == n - 1:
        break

    zidx = []
    start = b_idx  # count zeros in group
    while B[b_idx] == 0:
        zidx.append(b_idx)
        b_idx += 1

    zeros = b_idx - start

    a_zeros = 0  # get corresponding zeros in A
    a_zidx = []
    while a_zeros < zeros:
        if A[a_idx] == 0:
            a_zidx.append(a_idx)
            a_zeros += 1
        a_idx += 1

    l = max(1, start)  # swaps to move zeros to the group at the front
    r = a_idx - 1
    if a_zidx != zidx:
        moves.append((max(1, start), a_idx - 1))
        for i,j in zip(zidx, a_zidx):
            A[i], A[j] = A[j], A[i]

print(len(moves))
for i in moves:
    print(*i)

"""
9
1 1 0 0 1 1 1 0 0
0 1 0 1 1 0 0 1 1

bug: printing useless moves
8
1 1 1 1 1 0 0 0
1 1 1 0 1 0 1 0
"""
