"""
PYTHON IS TOO SLOW, CHECK C++ CODE

https://dmoj.ca/problem/year2016p8
longest contiguous segment with range updates, we also need to keep track of the indices of the longest
segment so we can remove it during type 2 queries

at each node we store:
- left most node covered by segment
- right most node covered by segment
- length of prefix ones
- length of suffix ones
- indices of [l, r] for the longest contiguous segment inside the current node

IMPORTANT:
- there doesn't exist a default that works for all empty segments since each segment have their own [L, R]
  therefore, we must create a default even for nodes that don't exist
- (in_l = 0) and (in_r = -1) for default segments as it represents a length 0 maximum segment

"""

from math import log2, ceil
from collections import namedtuple

# usually I wouldn't do this since it's slower than regular tuple but python TLE anyway so might as well get readability
node = namedtuple('node', ['L', 'R', 'best_l', 'best_r', 'in_l', 'in_r'])


def combine(left: node, right: node):
    """combine left and right segments"""
    best_r = right.best_r
    if right.in_r == right.R and right.in_l == right.L:  # right segment is full: expand best_r to left
        best_r = (right.R - right.L + 1) + left.best_r

    best_l = left.best_l
    if left.in_r == left.R and left.in_l == left.L:  # left segment is full: expand best_l to right
        best_l = (left.R - left.L + 1) + right.best_l

    res = node(left.L, right.R,
               best_l, best_r,
               *max((left.in_l, left.in_r), (left.R - left.best_r + 1, right.L + right.best_l - 1),
                    (right.in_l, right.in_r), key=lambda x: x[1] - x[0]))  # take l,r with largest range

    return res


class LazySegTree:  # update to value
    def __init__(self, N, f) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << layers
        self.seg = [None] * (2 * self.size)  # 1-indexed
        for i in range(self.size):  # base layer
            self.seg[self.size + i] = node(i, i, 0, 0, 0, -1)
        for i in reversed(range(1, self.size)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])
        self.lazy = [-1] * (2 * self.size)

    def push_down(self, i, L, R):
        """transfer lazy tag from parent to children"""
        if self.lazy[i] == -1:
            return
        self.lazy[i * 2] = self.lazy[i]  # transfer lazy tags
        self.lazy[i * 2 + 1] = self.lazy[i]
        mid = (L + R) // 2  # [l,mid], [mid+1, r]
        if self.lazy[i] == 1:  # everything on
            self.seg[i * 2] = node(L, mid, mid - L + 1, mid - L + 1, L, mid)
            self.seg[i * 2 + 1] = node(mid + 1, R, R - mid, R - mid, mid + 1, R)
        elif self.lazy[i] == 0:  # everything off
            self.seg[i * 2] = node(L, mid, 0, 0, 0, -1)
            self.seg[i * 2 + 1] = node(mid + 1, R, 0, 0, 0, -1)
        self.lazy[i] = -1

    def update(self, i, l, r, cur_l, cur_r, val) -> None:
        """add diff to [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return
        mid = (cur_l + cur_r) // 2
        if l <= cur_l and cur_r <= r:  # fully inside segment: update lazily
            self.lazy[i] = val
            if self.lazy[i] == 1:  # everything on
                self.seg[i] = node(cur_l, cur_r, cur_r - cur_l + 1, cur_r - cur_l + 1, cur_l, cur_r)
            elif self.lazy[i] == 0:  # everything off
                self.seg[i] = node(cur_l, cur_r, 0, 0, 0, -1)
            return
        self.push_down(i, cur_l, cur_r)  # partial covers, recurse deeper
        self.update(i * 2, l, r, cur_l, mid, val)
        self.update(i * 2 + 1, l, r, mid + 1, cur_r, val)
        self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    def query(self, i, l, r, cur_l, cur_r):
        """query [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return node(cur_l, cur_r, 0, 0, 0, -1)
        if l <= cur_l and cur_r <= r:  # fully inside segment
            return self.seg[i]

        mid = (cur_l + cur_r) // 2  # traverse down further
        self.push_down(i, cur_l, cur_r)
        return self.f(self.query(i * 2, l, r, cur_l, mid),
                      self.query(i * 2 + 1, l, r, mid + 1, cur_r))

    def query_range(self, l, r):
        return self.query(1, l, r, 0, self.size - 1)

    def update_range(self, l, r, val):
        return self.update(1, l, r, 0, self.size - 1, val)


N, Q = map(int, input().split())
seg = LazySegTree(N + 1, f=combine)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:  # turn off
        seg.update_range(q[1], q[2], 0)
        ans = seg.query_range(1, N)
        print(ans.in_r - ans.in_l + 1)
    elif q[0] == 1:  # turn on
        seg.update_range(q[1], q[2], 1)
        ans = seg.query_range(1, N)
        print(ans.in_r - ans.in_l + 1)
    else:
        _, _, _, _, l, r = seg.query_range(1, N)
        seg.update_range(l, r, 0)

"""
Sample Input:
3 2
1 1 3
0 2 2

Output:
3
1
"""

