# https://dmoj.ca/problem/acoinproblem
# Template unbounded knapsack DP with offline queries
# basically don't answer the queries in order, sort them and output all answers in the end

import sys

input = sys.stdin.readline
M_VAL = 10 ** 4 + 1
inf = 1 << 30

N, Q = map(int, input().split())
coins = list(map(int, input().split()))

# offline queries
queries = [tuple(map(int, input().split())) + (i,) for i in range(Q)]
queries.sort(key=lambda x: x[1])  # sort by number of items she can buy from
ans = [0] * Q

dp = [inf] * M_VAL
dp[0] = 0  # base case: have nothing

cur_q = 0  # current query
for i, coin in enumerate(coins, start=1):
    for v in range(coin, M_VAL):  # consider the option of using the i-th coin (i is 1-indexed)
        dp[v] = min(dp[v], dp[v - coin] + 1)

    while cur_q < Q and queries[cur_q][1] <= i:  # answer all queries that only use the first i items
        val, idx = queries[cur_q][0], queries[cur_q][2]
        ans[idx] = dp[val] if dp[val] != inf else -1
        cur_q += 1

print("\n".join(map(str, ans)))  # output everything in the right order
