import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

locs = [tuple(map(int, input().split())) for _ in range(K)]
locs.sort(key=lambda x: (x[0], -x[1]))

cnt = 0
total = 0
prev = -1
for idx in range(K):
    if locs[idx][0] == prev:
        cnt -= 1
    else:
        total += cnt
        prev = locs[idx][0]

        cnt = locs[idx][1]

print(total + cnt)
