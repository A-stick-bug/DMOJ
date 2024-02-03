# https://dmoj.ca/problem/dpn
# template interval DP, using PSA to speed things up
# the hard part is finding out how to do the state transition
# TC: O(N^3)

from itertools import accumulate


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    psa = [0] + list(accumulate(arr))
    query = lambda l, r: psa[r + 1] - psa[l]

    inf = 1 << 60
    dp = [[inf] * n for _ in range(n)]  # dp[i][j] contains the minimum cost to merge everything in [i, j] into 1

    for i in range(n):  # base case: single elements are already merged
        dp[i][i] = 0

    for i in reversed(range(n)):
        for j in range(i + 1, n):
            for s in range(i, j):  # combine: [l, s] + [s+1, r] -> [l, r]
                dp[i][j] = min(dp[i][j], dp[i][s] + dp[s + 1][j] + query(i, j))

    print(dp[0][n - 1])
    # for i in dp:
    #     print(i)


solve()
