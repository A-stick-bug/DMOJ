# Game theory DP, both people try to get the highest score possible
# recursive version can be found in [LC 877. Stone Game]

n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(n + 1)]
for i in reversed(range(n)):
    for j in range(i, n):  # looking for X-Y, so subtract other person's points
        dp[i][j] = max(arr[i] - dp[i + 1][j], arr[j] - dp[i][j - 1])

print(dp[0][-1])  # i starts at 0 and j starts at n-1, the 2 ends of the array
