"""
https://dmoj.ca/problem/ds1

Fenwick Tree question and using a frequency array to get # of elements <= N
O(log(n)) update and query
Note: Queries are 1-indexed
"""


# standard fenwick tree implementation, nothing special here
class FenwickTree:  # uses 1-indexing
    # def __init__(self, nums: list[int]):
    #     """Create a Fenwick tree from an array by adding elements one by one"""
    #     self.bit = [0] * (len(nums) + 1)
    #     for i, num in enumerate(nums):  # create binary index tree by using update on each element
    #         self.update(i + 1, num)

    def __init__(self, nums: list[int]):
        """Create a Fenwick tree using a Prefix Sum Array, O(n)"""
        psa = [0] * (len(nums) + 1)  # first create a PSA
        for i in range(1, len(nums) + 1):
            psa[i] = psa[i - 1] + nums[i - 1]  # assuming nums is 0-indexed

        self.bit = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):  # create BIT using PSA
            self.bit[i] = psa[i] - psa[i - (i & -i)]  # MUST HAVE PARENTHESIS ON (i & -i)!!!

    def update(self, i: int, val: int) -> None:
        """Add val to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += val
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total


n, queries = map(int, input().split())

arr = list(map(int, input().split()))
bit = FenwickTree(arr)

# create a BIT for the frequency array to get # of elements <= N
# by default, the Fenwick tree constructor uses a 0-indexed array to a 1-indexed BIT, ∴ freq has to be 0-indexed as well
freq = [0] * 100000
for num in arr:
    freq[num - 1] += 1
freq = FenwickTree(freq)

for _ in range(queries):
    line = input().split()
    q = line[0]
    if q == 'C':
        idx, new = int(line[1]), int(line[2])
        old = arr[idx - 1]  # element to be changed
        bit.update(idx, new - old)  # adding (new_element - previous_element) will turn the previous element to b
        freq.update(old, -1)  # -1 for the element that got changed
        freq.update(new, 1)  # +1 for the new element
        arr[idx - 1] = new  # update out original array

    elif q == 'S':
        left, right = int(line[1]), int(line[2])
        print(bit.query(right) - bit.query(left - 1))  # query is same as prefix sum

    else:
        a = int(line[1])
        print(freq.query(a))  # querying the frequency array will give us the number of elements less than v


# # Alternate method using sqrt decomposition: O(1) update, O(sqrt(n)) query
#
# from sys import stdin
# from math import isqrt
#
# input = stdin.readline
#
#
# class SqrtDecomp:
#     def __init__(self, nums):
#         self.nums = nums
#         self.width = isqrt(len(nums))
#         self.sqrtn = (len(nums) // self.width) + 1
#         self.blocks = [0] * self.sqrtn
#         for i in range(len(nums)):
#             self.blocks[i // self.width] += nums[i]
#
#     def update(self, i, diff):
#         self.nums[i] += diff
#         block_num = i // self.width
#         self.blocks[block_num] += diff  # update by difference
#
#     def query(self, i, j):
#         first = (i // self.width) + 1
#         last = (j // self.width) - 1
#         if first > last:
#             return sum(self.nums[i:j + 1])
#         res = sum(self.blocks[first:last + 1])
#         res += sum(self.nums[i:first * self.width])
#         res += sum(self.nums[(last + 1) * self.width:j + 1])
#         return res
#
#
# n, queries = map(int, input().split())
# arr = [0] + list(map(int, input().split()))  # 1-indexing
# bit = SqrtDecomp(arr)
#
# # use a frequency array to get the number of elements <= x
# freq = [0] * 100001
# for num in arr:
#     freq[num] += 1
# freq = SqrtDecomp(freq)
#
# for _ in range(queries):
#     q = input().split()
#
#     if q[0] == 'C':
#         i, new = map(int, q[1:])
#         old = bit.nums[i]  # element to be changed
#         bit.update(i, new - old)
#         freq.update(old, -1)
#         freq.update(new, 1)
#
#     elif q[0] == 'S':
#         l, r = map(int, q[1:])
#         print(bit.query(l, r))
#
#     else:
#         a = int(q[1])
#         print(freq.query(0, a) - 1)  # -1 to remove the count of the extra 0 we used for 1-indexing
