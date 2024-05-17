"""
https://dmoj.ca/problem/tle16c6s3
Interval DP
Base case is just that you can visit the origin, fill dp table by interval size
DP[i][j][l/r]: maximum candy leftover after collecting all houses in [i,j] ending at l/r end of interval

NOTE: left and right are both DP arrays, I simply split them because 3D lists are extremely slow in Python
"""

import sys
from itertools import accumulate

input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

start = arr[0]
arr.sort(key=lambda x: x[0])  # sort by location
si = arr.index(start)

left = [[-1] * n for _ in range(n)]
right = [[-1] * n for _ in range(n)]
left[si][si] = right[si][si] = arr[si][1]  # base case: starting point

for length in range(1, n):
    for l in range(n - length):
        r = l + length

        # right transition (l, r-1) -> (l, r)
        dist = abs(arr[r - 1][0] - arr[r][0])  # from right end
        if right[l][r - 1] >= dist:
            right[l][r] = right[l][r - 1] - dist + arr[r][1]

        dist = abs(arr[l][0] - arr[r][0])  # from left end
        if left[l][r - 1] >= dist:
            right[l][r] = max(right[l][r], left[l][r - 1] - dist + arr[r][1])

        # left transition (l+1, r) -> (l, r)
        dist = abs(arr[l][0] - arr[l + 1][0])  # from left end
        if left[l + 1][r] >= dist:
            left[l][r] = left[l + 1][r] - dist + arr[l][1]

        dist = abs(arr[l][0] - arr[r][0])  # from right end
        if right[l + 1][r] >= dist:
            left[l][r] = max(left[l][r], right[l + 1][r] - dist + arr[l][1])

psa = [0] + list(accumulate(a[1] for a in arr))  # PSA to get sum of pie values in a range
query = lambda l, r: psa[r + 1] - psa[l]
ans = 0
for i in range(si + 1):
    for j in range(si, n):
        # we can collect all pies in [i,j] so the fox can move the sum of the pie's values in total
        if left[i][j] != -1 or right[i][j] != -1:
            ans = max(ans, query(i, j))
print(ans)

"""
Example case
5
0 2
-100 10
-5 20
2 7
15 100
"""
