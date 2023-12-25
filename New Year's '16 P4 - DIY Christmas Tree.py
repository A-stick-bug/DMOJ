# https://dmoj.ca/problem/year2016p4
# dfs traversal while keeping track of some numbers
# strategy: draw out a tree and solve by hand, then convert that to code

import sys

input = sys.stdin.readline
n = int(input())
graph = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]  # create graph from input

children = [0] * (n + 1)
res = []


def count_children(cur):
    c = 0
    for adj in graph[cur]:
        count_children(adj)
        c += children[adj] + 1
    children[cur] = c


def dfs(cur, num):
    res.append(num)
    total = children[cur]
    done = 0

    for adj in graph[cur]:
        dfs(adj, num + (total - children[adj]) - done)  # use the largest possible numbers on each subtree
        done += children[adj] + 1


count_children(1)  # first, precompute how many children each node has

dfs(1, 1)
print(*res)
