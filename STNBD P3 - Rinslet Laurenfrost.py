from collections import Counter

s = Counter(input())
t = Counter(input())

total = 0
letters = "qwertyuiopasdfghjklzxcvbnm"
for char in letters:
    total += abs(s[char] - t[char])
print(total)
