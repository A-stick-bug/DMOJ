# template BFS problem

import sys

N, M, A, B = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [A]
vis = [False] * (N + 1)
vis[A] = True
while stack:
    cur = stack.pop()
    if cur == B:
        print("GO SHAHIR!")
        sys.exit()

    for adj in graph[cur]:
        if not vis[adj]:
            vis[adj] = True
            stack.append(adj)

print("NO SHAHIR!")
