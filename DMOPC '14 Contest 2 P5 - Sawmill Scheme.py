# https://dmoj.ca/problem/dmopc14c2p5
# topo sort (DAG DP also works)

import sys
from collections import deque

input = sys.stdin.readline
fast_print = lambda x: sys.stdout.write(str(x) + "\n")

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
prob = [0] * (N + 1)
prob[1] = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque([(i, prob[i]) for i in range(1, N + 1) if in_degree[i] == 0])

while q:
    cur, p = q.popleft()

    if len(graph[cur]) == 0:
        continue

    flow_prob = 1 / len(graph[cur])
    for adj in graph[cur]:
        prob[adj] += p * flow_prob
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            q.append((adj, prob[adj]))

for i in range(1, N + 1):
    if len(graph[i]) == 0:
        fast_print(prob[i])
