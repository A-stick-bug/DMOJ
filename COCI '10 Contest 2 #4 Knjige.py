import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.reverse()

start = arr.index(n)
best = 1
cur = n
for i in range(start + 1, n):
    if arr[i] == cur - 1:
        best += 1
        cur -= 1

print(n - best)
