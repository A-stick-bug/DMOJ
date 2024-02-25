import sys
from itertools import accumulate

print = lambda x: sys.stdout.write(str(x) + "\n")

N, K = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))

to_minus = [0] * K  # both 0-indexed
push = [1 << 30] * K
psa = [0] + list(accumulate(a))
query = lambda l, r: psa[r + 1] - psa[l]

for i in reversed(range(N)):
    val = a[i]
    if push[val - 1] > i:
        to_minus[val - 1] += query(max(0, i - x[val - 1]), i)
        push[val - 1] = i - x[val - 1] - 1
    else:
        diff = i - push[val - 1]
        if push[val - 1] >= 0:
            to_minus[val - 1] += query(max(0, i - x[val - 1] - diff), max(0, i - diff))
        push[val - 1] -= x[val - 1] + 1

s = sum(a)
for i in range(K):
    print(s - to_minus[i])

"""
10 5
2 4 4 1 3 2 2 3 1 4
1 1 1 1 1

5 2
1 1 2 2 2
2 1

"""
