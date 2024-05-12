# WARNING: VERY CLOSE TO TIME LIMIT
# https://dmoj.ca/problem/si17c3p5
#
# Template centroid decomposition
# - Start off with the centroid as the root
# - Get all subtree path values and join 2 paths passing through the current node that add to 1 or -1
#   - we can use a dict (2-sum method) to do this in O(n)
# - Remove the centroid and do the same for all subtrees
#
# This will guarantee that every path in the tree is considered (processed N^2 paths efficiently)
# TC: O(nlogn)

import sys
from collections import defaultdict

sys.setrecursionlimit(100000)  # set to 200000 if submitting with PY3, keep as it is with PYPY3
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = input().split()
    a, b = int(a), int(b)
    graph[a].append((b, 1 if c == "r" else -1))
    graph[b].append((a, 1 if c == "r" else -1))

size = [0] * (N + 1)
cut = [False] * (N + 1)  # determine is node i is removed
total = 0


def get_sizes(cur, prev):
    size[cur] = 1
    for adj, _ in graph[cur]:
        if adj == prev or cut[adj]:
            continue
        get_sizes(adj, cur)
        size[cur] += size[adj]


def get_centroid(cur, prev, comp_size):
    for adj, _ in graph[cur]:
        if not cut[adj] and adj != prev and size[adj] > comp_size // 2:
            return get_centroid(adj, cur, comp_size)
    return cur


def get_paths(cur, prev):  # get all path values ending in cur's subtree
    stack = [(0, cur, prev)]
    paths = []
    while stack:
        val, cur, prev = stack.pop()
        paths.append(val)
        for adj, adj_v in graph[cur]:
            if not cut[adj] and adj != prev:
                stack.append((val + adj_v, adj, cur))
    return paths


def solve(root):  # solve all paths in root's subtree
    global total
    get_sizes(root, -1)
    centroid = get_centroid(root, -1, size[root])  # centroid of this component

    match = defaultdict(int)  # 2-sum strategy to match pairs that add to 1 and -1
    match[0] = 1  # extra option: don't join 2 paths, just use 1
    for adj, val in graph[centroid]:  # collect subtree paths
        if cut[adj]:
            continue
        adj_path = list(map(lambda x: x + val, get_paths(adj, centroid)))  # include edge from here to children

        for le in adj_path:  # try to match current length
            total += match[1 - le] + match[-1 - le]
        for le in adj_path:  # add current length as a matching option
            match[le] += 1

    cut[centroid] = True  # disconnect centroid
    for adj, _ in graph[centroid]:  # solve for all subtrees
        if not cut[adj]:
            solve(adj)


solve(1)
print(total - (N - 1))
