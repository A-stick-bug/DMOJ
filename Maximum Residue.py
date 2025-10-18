# note: this problem is from a DMOJ mirror
# https://stroj.ca/problem/maximumresidue
# Q: n, a[i] <= 10**5, find max(a[i] % a[j]) where a[i] >= a[j]
# Line sweep with math observations
#
# Key idea: maintain a list of the largest multiples of all smaller numbers than current
# note: this runs quite slow on average since it doesn't have any short circuiting
#
# TC: O(n*log^2(n)), nlogn divisors with logn multiset operations

from heapq import heappush, heappop, heapify


class Multiset:
    def __init__(self, arr=None):
        """Create multiset from list"""
        if arr is None:
            arr = []
        self.heap = arr  # keeps track of smallest element, with lazy removal (not real time, only update when removing)
        heapify(self.heap)
        self.freq = {}  # keeps track of the actual elements in real time
        for i in arr:
            if i not in self.freq:
                self.freq[i] = 0
            self.freq[i] += 1

    def add(self, val) -> None:
        """Add an element to the multiset"""
        heappush(self.heap, val)

        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1

    def remove(self, val) -> None:
        """Remove an element from multiset by value"""
        if val not in self.freq:
            raise Exception("Element not in Multiset") from ValueError

        self.freq[val] -= 1
        if self.freq[val] == 0:  # remove useless keys
            del self.freq[val]

    def discard(self, val):
        """Remove an element from multiset by value without raising error is the element doesn't exist"""
        if val not in self.freq:
            return False
        self.remove(val)
        return True

    def smallest(self):
        """Get the smallest element in the multiset"""
        while self.heap:
            el = self.heap[0]
            if el in self.freq:
                return el
            heappop(self.heap)  # lazy remove
        raise Exception("Cannot get smallest element from empty multiset") from ValueError

    def pop(self):
        """Removes and returns the smallest element in the multiset"""
        while self.heap:
            el = heappop(self.heap)
            if el in self.freq:
                self.freq[el] -= 1  # update frequency
                if self.freq[el] == 0:
                    del self.freq[el]
                return el
        raise Exception("Cannot pop from empty multiset") from ValueError

    def count(self, val) -> int:
        if val in self.freq:
            return self.freq[val]
        return 0

    def __bool__(self):
        return len(self.freq) != 0

    def __contains__(self, item):
        return item in self.freq

    def __str__(self):
        res = []
        for el, cnt in self.freq.items():
            res.extend([el] * cnt)
        return str(res)


from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
MN = max(arr) + 1

arr = sorted(set(arr))

mods = defaultdict(list)  # divisors of i (that are in arr)
for i in arr:
    for j in range(i, MN, i):
        mods[j].append(i)

options = Multiset()
cur_idx = 1
best = 0
for i in arr:
    while cur_idx <= i:
        for val in mods[cur_idx]:
            if val == cur_idx:  # new value
                ...
            else:
                # remove old
                options.remove(cur_idx - val)
            options.add(cur_idx)
        cur_idx += 1

    if options:
        best = max(best, i - options.smallest())

print(best)
