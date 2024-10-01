# https://dmoj.ca/problem/coci15c7p3
# Pattern observation and PSA optimization
# XOR terms cancel out
# 1 2 3 1^2^3 2^3^(1^2^3)=1 3^(1^2^3)^1=2 (1^2^3)^1^2=3

import sys
from functools import reduce
from itertools import accumulate

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

# 1,2,3, 1^2^3, 1,2,3, 1^2^3, ..., pattern continues
seq_len = N + 1
seq = arr.copy()
seq.append(reduce(lambda x, y: x ^ y, arr))
seq *= 4
psa = [0] + list(accumulate(seq, func=lambda x, y: x ^ y))
query = lambda l, r: psa[r + 1] ^ psa[l]

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    diff = (r - l) % (seq_len * 2)  # ignore part of the sequence that cancels out
    l %= (seq_len * 2)
    r = l + diff

    print(query(l, r))
