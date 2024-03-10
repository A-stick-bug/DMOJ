# https://dmoj.ca/problem/coci15c2p2
# bitmask DP
# generating all subsets with constraints

def solve():
    N, M = map(int, input().split())

    cant = [[False] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        cant[a - 1][b - 1] = True
        cant[b - 1][a - 1] = True

    dp = [0] * (1 << N)
    dp[0] = 1

    for mask in range(1 << N):
        if not dp[mask]:
            continue
        for i in range(mask.bit_length(), N):
            if not (mask & (1 << i)) and all(not cant[i][j] or not (mask & (1 << j)) for j in range(N)):
                dp[mask | (1 << i)] = 1

    print(sum(dp))


solve()
