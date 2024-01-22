from itertools import accumulate

MN = 10 ** 6
n, k = map(int, input().split())
arr = list(map(int, input().split()))
psa = [0]+list(accumulate(arr))

rem = [-1] * (MN + 1)
for i, val in enumerate(psa):
    if rem[val % k] == -1:
        rem[val % k] = i

best = 0
for i, val in enumerate(psa):
    if rem[val % k] != -1:
        best = max(best, i - rem[val % k])

print(best)
