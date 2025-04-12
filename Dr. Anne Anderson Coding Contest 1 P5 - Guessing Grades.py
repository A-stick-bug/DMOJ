# https://dmoj.ca/problem/daacc1p5
# Greedy, proof by AC

from collections import Counter

n = int(input())
s = list(input())
t = list(input())
freq = Counter()
for a, b in zip(list("ABCD"), list(map(int, input().split()))):
    freq[a] = b

wrong = 0
unsure = Counter()
for i, j in zip(s, t):
    if j == "?":
        unsure[i] += 1
    else:
        freq[j] -= 1  # already used
        wrong += (i != j)

for i in "ABCD":
    cur = freq[i]
    other = sum(unsure[j] for j in "ABCD" if i != j)
    wrong += min(cur, other)

print(n - wrong)
# print(freq)
# print(unsure)
