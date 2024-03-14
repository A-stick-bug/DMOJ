"""
MLE, check C++ code

https://dmoj.ca/problem/gfssoc2s5

Using tarjan's algorithm for SCC, compress SCC into a single node

Observations:
- provinces are just strongly connected components (SCCs), once you get there, you might as well
  borrow everything in this province
- we can just turn each SCC into a single node with the sum of money you can borrow
- now we get a DAG, and we can use graph DP

Note that we use 1-indexing for everything
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(500000)
MOD = 10 ** 9 + 7


def get_scc(graph):
    n = len(graph)

    scc_money = [0] * n  # sum of money available in the i-th SCC
    scc = [-1] * n  # the component that node i belongs to
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
                scc_money[comp] += borrow[path[-1]]
                scc[path.pop()] = comp
            in_path[cur] = False
            scc_money[comp] += borrow[cur]
            scc[path.pop()] = comp
            comp += 1

    for i in range(1, n):
        if node_id[i] == -1:
            dfs(i)
    return scc, scc_money


N, M = map(int, input().split())
borrow = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

scc, scc_money = get_scc(graph)  # compress SCCs into 1 node with the sum of money you can borrow
graph2 = [[] for _ in range(max(scc) + 1)]
for i in range(1, len(graph)):
    for adj in graph[i]:
        if scc[i] != scc[adj]:
            graph2[scc[i]].append(scc[adj])
graph2 = list(map(lambda x: list(set(x)), graph2))  # save memory by removing duplicates

# now we have a DAG, we can use graph DP to get max money and number of ways to do so
cache = [[(-1, -1) for _ in range(len(graph2))] for _ in range(2)]


def solve(cur, take):
    if cur == scc[N]:
        return take * scc_money[cur], 1
    if cache[take][cur] != (-1, - 1):
        return cache[take][cur]

    best = 0
    ways = 1
    for adj in graph2[cur]:
        if take:  # take from this one, can't take from the next
            res, cnt = solve(adj, False)
            res += scc_money[cur]
            if res == best:
                ways = (ways + cnt) % MOD
            elif res > best:
                best = res
                ways = cnt % MOD
        res, cnt = solve(adj, True)  # don't take from this one, can take from the next
        if res == best:
            ways = (ways + cnt) % MOD
        elif res > best:
            best = res
            ways = cnt % MOD

    cache[take][cur] = (best, ways)
    return cache[take][cur]


print(*solve(scc[1], True))
