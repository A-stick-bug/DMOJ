"""
TLE, CHECK C++ CODE

https://dmoj.ca/problem/2dperm
typical annoying ad hoc question

Using offline queries (definitely not intended solution)
Note: the intended solution uses a difference array (and doesn't have that extra log factor from sorting)

TC: O(MN*log(MN) + Qlog(Q))
"""

import sys

input = sys.stdin.readline
N, M, Q = map(int, input().split())
area = N * M
table = sorted(i * j for i in range(1, N + 1) for j in range(1, M + 1))

queries = [(int(input()), i) for i in range(Q)]
queries.sort(key=lambda x: x[0], reverse=True)  # sort by value
ans = [0] * Q

i = 0
j = area - 1
for num, idx in queries:
    while i + 1 < area and table[i + 1] + num - 1 <= area:
        i += 1
    while j - 1 >= 0 and table[j - 1] > num:
        j -= 1

    ans[idx] = i - (area - j) + 1
    if num == area:  # weird corner case
        ans[idx] = 1

print("\n".join(map(str, ans)))

# # 50/100, brute force code
# N, M, Q = map(int, input().split())
# area = N * M
#
# for _ in range(Q):
#     q = int(input())
#     total = 0
#
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             less = i * j
#             more = (N-i+1) * (M-j+1)
#             if less + q - 1 <= area and more <= q:
#                 total += 1
#
#     print(total)
