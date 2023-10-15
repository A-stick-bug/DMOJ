# https://dmoj.ca/problem/mwc15c3p3
# Literally the same as [LC 212 - Word Search II]
# So I just copied the explanation here
"""
Backtracking solution using a trie

1. Create a trie containing every word
2. Do a DFS on every cell:
    i. mark the current node as visited
    ii. for every adjacent nodes, if it is a children of the current node in the trie, use dfs
3. Restore the state of the board by removing the current node from visited

"""

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

    def insert(self, word):
        cur = self
        for letter in word:
            cur = cur.children[letter]  # defaultdict will create empty node if needed
        cur.word = word  # end node contains the word


N, Q = map(int, input().split())
board = [input().split() for _ in range(N)]
words = []

trie = TrieNode()
for _ in range(Q):  # words to find
    word = input()
    words.append(word)
    trie.insert(word)

dir_8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
found = set()  # set of found words


def dfs(row, col, cur):
    # cur represents the TrieNode for the current cell
    if cur.word:
        found.add(cur.word)  # found a word
        cur.word = None  # mark as found to prevent duplicates

    # mark as visited, store value for later
    temp = board[row][col]
    board[row][col] = "#"

    # try adjacent cells
    for dr, dc in dir_8:
        new_r = row + dr
        new_c = col + dc

        # stay inside the board to prevent index out of range
        if 0 <= new_r < N and 0 <= new_c < N:
            adj = board[new_r][new_c]
            if adj in cur.children:
                dfs(new_r, new_c, cur.children[adj])

    board[row][col] = temp  # backtrack


# start a dfs from all cells where the first letter matches a word
for i in range(N):
    for j in range(N):
        letter = board[i][j]
        if letter in trie.children:
            dfs(i, j, trie.children[letter])

for word in words:
    if word in found:
        print("good puzzle!")
    else:
        print("bad puzzle!")
