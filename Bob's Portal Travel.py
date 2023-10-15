# Olympiads School practice
# First get the length of the cycle and the relative position of nodes in the cycle
# Now we can use K % (length of cycle)

import sys

N, K = map(int, input().split())
adj = [0] + list(map(int, input().split()))  # 1-indexed
dist = [-1 for _ in range(N + 1)]  # dist[i]: portals to get from 1 to i
sys.setrecursionlimit(200001)


def dfs(cur, d):
    if dist[cur] != -1:  # visited this node before
        return dist[cur], d - dist[cur]  # (distance from 1 to cycle, length of cycle)

    dist[cur] = d
    return dfs(adj[cur], d + 1)


d_start, length = dfs(1, 0)
K -= d_start  # takes d_start to get from 1 to the cycle start
if K > 0:
    K %= length  # mod length of the cycle, if we can get there
K += d_start  # add distance to cycle back

print(dist.index(K))