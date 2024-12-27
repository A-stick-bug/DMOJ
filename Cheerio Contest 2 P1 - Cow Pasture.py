from math import dist

x, y, n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda a: dist(a, (x, y)))

print(dist(arr[m - 1], (x, y)))
