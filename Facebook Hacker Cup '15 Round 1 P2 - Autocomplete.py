"""
https://dmoj.ca/problem/fhc15c1p2
Huge input file so we use standard input

Solution using trie data structure

For each word, BEFORE inserting it, we check if it already exists in the trie
- if it does, we need to type out every letter because the word is the prefix of another word
- else, we need to find how many letters of the work already exists in the (and +1 to the answer)
"""

import sys
from collections import defaultdict

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

    def insert(self, word):
        cur = self
        for letter in word:
            cur = cur.children[letter]  # defaultdict will create empty node if needed


# for all test cases
t = int(input())
for test in range(1, t + 1):
    trie = TrieNode()  # create empty trie
    n = int(input())
    total = 0

    for _ in range(n):  # check letters needed for each word
        word = input().strip()

        prefix = 1  # smallest possible is 1 (can't have empty)
        cur = trie
        for i, char in enumerate(word):  # search in trie
            if char in cur.children:
                cur = cur.children[char]
            else:
                prefix = i + 1
                break

        # code is reached if the for loop exists 'naturally' and didn't break
        else:
            prefix = len(word)  # didn't each a leaf node, therefore, we must type the entire word

        total += prefix
        trie.insert(word)  # add word AFTER checking how many letters we need to type

    print(f"Case #{test}: {total}")
