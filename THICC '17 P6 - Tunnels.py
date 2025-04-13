# https://dmoj.ca/problem/thicc17p6
# - To optimally search all nodes from X, take an Euler tour minus the longest path from X
# - Since the Euler tour distance is the same no matter where you start, we just need to find
#   the longest distance from all possible nodes X
# - This is a standard tree rerooting DP problem
#
# Solving: 'find the longest path starting from node X'
# - at each node, store the top 2 longest paths downwards (only count each child once)
# - when rerooting towards the longest path, take the 2nd longest path instead as 'up'
# - for any other, take the longest

import sys
from heapq import nlargest

input = sys.stdin.readline
sys.setrecursionlimit(200000)

euler_le = 0
n, T = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    euler_le += 2 * c
    graph[a].append((b, c))
    graph[b].append((a, c))

top2_child = [[-1, -1] for _ in range(n + 1)]  # top 2 longest from children
down_mx = [-1] * (n + 1)  # longest path downwards


def compute_root(cur, prev):
    if cur != 1 and len(graph[cur]) == 1:  # leaf
        down_mx[cur] = 0
        return
    paths = [-1, -1]  # defaults
    for adj, d in graph[cur]:
        if adj == prev:
            continue
        compute_root(adj, cur)
        paths.append(down_mx[adj] + d)
        down_mx[cur] = max(down_mx[cur], down_mx[adj] + d)
    top2_child[cur] = nlargest(2, paths)


up_mx = [0] * (n + 1)


def reroot(cur, prev):
    for adj, d in graph[cur]:
        if adj == prev:
            continue

        if down_mx[adj] + d == top2_child[cur][0]:
            up_mx[adj] = top2_child[cur][1] + d  # going down top1, take top2
        else:
            up_mx[adj] = top2_child[cur][0] + d  # take top1

        up_mx[adj] = max(up_mx[adj], up_mx[cur] + d)  # continue from cur

        reroot(adj, cur)


compute_root(1, -1)
reroot(1, -1)

# print(top2_child)
# print(down_mx)
# print(up_mx)

for i in range(1, n + 1):
    if len(graph[i]) == T:
        print(i, euler_le - max(up_mx[i], down_mx[i]))
