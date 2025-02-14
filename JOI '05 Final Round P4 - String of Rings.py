# TLE, 14/20, need weird optimizations
# https://dmoj.ca/problem/joi05fp4
#
# Model the question as a graph
# We are looking for the longest path in the graph (this is NP hard)
# Note: Rings are useless as they don't contribute length

def get_farthest_dist(start):
    vis = [False] * MN
    mx = 0

    def dfs(cur):
        nonlocal mx
        if vis[cur]:
            return 0
        vis[cur] = True
        c = 0
        for adj in graph[cur]:
            c = max(c, dfs(adj) + 1)
        vis[cur] = False
        mx = max(mx, c)
        return c

    dfs(start)
    return mx


MN = 101
n = int(input())
graph = [[] for _ in range(MN)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(max(get_farthest_dist(i) for i in range(1, MN)))
