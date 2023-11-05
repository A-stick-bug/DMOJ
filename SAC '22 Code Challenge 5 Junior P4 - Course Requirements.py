# https://dmoj.ca/problem/sac22cc5jp4
# template topological sort question
# using python built-in

from graphlib import TopologicalSorter
import sys

input = sys.stdin.readline
N = int(input())

pre_req = {i: list(map(int, input().split()))[1:] for i in range(1, N + 1)}  # create graph from input
ts = TopologicalSorter(pre_req)

print(*ts.static_order())
