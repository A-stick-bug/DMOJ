from bisect import bisect_right

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

count = 0
for i in range(N):
    j = bisect_right(arr, M - arr[i])
    if j > i:
        count += j - i - 1

print(count)
