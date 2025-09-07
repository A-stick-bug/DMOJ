# https://dmoj.ca/problem/halloween14p3
# Key observation:
# - a string is special iff it consists of >=2 repeated parts
#   - eg. [aba][aba] or [ab][ab][ab]
# - a standard trick in counting substrings is to try all starting points
#
# I will be using hashing for everything since you need to hash substrings anyway
#
# TC: O(n^2 * log(n)), better on average due to optimizations
# MC: O(n^2)

MN = 5001


class SubstringHash:
    def __init__(self, arr, p=29, mod=10 ** 9 + 7):
        # precompute powers of `p`, with MOD
        self.mod = mod
        self.power = [0] * MN
        self.power[0] = 1
        for i in range(1, MN):
            self.power[i] = (self.power[i - 1] * p) % self.mod

        # precompute hashes of each character in `str1`
        n = len(arr)
        self.psa = [0] * (n + 1)
        for i in range(1, n + 1):
            self.psa[i] = (arr[i - 1] * self.power[MN - i] + self.psa[i - 1]) % self.mod

    def query(self, l, r):  # query hash of [l,r]
        # shift up to match `mn`
        hs = (self.psa[r + 1] - self.psa[l]) * self.power[l] % self.mod
        return hs


s = input()
n = len(s)
hs = SubstringHash([ord(c) - ord('a') + 1 for c in s], mod=202155470168200)

works = set()
for start in range(n):
    le = n - start

    for sz in range(1, le // 2 + 2):  # harmonic series ~ n*log(n)
        to_match = hs.query(start, start + sz - 1)
        if to_match in works:  # optimization: consists of smaller parts, must've already counted this
            continue

        for j in range(sz, le - sz + 1, sz):
            if hs.query(start + j, start + j + sz - 1) == to_match:
                # print("!!!!!!!!!", s[start: start+j+sz])
                works.add(hs.query(start, start + j + sz - 1))
            else:  # optimization: can't extend this starting point further
                break
#     print(s[start:])
#     print(matching)
#     print("---")
# print(works)

print(len(works))

"""
abababab
5
"""
