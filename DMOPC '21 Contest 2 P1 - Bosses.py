"""
https://dmoj.ca/problem/dmopc21c2p1

To beat level i, power must be >= level[i]
Level ordering doesn't matter because it is optimal to upgrade to the desired level at the start
For each power level, we check the cost of upgrading to s[i] hp and beating the other levels with potions

"""

N, H, P = map(int, input().split())  # number of levels, cost for power increase, cost for 1 level power increase

N += 1  # add a 0 to consider the case where we only use potions
level = [0] + list(map(int, input().split()))
s = sorted(level)

psa = [0] * (N + 1)  # psa[i] is how many potions you will need to beat all level after i (including i)
for i in reversed(range(N)):
    psa[i] = psa[i + 1] + s[i]

res = float('inf')
for i in range(N):
    after = N - i - 1  # number of levels AFTER i
    hp = s[i] * H  # amount spent on HP
    # because we upgrade at the start, minus (after * s[i]) because we don't need any potions to get to those levels
    potion = (psa[i + 1] - after * s[i]) * P  # amount spent on potions
    res = min(res, hp + potion)

# # this is less readable but faster than the for loop
# res = min((s[i] * H) + P * (psa[i + 1] - (N - i - 1) * s[i]) for i in range(N))

print(res)
