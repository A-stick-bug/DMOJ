# https://dmoj.ca/problem/pickit
# same as https://leetcode.com/problems/burst-balloons/description/ but addition instead of multiplication
# Interval DP: store the max score after removing everything in [i,j] (dp[i][j])
# order to remove: [i,c-1] -> [c+1, j] -> remove c, score added is arr[i-1] + arr[c] + arr[j+1]

while True:
    n, *arr = map(int, input().split())
    if n == 0:  # end of test cases
        break

    dp = [[0] * n for _ in range(n)]

    for length in range(n):
        for i in range(1, n - length - 1):
            j = i + length
            for c in range(i, j + 1):
                dp[i][j] = max(dp[i][j], dp[i][c - 1] + (arr[i - 1] + arr[c] + arr[j + 1]) + dp[c + 1][j])

    print(dp[1][n - 2])

# # recursive version
# while True:
#     n, *arr = map(int, input().split())
#     if n == 0:  # end of test cases
#         break
#
#     cache = [[-1]*n for _ in range(n)]
#
#     def solve(l, r):
#         if l > r:  # invalid interval
#             return 0
#         if cache[l][r] != -1:
#             return cache[l][r]
#
#         res = 0
#         for i in range(l, r + 1):
#             gain = arr[l - 1] + arr[i] + arr[r + 1]
#             res = max(res, gain + solve(l, i - 1) + solve(i + 1, r))
#         cache[l][r] = res
#         return cache[l][r]
#
#
#     print(solve(1, n - 2))
