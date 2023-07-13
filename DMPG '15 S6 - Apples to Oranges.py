# NOTE: I MAY HAVE USED OVERCOMPLICATED SOLUTIONS, PERHAPS SIMPLE BFS/DFS WOULD WORK

# For some reason, this SPFA (shortest path faster algorithm) code is faster than dijkstra's
from collections import deque
import sys

n_fruits, n_edges = map(int, input().split())

graph = {}
for i in range(n_fruits):
    amt = input()
    graph[amt] = []

for i in range(n_edges):
    a, b, c = input().split()
    graph[a].append((b, float(c)))

# SPFA
dist = {v: 0 for v in graph}
dist["APPLES"] = 1
in_queue = {v: False for v in graph}
q = deque()
q.append(("APPLES", 1))

while q:
    fruit, amt = q.popleft()
    in_queue[fruit] = False

    if fruit == "APPLES" and amt-1 > 0.0000000001:
        print("YA")
        sys.exit()

    for adj, multi in graph[fruit]:
        if dist[adj] < dist[fruit] * multi:
            dist[adj] = dist[fruit] * multi
            if not in_queue[adj]:
                q.append((adj, amt * multi))
                in_queue[adj] = True

print("NAW")

# Dijkstra's algorithm
# import heapq
# import sys
#
# n_fruits, n_edges = map(int, input().split())
# graph = {}
# for i in range(n_fruits):
#     fruit = input()
#     graph[fruit] = []
# for i in range(n_edges):
#     a, b, c = input().split()
#     graph[a].append((float(c), b))
#
#
# costs = {node: 0 for node in graph}
# costs["APPLES"] = 1
# pq = [(-1, "APPLES")]  # make negative for max heap
#
# while pq:
#     cost, node = heapq.heappop(pq)
#     cost = -cost
#
#     for multi, adj in graph[node]:
#         new_cost = cost * multi
#         if adj == "APPLES" and new_cost-1 > 0.0000000001:  # need this because of floats not being precise, smh
#             print("YA")
#             sys.exit()
#
#         if costs[adj] < new_cost:
#             costs[adj] = new_cost
#             heapq.heappush(pq, (-new_cost, adj))
#
# print("NAW")
