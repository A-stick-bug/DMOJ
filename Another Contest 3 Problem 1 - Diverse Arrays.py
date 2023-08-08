# TLE, check c++ solution

import sys
from collections import defaultdict

input = sys.stdin.readline  # need this, up to 1 mil lines of input

n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

total = (n * (n + 1)) // 2  # total number of sub arrays

freq = defaultdict(int)
left = 0  # sliding window
for right in range(n):
    freq[nums[right]] += 1

    while len(freq) >= k:
        left_num = nums[left]
        freq[left_num] -= 1
        if freq[left_num] == 0:
            del freq[left_num]
        left += 1

    total -= (right - left + 1)

print(total)
