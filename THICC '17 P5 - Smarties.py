# https://dmoj.ca/problem/thicc17p5
# literally the same as https://dmoj.ca/problem/acc3p1 but different input format

n, k = map(int, input().split())
nums = list(map(int, input().split()))

total = (n * (n + 1)) // 2  # total number of sub arrays

freq = [0] * 1_000_001  # this is faster than a dictionary (and defaultdict)
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

    total -= (right - left + 1)  # minus the length of the current window

print(total)
