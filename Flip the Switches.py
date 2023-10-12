# https://dmoj.ca/problem/fts
# just implementation with a bit of logic

n = int(input())
s = input()

if s[0] == "1":  # first switch is 1
    flips = 1
    prev = 1
else:  # first switch is 0
    flips = 0
    prev = 0

for i in s[1:]:
    if i == "1":
        if prev == 0:  # current is 1, previous is 0, we need 2 flips to turn the current one off
            prev = 1
            flips += 2
        # if the previous is 1, we don't need any flips because we can flip the current one along with the previous one

    else:
        prev = 0

print(flips)
