# https://dmoj.ca/problem/yac3p4
# We want to find the answer in log2(n) queries
# In other words, we must cut the search space in half with the information from every query
# Split tree in half -> centroid decomposition
#
# - Every time, we query the current search space's centroid so that when we get the answer for
#   a closer node, we simply narrow down the search space to that subtree
# - Note that since we queried the centroid, all subtrees have at most half the original size
# - When repeating this, we must compute the subtree sizes (to help find centroid) for the new subtree
#   and disconnect the previous root (so the other half of the tree isn't accessed)

import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

N = int(input())
graph = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

size = [0] * (N + 1)  # number of nodes in i's subtree


def compute_size(cur, prev):  # compute [size] for a component
    size[cur] = 1  # base case
    for adj in graph[cur]:
        if adj == prev:
            continue
        compute_size(adj, cur)
        size[cur] += size[adj]


def get_centroid(cur, prev, comp_size):  # find the centroid in cur's component
    for adj in graph[cur]:
        if adj != prev and size[adj] > comp_size // 2:
            return get_centroid(adj, cur, comp_size)
    return cur


root = 1  # current search space's root
while True:
    compute_size(root, -1)  # compute the subtree sizes for the current search space
    centroid = get_centroid(root, -1, size[root])
    print(centroid)
    sys.stdout.flush()  # MUST HAVE THIS OR ELSE TLE
    closer = int(input())  # this is the subtree we want to go to

    if closer == 0:  # found answer
        break

    for adj in graph[centroid]:  # disconnect centroid
        graph[adj].remove(centroid)

    root = closer  # change root to the new subtree's
