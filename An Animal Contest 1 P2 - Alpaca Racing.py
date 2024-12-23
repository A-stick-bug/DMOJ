# https://dmoj.ca/problem/aac1p2
# remember to break early

import sys

n, d, k, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
p = int(input())

for i in a:
    while i >= p:
        i = i * (100 - x) // 100
        if k == 0:
            print("NO")
            sys.exit()
        k -= 1
print("YES")
