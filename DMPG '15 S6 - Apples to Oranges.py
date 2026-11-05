# # https://dmoj.ca/problem/dmpg15s6
# # Graph DP/Bellman-Ford
# #
# # dp[node] = max value at node
# # Use logarithmic scale to avoid big numbers
# # So x->cx becomes log(x)->log(cx)=log(c)+log(x)
# # The goal is now to look for a positive weight cycle that reaches `src` (apples)
# #
# # TC: O(nm)
# #
# # Adjust epsilon until it passes
# # - too small eps: cycles <=1 become >1+eps by rounding, get WA, false positive
# # - too big eps: cycles barely over 1 are <1+eps, get WA, false negative
#
# import sys
# from math import log
#
# n, m = map(int, input().split())
# names = [input().strip() for _ in range(n)]
# mp = {names[i]: i for i in range(n)}
#
# rev_graph = [[] for _ in range(n)]
# edges = []
# for _ in range(m):
#     a, b, c = input().split()
#     a, b = mp[a], mp[b]
#     c = log(float(c))
#     rev_graph[b].append((a, c))
#     edges.append((a, b, c))
#
# src = mp["APPLES"]
#
#
# # get reachable nodes from source
# def reachable(source):
#     stack = [source]
#     reach = [False] * n
#     reach[source] = True
#     while stack:
#         cur = stack.pop()
#         for adj, _ in rev_graph[cur]:
#             if reach[adj]:
#                 continue
#             reach[adj] = True
#             stack.append(adj)
#     return reach
#
#
# reach = reachable(src)  # reach[x]=True if you can reach apples from x
#
# inf = 1 << 60
# eps = 1e-15
#
# dp = [-inf] * n
# dp[src] = 0
# for _ in range(n - 1):
#     for a, b, c in edges:
#         if dp[a] == -inf:
#             continue
#         dp[b] = max(dp[b], dp[a] + c - eps)
#
# for a, b, c in edges:
#     if dp[a] == -inf:
#         continue
#     # improvement must be in a positive cycle
#     if reach[b] and dp[a] + c > dp[b] + eps:
#         print("YA")
#         sys.exit()
#
# print("NAW")
from itertools import permutations

n=8
s = 0
from collections import Counter
mp = Counter()
for perm in permutations(list(range(1, n+1))):
    perm = perm + (perm[0],)
    adj = sum(min(perm[j], perm[j-1]) for j in range(1, n+1))
    mp[adj] += 1
print(mp)