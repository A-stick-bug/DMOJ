# template fenwick tree questions
# bruh BIT on a junior contest??

import sys


class FenwickTree:  # uses 1-indexing
    # def __init__(self, size):
    #     """Create empty Fenwick Tree"""
    #     self.bit = [0]*(size+1)

    # Create in O(n)
    def __init__(self, nums: list[int]):
        """Create a Fenwick tree using a Prefix Sum Array"""
        psa = [0] * (len(nums) + 1)  # first create a PSA
        for i in range(1, len(nums) + 1):
            psa[i] = psa[i - 1] + nums[i - 1]  # assuming nums is 0-indexed

        self.bit = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):  # create BIT using PSA
            self.bit[i] = psa[i] - psa[i - (i & -i)]  # MUST HAVE PARENTHESIS ON (i & -i)!!!

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

    def query_range(self, left, right):
        """Query the sum of elements from left to right, inclusive"""
        return self.query(right) - self.query(left - 1)


input = sys.stdin.readline
print = sys.stdout.write
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

bit = FenwickTree(arr)

for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:  # move left
        bit.update(b, -c)
        bit.update(b - 1, c)
    elif a == 2:  # move right
        bit.update(b, -c)
        bit.update(b + 1, c)
    else:
        print(str(bit.query_range(b, c)) + "\n")
