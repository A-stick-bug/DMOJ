# template prefix minimum and prefix maximum problem

n = int(input())
arr = list(map(int, input().split()))

prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = max(prefix[i - 1], arr[i])
suffix = [0] * n
suffix[-1] = arr[-1]
for i in reversed(range(n - 1)):
    suffix[i] = max(suffix[i + 1], arr[i])

total = 0
for i in range(1, n - 1):
    total += max(0, (min(prefix[i], suffix[i]) - arr[i]))
print(total)
