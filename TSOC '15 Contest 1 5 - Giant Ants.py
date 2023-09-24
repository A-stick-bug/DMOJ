"""
https://dmoj.ca/problem/tsoc15c1p5
- Extremely low constraints
- Graph may not be connected

Use BFS, on every 4th turn, move the ants first 1 node outwards before moving the car
Nodes start at 1, use 1-indexing for graph

"""

from collections import deque
import sys

input = sys.stdin.readline
NODES, EDGES = map(int, input().split())

graph = [[] for _ in range(NODES + 1)]
for _ in range(EDGES):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # roads are bidirectional

n_ants = int(input())
ants = {int(input()) for _ in range(n_ants)}  # put ants in a set

ant_move = 0
q = deque([(1, 0)])
vis = [False] * (NODES + 1)
vis[1] = True

while q:
    cur, dist = q.popleft()
    if cur == NODES:
        print(dist)
        sys.exit()

    for adj in graph[cur]:
        new_dist = dist + 1
        if new_dist // 4 > ant_move:  # ants have expanded 1 node outwards
            ant_move += 1
            for ant in ants.copy():  # make copy because original set changes
                for node in graph[ant]:
                    ants.add(node)

        if adj in ants or vis[adj]:
            continue
        vis[adj] = True

        q.append((adj, dist + 1))

print("sacrifice bobhob314")
