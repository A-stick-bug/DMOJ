# https://dmoj.ca/problem/dpq
# Same as the Fenwick Tree solution of Longest Increasing Subsequence (LIS), but we're adding a value instead of 1
# Note: flowers heights are a permutation of 1-N, it's basically coordinate compressed for us

class FenwickTree:  # uses 1-indexing
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, val: int) -> None:
        """Set self.bit[i] to val"""
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += i & (-i)

    def query(self, i: int):
        """Get the max up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total = max(total, self.bit[i])
            i -= i & (-i)
        return total


n = int(input())
arr = list(map(int, input().split()))
beauty = list(map(int, input().split()))

bit = FenwickTree(n)

for i, num in enumerate(arr):
    best = bit.query(num - 1)  # get the best previous best sequence less than num
    bit.update(num, best + beauty[i])  # add the current flower to that sequence

print(bit.query(n))  # get the best sequence of all
