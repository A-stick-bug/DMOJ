# https://dmoj.ca/problem/dwite09c1p5
# cycle detection using dfs (backtracking)

def dfs(cur, d):
    # cur: current node, d: distance to current node from start
    if dist[cur] == inf:
        dist[cur] = d  # haven't explored this yet
    else:
        return d - dist[cur]  # found cycle

    for adj in graph[cur]:
        a = dfs(adj, d + 1)  # try exploring further
        if a:
            return a

    dist[cur] = inf  # backtrack
    return False


inf = 1000
for _ in range(5):
    n = int(input())
    graph = [[] for _ in range(101)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)

    dist = [inf] * 101
    print(dfs(1, 0))
