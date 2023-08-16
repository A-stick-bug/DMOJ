# https://dmoj.ca/problem/dmopc21c4p2
# greedy algorithms, counting sort, number theory
# use counting sort but ignore duplicate values

_ = int(input())
nums = [int(x) for x in input().split()]

groups = 0
n = 5_000_002
multiples = [False] * n
for i in nums:
    multiples[i] = True

for num in range(1, n):
    if multiples[num]:
        groups += 1
        for i in range(num, n, num):
            multiples[i] = False

print(groups)
