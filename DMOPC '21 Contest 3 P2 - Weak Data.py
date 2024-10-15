# https://dmoj.ca/problem/dmopc21c3p2
# - Binary search and math
# - Cheese by OEIS and observations
# - For an array of length N, we can put all zeros on the left and 1 on the right
#   This will still give us all possible counts of even sum subarrays
# - f(x,y) = array with x elements, first y elements are 0 (0 <= y <= x <= 10^6)
# - We can compute f(x,y) using math and try all values of x, binary search for y

import sys


def f(x, y):
    part1 = x * x // 4
    if x % 2 == 1:
        y += 1
        part2 = (y // 2) * (y // 2)
    else:
        part2 = (y // 2) * (y // 2 + 1)
    return part1 + part2


K = int(input())
MN = 10 ** 6

if K > MN * (MN + 1) // 2:  # too many
    print(-1)
    sys.exit()

for n in range(1, 10 ** 6 + 1):
    lower = f(n, 0)
    upper = f(n, n)
    if not (lower <= K <= upper):  # not in range
        continue

    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if f(n, mid) == K:
            arr = [0] * mid + [1] * (n - mid)
            print(len(arr))
            print(" ".join(map(str, arr)))
            sys.exit()
        elif f(n, mid) < K:
            low = mid + 1
        else:
            high = mid - 1

print(-1)

# def slow_solve(arr):  # count even subarrays
#     n = len(arr)
#     from itertools import accumulate
#     arr = list(map(lambda x: x % 2, arr))
#     psa = [0] + list(accumulate(arr, func=lambda x, y: x ^ y))
#     cnt = [1, 0]
#     total = 0
#     for i in range(1, n + 1):
#         total += cnt[psa[i]]
#         cnt[psa[i]] += 1
#     return total
