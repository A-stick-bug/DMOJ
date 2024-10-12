# https://dmoj.ca/problem/dwite10c5p3
# Classic knapsack problem
# Extremely weak data, the solution might be wrong
# To make difference as small as possible, we want to get as close to half on one hand

def solve():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    s = sum(arr)

    mask = 1
    for w in arr:
        mask |= mask << w

    best = float('inf')
    for i in range(sum(arr) // 2 + 1):
        if mask & (1 << i):
            best = min(best, s - 2 * i)
    print(best)


for _ in range(5):
    solve()
