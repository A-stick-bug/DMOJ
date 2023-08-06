import sys

input = sys.stdin.readline

n = int(input())

# build a prefix sum array
trees = [0]
for _ in range(n):
    trees.append(trees[-1] + int(input()))

q = int(input())
for _ in range(q):
    start, end = map(int, input().split())
    print(trees[end + 1] - trees[start])
