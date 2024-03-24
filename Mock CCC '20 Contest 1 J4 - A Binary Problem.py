# simple precomputation

n = int(input())
arr = list(map(int, list(input())))

inf = 1 << 30
closest = [inf] * n

left = inf
for i in range(n):
    if arr[i] == 1:
        left = 0
    else:
        left += 1
    closest[i] = left

right = inf
for i in reversed(range(n)):
    if arr[i] == 1:
        right = 0
    else:
        right += 1
    closest[i] = min(closest[i], right)

print(sum(closest))
