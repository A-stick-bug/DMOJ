# https://dmoj.ca/problem/aac4p2
# Prefix LCM queries with binary search
# - During the i-th second, a light will be on if i%value == 0
# - Thus, the first X lights will be on if i%LCM == 0  (first X divides i)

from math import lcm
import sys

input = sys.stdin.readline
inf = 10 ** 9 + 7
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

psa = [arr[0]]  # prefix lcm
for i in range(1, N):
    psa.append(lcm(arr[i], psa[-1]))
    # no need to go over 10^9 since nothing will divide it anyway
    psa[-1] = min(psa[-1], inf)

for _ in range(Q):
    i = int(input())

    # binary search
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        if i % psa[mid] == 0:
            low = mid + 1
        else:
            high = mid - 1
    if low >= N:
        print(-1)
    else:
        print(low + 1)  # 1-indexed
