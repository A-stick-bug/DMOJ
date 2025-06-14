# https://dmoj.ca/problem/triplequeue
# Maintain 2 queues, while keeping the number of elements balanced

from collections import deque
import sys


def balance_queues():
    while len(q2) > len(q1):
        q1.append(q2.popleft())
    while len(q1) > len(q2):  # order matters to ensure q2 has the extra element during odd parity
        q2.appendleft(q1.pop())


input = sys.stdin.readline
fast_print = lambda x: sys.stdout.write(str(x) + "\n")

N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

q1 = deque(arr)
q2 = deque()
balance_queues()

for _ in range(Q):
    qry = input().split()
    if qry[0] == "pop":
        if qry[1] == "left":
            print(q1.popleft())
        elif qry[1] == "middle":
            print(q2.popleft())
        else:
            print(q2.pop())

    else:  # append
        x = int(qry[2])
        if qry[1] == "left":
            q1.appendleft(x)
        elif qry[1] == "middle":
            if len(q1) != len(q2):
                q1.append(q2.popleft())  # shift first element over
            q2.appendleft(x)
        else:
            q2.append(x)

    balance_queues()
