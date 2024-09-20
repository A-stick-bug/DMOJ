# https://dmoj.ca/problem/scb24p2
# - use the fact that there are only 26 letters
# - each letter will only become 1 other letter
#   - we can't have some `a` turning into `b` and some turning into `c`
# - so just track what each letter will become (loop 26 times)

s = input()
n = int(input())

changes = [input().split() for _ in range(n)]
mp = {}
for letter in "qwertyuiopasdfghjklzxcvbnm":
    if letter not in s:
        continue

    cur = letter
    for old, new in changes:
        if old == cur:
            cur = new
    mp[letter] = cur

print("".join(mp[i] for i in s))
