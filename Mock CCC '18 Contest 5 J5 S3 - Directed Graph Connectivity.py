# https://dmoj.ca/problem/nccc5j5s3
# check if you can get from 1 to N after removing an edge
# brute force for every edge O(M*(N+M))

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):  # create graph from input
    a, b = map(int, input().split())
    graph[a].append((b, i))  # (adj, edge ID)


def can_reach_N(removed:int):
    stack = [1]
    vis = [False]*(N+1)
    while stack:
        cur = stack.pop()
        if cur == N:
            return True
        for adj, id in graph[cur]:
            if vis[adj] or id == removed:
                continue
            vis[adj] = True
            stack.append(adj)
    return False


for i in range(M):
    if can_reach_N(i):
        print("YES")
    else:
        print("NO")
