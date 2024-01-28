# https://dmoj.ca/problem/hopscotch2
# extension of https://dmoj.ca/problem/smac08c1p3 (this one has much better time constraints)
#
# Classic DP problem where you can reach the current state from many previous states, so we need a data structure
# to quickly get the cheapest previous cost
# In this case, we use a monotonic queue

from collections import deque

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [0]  # add padding to prevent index error

prev = [-1] * (N + 2)  # keep track of the stone we came from to trace back the path
min_q = deque([(0, 0)])  # index, cost

for i in range(1, N + 2):
    prev[i] = min_q[0][0]  # index of cheapest previous path
    cur_cost = min_q[0][1] + arr[i]  # current minimum cost

    while min_q and min_q[-1][1] >= cur_cost:  # add current cost as an option
        min_q.pop()
    min_q.append((i, cur_cost))

    if min_q[0][0] == i - K:  # can't reach from the left anymore, move window
        min_q.popleft()

path = []  # trace back the path we took
i = N + 1
while i != 0:
    path.append(i)
    i = prev[i]
path.pop(0)

print(min_q[-1][1])
print(" ".join(map(str, path[::-1])))
