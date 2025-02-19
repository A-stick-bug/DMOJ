# https://dmoj.ca/problem/othscc3p3
# Line sweep

from heapq import heappush, heappop, heapify
import sys

input = sys.stdin.readline


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
            raise Exception("Cannot remove from empty multiset") from ValueError

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


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

get_idx = {arr[i][2]: i for i in range(N)}

events = []
for l, r, s in arr:
    l -= 1
    r -= 1
    events.append([1, l, s])
    events.append([-1, r + 1, s])
events.sort(key=lambda x: x[1])  # sort by time of event

ans = [0] * N
highest = Multiset()

for i in range(len(events) - 1):
    t, l, s = events[i]
    if t == 1:
        highest.add(-s)
    elif t == -1:
        highest.remove(-s)
    if not highest:
        continue
    mx_s = -highest.smallest()
    ans[get_idx[mx_s]] += events[i + 1][1] - l

print(" ".join(map(str, ans)))
