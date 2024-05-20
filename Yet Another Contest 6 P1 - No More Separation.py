# https://dmoj.ca/problem/yac6p1
# minimize the sum of distances of all paths
# by intuition, it makes sense to build a star graph
# then we can just connect any 2 not already connected edges with the leftover ones

def solve():
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]

    star_edges = min(m, n - 1)
    extra_edges = m - star_edges

    for i in range(star_edges):
        graph[0][i + 1] = 1

    for i in range(n):
        for j in range(i + 1, n):
            if extra_edges == 0:
                break
            if graph[i][j]:  # already connected
                continue
            extra_edges -= 1
            graph[i][j] = 1

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j]:
                print(i + 1, j + 1)


solve()
