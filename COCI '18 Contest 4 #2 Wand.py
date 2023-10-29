# https://dmoj.ca/problem/coci18c4p2
# simple bfs/dfs starting from the nodes adjacent to the start

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # make graph from input
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)  # if a and b fight, a will win and b gives the wand to a

vis = set()
res = [0] * (N + 1)


def dfs(cur):
    if cur in vis:
        return
    vis.add(cur)

    res[cur] = 1
    for adj in graph[cur]:
        dfs(adj)


if not graph[1]:  # corner case: person 1 doesn't need to face anyone (can keep wand)
    res[1] = 1

for second in graph[1]:  # start from the second nodes to check if 1 can have the wand
    dfs(second)
print(*res[1:], sep="")
