from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

res = []
for n in arr:
    i = bisect_left(res, n)
    if i == len(res):  # current element is largest
        res.append(n)
    else:
        res[i] = n

print(len(res))
