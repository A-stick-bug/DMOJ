# https://dmoj.ca/problem/dmopc21c5p1
# for 2 numbers' sum to be non-prime, we can just make it even
# for the middle gap, we use 7 and 2 because 9 is the smallest composite odd number

import sys

n = int(input())

if n == 1:
    print(1)
    sys.exit()
elif n < 5:
    print(-1)
    sys.exit()

arr = []
for i in range(1, n + 1, 2):
    if i == 7:
        continue
    arr.append(i)

if n >= 7:
    arr += [7,2]  # smallest non-prime odd number

for i in range(4, n+1, 2):
    arr.append(i)

if 7 > n > 1:
    arr.append(2)

print(*arr)
