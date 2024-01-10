# given a list of coins, we need to find which coins can be formed by combining other coins in the list
# since N < 100, we can just run a knapsack DP on each coin and remove it if it can be created from other coins


def knapsack(target, arr):
    """check if elements in arr can sum up to target (assuming unlimited usage of everything)"""
    dp = [0] * (target + 1)
    dp[0] = 1  # base case: we can always have nothing
    for coin in arr:
        for i in range(coin, target + 1):
            dp[i] |= dp[i - coin]
    return dp[target]


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    coins = arr.copy()
    rem = 0  # number of useless coins

    for coin in arr:
        temp_remove = coin
        coins.remove(coin)
        if knapsack(coin, coins):  # we can get the current amount from other coins, we don't need this coin
            rem += 1
        else:
            coins.append(coin)  # we need this coin, add it back

    print(n - rem)
