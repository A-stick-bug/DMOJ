# https://dmoj.ca/problem/othscc3p2
# Implementation with simple data structures

from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))
ordered = list(map(int, input().split()))

loc = defaultdict(set)
for i, v in enumerate(arr):
    loc[v].add(i)

n = len(arr)
swaps = []
for i in range(n):
    if ordered[i] != arr[i]:
        other_idx = loc[ordered[i]].pop()
        loc[arr[i]].remove(i)
        loc[arr[i]].add(other_idx)
        arr[i], arr[other_idx] = arr[other_idx], arr[i]
        swaps.append((i + 1, other_idx + 1))
    else:
        loc[arr[i]].remove(i)

print(len(swaps))
for a, b in swaps:
    print(a, b)
