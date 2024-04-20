# TLE, CHECK C++ CODE
# https://dmoj.ca/problem/btoi15p3
# same logic as https://dmoj.ca/problem/cco07p6 except we don't need to compress the biconnected components
# Strategy:
# - connect all leaf nodes in pairs
# - if we have an odd number of leaf nodes, just connect the single one to any other leaf

import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = []


def traversal(cur, prev):
    if len(graph[cur]) == 1:
        order.append(cur)
    for adj in graph[cur]:
        if adj == prev:
            continue
        traversal(adj, cur)


traversal(1, -1)
cnt = len(order)
print((cnt + 1) // 2)  # number of pairs

if cnt % 2 == 1:  # odd case, pair with any other leaf
    print(order[0], order[-1])
    cnt -= 1
    order.pop()

offset = cnt // 2  # match first half with second half
for i in range(cnt // 2):
    print(order[i], order[i + offset])
