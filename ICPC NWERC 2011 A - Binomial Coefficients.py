# https://dmoj.ca/problem/nwerc11a
# Useful observation:
# - Pascal's triangle is symmetric, we will only use the left side
# - The center of Pascal's triangle grows exponentially
#   - This means there will be only around log(n) possible K values in nCk
#
# Approach: brute force all values of K and binary search the respective N value
#
# TC: O(T * log^2(n))

from math import comb

ranges = [(44721361, 2), (181714, 3), (12449, 4), (2608, 5), (950, 6), (473, 7), (286, 8), (197, 9), (148, 10),
          (119, 11), (100, 12), (87, 13), (78, 14), (72, 15), (67, 16), (63, 17), (61, 18), (59, 19), (57, 20),
          (56, 21), (55, 22), (54, 23), (54, 24), (54, 25), (54, 26), (54, 27)]


def solve():
    def add_pair(a, b):
        res.append((a, b))
        if b != a - b:
            res.append((a, a - b))

    n = int(input())

    res = []
    add_pair(n, 1)  # trivial case

    for mx, k in ranges:
        low = 2
        high = mx
        while low <= high:
            mid = (low + high) // 2
            val = comb(mid, k)
            if val == n:
                add_pair(mid, k)
                break
            elif val > n:
                high = mid - 1
            else:
                low = mid + 1

    # format output
    res = sorted(set(res))
    str_res = [f"({a},{b})" for a, b in res]
    print(len(res))
    print(" ".join(str_res))


for _ in range(int(input())):
    solve()

# # precomputation
# from math import comb
#
# MX = 10 ** 15
#
# ranges = []
# for i in range(2, 50):
#     for cur in range(10 ** 15):
#         n = cur
#         k = i
#         if comb(n, k) > MX:
#             ranges.append((n, k))
#             print(n, k, round(comb(n, k), 2))
#             break
#
# print(ranges)
