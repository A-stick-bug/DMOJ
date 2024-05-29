# https://dmoj.ca/problem/utso18p4
# Group items by value and process each group independently (taking the best answer)
# - For each group, we sort by (M_i - K_i) and use 2 pointers to get max value
# - Sorting by (M_i - K_i) will make it optimal to get K from the left and M from the right

import sys

input = sys.stdin.readline
n = int(input())
MV = 100001
groups = [[] for _ in range(MV)]
for _ in range(n):
    k, m = map(int, input().split())
    groups[k + m].append((k, m))

best = 0
for group in groups:
    group.sort(key=lambda x: x[1] - x[0])  # sort by M-K
    k_sum = m_sum = 0
    i = 0
    j = len(group) - 1
    while i <= j:
        if k_sum < m_sum:  # use 2 pointers to find most optimal split
            k_sum += group[i][0]
            i += 1
        else:
            m_sum += group[j][1]
            j -= 1
    best = max(best, min(k_sum, m_sum))

print(best)
