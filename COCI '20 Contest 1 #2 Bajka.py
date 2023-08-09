# BFS, passes in python

from collections import deque
from sys import exit

n, m = map(int, input().split())
str1 = input()
str2 = input()

times = [[-1] * n for _ in range(m)]
q = deque()
for i in range(n):
    if str1[i] == str2[0]:
        times[0][i] = 0
        q.append((0, i))

while q:
    index, pos = q.popleft()
    if index == m - 1:
        print(times[index][pos])
        exit()

    if str1[pos] == str2[index]:  # matched letter
        if pos - 1 >= 0 and str2[index + 1] == str1[pos - 1] and times[index + 1][pos - 1] == -1:
            times[index + 1][pos - 1] = times[index][pos] + 1
            q.append((index + 1, pos - 1))

        if pos + 1 < n and str2[index + 1] == str1[pos + 1] and times[index + 1][pos + 1] == -1:
            times[index + 1][pos + 1] = times[index][pos] + 1
            q.append((index + 1, pos + 1))

    # letter did not match
    if pos - 1 >= 0 and times[index][pos - 1] == -1:
        times[index][pos - 1] = times[index][pos] + 1
        q.append((index, pos - 1))

    if pos + 1 < n and times[index][pos + 1] == -1:
        times[index][pos + 1] = times[index][pos] + 1
        q.append((index, pos + 1))

print(-1)


# # Dijkstra's algorithm, TLE in python, same algorithm passes in c++ and java
#
# from collections import defaultdict
# import sys
# import heapq
#
# n, m = map(int, input().split())
# str1 = input()
# str2 = input()
#
# graph = defaultdict(list)  # store the indices of each letter
# for i, char in enumerate(str1):
#     graph[char].append(i)
#
# pq = [(0, i, 0) for i in graph[str2[0]]]
# heapq.heapify(pq)
#
# times = [[1_000_000] * m for _ in range(n)]
# while pq:
#     time, pos, index = heapq.heappop(pq)  # current index
#     if index == m-1:  # reached last letter
#         print(time)
#         sys.exit()
#
#     if times[pos][index] < time:
#         continue
#
#     for adj in graph[str1[pos]]:  # try moving to same letter
#         if adj == pos:
#             continue
#
#         new_time = time + abs(pos - adj)
#         if times[adj][index] > new_time and str1[adj] == str2[index]:
#             times[adj][index] = new_time
#             heapq.heappush(pq, (new_time, adj, index))
#
#     index += 1
#     new_time = time + 1
#     if pos != 0:  # move left
#         adj = pos - 1
#         if str1[adj] == str2[index]:  # valid next letter
#             if times[adj][index] > new_time:
#                 times[adj][index] = new_time
#                 heapq.heappush(pq, (time + 1, pos - 1, index))
#
#     if pos != n-1:  # move right
#         adj = pos + 1
#         if str1[adj] == str2[index]:
#             if times[adj][index] > new_time:
#                 times[adj][index] = new_time
#                 heapq.heappush(pq, (time + 1, pos + 1, index))
#
# print(-1)
