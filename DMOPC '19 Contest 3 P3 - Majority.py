"""
https://dmoj.ca/problem/dmopc19c3p3

Very confusing, so first we convert all 2s to -1
Now the question becomes, count the number of subarrays with a sum of > 0
If we take the PSA of the array, the question becomes count the number of inversions???

"""

from itertools import accumulate


class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, i: int, val: int) -> None:
        while i <= self.size:
            self.bit[i] += val
            i += i & (-i)

    def query(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total


N = int(input())
bit = FenwickTree(2 * N)

arr = list(map(lambda x: int(x) if x == "1" else -1, input().split()))  # convert 2 to -1
psa = [0] + list(accumulate(arr))
psa = list(map(lambda i: i + N, psa))  # increase all elements by N so they are all positive

inversions = 0
for i in range(N + 1):  # use BIT to count the number of inversions in the PSA
    inversions += bit.query(psa[i])
    bit.update(psa[i] + 1, 1)

print(inversions)
