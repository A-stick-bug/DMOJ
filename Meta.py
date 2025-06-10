# https://dmoj.ca/problem/meta
# Q: Find all nodes covered by all diameters
#
# Implementation exercise with tree diameter and some casework
# Basically find all endpoints and centers, then do some simple tree DP
#
# TC: O(n)

import sys

sys.setrecursionlimit(100005)
input = sys.stdin.readline
n = int(input())

if n <= 3:
    print(n)
    sys.exit()

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start):
    st = [start]
    dist = [-1] * (n + 1)
    dist[start] = 0
    while st:
        cur = st.pop()
        for adj in graph[cur]:
            if dist[adj] == -1:
                dist[adj] = dist[cur] + 1
                st.append(adj)
    return dist


endpoints = []
d0 = dfs(graph, 1)
e1 = d0.index(max(d0))
d1 = dfs(graph, e1)
md1 = max(d1)
e2 = d1.index(md1)
endpoints.extend([i for i in range(1, n + 1) if d1[i] == md1])
d2 = dfs(graph, e2)
md2 = max(d2)
endpoints.extend([i for i in range(1, n + 1) if d2[i] == md2])
endpoints = set(endpoints)
radius = min(max(d1[i], d2[i]) for i in range(1, n + 1))
centers = [i for i in range(1, n + 1) if max(d1[i], d2[i]) == radius]

dp = [0] * (n + 1)  # number of diameter endpoints in subtree


def get_subtrees(cur, prev):
    if cur in endpoints:
        dp[cur] = 1
    for adj in graph[cur]:
        if adj == prev:
            continue
        get_subtrees(adj, cur)
        dp[cur] += dp[adj]


if len(centers) == 1:  # centered at node
    get_subtrees(centers[0], -1)
    nxt = [(adj, centers[0]) for adj in graph[centers[0]] if dp[adj] > 0]

    # special case: >2 branches
    if len(nxt) > 2:
        print(1)
        sys.exit()

    case = 3  # add 3 center nodes

else:  # centered at edge (2 nodes)
    get_subtrees(centers[0], centers[1])
    get_subtrees(centers[1], centers[0])
    nxt = [(centers[0], centers[1]), (centers[1], centers[0])]
    case = 2  # add 2 center nodes


# `nxt` is the subtree roots that together contain all diameter endpoints (at most 2 nodes in `nxt`)


def farthest(cur, prev):  # check how far you can extend such that all diameter endpoints are still covered
    total = 0
    while True:
        nxt = [adj for adj in graph[cur] if adj != prev and dp[adj] == dp[cur]]
        if not nxt:
            break
        cur, prev = nxt[0], cur
        total += 1
    return total


# sum of length going both ways + the ones in the center
print(sum(farthest(*i) for i in nxt) + case)
