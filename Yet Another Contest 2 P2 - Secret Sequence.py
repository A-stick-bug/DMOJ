"""
https://dmoj.ca/problem/yac2p2
Imagine the question was addition instead of XOR, you would just query everything, then query everything
except the last element to get the value of the last element (by subtraction)

Once you get the idea to solve that, replace both addition and subtraction with XOR as it is its own inverse
Note that to fit under N queries, we must find our last number based on all other numbers
"""

import sys
from functools import reduce


def ask(l, r):
    print("? " + str(l) + " " + str(r))
    sys.stdout.flush()  # MUST HAVE THIS OR ELSE TLE
    # return eval(input())  # tip: use eval when testing since I'm too lazy to evaluate the XORs in my head
    return int(input())


input = sys.stdin.readline
print = lambda x: sys.stdout.write(x + "\n")
n = int(input())
res = [0] * n

xor_all = ask(1, n)
hf = (n - 1) // 2  # observation on n=5 and n=6 shows that (r - l) is at least this much when querying optimally

prev = xor_all
for i in reversed(range(hf, n - 1)):  # fill the second half of the array
    cur = ask(1, i + 1)
    res[i + 1] = cur ^ prev
    prev = cur

prev = xor_all
for i in range(1, hf + 1):  # fill the first half of the array
    cur = ask(i + 1, n)
    res[i - 1] = cur ^ prev
    prev = cur

res[hf] = xor_all ^ reduce(lambda a, b: a ^ b, res)  # find missing number without using a query
print("! " + " ".join(map(str, res)))
