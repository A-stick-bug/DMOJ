# MLE, check c++ code
#
# https://dmoj.ca/problem/vmss7wc16c6p3
# Template problem for finding articulation points (cut vertices) in a graph (undirected)
# using Tarjan's algorithm

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)


def get_cut_vertices():
    def dfs(cur, prev):
        nonlocal node_id, low_link, cut_vertex, time
        node_id[cur] = low_link[cur] = time
        time += 1

        c = 0  # number of children
        for adj in graph[cur]:
            if node_id[adj] == -1:  # not visited
                dfs(adj, cur)
                c += 1
                low_link[cur] = min(low_link[cur], low_link[adj])
                if low_link[adj] >= node_id[cur] and prev != -1:
                    cut_vertex[cur] = True
            else:
                low_link[cur] = min(low_link[cur], node_id[adj])

        # Special handling for the root: cut vertex if it connects 2 components
        if prev == -1 and c > 1:
            cut_vertex[cur] = True

    N = len(graph)
    node_id = [-1] * N
    low_link = [-1] * N
    cut_vertex = [False] * N
    time = 0

    for u in range(N):
        if node_id[u] == -1:
            dfs(u, -1)

    return [u for u in range(N) if cut_vertex[u]]


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cut = sorted(get_cut_vertices())
print(len(cut))
print("\n".join(map(str, cut)))

"""
Test case 1
6 18
1 2
1 3
1 4
2 5
2 1
2 6
2 4
3 1
3 4
3 5
3 6
4 1
4 2
4 3
5 2
5 3
6 2
6 3
"""
