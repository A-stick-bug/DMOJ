# https://dmoj.ca/problem/utso24p1
# take farthest first

n = int(input())
k = int(input())

total = 0

cur = n
while cur > 0:
    total += 2 * cur
    cur -= k
print(total)
