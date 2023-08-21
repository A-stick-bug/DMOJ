# this question is the partition function
# except the answer is 1 less than the partition function of n because the n itself is not counted in this question

# more about the partition function here:
# https://en.wikipedia.org/wiki/Partition_function_%28number_theory%29

from collections import deque

n = int(input())
q = deque()
for i in range(1, n // 2 + 1):
    q.append((i, [i]))

total = 0

while q:
    cur, sequence = q.popleft()
    if cur == n:
        print(f"{n}={'+'.join(map(str, sequence))}")
        total += 1

    for i in range(sequence[-1], n - cur + 1):
        q.append((cur + i, sequence + [i]))

print(f"total={total}")

"""
Input:
6

Output: (any order)
6=1+5
6=2+4
6=3+3
6=1+1+4
6=1+2+3
6=2+2+2
6=1+1+1+3
6=1+1+2+2
6=1+1+1+1+2
6=1+1+1+1+1+1
total=10
"""