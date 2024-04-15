# note that due to low constraints, we need memory efficiency

from bisect import bisect_left
from array import array

n = int(input())

res = array("i", [])
for n in map(int, input().split()):
    i = bisect_left(res, n)
    if i == len(res):  # current element is largest
        res.append(n)
    else:
        res[i] = n

print(len(res))
