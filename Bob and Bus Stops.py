from bisect import bisect_left, bisect_right
from sys import stdin

input = stdin.readline
n_stops, n_queries = map(int, input().split())
stops = sorted(list(map(int, input().split())))

for _ in range(n_queries):
    left, right = map(int, input().split())
    print(bisect_right(stops, right) - bisect_left(stops, left))
