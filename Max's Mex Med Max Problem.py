# https://dmoj.ca/problem/mexmedmax
# Binary search, loop over possible MEX values while maintaining the current range
# To ensure the median is >=X, we ensure at least half the numbers (offset -1) are greater

def f(x):
    loc = [-1] * N
    for i, v in enumerate(arr):
        loc[v] = i

    l = r = loc[0]  # current range with mex, may extend l and r to manipulate median
    mex = 1
    total = 0

    while mex < N:
        idx = loc[mex]
        if l <= idx <= r:  # already contained, skip
            mex += 1
            continue

        target = mex - x  # want median <= target

        lesser = target + 1 - (x == 0)  # number of elements <= target, note that [0,mex-1] all exist in [l,r]
        more = (r - l + 1) - lesser
        delta = lesser - more
        delta += 1  # non strict

        # note that everything outside [l,r] is >=mex, thus >=target (they only make median higher than we want)

        if idx < l:  # expand left
            r_to_n = N - r
            total += max(0, min(r_to_n, delta))
            for i in reversed(range(idx + 1, l)):
                delta -= 1
                total += max(0, min(r_to_n, delta))
            l = idx

        else:  # expand right
            zero_to_l = l + 1
            total += max(0, min(zero_to_l, delta))
            for i in range(r + 1, idx):
                delta -= 1
                total += max(0, min(zero_to_l, delta))
            r = idx
        mex += 1

    # extra case: mex = N, take entire array
    if N - x >= (N - 1) // 2:
        total += 1

    return total


N, K = map(int, input().split())
arr = list(map(int, input().split()))
# print(f(3))
low = 0
high = N
ans = -1
while low <= high:
    mid = (low + high) // 2
    if f(mid) >= K:
        low = mid + 1
        ans = mid
    else:
        high = mid - 1

print(ans)
