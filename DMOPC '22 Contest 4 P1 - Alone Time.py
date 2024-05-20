# just try moving every element forwards or backwards and take the best answer

n, m, k = map(int, input().split())
arr = 3 * [0] + list(map(int, input().split())) + [m + 1] * 4

best = 0
for i in range(2, n + 4):
    best = max(best, min(arr[i + 2], arr[i + 1] + k) - arr[i] - 1)
for i in reversed(range(2, n + 4)):
    best = max(best, arr[i] - max(arr[i - 2], arr[i - 1] - k) - 1)
print(best)
