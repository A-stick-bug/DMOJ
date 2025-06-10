# https://dmoj.ca/problem/mathp3
# First filter out the impossible cases
# After adding a number to the end, the LIS either stays the same or increases by 1
#
# We can add a sequence of reversed consecutive integers to avoid increasing LIS

import sys
from collections import Counter


def impossible():
    print(-1)
    sys.exit()


n = int(input())
arr = list(map(int, input().split()))

if arr[0] != 1:
    impossible()
for i in range(1, n):
    if not (arr[i] == arr[i - 1] or arr[i] == arr[i - 1] + 1):
        impossible()

freq = Counter(arr)
ans = []
for k in sorted(freq.keys()):
    to_add = freq[k]
    start = len(ans) + 1
    ans.extend(list(reversed(range(start, start + to_add))))

print(" ".join(map(str, ans)))

"""
6
1 2 2 2 3 4
ans: [1] [4 3 2] [5] [6]
"""
