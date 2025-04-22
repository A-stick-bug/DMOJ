# https://dmoj.ca/problem/dmopc17c2p4
# Extension of https://leetcode.com/problems/shortest-palindrome/
# Key observation:
# - all possible palindrome prefixes start at index 0, they build on top of each other
# - thus, we can match them all at once using the z-algorithm
#
# - First use the z-algorithm to find all prefixes that are palindromes
#   - This can be done with other algorithms, but we need Z for the matching later anyway
# - Find the longest prefix that appears elsewhere in `s` by matching with z[1:]
#
# TC: O(n)
# note: you don't actually need binary search at the end

import sys
from bisect import bisect_right


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


s = input()
n = len(s)

if n == 1:  # corner case
    print(0)
    sys.exit()

# Z-algorithm for finding all prefixes that are palindromes
match_str = s + "!" + s[::-1]
z = z_algorithm(match_str)
match_le = z[n + 1:][::-1]

valid_le = []  # valid prefix lengths (equal to `end index + 1`)
for i in range(n):
    if match_le[i] == i + 1:  # prefix match: fully extends left to 0
        valid_le.append(i + 1)

match_str2 = s + "!" + s[1:]
z2 = z_algorithm(match_str2)
longest = max(z2[n + 1:])  # max length prefix that appears elsewhere

print(valid_le[bisect_right(valid_le, longest) - 1])  # largest value in valid_le that is <= longest
