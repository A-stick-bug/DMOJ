# using prefix sum and monotonic queue

from collections import deque

n, m = map(int, input().split())
slices = list(map(int, input().split()))
slices.extend(slices)  # add an extra copy of it at the end because it is circular

prefix_sum = [0] * (2 * n + 1)
for i in range(1, 2 * n + 1):
    prefix_sum.append(prefix_sum[i - 1] + slices[i - 1])

res = 0  # max deliciousness obtained
q = deque()

for i in range(1, 2 * n + 1):
    while q and i - q[0] > m:
        q.popleft()
    if q:
        res = max(res, prefix_sum[i] - prefix_sum[q[0]])
    while q and prefix_sum[q[-1]] >= prefix_sum[i]:
        q.pop()
    q.append(i)

print(res)
