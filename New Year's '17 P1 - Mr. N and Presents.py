# keep track of when the num was added, so we can check if it's been removed

from collections import deque, defaultdict

n = int(input())
q = deque()
rem = defaultdict(int)

for i in range(n):
    op, num = input().split()
    num = int(num)
    if op == "F":
        q.appendleft((num, i))
    elif op == "E":
        q.append((num, i))
    else:
        rem[num] = i

for num, i in q:
    if i > rem[num]:  # after removal
        print(num)
