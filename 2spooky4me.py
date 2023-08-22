# https://dmoj.ca/problem/2spooky4me
# difference array using coordinate compression

from collections import defaultdict

N, L, S = map(int, input().split())
diff = defaultdict(int)  # use a dictionary to save space

for _ in range(N):
    a, b, s = map(int, input().split())
    diff[a] += s
    diff[b + 1] -= s

diff = [(loc, scare) for loc, scare in diff.items()]
diff.sort(key=lambda x: x[0])  # sort by location

cur = 0  # spookiness at current house
total = 0
prev = 0  # previous house location

for location, scare in diff:
    if cur < S:
        total += location - prev
    prev = location
    cur += scare

if cur < S:  # check from last point to the end
    total += L - prev

print(total)
