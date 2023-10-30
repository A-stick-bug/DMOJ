"""
https://dmoj.ca/problem/sleigh
(90/110) Requires stupid memory optimization to pass in python so just use c++

Q: Given a tree (0 is root), find the shortest path to visit all nodes (don't need to get back to start)

Because we don't need to get back to the start, we just find the furthest path down the tree
and minus that from (total length of all the path)*2
This works because we need to take each path exactly twice if we do need to get back to the start,
but since we don't, we can visit the furthest node last to save the most distance
"""

import sys

input = sys.stdin.readline
n = int(input())

total_cost = 0
graph = [[] for _ in range(n + 1)]  # create graph from input
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    total_cost += c

highest = 0
prev = -1  # use -1 as placeholder previous value
stack = [(0, 0, -1)]  # (cur, dist, prev)

while stack:
    cur, dist, prev = stack.pop()
    highest = max(highest, dist)

    for adj, d in graph[cur]:
        if adj == prev:  # prevent infinite loop
            continue
        stack.append((adj, dist + d, cur))

print(total_cost * 2 - highest)
