# https://dmoj.ca/problem/coci07c1p5
# "Median trick": Keep track of numbers greater than and less than median
# -1 is less than median, 1 is more than medium
# A sum of zero will make it valid
#
# Brute force all position on the left and find matches on the right using a dict
# Since the subarray always contains a 0, anything that sums to 0 will automatically be odd length

from itertools import accumulate
from collections import Counter

N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr = [0 if i == K else (1 if i > K else -1) for i in arr]

left = arr[:arr.index(0) + 1]
right = arr[arr.index(0) + 1:]
psa_r = [0] + list(accumulate(right))

freq = Counter(psa_r)

total = 0
cur = 0
for i in reversed(range(len(left))):
    cur += left[i]
    total += freq[-cur]

print(total)
