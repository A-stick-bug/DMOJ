"""
6/7 MLE, check C++ code
https://dmoj.ca/problem/gooda

Observation:
- if we can reach a node in a strongly connected component (SCC), we can get the fun values of all other
  nodes in this SCC, which motivates us to turn SCCs into a single node
- after compressing SCCs into a single node (with tarjan's algorithm) , we are left with a DAG
  - this allows us to use graph DP
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)


def get_scc(graph):
    n = len(graph)

    scc = [-1] * n  # the component that node i belongs to
    scc_fun = [0] * n  # sum of fun values in this SCC
    comp = 1  # current component
    low_link = [-1] * n  # smallest time reachable of a node reachable from the DFS subtree of node i
    node_id = [-1] * n  # time at which node i was discovered
    time = 0
    path = []  # nodes currently in the dfs traversal
    in_path = [False] * n

    def dfs(cur):
        nonlocal time, comp
        node_id[cur] = low_link[cur] = time
        path.append(cur)
        in_path[cur] = True
        time += 1

        for adj in graph[cur]:
            if node_id[adj] == -1:  # not yet visited
                dfs(adj)
                low_link[cur] = min(low_link[cur], low_link[adj])

            elif in_path[adj]:  # back edge, since we arrived at a node on the current path
                low_link[cur] = min(low_link[cur], node_id[adj])

            else:
                # 1-way path to another component, NOT back edge
                continue

        if node_id[cur] == low_link[cur]:  # root in dfs tree, assign SCC values to everything in this SCC
            while path[-1] != cur:
                in_path[path[-1]] = False
                scc_fun[comp] += fun[path[-1]]
                scc[path.pop()] = comp
            in_path[cur] = False
            scc_fun[comp] += fun[cur]
            scc[path.pop()] = comp
            comp += 1

    for i in range(1, n):
        if node_id[i] == -1:
            dfs(i)
    return scc, scc_fun


N, M, start, end = map(int, input().split())
fun = [-1] + [int(input()) for _ in range(N)]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# compress SCCs into a single node with the sum of their fun values
scc, scc_fun = get_scc(graph)
compressed = [[] for _ in range(max(scc) + 1)]
for i in range(1, len(graph)):
    for adj in graph[i]:
        if scc[i] != scc[adj]:
            compressed[scc[i]].append(scc[adj])
compressed = list(map(lambda x: list(set(x)), compressed))  # remove duplicates

# the compressed graph is now a DAG, run simple graph DP on it to get maximum fun
cache = [-1] * len(compressed)


def solve(cur):
    if cache[cur] != -1:
        return cache[cur]
    if cur == scc[end]:  # reached end SCC
        return scc_fun[scc[end]]
    best = 0
    for adj in compressed[cur]:
        best = max(best, solve(adj) + scc_fun[cur])  # go to next SCC, add current SCC's fun value
    cache[cur] = best
    return cache[cur]


print(solve(scc[start]))
