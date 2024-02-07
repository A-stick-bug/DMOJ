# https://dmoj.ca/problem/dpn
# template interval DP, using PSA to speed things up
#
# Transition: loop from smaller to larger intervals, the current interval can be created from 2 smaller ones,
#             try all possible split point (in other words try all pairs of intervals on the left and right)
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

    for length in range(n):  # 0-indexed length, true length of current [i,j] is actually 1 more
        for i in range(n - length):
            j = i + length
            for s in range(i, j):  # find best way to combine: [l, s] + [s+1, r] -> [l, r]
                # these segments are guaranteed to exist already since they are smaller
                dp[i][j] = min(dp[i][j], dp[i][s] + dp[s + 1][j] + query(i, j))

    print(dp[0][n - 1])
    # for i in dp:
    #     print(i)


solve()
