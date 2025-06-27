"""
https://dmoj.ca/problem/dpz
Monotonic (non-dynamic) convex hull trick with updates only

States: dp[i] = min cost to get to index `i`
Note: the a_i < a_{i+1} property means we only insert to the end of the hull
This significantly reduces implementation amount as we only need a monotonic stack

Transition cost: A is previous height, B is current height
dp[i] = dp[prev] + A^2 - 2AB + B^2 + C
the following is constant at `i`: B^2 + C
the following is linear at `prev`, B is variable: -2AB + (dp[prev] + A^2)

TC: O(nlogn), due to binary search
"""

from bisect import bisect_left


def intersect(l1, l2):
    a, b = l1
    c, d = l2  # ax + b = cx + d
    x_int = (d - b) / (a - c)  # slope must not be equal
    return x_int


def query_min(x):  # return the min y value at `x`
    idx = bisect_left(cht, x, key=lambda x: x[2]) - 1
    m, b, _ = cht[idx]
    return m * x + b


def add_line(m, b):  # add y=mx+b, new line has smaller slope than all before
    while len(cht) >= 1 and intersect((m, b), cht[-1][:2]) <= cht[-1][2]:
        cht.pop()
    mx_start = intersect((m, b), cht[-1][:2])
    cht.append((m, b, mx_start))


inf = 1 << 60
n, C = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * n
cht = []  # (slope, y-int, maximum start)

cht.append((-2 * arr[0], dp[0] + arr[0] ** 2, -inf))  # base case

for i in range(1, n):
    prev_cost = query_min(arr[i])
    cur_cost = arr[i] ** 2 + C
    dp[i] = prev_cost + cur_cost

    add_line(-2 * arr[i], dp[i] + arr[i] ** 2)

print(dp[-1])
