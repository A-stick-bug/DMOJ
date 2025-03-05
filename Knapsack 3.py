# https://dmoj.ca/problem/knapsack
# Bounded knapsack with binary packaging
# TC: O(n * W * logF)
# n: number of items, W: max weight, F: max frequency of items

log2 = lambda x: x.bit_length() - 1
inf = 1 << 30
MN = 5000

n, q = map(int, input().split())

items = []
for _ in range(n):  # binary packaging
    freq, cost, value = map(int, input().split())
    for p in range(32):
        f = 1 << p
        if freq >= f:
            items.append((f * cost, f * value))
            freq -= f
        else:
            items.append((freq * cost, freq * value))
            break

# run standard knapsack on packaged items
dp = [0] * (MN + 1)
for cost, val in items:
    for c in reversed(range(cost, MN + 1)):
        dp[c] = max(dp[c], dp[c - cost] + val)

# try all possible trucks
best = -inf
for _ in range(q):
    c, f = map(int, input().split())
    best = max(best, dp[c] - f)
print(best)
