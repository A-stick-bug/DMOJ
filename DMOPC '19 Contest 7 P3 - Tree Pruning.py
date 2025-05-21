"""
https://dmoj.ca/problem/dmopc19c7p3
Extension of https://codeforces.com/problemset/problem/1446/A on a tree

The main idea is the same
- Don't take anything with value >2k
- If there's any node with value in [k, 2k], just take it and we're done
- Otherwise, taking 1 by 1 is guaranteed to never overshoot 2k
  - Note: since the stuff we take must be connected, individually
          consider each component separated by nodes with value >2k
"""

import sys

input = sys.stdin.readline
N, K = map(int, input().split())

arr = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# check if we can take a single node with value in [k, 2k]
for i in range(1, N + 1):
    if K <= arr[i] <= 2 * K:
        print(1)
        print(i)
        sys.exit()

vis = [False] * (N + 1)


def check_component(start):
    # do a dfs traversal since any prefix is guaranteed to be connected
    vis[start] = True
    order = []
    stack = [start]
    while stack:
        cur = stack.pop()
        order.append(cur)
        for adj in graph[cur]:
            if not vis[adj] and arr[adj] <= 2 * K:  # can't cross nodes with value >2k
                stack.append(adj)
                vis[adj] = True

    cur_sum = 0  # check if this component has >=k
    for i in range(len(order)):
        cur_sum += arr[order[i]]
        if cur_sum >= K:
            print(i + 1)
            print(" ".join(map(str, order[:i + 1])))
            sys.exit()


for i in range(1, N + 1):
    if not vis[i] and arr[i] < K:
        check_component(i)

print(-1)  # nothing found
