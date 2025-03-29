# https://dmoj.ca/problem/mnyc17p3
# String algorithms, possible methods include hashing and Z function
# combine strings s and t like this: t + "!" + s
# Then use Z function to match the longest prefix of t that is a suffix of s

import sys


def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if l <= i <= r:
            # fully within a larger matching segment, reuse answer
            if i + z[i - l] - 1 < r:
                z[i] = z[i - l]

            # extends to the end of a matching segment, check if we can extend farther
            else:
                z[i] = r - i + 1
                l = i
                # start from `r` since before that already matches
                for j in range(r + 1, n):
                    if s[j - i] == s[j]:
                        z[i] += 1
                        r = j
                    else:
                        break
        # manually match
        else:
            l = i
            for j in range(i, n):
                if s[j - i] == s[j]:
                    z[i] += 1
                    r = j
                else:
                    break
    return z


s, t = input().split()
n, m = len(s), len(t)

merged = t + "!" + s
z = z_algorithm(merged)

for i in range(m + 1, n + m + 1):
    if i + z[i] == n + m + 1:  # suffix match
        overlap = (n + m + 1) - i
        print(s + t[overlap:])
        sys.exit()

# no match
print(s + t)

# # alternate hashing solution
# # basically brute force optimized with hashing for O(1) substring query
#
# import sys
#
# # max possible length of anything string
# # all hashes are aligned with this maximum length
# MN = 10 ** 6
#
#
# class SubstringHash:
#     def __init__(self, arr, p=29, mod=10 ** 9 + 7):
#         # precompute powers of `p`, with MOD
#         self.mod = mod
#         self.power = [0] * MN
#         self.power[0] = 1
#         for i in range(1, MN):
#             self.power[i] = (self.power[i - 1] * p) % self.mod
#
#         # precompute hashes of each character in `str1`
#         n = len(arr)
#         self.psa = [0] * (n + 1)
#         for i in range(1, n + 1):
#             self.psa[i] = (arr[i - 1] * self.power[MN - i] + self.psa[i - 1]) % self.mod
#
#     def query(self, l, r):  # query hash of [l,r]
#         # shift up to match `mn`
#         hs = (self.psa[r + 1] - self.psa[l]) * self.power[l] % self.mod
#         return hs
#
#
# s, t = input().split()
# n, m = len(s), len(t)
#
# ss = [ord(i) - ord("A") for i in s]
# tt = [ord(i) - ord("A") for i in t]
# s_hash = SubstringHash(ss)
# # s_hash2 = SubstringHash(ss, mod=1000000009)
# t_hash = SubstringHash(tt)
# # t_hash2 = SubstringHash(tt, mod=1000000009)
#
# for le in reversed(range(1, min(n, m) + 1)):  # larger possible matches first
#     # method 1: first check hash, then confirm by checking actual string
#     # this works since as soon as we have an actual match, we break and there are little false positives
#     if s_hash.query(n - le, n - 1) == t_hash.query(0, le - 1) and s[n - le:n] == t[:le]:
#         print(s + t[le:])
#         sys.exit()
#
#     # # method 2: double hash (slower in this case)
#     # if (s_hash.query(n - le, n - 1) == t_hash.query(0, le - 1) and
#     #         s_hash2.query(n - le, n - 1) == t_hash2.query(0, le - 1)):
#
# print(s + t)
