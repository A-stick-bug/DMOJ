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
