import sys

n = int(input())
s = input()
t = input()

matched = sum(s[i + 1] == t[i] for i in range(n - 1))
best = matched

for i in range(n - 1):
    matched -= s[i + 1] == t[i]
    matched += s[i] == t[i]
    best = max(best, matched)
print(best)
