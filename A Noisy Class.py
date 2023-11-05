# https://dmoj.ca/problem/anoisyclass
# Cycle detection problem
# Using topo sort (dfs might also works)

from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

distract = [[] for _ in range(N + 1)]  # distract[i] has the list of nodes distracted by i
in_degree = [0] * (N + 1)  # in_degree[i] is how many people distract i, when this number is 0, they will be silent

for _ in range(M):
    noisy, distracted = map(int, input().split())
    distract[noisy].append(distracted)
    in_degree[distracted] += 1

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:  # people who are not distracted
        q.append(i)

while q:
    cur = q.popleft()
    # this person is not distracted anymore, check if anyone is not distracted either as a result
    for d in distract[cur]:
        in_degree[d] -= 1
        if in_degree[d] == 0:
            q.append(d)

if sum(in_degree) == 0:  # everyone stopped talking
    print("Y")
else:
    print("N")
