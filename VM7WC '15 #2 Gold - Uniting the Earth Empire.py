# https://dmoj.ca/problem/coi06p1, same as https://dmoj.ca/problem/vmss7wc15c2p3
# similar to (but harder than) https://dmoj.ca/problem/mwc15c2p2
#
# Monotonic stack question (decreasing stack)
# Each person looks at the left and count how many people they can see, with taller people blocking shorter ones
# Special cases:
# - they may also see one extra person (the first person who is taller than them)
# - people with same height don't block each other

import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

total = 0
stack = [[0, 1]]  # (index, number of equal elements before index, including index)

for i in range(1, n):
    see = 0
    while stack and arr[i] > arr[stack[-1][0]]:  # keep stack decreasing by removing smaller elements
        see += stack.pop()[1]  # add previous smaller elements as we cna see them

    if stack and arr[i] == arr[stack[-1][0]]:  # equal elements, can see everything before of equal height
        see += stack[-1][1]
        stack[-1][1] += 1  # the current element is also equal, so we now have 1 more
    else:
        stack.append([i, 1])

    if stack and arr[stack[0][0]] > arr[i]:  # we can see 1 extra person who is taller at the left
        see += 1

    # print(f"Person {i} can see {see} people")
    total += see

print(total)

"""
Some custom sample cases to help debug
7
1
0
1
1
1
1
2

Output: 17

11
2
10
5
7
10
10
10
10
1
2
10

Output: 24
"""
