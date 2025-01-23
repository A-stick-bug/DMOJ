import sys

avg = int(input())
n = int(input())

req = 80 * (n + 1)
cur = avg * n
last = req - cur

if last <= 100:
    print(max(0, last))
else:
    print(-1)
