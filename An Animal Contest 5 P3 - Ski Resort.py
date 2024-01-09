# https://dmoj.ca/problem/aac5p3
# python is too slow, TLE
# dfs while keeping track of intervals

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
inf = 1 << 31

n, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

pandas = list(map(int, input().split()))
graph = list(map(lambda x: sorted(x, key=lambda a: a[1]), graph))  # sort edges by difficulty
interval = [(0, -1)] * (n + 1)


def solve(cur, prev, l, r):
    stack = [(cur, prev,l,r)]
    while stack:
        cur, prev, l, r = stack.pop()

        for i in range(len(graph[cur])):  # remove previous node to prevent infinite loop
            if graph[cur][i][0] == prev:
                graph[cur].pop(i)
                break

        interval[cur] = (l, r)  # store current answer

        # get the skier range going down each path
        graph[cur] = [(-1, -inf)] + graph[cur] + [(-1, inf)]  # add padding
        for i in range(1, len(graph[cur]) - 1):
            prev = graph[cur][i - 1]
            mid = graph[cur][i]
            after = graph[cur][i + 1]
            pre_interval = max(l, (prev[1] + mid[1]) // 2 + 1)
            post_interval = min(r, (mid[1] + after[1]) // 2)
            stack.append((mid[0], cur, pre_interval, post_interval))


solve(1, 0, 1, 10**9)
res = [0] * n
pandas.sort()

for i in range(len(interval)):
    l, r = interval[i]
    low = bisect_left(pandas, l)
    high = bisect_right(pandas, r)
    res[i - 1] = max(0, high - low)

print(*res)
