# https://dmoj.ca/problem/bbc09c
# - The path taken will be a modified Euler Tour
# - Fix the nodes bottom up

import sys

input = sys.stdin.readline
sys.setrecursionlimit(500000)

n = int(input())
arr = [-1] + [input().strip() == "1" for _ in range(n)]
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

arr[1] ^= 1  # flip first node since we start there
path = []


def visit(node):
    path.append(node)
    arr[node] ^= 1


def solve(cur, prev):
    visit(cur)

    for adj in graph[cur]:
        if adj == prev:
            continue
        solve(adj, cur)

        visit(cur)

        if not arr[adj]:  # fix children
            visit(adj)
            visit(cur)


solve(1, -1)

if not arr[1]:  # corner case: fix root
    visit(graph[1][0])
    visit(1)
    visit(graph[1][0])

print(" ".join(map(str, path)))
