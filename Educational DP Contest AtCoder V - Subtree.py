# https://dmoj.ca/problem/dpv
# Tree rerooting DP
# Note:
# - When rerooting, we take the product of the children except the ones we are rerooting towards
# - Since M is not always prime (no mod inverse), we just use prefix and suffix products to exclude 1 single element
#
# TC: O(n)

import sys
from itertools import accumulate

input = sys.stdin.readline
sys.setrecursionlimit(200000)

N, M = map(int, input().split())
mod_mul = lambda x, y: x * y % M

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# number of ways of selecting x's subtree (rooted at 1), must take x
ways = [1] * (N + 1)


def solve_root(cur, prev):
    total = 1
    for adj in graph[cur]:
        if adj == prev:
            continue
        solve_root(adj, cur)
        total = (total * (ways[adj] + 1)) % M  # +1 to include option of not taking subtree
    ways[cur] = total


ans = [-1] * (N + 1)


def reroot(cur, prev, ways_above):
    if cur != 1:
        graph[cur].remove(prev)
    child_ways = [ways[adj] + 1 for adj in graph[cur]]

    prefix = list(accumulate(child_ways, func=mod_mul)) + [1]  # negative indexing padding
    suffix = list(accumulate(child_ways[::-1], func=mod_mul))[::-1] + [1]

    if cur != 1:  # non-root nodes can choose to take nothing above
        ways_above += 1

    ans[cur] = ways[cur] * ways_above % M

    for i in range(len(graph[cur])):
        adj = graph[cur][i]
        above = prefix[i - 1] * suffix[i + 1] % M
        reroot(adj, cur, above * ways_above % M)


solve_root(1, -1)
reroot(1, -1, 1)

print("\n".join(map(str, ans[1:])))

"""
4 99999999999999999
1 2
2 3
2 4
"""

# # brute force method without rerooting, O(n^2)
# for root in range(1, N + 1):
#     ways = [1] * (N + 1)
#     solve_root(root, -1)
#     print(ways[root])
