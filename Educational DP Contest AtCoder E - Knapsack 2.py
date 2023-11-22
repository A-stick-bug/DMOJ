"""
https://dmoj.ca/problem/dpe
Variation of the 0/1 knapsack dp problem
For each item, maximize the value while minimizing weight

Since the value of each item is small, we can do a O(N^2*V) solution, where N*V is the maximum value achievable
using items. Check if we can get a value of V without exceeding the weight to fill in dp table
"""

N, W = map(int, input().split())
inf = 1 << 31
MN = 100001

dp = [inf] * MN  # table[i], min weight used to get a value of i
dp[0] = 0  # base case: 0 items to get 0 value

for item in range(N):
    weight, value = map(int, input().split())
    for i in reversed(range(value, MN)):  # iterate in reverse, just like in regular knapsack
        dp[i] = min(dp[i], dp[i - value] + weight)  # take or don't take

# find the largest reachable value that needs a weight <=W
for i in reversed(range(MN)):
    if dp[i] <= W:
        print(i)
        break
