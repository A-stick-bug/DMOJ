# https://dmoj.ca/problem/gcc16p1
# Cheese by maintaining intervals with a SortedList
# Actual code begins on line 318
# TC: O(log^2(n))

import sys

input = sys.stdin.readline
inf = 1 << 30


class SortedList:
    def __init__(self, iterable=None, _load=200):
        '''Initialize sorted list instance.'''
        if iterable is None:
            iterable = []
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def add(self, value):
        '''Add `value` to sorted list.'''
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        '''Remove `value` from sorted list if it is a member.'''
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        '''Remove `value` from sorted list; `value` must be a member.'''
        _len = self._len
        self.discard(value)
        if _len == self._len: raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        '''Remove and return value at `index` in sorted list.'''
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        '''Return the first index to insert `value` in the sorted list.'''
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        '''Return the last index to insert `value` in the sorted list.'''
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        '''Return number of occurrences of `value` in the sorted list.'''
        return self.bisect_right(value) - self.bisect_left(value)

    def _fen_build(self):
        '''Build a fenwick tree instance.'''
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        '''Update `fen_tree[index] += value`.'''
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        '''Return `sum(_fen_tree[:end])`.'''
        if self._rebuild: self._fen_build()
        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        '''Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`).'''
        _list_lens = self._list_lens
        if k < _list_lens[0]: return 0, k
        if k >= self._len - _list_lens[-1]: return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild: self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        '''Delete value at the given `(pos, idx)`.'''
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        '''Return an index pair that corresponds to the first position of `value` in the sorted list.'''
        if not self._len: return 0, 0
        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]: pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        '''Return an index pair that corresponds to the last position of `value` in the sorted list.'''
        if not self._len: return 0, 0
        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def __len__(self):
        '''Return the size of the sorted list.'''
        return self._len

    def __getitem__(self, index):
        '''Lookup value at `index` in sorted list.'''
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        '''Remove value at `index` from sorted list.'''
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        '''Return true if `value` is an element of the sorted list.'''
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        '''Return an iterator over the sorted list.'''
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        '''Return a reverse iterator over the sorted list.'''
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        '''Return string representation of sorted list.'''
        return 'SortedList({0})'.format(list(self))

    def val(self, it):  # added
        '''Return the value of the `it` in the sorted list.'''
        pos, idx = it
        return self._lists[pos][idx]

    def begin(self):  # added
        '''Return the begin of the it in the sorted list.'''
        return (0, 0)

    def end(self):  # added
        '''Return the end of the it in the sorted list.'''
        return (len(self._lists) - 1, len(self._lists[-1])) if self._lists else (0, 0)

    def prev(self, it):  # added
        '''Return the previous `it` in the sorted list.'''
        if it == self.begin(): raise ValueError('{0!r} already list begin'.format(it))
        pos, idx = it
        return (pos, idx - 1) if idx else (pos - 1, len(self._lists[pos - 1]) - 1)

    def next(self, it):  # added
        '''Return the next `it` in the sorted list.'''
        if it == self.end(): raise ValueError('{0!r} already list end'.format(it))
        pos, idx = it
        return (pos, idx + 1) if pos + 1 == len(self._lists) or idx + 1 != len(self._lists[pos]) else (pos + 1, 0)


class RangeModule:
    def __init__(self):
        # list of disjoint intervals [l,r], first add padding to prevent index errors
        self.intervals = SortedList([[-inf, -inf], [inf, inf]])

    def addRange(self, left: int, right: int) -> None:
        """Mark [left, right) as true"""
        right -= 1  # inclusive
        idx = self.intervals.bisect_right([left, inf])  # find index based on left

        # merge interval to the left, overlaps with at most 1
        if self.intervals[idx - 1][1] + 1 >= left:  # extend previous
            self.intervals[idx - 1][1] = max(self.intervals[idx - 1][1], right)
            idx -= 1
        else:  # insert new
            self.intervals.add([left, right])

        # merge intervals to the right, can overlap with many
        while idx + 1 < len(self.intervals) and self.intervals[idx + 1][0] <= right + 1:
            self.intervals[idx][1] = max(self.intervals[idx][1], self.intervals.pop(idx + 1)[1])

    def queryRange(self, left: int, right: int) -> bool:
        """Check if everything in [left, right) is true"""
        right -= 1  # inclusive
        idx = self.intervals.bisect_right([left, inf]) - 1
        return self.intervals[idx][0] <= left <= right <= self.intervals[idx][1]

    def removeRange(self, left: int, right: int) -> None:
        """Mark [left, right) as false"""
        right -= 1  # inclusive
        idx = self.intervals.bisect_right([left, inf]) - 1

        # remove intervals to the right, can remove many
        while idx + 1 < len(self.intervals) and self.intervals[idx + 1][0] <= right:
            if self.intervals[idx + 1][1] <= right:  # fully covered
                self.intervals.pop(idx + 1)
            else:  # cut left
                self.intervals[idx + 1][0] = max(self.intervals[idx + 1][0], right + 1)

        # remove interval to the left, removes at most 1
        l, r = self.intervals[idx]
        if r < left:  # no overlap
            return
        elif l == left:  # cut left
            self.intervals[idx][0] = right + 1
        elif left <= l and r <= right:  # full remove
            self.intervals.pop(idx)
        elif l < left <= right < r:  # cut interval in half
            self.intervals.pop(idx)
            self.intervals.add([l, left - 1])
            self.intervals.add([right + 1, r])
        else:  # cut right
            self.intervals[idx][1] = left - 1


N, A, C = map(int, input().split())

res = RangeModule()
for _ in range(A):
    l, r = map(int, input().split())
    res.addRange(l, r + 1)
for _ in range(C):
    l, r = map(int, input().split())
    res.removeRange(l, r + 1)

# get total length and subtract padding intervals
print(sum(r - l + 1 for l, r in res.intervals) - 2)
