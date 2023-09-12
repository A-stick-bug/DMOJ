# determine is a graph is a tree:
# edges is nodes - 1
# everything is connected

graph = [list(map(int, input().split())) for _ in range(4)]

edges = 0
for i in range(4):
    for j in range(i, 4):
        edges += graph[i][j]

if edges != 3:
    print("No")
else:
    stack = [0]
    visited = [False] * 4
    visited[0] = True

    while stack:
        node = stack.pop()

        adj = graph[node]
        for i in range(4):
            if adj[i]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True

    # print(visited)
    if sum(visited) == 4:
        print("Yes")
    else:
        print("No")
