# https://dmoj.ca/problem/coci16c4p3
# Dynamic programming, optimized version

MN = 200002
n = int(input())
arr = [int(input()) for _ in range(n)]
total = sum(arr)
inf = 1 << 30

prev_dp = [-inf] * MN
prev_dp[0] = 0  # base case: have nothing

for val in arr:
    dp = [0] * MN
    for i in range(total + 1):
        dp[i] = max(prev_dp[i],
                    prev_dp[abs(i - val)] + val,  # abs() since dp states are symmetric
                    prev_dp[i + val] + val)
    prev_dp = dp

print(total - prev_dp[0] // 2)
