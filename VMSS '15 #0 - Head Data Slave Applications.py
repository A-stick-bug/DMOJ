# https://dmoj.ca/problem/vmss15c1p0
# combinatorics + modular arithmetic
# note: since n < 500, an alternate solution is to just build Pascal's triangle for nCr

### MODULAR ARITHMETIC TEMPLATE START ###
MOD = 10 ** 9 + 7
MN = 501

factorial = [1] * MN  # precompute factorials
for i in range(2, MN):
    factorial[i] = (factorial[i - 1] * i) % MOD

mod_div = lambda p, r: (p * pow(r, MOD - 2, MOD)) % MOD
comb = lambda n, k: mod_div(factorial[n], (factorial[k] * factorial[n - k])) if n >= k else 0  # N choose K
paths = lambda r1, c1, r2, c2: comb((r2 - r1) + (c2 - c1), (r2 - r1))
### MODULAR ARITHMETIC TEMPLATE END ###


n = int(input())
arr = [int(input()) for _ in range(n)]

empty = sum(arr)  # empty spots
ways = 1

for i in reversed(range(n)):
    arr[i] -= 1  # has to go in last available position
    empty -= 1
    ways = (ways * comb(empty, arr[i])) % MOD  # place everything else however we want
    empty -= arr[i]
print(ways)
