# https://dmoj.ca/problem/dmopc18c6p4
# 2 pointers and sorting
# note: using binary search is probably much easier...

import sys

input = sys.stdin.readline

N, P, M = map(int, input().split())
arr = [list(map(int, input().split())) + [i + 1] for i in range(N)]
phys = list(map(int, input().split()))
magic = list(map(int, input().split()))

# from i to i + 1, def decreases, res increases
# we can prove the optimal tank is one of these
arr.sort(key=lambda x: (-x[0], -x[1], x[2]))
filtered = [arr[0]]
for de, re, tank_id in arr[1:]:
    if re >= filtered[-1][1]:
        filtered.append([de, re, tank_id])
arr = filtered

phys.sort()
magic.sort()

best = float('inf')
best_idx = -1
i = P  # keep track of attacks that deal non-zero damage
j = -1
p_sum = 0
m_sum = sum(magic)
for de, re, tank_id in arr:
    while i - 1 >= 0 and phys[i - 1] > de:  # everything after i deals damage
        i -= 1
        p_sum += phys[i]
    while j + 1 <= M - 1 and magic[j + 1] <= re:  # everything after j deals damage
        j += 1
        m_sum -= magic[j]

    new_ans = p_sum - de * (P - i) + m_sum - re * (M - j - 1)
    if new_ans < best:
        best = new_ans
        best_idx = tank_id

print(best_idx)
