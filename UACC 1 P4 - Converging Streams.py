# https://dmoj.ca/problem/uacc1p4
# graph is a DAG
# we can use dfs + memoization (graph DP)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

rc = [True] * (n + 1)  # possible roots
rc[0] = False

for _ in range(m):
    a, b, p = map(int, input().split())
    graph[b].append((a, p))  # reversed graph, root becomes base case
    rc[b] = False

source = rc.index(True)  # root of DAG

pollution = [-1] + list(map(int, input().split()))
perc = [-1] * (n + 1)  # percentage of water at node i
perc[source] = 1  # base case


def get_perc(cur):
    if perc[cur] != -1:  # memo
        return perc[cur]
    p = 0
    for adj, np in graph[cur]:
        p += get_perc(adj) * np / 100
    perc[cur] = p
    return perc[cur]


for i in range(1, n + 1):  # get percentage at all nodes O(n) because of cache
    get_perc(i)

res = [-1] * (n + 1)  # using the computed percentages to take average, we can find the pollution
res[source] = pollution[source]


def dfs(cur):
    if res[cur] != -1:
        return res[cur]

    total = 0
    total_p = 0
    for adj, p in graph[cur]:
        total_p += perc[adj] * p
        total += dfs(adj) * perc[adj] * p

    res[cur] = pollution[cur] + total / (total_p)  # take average of all sources
    return res[cur]


for i in range(1, n + 1):  # get pollutions from all nodes, also O(n)
    dfs(i)

for i in res[1:]:
    print(i)
