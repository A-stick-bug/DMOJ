# https://dmoj.ca/problem/daacc1p4
# Brute force optimized with Fenwick Tree
# Greedy idea: if we need a light, place it as far as possible to cover the most stuff

class FenwickTree:  # point update, range query, 1-indexed
    def __init__(self, nums: list[int]):
        """Create a Fenwick tree from array"""
        psa = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            psa[i] = psa[i - 1] + nums[i - 1]
        self.bit = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.bit[i] = psa[i] - psa[i - (i & -i)]

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


n = int(input())
k = int(input())
s = list(map(int, input()))

bit = FenwickTree(s)

flips = 0
for i in range(n):
    l_bound = max(0, i - k)
    r_bound = min(n - 1, i + k)
    if bit.query_range(l_bound + 1, r_bound + 1) == 0:  # 1-index
        bit.update(r_bound + 1, 1)  # 1-index
        flips += 1

print(flips)
