# MLE, CHECK C++ CODE
# https://dmoj.ca/problem/subway
# Q: count the number of longest paths in a tree
# A: all paths tree DP
#
# TC: O(nlogn), extra logn from sorting paths

from collections import defaultdict

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

path_cnt = [0] * n  # number of paths with length i (only accurate for longest)


def match_longest(paths, longest):
    """count of number of ways of joining 2 paths to form the longest possible"""
    match = defaultdict(int)
    total = 0
    for length, cnt in paths:
        if longest - length in match:
            total += cnt * match[longest - length]
        match[length] += cnt
    return total


def solve(cur, prev):
    if len(graph[cur]) == 1 and cur != 1:  # leaf node: path of length 0 occurs once
        return 0, 1

    # paths starting at the current node and ending below
    # (path length, number of ways of creating this path)
    paths = []
    for adj in graph[cur]:
        if adj == prev:
            continue
        length, cnt = solve(adj, cur)
        paths.append((length + 1, cnt))

    paths.sort(key=lambda x: x[0])  # sort by length
    if len(paths) >= 2:
        longest = paths[-1][0] + paths[-2][0]  # join 2 longest paths
        cnt = match_longest(paths, longest)
        path_cnt[longest] += cnt

    # longest path starting at cur and ending below
    longest, cnt = paths[-1][0], sum(j * (i == paths[-1][0]) for i, j in paths)
    path_cnt[longest] += cnt  # it is possible that the longest path isn't formed by joining 2 nodes
    return longest, cnt


solve(1, -1)
for i in reversed(range(n)):
    if path_cnt[i] != 0:
        print(path_cnt[i])
        break
