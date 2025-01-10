# https://dmoj.ca/problem/sac22cc1p4
# 2D dynamic programming

MN = 101
n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 4 for _ in range(MN)]

total = 0
for num in arr:
    for i in reversed(range(num, MN)):
        for j in reversed(range(1, 4)):
            dp[i][j] += dp[i - num][j - 1]

    total += dp[num][3]

    dp[num][1] += 1

print(total)
