"""
https://dmoj.ca/problem/dpg
Q: find the longest path in a DAG
Classic graph DP problem
"""

from functools import cache
import sys

sys.setrecursionlimit(100005)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # create DAG from input
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


@cache
def solve(cur):
    if not graph[cur]:  # base case: no adjacent nodes
        return 0
    longest = 0
    for adj in graph[cur]:  # find the longest path
        longest = max(longest, solve(adj))
    return longest + 1  # add the current node to the distance


print(max(solve(u) for u in range(1, N + 1)))
