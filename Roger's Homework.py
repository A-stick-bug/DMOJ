# 80/100, TLE, Python is too slow, check C++ code for alternate solution
# greedy algorithm with heap
# first sort by deadline, then for each question, we remove previous question until we can solve the current one and
# get the best answer out of all days

from heapq import heappop, heappush
import sys

input = sys.stdin.readline
n = int(input())

questions = [list(map(int, input().split())) for _ in range(n)]
questions.sort()  # sort by deadline

solved = []
best = cur = 0

for deadline, pt in questions:
    heappush(solved, pt)  # first pretend we solved this question
    cur += pt
    while len(solved) > deadline:  # we must not solve some previous questions or else we can't solve the current one
        cur -= heappop(solved)  # use a heap so the questions we choose not to solve give the least points

    best = max(best, cur)

print(best)
