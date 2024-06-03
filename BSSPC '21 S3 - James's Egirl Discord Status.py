# troll solution

from itertools import accumulate


def solve_big_K():  # standard brute force O(N^2/K)
    arr = list(map(int, input().split()))
    psa = [0] + list(accumulate(arr))
    best = 0
    for i in range(1, n + 1):
        for j in range(1, i // k + 1):
            best = max(best, psa[i] - psa[i - j * k])
    print(best)


def solve_small_K():  # grouping: O(NK)
    arr = list(map(int, input().split())) + [0]*k
    best = 0
    psa = [0] + list(accumulate(arr))
    for start in range(k):
        # todo: something is wrong here, fix later
        arr = [psa[start + (i + 1) * k] - psa[start + i * k] for i in range(n // k)]
        # sliding window max with kadane's algo
        cur_s = 0
        for i in arr:
            cur_s = max(cur_s + i, 0)
            best = max(best, cur_s)
    print(best)


n, k = map(int, input().split())
if k > 1000:
    solve_big_K()
else:
    solve_small_K()
