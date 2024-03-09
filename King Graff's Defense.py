"""
MLE, 10/28, whoever set the memory limit this low is actually trolling

https://dmoj.ca/problem/graffdefense

Note: this is just bi-connected components, but I didn't know that when I did this problem

- let a component be a part of the graph with no bridges inside
- first find all bridges and remove them from the graph
- now, any connected nodes in the graph will be part of the same component

- there are NC2 ways to put the 2 soldiers
- for each component, add XC2 to the valid positions, where X is the # of nodes in that component
- answer will be (# of valid positions)/(numbers of ways to put 2 soldiers)
"""

from math import comb
import sys

input = sys.stdin.readline
sys.setrecursionlimit(500000)


def get_bridges(graph):
    n = len(graph)

    bridges = []
    low_link = [-1] * n  # smallest time reachable of a node reachable from the DFS subtree of node i
    node_id = [-1] * n  # time at which node i was discovered
    time = 0

    def dfs(cur, p):
        nonlocal time
        node_id[cur] = low_link[cur] = time
        time += 1

        for adj in graph[cur]:
            if adj == p:  # doesn't count as back edge since removing it still disconnects the graph
                continue
            if node_id[adj] == -1:  # not yet visited
                dfs(adj, cur)
                low_link[cur] = min(low_link[cur], low_link[adj])
                if low_link[adj] > node_id[cur]:  # no back edges, therefore is a bridge
                    bridges.append(frozenset((cur, adj)))

            else:  # back edge
                low_link[cur] = min(low_link[cur], node_id[adj])

    dfs(1, -1)
    return bridges


def get_components():
    vis = [False] * (N + 1)

    def dfs(start):
        cnt = 1
        stack = [start]
        vis[start] = True
        while stack:
            cur = stack.pop()
            for adj in graph[cur]:
                if vis[adj]:
                    continue
                vis[adj] = True
                cnt += 1
                stack.append(adj)
        return cnt

    comps = []
    for i in range(1, N + 1):
        if not vis[i]:
            comp_size = dfs(i)
            comps.append(comp_size)
    return comps


N, M = map(int, input().split())

edges = []
graph = [[] for _ in range(N + 1)]  # original graph
for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue
    edges.append(frozenset((a, b)))
    graph[a].append(b)
    graph[b].append(a)
edges = set(edges) - set(get_bridges(graph))

graph = [[] for _ in range(N + 1)]  # graph after removing bridges
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

components = get_components()
valid = sum(comb(c, 2) for c in components)
prob = valid / comb(N, 2)
print(f"{1 - prob:.5f}")  # print to 5 decimal places with trailing zeros
