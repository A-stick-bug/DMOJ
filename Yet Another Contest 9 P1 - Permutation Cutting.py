# https://dmoj.ca/problem/yac9p1
# Turn an array into another using moves
# Simplify the question by mapping to where each element should be
#
# Fun fact: just like YAC8, this can also be solved trivially using a SortedList

n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

loc = [-1] * (n + 1)
for i in range(n):
    loc[a2[i]] = i + 1

arr = [loc[i] for i in a1]

cur = 1
for i in range(1, n):
    if arr[i] != arr[i - 1] + 1:
        cur += 1

print(cur)
