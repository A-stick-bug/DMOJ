"""
https://dmoj.ca/problem/coci13c2p5
Graph theory observations and combinatorics

- find number of possible colorings in a functional/successor graph (at most 1 cycle per component)
- solve for each component separately and multiply the answers
- if we fix the colors in the cycle, each node not in the cycle can be one of (K-1) colors
- find the number of colorings using this https://en.wikipedia.org/wiki/Chromatic_polynomial
- note: if there is no cycle, it's the same as having a cycle of length 1
"""

import sys

sys.setrecursionlimit(100000)

MOD = 10 ** 9 + 7
N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
vis = [False] * (N + 1)


def get_comp(cur, prev, depth):
    global cycle_length, component_size
    vis[cur] = True
    component_size += 1
    c_depth = c_node = -1
    for adj in graph[cur]:
        if adj == prev:
            continue
        if vis[adj]:  # cycle found
            c_depth, c_node = depth, adj
            continue
        temp_depth, temp_node = get_comp(adj, cur, depth + 1)  # cycle found in children
        if c_node == -1:
            c_depth, c_node = temp_depth, temp_node
        if c_node == cur:  # cur is the root of the cycle
            cycle_length = c_depth - depth
    return c_depth, c_node


def color_cycle(nodes):
    if nodes == 1:
        return K
    ways = 1
    for _ in range(nodes):
        ways = (ways * (K - 1)) % MOD
    if nodes % 2 == 0:
        ways = (ways + (K - 1)) % MOD
    else:
        ways = (ways - (K - 1)) % MOD
    return ways


graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    if i != arr[i]:
        graph[i].append(arr[i])
        graph[arr[i]].append(i)

# process each component separately
ways = 1
for i in range(1, N + 1):
    if vis[i]:
        continue
    cycle_length = component_size = 0
    get_comp(i, -1, 0)
    cycle_length += 1  # account for root node
    # print(f"node {i}, size {component_size}, length {cycle_length}")

    in_cycle = cycle_length
    not_in_cycle = component_size - cycle_length

    ways = (ways * color_cycle(in_cycle)) % MOD  # get ways to color cycle
    # get ways to color rest of the tree/graph
    for _ in range(not_in_cycle):
        ways = (ways * (K - 1)) % MOD

print(ways)
