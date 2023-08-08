# https://dmoj.ca/problem/acc3p1
# using a frequency array and sliding window, and some weird subarray formula

import sys

input = sys.stdin.readline  # need this, up to 1 mil lines of input

n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

total = (n * (n + 1)) // 2  # total number of sub arrays

freq = [0] * (n + 1)  # this is faster than a dictionary (and defaultdict)
unique = 0  # unique elements in current window
left = 0  # sliding window
for right in range(n):
    if freq[nums[right]] == 0:  # element not in window
        unique += 1
    freq[nums[right]] += 1

    while unique >= k:  # move pointer until there is less than K unique elements
        left_num = nums[left]
        freq[left_num] -= 1
        if freq[left_num] == 0:  # element moved out of window
            unique -= 1
        left += 1

    total -= (right - left + 1)

print(total)
