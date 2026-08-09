# TLE in python, check C++ version
# probably need O(nlogn) construction
#
# https://dmoj.ca/problem/bf2hard
# Suffix array solution
# Note that shorter strings are lex smaller, so the answer always has a length of exactly K

def suffix_array(s):  # O(n * log^2(n))
    n = len(s)
    perm = list(range(n))

    perm.sort(key=lambda x: s[x])  # sort first character
    rank = [0] * n  # order rank by first character, equality -> tied
    for i in range(1, n):
        rank[perm[i]] = rank[perm[i - 1]] + (1 if s[perm[i]] != s[perm[i - 1]] else 0)

    p2 = 1
    while p2 < n:
        perm.sort(key=lambda x: (rank[x], rank[x + p2] if x + p2 < n else -1))  # double sorted prefix

        new_rank = [0] * n
        for i in range(1, n):  # rerank
            prev = perm[i - 1]
            cur = perm[i]
            prev_pair = (rank[prev], rank[prev + p2] if prev + p2 < n else -1)
            curr_pair = (rank[cur], rank[cur + p2] if cur + p2 < n else -1)
            new_rank[cur] = new_rank[prev] + (1 if curr_pair != prev_pair else 0)

        rank = new_rank
        if rank[perm[-1]] == n - 1:
            break
        p2 *= 2

    return perm


s = input()
n = len(s)
k = int(input())

sa = suffix_array(s)
for i in range(n):
    if n - sa[i] >= k:  # first one with length >=k
        print(s[sa[i]: sa[i] + k])
        break
