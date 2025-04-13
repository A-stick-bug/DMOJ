# https://dmoj.ca/problem/dmopc14c4p6
# Unweighted version of https://dmoj.ca/problem/thicc17p6 (this one needs rerooting DP)
# - For each node, we need to the find longest path in the tree starting from that node
# - We can use the fact that the farthest distance from a node X is equal to the distance to
#   the farther diameter endpoint
#   - brief proof: by contradiction, if the farthest distance is greater than that of the
#     diameter endpoint, then the diameter endpoint we found would not be optimal
#
# TC: O(n)

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())  # change to 0-indexing
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    """return the distance to every node in the tree starting from start"""
    dist = [-1] * n
    dist[start] = 0
    stack = [start]
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if dist[adj] != -1:
                continue
            dist[adj] = dist[cur] + 1
            stack.append(adj)
    return dist


d1 = dfs(1)
end1 = d1.index(max(d1))  # find first diameter endpoint

d2 = dfs(end1)
end2 = d2.index(max(d2))  # find second diameter endpoint
d3 = dfs(end2)  # find distances from second diameter endpoint

for i in range(n):
    print(max(d2[i], d3[i]) + 1)  # check which endpoint it is farther from
