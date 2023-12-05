# https://dmoj.ca/problem/dmopc19c2p3
# To find the k-th largest element in a range, we can use a segment tree (this is quite complicated)
# However, the values of each element is between 0 and 20, we can just make 21 Fenwick Trees
# note: array is 0-indexed, BITs are 1-indexed

import sys


class FenwickTree:  # uses 1-indexing
    def __init__(self, size: int):
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: int) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total

    def range_query(self, left, right):
        """Query the sum of elements from left to right, inclusive"""
        return self.query(right) - self.query(left - 1)


input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# bits[v] has the frequency array of v and can count how many times v appears in a range in log(n)
bits = [FenwickTree(N + 1) for _ in range(21)]
for i, v in enumerate(arr):
    bits[v].update(i + 1, 1)

for _ in range(M):
    q = list(map(int, input().split()))
    if q[0] == 1:  # update
        index, val = q[1:]
        bits[arr[index - 1]].update(index, -1)  # remove old element
        arr[index - 1] = val
        bits[val].update(index, 1)  # add new element

    else:  # query
        left, right, rank = q[1:]
        elements = [0] * 21
        for i in range(21):
            elements[i] += bits[i].range_query(left, right)

        for i in reversed(range(21)):
            if rank <= elements[i]:  # look for k-th largest
                print(i)
                break
            rank -= elements[i]
