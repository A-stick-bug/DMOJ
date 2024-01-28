# https://dmoj.ca/problem/dmpg16s5
# same strategy as https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# Using prefix sum array (PSA) and monotonic queue
#
# find maximum subarray sum with length less than K
# we can use a decreasing monotonic queue that stores (index, sum up to index) so we can remove everything up to index
# since it is better to have a greater sum, we want to remove the minimum sum possible, while keeping the length (< K)

from collections import deque
from itertools import accumulate

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split())) * 2  # double array as it is circular
psa = tuple(accumulate(arr))

best = 0
q = deque([0])  # add the option to remove nothing
for i in range(1, 2 * N + 1):
    best = max(best, psa[i] - psa[q[0]])  # remove the minimum possible slice option (so we keep the most)

    while q and psa[q[-1]] >= psa[i]:  # add current sum as an option to remove, only keep smaller sums
        q.pop()
    q.append(i)

    if i - q[0] == K:  # slice is too big, move window
        q.popleft()

print(best)
