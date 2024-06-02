# https://dmoj.ca/problem/dpo
# bitmask DP with optimization for transitions
# Note: .bit_count() is the fastest way to count the number of set bits
# TC: O(n*2^n)

MOD = 10 ** 9 + 7
n = int(input())
match = [list(map(int, input().split())) for _ in range(n)]

states = [[] for _ in range(n + 1)]  # the states with i bits set
for i in range(1 << n):
    states[i.bit_count()].append(i)

# dp[i][state] number of ways to match up to i-th man, state represents which women are taken
# note we remove the first state for memory efficiency just like what we do in knapsack
dp = [0] * (1 << n)
dp[0] = 1
for i in range(n):
    for state in reversed(states[i + 1]):  # after matching the i-th man, the number of women matched must also be i
        for bit in range(n):
            if state & (1 << bit) and match[i][bit]:  # transition: match with previously unmatched woman
                dp[state] = (dp[state] + dp[state - (1 << bit)]) % MOD

print(dp[-1])

# # alternate (slightly faster) solution
# MOD = 10 ** 9 + 7
# n = int(input())
# match = [list(map(int, input().split())) for _ in range(n)]
# states = 1 << n
#
# dp = [0] * states
# dp[0] = 1  # no pairs at the start
#
# for s in range(states):
#     set_bits = s.bit_count()
#     for w in range(n):  # transition from previous state by adding 1 bit
#         if not s & (1 << w) and match[set_bits][w]:
#             dp[s | (1 << w)] = (dp[s] + dp[s | (1 << w)]) % MOD
#
# print(dp[-1])  # get state for all bits set to 1 (all pairs matched)
