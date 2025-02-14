"""
https://dmoj.ca/problem/yac9p3

Only the largest prime factor matters, so we turn each number into their largest prime factor
The problem becomes count subarrays where all elements are <= their indices

If we fix the `l` of the subarray, valid `r`s is a monotonic function (first true then false)
This allows us to use a monotonic stack

TC: O(n)
"""

MN = 10 ** 6 + 1
lp = [-1] * MN  # largest prime factor
lp[1] = 1
for i in range(2, MN):
    if lp[i] == -1:
        for j in range(i, MN, i):
            lp[j] = i

n = int(input())
arr = list(map(int, input().split()))
arr = list(map(lambda x: lp[x], arr))

total = 0
stack = []

for l in reversed(range(n)):
    stack.append(l)
    while stack and arr[stack[-1]] <= stack[-1] - l + 1:
        stack.pop()

    if not stack:
        total += n - l
    else:
        total += stack[-1] - l

print(total)

"""
10
1 1 1 2 1 5 1 1 2 3

Expected: 30
"""

# def slow(a):  # reference slow solution
#     arr = a.copy()
#     total = 0
#     while arr:
#         i = 0
#         if arr[i] == 1:
#             while i < len(arr) and arr[i] <= i + 1:  # 1 indexing
#                 i += 1
#
#         total += i
#         arr.pop(0)
#
#     return total
#
#
