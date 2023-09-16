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

from collections import defaultdict
import heapq
from sys import stdin

input = stdin.readline

N, S = map(int, input().split())
apples = [set() for _ in range(N + 1)]
loc = [0] + list(map(int, input().split()))
dist = defaultdict(list)

for _ in range(S):
    stand, k = map(int, input().split())
    if k not in apples[stand]:
        apples[stand].add(k)
        heapq.heappush(dist[k], (loc[stand], stand))

q = int(input())
for _ in range(q):
    query = input().split()

    # stand starts selling a new type of apple
    if query[0] == 'A':
        stand, k = map(int, query[1:])
        apples[stand].add(k)
        heapq.heappush(dist[k], (loc[stand], stand))

    # stands stop selling a type of apple
    elif query[0] == 'S':
        stand, k = map(int, query[1:])
        apples[stand].discard(k)  # prevent error if element is not in set

    # stand changes location and stops selling all apples
    elif query[0] == 'E':
        stand, k = map(int, query[1:])
        apples[stand].clear()  # stand is no longer selling any apples after moving
        loc[stand] = k  # changed location

    # query the distance of a type of apple
    else:
        k = int(query[1])
        if k not in dist:  # stand does not sell apples
            print(-1)
        else:
            # keep popping from the heap until we get a valid apple
            # note: the invalid ones are the ones that are already removed (not in the set)
            while dist[k] and (k not in apples[dist[k][0][1]] or dist[k][0][0] != loc[dist[k][0][1]]):
                heapq.heappop(dist[k])
            if not dist[k]:
                print(-1)
            else:
                print(dist[k][0][1])
