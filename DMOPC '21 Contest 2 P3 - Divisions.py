# https://dmoj.ca/problem/dmopc21c2p3
#
# To gain intuition, first visualize the binary numbers as a tree [1][2 3][4 5 6 7]
# Going right -> append 0 to the end, going left -> append 1 to the end
# Distance between 2 nodes (numbers) is the min number of operations
# - makes sense if you think in terms of LCA
#
# We need to get 60 bits of information in 32 guesses
# The number of guesses is averaged across 1000 cases, allowing for non-deterministic algorithms
#
# Useful trick: guess 0 to get the depth of the node, simplifies things a lot
# Consider the following trivial strategy first:
# - get the bits one by one (i.e. start at root and see which subtree to go to)
#   - 1 bit per query -> need 60 guesses (passes subtask 1)
#
# Instead, let's guess 11111
# Notice how worst case, the first digit is 0 and we only get 1 bit of information
# But if there are any leading 1s, we get more than 1 bit of information
# Assuming random data, we get 1*(1/2) + 2*(1/4) + 3*(1/8) + 4*(1/16) + ... ~ 2 bits of information
# - note that we might only get 1 bit on the last guess but that's ok since 60/2=30 bits and we have 32 guesses
# By symmetry, we can actually guess any number with 5 bits in this example

import random
from random import randint

random.seed(1434)  # make deterministic for testing, should be fine since test data doesn't change


def guess(n):
    print(n)
    return int(input())


def solve():
    depth = guess(0)

    if depth == 0:
        return

    l = 1 << (depth - 1)  # [l,r] is current range of possible numbers
    r = (1 << depth) - 1
    while True:
        pick = randint(l, r)
        dist = guess(pick)
        if dist == 0:
            return

        diff = dist // 2  # trailing `diff` bits are different

        # move [l,r] range based on the new information
        lca_b = pick >> diff  # common prefix
        bin_l = lca_b * 2 + (1 ^ (1 & (pick >> (diff - 1))))  # we know the next bit is opposite
        l = bin_l << (diff - 1)
        r = (bin_l << (diff - 1)) + (1 << (diff - 1)) - 1


t = int(input())
for _ in range(t):
    solve()
