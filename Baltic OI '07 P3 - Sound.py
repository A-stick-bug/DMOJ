"""
https://dmoj.ca/problem/btoi07p3
Question: Given an array, find all windows of length M where max(window) - min(window) <= C

Monotonic queue approach (many other approaches work as well: https://dmoj.ca/problem/btoi07p3/editorial):
- have 2 deques, one for maximum and one for minimum (decreasing and increasing respectively)
- print the current window START index, if max_q[0] - min_q[0] <= C
"""

from collections import deque

N, M, C = map(int, input().split())
nums = list(map(int, input().split()))

max_q = deque()
min_q = deque()
left = 0  # left is start of window, right is end
no = True  # check if there is no silence

for right in range(N):
    while max_q and nums[max_q[-1]] < nums[right]:
        max_q.pop()
    max_q.append(right)

    while min_q and nums[min_q[-1]] > nums[right]:
        min_q.pop()
    min_q.append(right)

    # check if the length is M, otherwise, it has to be longer
    if (right - left + 1) == M:
        if nums[max_q[0]] - nums[min_q[0]] <= C:  # current window is 'silent'
            print(left + 1)  # +1 because the question is 1-indexed
            no = False

        # increment left pointer, check if the max/min value gets pushed out
        if left == min_q[0]:
            min_q.popleft()
        if left == max_q[0]:
            max_q.popleft()
        left += 1

# corner case: no silence
if no:
    print("NONE")
