from collections import deque

# adjacency matrix
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

start, end = 0, n-1
q_start = deque([start])
q_end = deque([end])

visited_start = {start: 0}
visited_end = {end: 0}

while q_start and q_end:
    state_start = q_start.popleft()
    distance_start = visited_start[state_start]

    if state_start in visited_end:
        print(distance_start + visited_end[state_start])
        break

    for adj, connected in enumerate(graph[state_start]):
        if connected and adj not in visited_start:
            q_start.append(adj)
            visited_start[adj] = distance_start + 1

    state_end = q_end.popleft()
    distance_end = visited_end[state_end]

    if state_end in visited_start:
        print(distance_end + visited_start[state_end])
        break

    # get neighbours from the other direction if the graph is directional
    for adj, connected in enumerate([graph[i][state_end] for i in range(n)]):
        if connected and adj not in visited_end:
            q_end.append(adj)
            visited_end[adj] = distance_end + 1
