# https://dmoj.ca/problem/coci14c2p3
# Key observations:
# - only groups matter, we just turn all numbers into what group they are in
# - now we just need to find the minimum number of moves to sort the array using insertions
# - seems like n - |LIS| works, not sure why

from bisect import bisect_right


def lis_non_strict(arr):
    """get |LIS|, non-strict increasing"""
    res = []
    for num in arr:
        i = bisect_right(res, num)
        if i == len(res):  # current element is largest
            res.append(num)
        else:
            res[i] = num

    return len(res)


n, k = map(int, input().split())
arr = list(map(int, input().split()))

ordered = sorted(arr)  # turn elements into their group number
loc = {}
for i, v in enumerate(ordered):
    loc[v] = i
for i in range(n):
    arr[i] = loc[arr[i]] // k

print(n - lis_non_strict(arr))
