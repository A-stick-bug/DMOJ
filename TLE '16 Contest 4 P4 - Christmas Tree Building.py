"""
https://dmoj.ca/problem/tle16c4p4
Tree radius and diameter
Q: create a tree with maximum or minimum height (you can choose the root) given pieces of the tree (connect a forest)

Let the center of a tree be the node that minimized the tree's height whe rooted there
We know that the center will always be on the diameter and divides it as evenly as possible

- To make the greatest height tree, we put all trees in a line, along their diameters and connect them
- To make the smallest height tree, we join all trees at their center (we first need to find the radius of all trees)
  note that we need to increase every radius by 1 as connecting them to another tree takes and edge of length 1
  HOWEVER, we don't need to minus the highest radius by 1 since if we make it the root, it won't get any extra length

"""
import sys


def dfs(start):
    """returns the distance to every other node (in the same component) from a starting point"""
    dist = {start: 0}
    stack = [start]
    while stack:
        cur = stack.pop()
        for adj, d in graph[cur]:
            if adj in dist:
                continue
            dist[adj] = dist[cur] + d
            stack.append(adj)
    return dist


input = sys.stdin.readline
N, M, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

if Q == 1:  # maximize height
    vis = [False] * (N + 1)
    total = 0

    for i, v in enumerate(graph):
        if not v or vis[i]:  # node does not exist yet or already visited
            continue

        end1 = max(dfs(i).items(), key=lambda x: x[1])[0]  # find first diameter endpoint
        end2 = dfs(end1)
        diameter = max(end2.items(), key=lambda x: x[1])[1]
        for i in end2:
            vis[i] = True
        total += diameter

    print(total + (N - M - 1))  # sum of diameters + distance to join them together

else:  # minimize height
    if M == 0:  # corner case: no edges given, so we can just make a star graph
        print(1)
        sys.exit()

    vis = [False] * (N + 1)
    radii = []

    for i, v in enumerate(graph):
        if not v or vis[i]:  # node does not exist yet or already visited
            continue

        # to find radius, we first need the diameter
        end1 = max(dfs(i).items(), key=lambda x: x[1])[0]  # find first diameter endpoint
        dist1 = dfs(end1)
        end2 = max(dist1.items(), key=lambda x: x[1])[0]
        dist2 = dfs(end2)

        # find node along diameter and divides most evenly
        smallest = float('inf')
        for node in dist1:
            smallest = min(smallest, max(dist1[node], dist2[node]))
        radii.append(smallest)

        for node in dist1:
            vis[node] = True

    radii = list(map(lambda x: x + 1, radii))  # it takes an edge to connect the trees
    radii[radii.index(max(radii))] -= 1  # minus 1 from highest radius which will be the root
    print(max(radii))
