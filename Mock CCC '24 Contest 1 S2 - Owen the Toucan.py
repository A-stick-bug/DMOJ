n, k = map(int, input().split())
arr = list(range(1, n + 1))
for i in range(n - k):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(" ".join(map(str, arr)))
