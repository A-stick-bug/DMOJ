# https://dmoj.ca/problem/bsspc21j6
# Tree DP
# Let a node be 'good' if it has at most 2 children (except root which can have 3)
#
# 2 options when considering subtrees at each node:
#   1. fully cut the subtree (cost = sum of values in subtree)
#   2. keep the subtree by making all nodes in the subtree 'good' (dp to calculate cost)
#      note: we can only keep at most 2 subtrees so the current node stays good (or 3 for the root)
#      Greedy idea: keep the subtrees that saves the most cost compared to fully cutting it
#
# TC: O(nlogn) from sorting

import sys

input = sys.stdin.readline

n = int(input())
arr = [-1, -1] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

fully_cut = [-1, -1] + arr  # cost to prune `i`'s subtree
make_good = [-1] * (n + 1)


def solve(cur, prev):
    fully_cut[cur] = arr[cur]
    if cur != 1 and len(graph[cur]) == 1:  # leaf, base cases
        make_good[cur] = 0
        return

    options = []
    for adj in graph[cur]:
        if adj == prev:
            continue
        solve(adj, cur)
        fully_cut[cur] += fully_cut[adj]
        options.append((fully_cut[adj], make_good[adj]))

    # save the most cost possible when keeping nodes
    options.sort(key=lambda x: x[0] - x[1], reverse=True)

    # EDGE CASE!! we can keep 3 nodes at the root since there's nothing above
    keep = 3 if cur == 1 else 2
    make_good[cur] = sum(b for a, b in options[:keep]) + sum(a for a, b in options[keep:])


solve(1, -1)
print(make_good[1])
