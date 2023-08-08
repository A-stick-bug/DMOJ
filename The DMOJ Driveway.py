# https://dmoj.ca/problem/stack1
# basic queue usage

from collections import deque

t, m = map(int, input().split())
q = deque()
front = 0

for _ in range(t):
    person, in_out = input().split()
    if in_out == "out" and q[0] == person and front < m:  # up to m cars can leave from the front
        q.popleft()
        front += 1
    elif in_out == "out" and q[-1] == person:
        q.pop()
    elif in_out == "in":
        q.append(person)

print(*q, sep="\n")
