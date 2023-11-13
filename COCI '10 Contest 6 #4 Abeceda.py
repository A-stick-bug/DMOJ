# https://dmoj.ca/problem/coci10c6p4
# topological sort, alphabet ordering question

from collections import defaultdict, deque
import sys

n = int(input())
words = []

graph = defaultdict(set)  # word goes before everything in graph[word]
chars = set()  # all characters than appear

for _ in range(n):  # create graph
    word = input()
    for prev_word in words:
        for i in range(min(len(word), len(prev_word))):
            if word[i] != prev_word[i]:
                graph[prev_word[i]].add(word[i])
                break
    words.append(word)
    for c in word:
        chars.add(c)

in_degree = defaultdict(int)  # in_degree[c] letters are before c
for c in graph:
    for adj in graph[c]:
        in_degree[adj] += 1

# put characters that go first into queue
q = deque()
for c in chars:
    if in_degree[c] == 0:
        q.append(c)

order = []
while q:
    # if there is more than 1 item in the queue at any time, there is more than one possible ordering
    if len(q) > 1:
        print('?')
        sys.exit()

    cur = q.popleft()
    order.append(cur)
    for adj in graph[cur]:  # find next letter
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            q.append(adj)

if all(v == 0 for v in in_degree.values()):
    print("".join(order))
else:  # some nodes were not visited
    print("!")
