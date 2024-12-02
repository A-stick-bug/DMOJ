# https://dmoj.ca/problem/casinv
# binary search and sorting
# note that we need to ensure the data is consistent on both rows and columns so solve twice

from bisect import bisect_left
from itertools import accumulate

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def solve(arr1, arr2):
    arr1.sort()
    psa = [0] + list(accumulate(arr1))
    total = 0
    for mx in arr2:
        idx = bisect_left(arr1, mx)
        if idx == n:  # maximum doesn't match
            return -1
        total += psa[idx] + (n - idx) * mx
    return total


ans1 = solve(arr1, arr2)
ans2 = solve(arr2, arr1)
if ans1 != ans2:  # ensure answers are consistent
    print(-1)
else:
    print(ans1)
