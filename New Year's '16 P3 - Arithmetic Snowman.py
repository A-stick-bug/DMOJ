from bisect import bisect_left, bisect_right
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = Counter(arr)
exists = lambda a, el: bisect_left(a, el) != bisect_right(a, el)

best = 0
for i in range(1, n - 1):
    for j in range(i):
        diff = (arr[i] - arr[j])
        third = arr[i] + diff
        if diff == 0:
            if cnt[arr[i]] >= 3:
                best = max(best, arr[i] * 3)
        else:
            if exists(arr, third):
                best = max(best, arr[i] * 3)
print(best)
