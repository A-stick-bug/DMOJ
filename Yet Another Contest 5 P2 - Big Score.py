# note to self: review this later

import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    a3 = list(map(int, input().split()))

    person = [-1, -1, -1]
    order = [(a1, 0), (a2, 1), (a3, 2)]
    person[max(order)[1]] = "Josh"
    order = list(map(lambda x:[x[0][::-1], x[1]], order))
    person[max(order)[1]] = "Nils"
    for i in range(3):
        if person[i] == -1:
            person[i] = "Mike"

    print(*person)
