"""
https://dmoj.ca/problem/dmopc17c2p3

Multi start source BFS:
- store distance to nearest rabbit node for every node using reverse method starting from rabbit nodes

Storing path:
- use a parents array to store the path from start to end
- we take the minimum distance from every node in the path to a rabbit node (O(1) per node because we precomputed)

"""

from collections import deque

inf = 1 << 20
N, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# start a BFS from all rabbit locations to get the shortest distance from a point to a rabbit
q = deque([(0, int(input())) for _ in range(R)])  # (dist, location)
closest = [inf] * (N + 1)
for _, r in q:
    closest[r] = 0

while q:
    dist, cur = q.popleft()
    for adj in graph[cur]:
        new_dist = dist + 1
        if closest[adj] > new_dist:  # found a shorter path
            closest[adj] = new_dist
            q.append((new_dist, adj))

# now that we know the distance from every point to a rabbit, we just get the lowest distance in the path of the carrot
# since it is a tree, there is only 1 possible path
start, end = map(int, input().split())
q = deque([start])

parents = [0] * (N+1)
vis = [False] * (N + 1)
vis[start] = True

# use BFS to find the path from start to end, store path using an array that shows the reversed path (parents)
while q:
    cur = q.popleft()
    if cur == end:
        break
    for adj in graph[cur]:
        if vis[adj]:
            continue
        vis[adj] = True
        q.append(adj)
        parents[adj] = cur

res = inf  # closest distance to rabbit
node = end
while node != 0:  # go through the path to find min distance to rabbit
    res = min(res, closest[node])
    node = parents[node]

print(res)
