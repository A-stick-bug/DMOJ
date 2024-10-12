# https://dmoj.ca/problem/dmopc19c4p3
# DP, variation of the classic buy/sell stocks question, tricky transitions
# States: [current month][number of cue balls] = max money possible
# Transitions:
# - first sell and then buy to prevent selling balls you just bought
# - minus the cost of holding balls AFTER doing all transitions for the current month
#
# TC: O(N * 100^2)

N, M = map(int, input().split())
inf = 1 << 60
MX = 101  # max balls that you can hold
dp = [[-inf] * MX for _ in range(N + 1)]
dp[0][0] = 0

for idx in range(1, N + 1):
    max_buy, max_sell, buy_cost, sell_cost = map(int, input().split())

    # consider selling balls from before
    for balls in range(MX):
        for sell in range(min(max_sell + 1, MX - balls)):
            money = dp[idx - 1][balls + sell] + sell * sell_cost
            dp[idx][balls] = max(dp[idx][balls], money)

    # move the current state to the previous, so we can do buying transitions independently
    dp[idx - 1] = dp[idx].copy()
    dp[idx] = [-inf] * MX

    # consider buying balls
    for balls in range(MX):
        for buy in range(min(max_buy + 1, balls + 1)):
            money = dp[idx - 1][balls - buy] - buy * buy_cost
            dp[idx][balls] = max(dp[idx][balls], money)

    # account for cost of holding balls until next month
    # note: on the last iteration, this does nothing since te optimal answer is always dp[N][0] (sell all)
    dp[idx] = [x - i * M for i, x in enumerate(dp[idx])]

print(dp[-1][0])
