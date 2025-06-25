# https://dmoj.ca/problem/graph1p1
# Graph DP
# states: [node][current length] = number of ways
# here, we make the current length implicit to save memory

MOD = 2 ** 32
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [1] * N  # dp[x] = number of ways to get to node `x` after `i` moves (starting anywhere)
for _ in range(K):
    dp = [sum(dp[i] for i in range(N) if adj[i]) % MOD for adj in graph]

ans = sum(dp)


# weird answer extraction, provided by ChatGPT
def int32(x):
    x = x & 0xFFFFFFFF  # simulate unsigned 32-bit
    if x >= 0x80000000:  # if >= 2^31, it's negative in signed
        x -= 0x100000000
    return x


print(int32(ans))
