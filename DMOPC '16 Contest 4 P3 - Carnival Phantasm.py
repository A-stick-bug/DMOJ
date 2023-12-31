"""
https://dmoj.ca/problem/dmopc16c4p3
Based on this person's solution: https://dmoj.ca/submission/5606773

Highly not recommended to do this in python

Question rephrase/simplification:
The N stands in a line, S of them are selling apples at the start
Next line has N integers containing the locations on each stand
Next S lines has what the stands are selling at the start

Then we answer queries which are:
- stand switches to selling different flavors
- stand stops selling
- stand changes location

"""

import heapq
from sys import stdin

input = stdin.readline

N, S = map(int, input().split())
loc = [0] + list(map(int, input().split()))  # loc[i] is the distance from the start to stand i
stands = [set() for _ in range(N + 1)]  # keep track of what apples each stand sells
dist = [[] for _ in range(101)]  # stores the minimum distance to each apple flavor (100 unique flavors at most)

for _ in range(S):
    stand, k = map(int, input().split())
    if k not in stands[stand]:
        stands[stand].add(k)
        heapq.heappush(dist[k], (loc[stand], stand))

q = int(input())
for _ in range(q):
    query = input().split()

    # stand starts selling a new type of apple
    if query[0] == 'A':
        stand, k = map(int, query[1:])
        stands[stand].add(k)
        heapq.heappush(dist[k], (loc[stand], stand))  # add this stand to the list that sells flavor k

    # stands stop selling a type of apple
    elif query[0] == 'S':
        stand, k = map(int, query[1:])
        stands[stand].discard(k)  # prevent error if element is not in set

    # stand changes location and stops selling all apples
    elif query[0] == 'E':
        stand, k = map(int, query[1:])
        stands[stand].clear()  # stand is no longer selling any apples after moving
        loc[stand] = k  # changed location

    # query the distance of a type of apple
    else:
        k = int(query[1])

        # keep removing the old/invalid values from the heap, then the one at the top will be the minimum distance apple
        #             the stand stopped selling this flavor    this location is outdated (stand moved)
        while dist[k] and (k not in stands[dist[k][0][1]] or dist[k][0][0] != loc[dist[k][0][1]]):
            heapq.heappop(dist[k])

        if not dist[k]:  # no stands sell this apple
            print(-1)

        else:  # the minimum distance that is valid is now at the top of the heap
            print(dist[k][0][1])
