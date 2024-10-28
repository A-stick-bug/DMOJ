# https://dmoj.ca/problem/tc19summerb
# greedy with expected value math and sorting

import sys
from itertools import accumulate

input = sys.stdin.readline
n = int(input())
arr = [list(map(float, input().split()[1:])) for _ in range(n)]

for i in range(n):
    arr[i].sort(reverse=True)
    for j in range(1, len(arr[i])):
        arr[i][j] = arr[i][j - 1] + (1 - arr[i][j - 1]) * arr[i][j]

    for j in reversed(range(1, len(arr[i]))):  # calculate expected value gains
        arr[i][j] = arr[i][j] - arr[i][j - 1]

joined = []
for i in arr:
    joined.extend(i)
joined.sort(reverse=True)

print("\n".join(map(str, accumulate(joined))))
