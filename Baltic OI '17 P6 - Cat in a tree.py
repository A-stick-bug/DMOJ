# https://dmoj.ca/problem/btoi17p6
# Q: Given a tree, what is the max # of nodes you can mark if the distance between marked nodes is at least D
# Since x_i < i, we can treat the graph as a directed tree with smaller node numbers closer to the root
#
# The idea is greedy, mark a node as low in the tree as possible since all markings are weighted the same
# If any distance <D, we simply unmark the closest marked node
#
# TC: O(nlogn), from sorting

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)
N, D = map(int, input().split())

graph = [[] for _ in range(N)]
for a in range(1, N):
    b = int(input())
    graph[b].append(a)

marked = 0


def dfs(cur):
    global marked
    if len(graph[cur]) == 0:  # leaf node, mark it since it is at the bottom (following our greedy strategy)
        marked += 1
        return 0

    dists = []  # closest distances to marked nodes in the current node's children's subtrees
    for adj in graph[cur]:
        sub = dfs(adj) + 1  # distance from highest/closest marked node in this subtree
        dists.append(sub)

    dists.sort(reverse=True)
    while len(dists) >= 2 and dists[-1] + dists[-2] < D:  # remove any conflicts by unmarking the closest ones
        marked -= 1
        dists.pop()

    closest = min(dists)
    if closest == D:  # closest marked node is far enough that we can mark the current node
        marked += 1
        return 0
    else:
        return closest


dfs(0)
print(marked)
