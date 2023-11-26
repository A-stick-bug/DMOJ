# https://dmoj.ca/problem/coci16c1p3
# when the question says something about alphabetical order, first think about topo sort
# very annoying question with stupid corner cases

from collections import defaultdict, deque
import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
words = [input() for _ in range(n)]
order = list(map(int, input().split()))

ordering = []
for o in order:  # put the words in the order we want them to be in
    ordering.append(words[o - 1])

after = defaultdict(list[str])  # after[s] has the letters that go after s
in_degree = defaultdict(int)  # s has in_degree[s] before it

for i, word in enumerate(ordering):
    for next_word in ordering[i + 1:]:  # check the characters of every word after the current
        if word.startswith(next_word):
            print("NE")  # a lexicographically greater word cannot be a prefix of a smaller one
            sys.exit()
        for c in range(min(len(word), len(next_word))):
            if word[c] != next_word[c]:
                in_degree[next_word[c]] += 1
                after[word[c]].append(next_word[c])
                break  # remember to break because the letters after this don't affect the ordering anymore

# topological sort
q = deque(s for s in alphabet if in_degree[s] == 0)
cipher = []
while q:
    char = q.popleft()
    cipher.append(char)

    for adj in after[char]:
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            q.append(adj)

if len(cipher) != 26:
    print("NE")
else:
    print("DA")
    #print(cipher)

    res = [None] * 26
    for i, c in enumerate(cipher):  # getting the letters in the right order
        res[ord(c) - ord("a")] = chr(ord("a") + i)

    print(*res, sep="")
