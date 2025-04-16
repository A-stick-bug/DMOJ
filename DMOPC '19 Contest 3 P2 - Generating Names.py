# https://dmoj.ca/problem/dmopc19c3p2
# Notice the extremely low bounds
# Recursion to brute force all wildcard possibilities
# Count with permutation with duplicates method

from math import factorial


def permutations_with_dup(freq):  # n!/a!b!...z!
    assert freq[0] == 0  # no wildcards allowed
    total = factorial(sum(freq))
    for v in freq:
        total //= factorial(v)
    return total


def map_to_int(c):
    if c == "*":
        return 0
    return ord(c) - ord("a") + 1


n, k = map(int, input().split())
s = input()

freq = [0] * 27
for i in s:
    freq[map_to_int(i)] += 1

vis = set()


def solve(cur):
    if cur in vis:
        return 0
    vis.add(cur)

    if cur[0] == 0:  # out of wildcards
        return permutations_with_dup(cur)

    total = 0
    for i in range(1, 27):
        adj_state = list(cur)
        adj_state[0] -= 1  # spend wildcard
        adj_state[i] += 1
        total += solve(tuple(adj_state))
    return total


print(solve(tuple(freq)))
