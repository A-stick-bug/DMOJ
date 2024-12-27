# https://dmoj.ca/problem/cheerio2p5
# PSA with combinatorics and basic modular arithmetic
# Based on observation, NC0 + NC2 + NC4 + ... = 2^(N-1)

from itertools import accumulate
import sys

input = sys.stdin.readline
MOD = 10 ** 9 + 7
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

odd = [i % 2 == 1 for i in arr]
even = [i % 2 == 0 for i in arr]
odd = [0] + list(accumulate(odd))
even = [0] + list(accumulate(even))
qry = lambda psa, l, r: psa[r] - psa[l - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    e = qry(even, l, r)
    o = qry(odd, l, r)
    e_choice = (pow(2, e, MOD)) % MOD
    if o >= 2:  # avoid negative powers
        o_choice = (pow(2, o - 1, MOD)) % MOD
    else:
        o_choice = 1
    print((e_choice * o_choice - 1) % MOD)
