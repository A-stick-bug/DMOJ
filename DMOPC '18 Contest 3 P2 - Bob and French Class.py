# https://dmoj.ca/problem/dmopc18c3p2
# Sequence, fibonacci style DP
# extension of the house robber problem, take or don't take, can't take more than 2 in a row
# you can take 2 in a row, so we need an extra layer in dp, dp[i][j], max score at index i with j consecutive french
#
# note: it is possible to compress dp into 1D, but it will be more confusing

n = int(input()) + 3  # add padding to prevent index out of bounds
french = [0, 0, 0] + list(map(int, input().split()))
english = [0, 0, 0] + list(map(int, input().split()))

dp = [[0, 0, 0] for _ in range(n)]
for i in range(3, n):
    dp[i][0] = max(dp[i - 1]) + english[i]  # take english
    dp[i][1] = max(dp[i - 2]) + english[i - 1] + french[i]  # take french (1 in a row), previous is english
    dp[i][2] = dp[i - 1][1] + french[i]  # 2 in a row french

# for i in dp:
#     print(i)
print(max(dp[-1]))
