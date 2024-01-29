from collections import defaultdict

inf = 1 << 60


def spfa(start, end):
    q = [start]
    dist = defaultdict(lambda: inf)
    dist[start] = 0
    in_q = defaultdict(lambda: False)
    for cur in q:
        in_q[cur] = False
        for adj, d in graph[cur]:
            new_d = dist[cur] + d
            if new_d < dist[adj]:
                dist[adj] = new_d
                if not in_q[adj]:
                    q.append(adj)
                    in_q[adj] = True
    return dist[end]


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = input().split()
    graph[a].append((b, int(c)))

q = int(input())
for _ in range(q):
    a, b = input().split()
    d = spfa(a, b)
    if d == inf:
        print("Roger")
    else:
        print(d)
