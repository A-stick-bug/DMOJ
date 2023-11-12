# https://dmoj.ca/problem/deathgun
# topological sort, with a heap to output names in correct order

import heapq
from collections import defaultdict, deque

n = int(input())

order = {}
in_degree = defaultdict(int)  # a is being restricted by in_degree[a] people
graph = defaultdict(list)  # person b restricts graph[b] (must go to b before going to any node in graph[b])

i = 0
for _ in range(n):
    a, b = input().split()
    graph[b].append(a)
    in_degree[a] += 1
    if a not in order:  # keep track of order of the people in the input
        order[a] = i
        i += 1
    if b not in order:
        order[b] = i
        i += 1

# add people with no restrictions
pq = []
for person in order:
    if in_degree[person] == 0:
        pq.append((order[person], person))
heapq.heapify(pq)  # use heapq to print the people who appeared in the list earlier first

# topo sort to get order
while pq:
    rank, cur = heapq.heappop(pq)
    print(cur)
    for restriction in graph[cur]:
        in_degree[restriction] -= 1
        if in_degree[restriction] == 0:
            heapq.heappush(pq, (order[restriction], restriction))
