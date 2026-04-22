# https://dmoj.ca/problem/oly26practice6
# This problem combines numerous classic concepts
# Simple conceptually, but insane implementation exercise
#
# We get many functional graph components where edges represent that 2 people
# cannot be both selected
#
# Break down each component into cycle + trees
# - The trees can be precomputed by DP
#   - for each tree, we compute optimal if we do/don't take its root (root lies on the cycle)
#   - check this: https://dmoj.ca/problem/dpp
# - Then, do DP on the cycle, ensuring no 2 nodes along the cycle
#   are both selected
#   - Classic circular DP trick, consider take first node and don't take
#      - check this: https://leetcode.com/problems/house-robber-ii/description/

import sys

input = sys.stdin.readline
n = int(input())
arr = [-1] + [int(input()) for _ in range(n)]  # 1-index

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    if arr[i] != -1:
        graph[i].append(arr[i])
        graph[arr[i]].append(i)

vis = [False] * (n + 1)
in_path = [False] * (n + 1)
in_cycle = [False] * (n + 1)
parity = [-1] * (n + 1)


def solve_component(start):
    # get optimal allocation for this component

    def tree_mis(root):
        parent = {root: 0}
        order = [root]
        stack = [root]
        vis[root] = True

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v == parent[u] or in_cycle[v]:
                    continue
                if v in parent:
                    continue
                parent[v] = u
                vis[v] = True
                stack.append(v)
                order.append(v)

        dp0 = {}
        dp1 = {}
        for u in reversed(order):
            s0 = 0
            s1 = 1
            for v in graph[u]:
                if parent.get(v) == u:
                    s0 += max(dp0[v], dp1[v])
                    s1 += dp0[v]
            dp0[u] = s0
            dp1[u] = s1

        return dp0[root], dp1[root]

    # get cycle
    path = []
    cur = start
    cycle = []
    while True:
        if in_path[cur]:
            cycle = path[path.index(cur):]
            break
        vis[cur] = True
        path.append(cur)
        in_path[cur] = True
        if arr[cur] == -1:
            break
        cur = arr[cur]
    for c in cycle:
        in_cycle[c] = True

    # no cycle case
    if not cycle:
        ans = max(tree_mis(start))
    else:
        # precompute trees
        trees = []
        for c in cycle:
            trees.append(tree_mis(c))

        free = sum(x[0] for x in trees)
        gain = [x[1] - x[0] for x in trees]

        def path_mis(weights):
            dp0 = 0
            dp1 = -10 ** 18
            for w in weights:
                ndp0 = max(dp0, dp1)
                ndp1 = dp0 + w
                dp0, dp1 = ndp0, ndp1
            return max(dp0, dp1)

        m = len(cycle)
        if m == 1:
            ans = trees[0][0]
        else:
            ans = free + max(
                path_mis(gain[1:]),  # first cycle node not taken
                gain[0] + path_mis(gain[2:-1])  # first cycle node taken
            )

    # clean up
    for p in path:
        in_path[p] = False
    for c in cycle:
        in_cycle[c] = False
    return ans


total = 0
for i in range(1, n + 1):
    if not vis[i]:
        total += solve_component(i)
print(total)
