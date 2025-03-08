# https://dmoj.ca/problem/ioi04p5
# Spend some on the first type and the rest on the second
# Tight bounds -> need constant time optimizations
# For circles: 0/1 knapsack, try to only take full circles, if it's not full circles, we waste 1 move
# For lines: greedily take largest lines first
#
# TC: O(QM), 1/32 optimization using bitmask

Q, N, M = map(int, input().split())
circles = list(map(int, input().split()))
lines = list(map(int, input().split()))

# subset sum dp
dp = 1
for w in circles:
    dp |= dp << w

l_max = [0] * (Q + 1)  # maximum sum if you spend `i` on lines
lines.sort(reverse=True)
idx = 0
cur = 0
for i in range(2, Q):
    if idx == M:  # already took all
        l_max[i] = l_max[i - 1]
        continue

    cur += 1
    l_max[i] = l_max[i - 1] + 1
    if idx < M and cur > lines[idx]:  # full
        cur -= lines[idx]
        idx += 1
        l_max[i] -= 1

# try all splits between line and circles
print(max(l_max[Q - i] + i - (dp & (1 << i) == 0) for i in range(min(Q, sum(circles)) + 1)))

"""
19 3 3
13 4 8
4 8 6

more optimal to take the circle
30 1 6
40
6 6 6 6 6 6
"""
