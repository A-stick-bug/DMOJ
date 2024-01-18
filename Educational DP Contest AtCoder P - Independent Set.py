# https://dmoj.ca/problem/dpp
# Simple Tree DP problem
# Each node can be painted white or black, 2 adjacent nodes can't be both black
#
# Tip: for these tree DP questions, try to find a way to combine a node's children's answers in O(n)
# in this case, we multiply their answers

import sys
from functools import cache

sys.setrecursionlimit(400000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


@cache
def solve(cur, color, prev):
    total = 1
    for adj in graph[cur]:
        if adj == prev:
            continue
        if color:  # black node: next one must be white
            total *= solve(adj, 0, cur)
        else:  # white node: next one can be either black or white
            total *= (solve(adj, 0, cur) + solve(adj, 1, cur))
    return total % MOD


print((solve(1, True, -1) + solve(1, False, -1)) % MOD)
