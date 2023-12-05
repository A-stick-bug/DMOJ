# using order statistics tree to get median

class Better_OST:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res

    def select(self, k):  # get k-th smallest element
        i = 0
        bl = self.size.bit_length()
        for p in range(bl, -1, -1):
            if i + (1 << p) <= self.size and self.tree[i + (1 << p)] < k:
                i += 1 << p
                k -= self.tree[i]
        return i + 1

