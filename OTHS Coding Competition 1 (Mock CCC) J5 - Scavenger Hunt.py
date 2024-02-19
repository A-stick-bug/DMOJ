# https://dmoj.ca/problem/othscc1p5
# 2D dijkstras with virtual edges to handle more than 1 consecutive item in a building and creating items yourself

from heapq import heappop, heappush

N, M, T = map(int, input().split())
make_item = [0] + list(map(int, input().split()))  # cost of making item yourself
nt = list(map(int, input().split()))

item_loc = [None] + [[False] * (N + 1) for _ in range(T)]  # if item_loc[i][j] is True, item i is present at node j
for t in range(1, T + 1):
    a = list(map(int, input().split()))
    for b in a:
        item_loc[t][b] = True

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# a building can have more than 1 item, so we want to come back and check if the next item is also here
for a in range(1, N + 1):
    graph[a].append((a, 0))

# solve
inf = 1 << 60
dist = [[inf] * (T + 1) for _ in range(N + 1)]
dist[1][0] = 0
pq = [(0, 1, 0)]

while pq:
    d, cur, t = heappop(pq)
    if t == T:
        print(d)
        break
    if dist[cur][t] < d:
        continue
    for adj, adj_d in graph[cur]:
        new_d = d + adj_d
        if item_loc[t + 1][adj]:  # collect item here, move on to next item
            if dist[adj][t + 1] > new_d:
                dist[adj][t + 1] = new_d
                heappush(pq, (new_d, adj, t + 1))
        else:
            if dist[adj][t] > new_d:
                dist[adj][t] = new_d
                heappush(pq, (new_d, adj, t))

    # consider making item yourself
    new_d = d + make_item[t + 1]
    if new_d < dist[cur][t + 1]:
        dist[cur][t + 1] = new_d
        heappush(pq, (new_d, cur, t + 1))
