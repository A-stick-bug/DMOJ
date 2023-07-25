# O(n), simple greedy approach (yes, it the same code as Leetcode 376: Wiggle Subsequence)
# basically just find the number of times that the sequences goes from increase to decreasing and vice versa
# the actual difference between numbers is ignored

n = int(input())
nums = list(map(int, input().split()))

res = 1
prev = 0  # 0 is default, 1 means decreasing, 2 means increasing

for i in range(1, n):
    if nums[i] == nums[i - 1]:  # if 2 consecutive numbers are the same, we just ignore it
        continue
    elif nums[i] > nums[i - 1] and (prev == 1 or prev == 0):  # the last sequence was decreasing, now increasing
        prev = 2
        res += 1
    elif nums[i] < nums[i - 1] and (prev == 2 or prev == 0):  # the last sequence was increasing, now decreasing
        prev = 1
        res += 1

print(res)
