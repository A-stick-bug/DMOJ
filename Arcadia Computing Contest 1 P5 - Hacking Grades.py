# https://dmoj.ca/problem/ahscc1p5
# maximize average = maximize sum since the number of elements is fixed
# always add grades to the one that increases sum/avg by the most

from heapq import heappop, heappush, heapify

N, K = map(int, input().split())
num = list(map(int, input().split()))
denom = list(map(int, input().split()))

grades = list(zip(num, denom))  # x/y fractions

pq = [(-((x + 1) / (y + 1) - x / y), x, y) for x, y in grades]  # max heap
heapify(pq)
for _ in range(K):
    _, x, y = heappop(pq)
    heappush(pq, (-((x + 2) / (y + 2) - (x + 1) / (y + 1)), x + 1, y + 1))

avg = sum(x / y for _, x, y in pq) / N
print(avg * 100)

"""
x+1/y+1 - x/y
"""
