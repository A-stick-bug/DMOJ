# https://dmoj.ca/problem/ioi11p4io
# TLE in python, check C++ code for explanations

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N, M, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ends = [int(input()) for _ in range(K)]

# END INPUT

inf = 1 << 60
dist1 = [inf] * (N + 1)
dist2 = [inf] * (N + 1)
pq = []

vis = [False] * N
for e in ends:
    dist1[e] = 0
    dist2[e] = 0
    pq.append((0, e))

while pq:
    d, cur = heappop(pq)

    if vis[cur]: break
    vis[cur] = True

    for adj, w in graph[cur]:
        new_d = d + w
        if new_d <= dist1[adj]:
            if dist1[adj] != inf:
                dist2[adj] = dist1[adj]
                heappush(pq, (dist1[adj], adj))
            dist1[adj] = new_d
        elif new_d == dist1[adj] or new_d < dist2[adj]:
            dist2[adj] = new_d
            heappush(pq, (new_d, adj))

print(dist2[0])

"""
Some tree cases
7 6 5
0 6 9
0 4 3
1 4 8
2 4 4
3 4 1
4 5 2
6
2
1
3
5

8 7 5
0 5 8
0 7 9
1 4 5
1 6 5
1 7 4
1 3 5
2 7 5
4
6
3
2
5
"""

# # the pain I went through to debug this:
# import sys
# from heapq import heappush, heappop
#
# for _ in range(1000000000):
#     try:
#         input = sys.stdin.readline
#         # N, M, K = map(int, input().split())
#         # graph = [[] for _ in range(N)]
#         # for _ in range(M):
#         #     a, b, c = map(int, input().split())
#         #     graph[a].append((b, c))
#         #     graph[b].append((a, c))
#         # # ends = [int(input()) for _ in range(K)]
#         # ends = list(map(int, input().split()))
#         # is_end = [False] * N
#         # for e in ends:
#         #     is_end[e] = True
#
#         N, M, K = 8, 7, 3
#
#         from sortedcontainers import SortedList
#         from random import randint
#         def generate_random_tree_adj_list(n):
#             """Returns the 1-indexed adjacency list of a random tree with n nodes.
#             Note: the trees tend to be low depth"""
#             graph = [[] for _ in range(n)]
#
#             nodes = SortedList([i for i in range(n)])
#             for _ in range(n - 1):
#                 u = nodes.pop(randint(0, len(nodes) - 1))
#                 v = nodes.pop(randint(0, len(nodes) - 1))
#                 w = randint(1, 10)
#                 graph[u].append((v,w))
#                 graph[v].append((u,w))
#                 nodes.add([u, v][randint(0, 1)])
#             return graph
#
#         graph = generate_random_tree_adj_list(N)
#         # ends = [int(input()) for _ in range(K)]
#         ends = [i for i in range(1, N) if len(graph[i]) == 1]
#         K = len(ends)
#         is_end = [False] * N
#         for e in ends:
#             is_end[e] = True
#
#         def solve(cur, prev):
#             if is_end[cur]:
#                 return 0
#             res = []
#             for adj, w in graph[cur]:
#                 if adj == prev:
#                     continue
#                 res.append(solve(adj, cur) + w)
#             res.sort()
#             return res[1]
#
#
#         a1 = (solve(0, -1))
#
#         # END INPUT
#
#         inf = 1 << 60
#         dist1 = [inf] * (N + 1)
#         dist2 = [inf] * (N + 1)
#         pq = []
#
#         vis = [False] * N
#         for e in ends:
#             dist1[e] = 0
#             dist2[e] = 0
#             pq.append((0, e))
#
#         while pq:
#             d, cur = heappop(pq)
#
#             if vis[cur]: break
#             vis[cur] = True
#
#             for adj, w in graph[cur]:
#                 new_d = d + w
#                 if new_d <= dist1[adj]:
#                     if dist1[adj] != inf:
#                         dist2[adj] = dist1[adj]
#                         heappush(pq, (dist1[adj], adj))
#                     dist1[adj] = new_d
#                 elif new_d == dist1[adj] or new_d < dist2[adj]:
#                     dist2[adj] = new_d
#                     heappush(pq, (new_d, adj))
#
#
#         print(dist2[0])
#         if dist2[0] != a1:
#             print("err")
#             print(f"{graph=} {dist2[0]=} {a1=}")
#
#
#             def print_edge_list(graph):
#                 """given a graph, print its edges"""
#                 for i in range(len(graph)):
#                     for j,w in graph[i]:
#                         if i < j:
#                             print(i, j,w)
#
#             print_edge_list(graph)
#             print("!!")
#             break
#     except:
#         ...
# """
# 0 6 9
# 0 4 3
# 1 4 8
# 2 4 4
# 3 4 1
# 4 5 2
# """
