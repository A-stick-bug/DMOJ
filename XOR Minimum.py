# TLE, CHECK C++ CODE (to pass in python, you need to use the implicit seg tree trick)
#
# https://dmoj.ca/problem/xorm
# - Keep track of what we XORd with in the past instead of updating each element
#   (similar to lazy propagation)
# - Make a trie of the binary representation of each number (end point is index)
# - To get min, we keep on going down the left (0) branch if possible and right (1)
#   branch when the bit at that depth is flipped

import sys


class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.val = None


def insert_num(idx):
    """add the i-th number from arr to the trie"""
    cur = trie
    for bit in reversed(range(MN)):  # start with most significant bit
        i = bool(arr[idx] & (1 << bit))
        if not cur.child[i]:
            cur.child[i] = TrieNode()
        cur = cur.child[i]
    cur.val = idx  # store index at end point


def get_min():
    cur = trie
    for bit in reversed(range(MN)):
        if cur.child[flipped[bit]]:  # try going to smaller branch
            cur = cur.child[flipped[bit]]
        else:
            cur = cur.child[flipped[bit] ^ 1]
    return cur.val


MN = 32
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

trie = TrieNode()
# iterate in reverse to guarantee the earlier duplicate value is chosen
for i in reversed(range(N)):
    insert_num(i)

flipped = [False] * MN  # bits that are flipped due to XOR

for _ in range(Q):
    x = int(input())
    for bit in range(MN):  # update flipped bits
        if x & (1 << bit):
            flipped[bit] ^= 1

    print(get_min())
