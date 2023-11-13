# https://dmoj.ca/problem/aac7p2
# kind of like coloring a tree into 2 colors, but each of node 1's children gets their own color

import sys

input= sys.stdin.readline
sys.setrecursionlimit(200001)

n = int(input())

graph = [[] for _ in range(n + 1)]  # create original graph from input
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(len(graph[1]) + 1)
root = []  # nodes in here will be connected to the root


def dfs(cur, prev, parity):
    for adj in graph[cur]:
        if adj == prev:  # prevent infinite loop
            continue
        if parity:
            new_tree.append((prev, adj))
        dfs(adj, cur, not parity)


for c in graph[1] + [1]:
    new_tree = []
    dfs(c, 1, False)
    print(len(new_tree)+1)
    for u, v in new_tree:
        print(u, v)
