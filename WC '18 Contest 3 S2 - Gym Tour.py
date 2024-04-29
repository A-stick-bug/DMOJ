"""
 https://dmoj.ca/problem/wc18c3s2
 Tree pruning strategy

 Key observations:
 - the graph is a tree
 - we can prune off branches that don't contain Pokémon gyms/dragon (similar to CCC 2016 S3)

 The shortest path is done with one of the following methods, try both and get the minimum
 - Visit all nodes without dragon: 2*(P-1) - max_dist,
   where P is the number of nodes after pruning and max_dist is the farthest distance from node 1
 - With dragon: because the dragon lets you teleport to any visited node, you just get the dragon first and visit
   everything else like a dfs traversal, so you only go through each edge once
"""

N, GYMS, DRAGON = map(int, input().split())
gym = set(map(int, input().split()))
graph = [[] for _ in range(N + 1)]  # assuming no dragon usage
graph2 = [[] for _ in range(N + 1)]  # with dragon usage

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph2[a].append(b)
    graph2[b].append(a)


def dfs():  # get farthest distance from 1
    dist = [-1] * (N + 1)
    dist[1] = 0
    stack = [(1, 0)]
    while stack:
        cur, prev = stack.pop()
        for adj in graph[cur]:
            if adj == prev:
                continue
            stack.append((adj, cur))
            dist[adj] = dist[cur] + 1
    return max(dist)


# prune branches without gyms (this is without using dragon)
rem1 = 0
for node in range(2, N + 1):
    while len(graph[node]) == 1 and node not in gym and node != 1:  # leaves only have 1 connection
        prev = node
        node = graph[node][0]
        graph[prev].remove(node)  # remove connection, leaf is moved to the next node
        graph[node].remove(prev)
        rem1 += 1
ans1 = (N - rem1 - 1) * 2 - dfs()  # distance without using dragon, (number of edges) * 2 - (longest path from root)

# prune branches without gyms and without dragon (this is using dragon)
rem2 = 0
for node in range(2, N + 1):
    while len(graph2[node]) == 1 and node not in gym and node != 1 and node != DRAGON:  # leaves only have 1 connection
        prev = node
        node = graph2[node][0]
        graph2[prev].remove(node)  # remove connection, leaf is moved to the next node
        graph2[node].remove(prev)
        rem2 += 1
ans2 = N - rem2 - 1  # distance using dragon, (number of edges)

print(min(ans1, ans2))
