# this python code is just for reference, you can't actually use sortedcontainers on DMOJ
# note: you must use c++ with multiset

from sortedcontainers import SortedList

n = int(input())
arr = SortedList(list(map(int, input().split())))

cost = 0
while len(arr) > 1:
    small = arr.pop(0)
    big = arr.pop(-1)
    cost += small
    arr.add(small + big)  # combine smallest with largest is optimal
print(cost)
