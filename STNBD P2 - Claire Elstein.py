# ඞඞඞ
# https://dmoj.ca/problem/stnbd2
# DAG graph DP, you can basically think of it as tree DP if you expand the cached computations
# update the current node's state using each children's subtrees

import sys

MOD = 10 ** 9 + 7
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
root = [True] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    root[b] = False

paths = [0] * (N + 1)  # number of paths in i's subtree
ways = [-1] * (N + 1)  # (DP state) number of ways to reach endpoints from current node


def solve(cur):
    if len(graph[cur]) == 0:  # leaf node
        paths[cur] = 1  # there is technically a path of length 0 in a leaf's subtree
        return 0
    if ways[cur] != -1:  # return cache
        return ways[cur]

    total = 0
    for adj in graph[cur]:
        subtree_sum = solve(adj)
        paths[cur] += paths[adj]
        # note: we add the number of paths in the subtree since we are adding 1 to the length of all those paths
        total = (total + subtree_sum + paths[adj]) % MOD

    ways[cur] = total  # create cache
    return ways[cur]


total = 0
for i in range(1, N + 1):
    if root[i]:
        total = (total + solve(i)) % MOD
print(total)


"""
Example Input:
7 6
1 2
1 3
3 4
3 5
4 6
2 7

Example Output:
7
"""
