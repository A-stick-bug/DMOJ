# https://dmoj.ca/problem/coci19c6p2
# annoying implementation
# keep track of both the time and iteration count
# a better method would be getting time based on iteration count but i'm bad at math

from collections import deque
import sys

input = sys.stdin.readline
N, M, Q, K = map(int, input().split())
q = deque(map(int, input().split()))  # starting locations of bfs

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (N + 1)
for i in q:
    dist[i] = 0
m = [-1] * (N + 1)
for i in q:
    m[i] = 0

time = 1
move = K
while q:
    cur = q.popleft()
    if m[cur] >= move:
        time += 1
        move += time * K
    for adj in graph[cur]:
        if dist[adj] == -1:
            q.append(adj)
            dist[adj] = time
            m[adj] = m[cur] + 1

print(" ".join(map(str, dist[1:])))
