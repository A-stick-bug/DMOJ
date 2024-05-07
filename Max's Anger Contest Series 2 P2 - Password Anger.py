def get_hash(s):
    hash = 0
    for i in range(len(s)):
        hash = hash * 13 + ord(s[i]) - ord('a') + 1
    return hash


n = int(input())
m = int(input())
alphabet = "qwertyuiopasdfghjklzxcvbnm"

passwords = [""]
for _ in range(n):
    cop = []
    for p in passwords:
        for i in range(26):
            cop.append(p + alphabet[i])
    passwords = cop.copy()

total = 0
for i in passwords:
    total += get_hash(i) == m
print(total)
