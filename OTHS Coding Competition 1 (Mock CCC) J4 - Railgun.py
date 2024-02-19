# https://dmoj.ca/problem/othscc1p4
# if we remove stuff from the left and from the right, we are left with a subarray
# check all valid subarrays using PSA and take the best one

from itertools import accumulate
import sys

N, S, T = map(int, input().split())  # N enemies, S range, T bullets
arr = list(map(int, input().split()))
total = sum(arr)

if S * T >= N:  # everything is destroyed
    print(total)
    sys.exit()

psa = [0] + list(accumulate(arr))
query = lambda l, r: psa[r + 1] - psa[l]  # query psa, 1-indexed

res = float('inf')
empty = N - (S * T)
for i in range(0, N - empty + 1, S):
    res = min(res, query(i, i + empty - 1))

print(total - res)
