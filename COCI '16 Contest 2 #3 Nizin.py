# basically, merge values until you get a palindrome
# 2 pointer approach:

n = int(input())
nums = list(map(int, input().split()))

merges = 0
l, r = 0, n-1
while r >= l:
    if nums[l] == nums[r]:  # still a palindrome
        l += 1
        r -= 1

    elif nums[l] < nums[r]:  # left is smaller, combine 2 values on the left
        nums[l+1] += nums[l]
        l += 1
        merges += 1

    else:  # right is smaller, combine 2 values on the right
        nums[r-1] += nums[r]
        r -= 1
        merges += 1

print(merges)
