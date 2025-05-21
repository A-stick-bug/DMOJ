"""
https://dmoj.ca/problem/dpy
DP with combinatorics

dp[obstacle] = # of ways to get to `obstacle` without going through other obstacles

Notes:
- # of ways to get from (0,0) to (r,c): (r+c) choose r
"""

### MODULAR ARITHMETIC TEMPLATE START ###
MOD = 10 ** 9 + 7
MN = 2 * 10 ** 5 + 1

factorial = [1] * MN  # precompute factorials
for i in range(2, MN):
    factorial[i] = (factorial[i - 1] * i) % MOD

invfact = [1] * MN
invfact[MN - 1] = pow(factorial[MN - 1], MOD - 2, MOD)
for i in range(MN - 1, 0, -1):
    invfact[i - 1] = (invfact[i] * i) % MOD

mod_div = lambda p, r: (p * pow(r, MOD - 2, MOD)) % MOD
# comb = lambda n, k: mod_div(factorial[n], (factorial[k] * factorial[n - k])) if n >= k else 0  # N choose K

comb = lambda n, k: factorial[n] * invfact[k] % MOD * invfact[n - k] % MOD if n >= k else 0
paths = lambda r1, c1, r2, c2: comb((r2 - r1) + (c2 - c1), (r2 - r1))
### MODULAR ARITHMETIC TEMPLATE END ###

R, C, X = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(X)]
points.append((R, C))  # destination

points.sort()  # process in row major order

ways = [0] * (X + 1)
for i in range(X + 1):
    r, c = points[i]

    res = paths(1, 1, r, c)

    # check for overlap with previous
    for j in range(i):
        pr, pc = points[j]
        if pr <= r and pc <= c:
            res -= ways[j] * paths(pr, pc, r, c)

    ways[i] = res % MOD

print(ways[-1])

"""
9 2 2 2
9 9 9 9
0 0 8 9
0 0 8 9
"""
