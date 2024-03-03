# https://dmoj.ca/problem/neerc10k
# Graph theory
# Use dfs: for every node, assign the smallest color possible that is not used by any adjacent nodes
# this will guarantee the total number of colors used is minimal

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [-1] * (N + 1)
color[1] = 1
vis = [False] * (N + 1)
vis[1] = True


def assign_color(node):
    """assign the MEX color to current node to minimize colors used"""
    used = {color[i] for i in graph[node]}
    for i in range(1, N + 1):
        if i not in used:
            return i


stack = [1]
while stack:
    cur = stack.pop()
    for adj in graph[cur]:
        if vis[adj]:
            continue
        vis[adj] = True
        color[adj] = assign_color(adj)
        stack.append(adj)

print(max(len(graph[i]) for i in range(1, N + 1)) | 1)
print("\n".join(map(str, color[1:])))
