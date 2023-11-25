"""
https://dmoj.ca/problem/noi04p1
Order statistic tree (implemented with a Fenwick Tree)

Time complexity: O(N*log(N)) (I think)

Use an adjustment factor and offset for fast add and subtract operations and to keep numbers positive
- To add a new person, we add his salary minus the adjustment as he was not affected by previous adjustments, O(log(N))
- To increase everyone's salary, we simply increase the adjustment, O(1)
- To find the k-th highest salary, we 'traverse' the OST, O(log(N))
- To decrease everyone's salary, we decrease the adjustment, then check how many people's salaries are now below M
  Now, remove the lowest salary x times, amortized O(log(N))
  Reason for TC: finding how many elements to remove take log(N), from the query function, since each element can only
  be removed once, there will be N removals at most, where N is the number of employees

"""

import sys


class OST:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res

    def select(self, k):  # get k-th smallest element
        i = 0
        bl = self.size.bit_length()
        for p in range(bl, -1, -1):
            if i + (1 << p) <= self.size and self.tree[i + (1 << p)] < k:
                i += 1 << p
                k -= self.tree[i]
        return i + 1


MS = 250004  # maximum salary of an employee after applying adjustment and offset
OFFSET = 100002  # prevent negative values
adjustment = 0
input = sys.stdin.readline

N, M = map(int, input().split())  # number of operations, minimum salary

ost = OST(MS)  # create empty order statistics tree
employees = 0  # current number of employees
left = 0

for _ in range(N):
    cmd, val = input().split()
    val = int(val)

    if cmd == 'I':  # add new person
        if val < M:  # left immediately
            continue
        ost.update(val + OFFSET - adjustment, 1)  # new employee with wage of val
        employees += 1

    elif cmd == 'F':  # find k-th salary
        if val > employees:  # not enough people
            print(-1)
            continue
        print(ost.select(employees - val + 1) + adjustment - OFFSET)  # get k-th highest

    elif cmd == 'A':
        adjustment += val

    else:
        adjustment -= val
        rem = ost.query(M + OFFSET - adjustment - 1)  # number of people with salary less than M after subtracting
        for _ in range(rem):
            ost.update(ost.select(1), -1)  # remove lowest salary
        employees -= rem
        left += rem

print(left)
