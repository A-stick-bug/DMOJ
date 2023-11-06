# this question requires you to think very differently
# instead of trying to construct an array with min max subarray sum,
# we binary search for the largest min max subarray sum possible

def works(limit):
    subarrays = 1
    cur = 0
    for val in arr:
        cur += val
        if cur > limit:  # current subarray is full, get a new one
            subarrays += 1
            cur = val
    return subarrays <= M


N, M = map(int, input().split())
arr = list(map(int, input().split()))

low = max(arr)
high = sum(arr)
while low <= high:
    mid = (low + high) // 2
    if works(mid):
        high = mid - 1
    else:
        low = mid + 1

print(low)
