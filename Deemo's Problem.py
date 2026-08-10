# https://dmoj.ca/problem/dproblem
# Probabilistic solution
# Map each number to a hash so that sum(hash[i]) = 0
# Now, counting subarrays that have equal, nonzero frequency becomes counting subarrays summing to 0
#
# TC: O(n)

from collections import Counter
from random import randint

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# generate a hash for each number, ensure that the sum of all hashes is 0
val = [0] * m
sz = 10 ** 18
for i in range(m - 1):
    val[i] = randint(-sz, sz)
val[-1] = -sum(val)  # force sum(val) = 0

# count subarray with sum of 0
arr2 = [val[i - 1] for i in arr]  # 0-index
prev = Counter({0: 1})
cur = 0
total = 0
for v in arr2:
    cur += v
    if cur in prev:
        total += prev[cur]
    prev[cur] += 1

print(total)
