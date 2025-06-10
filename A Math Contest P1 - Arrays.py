# https://dmoj.ca/problem/mathp1
# Can either add or subtract any multiple of each element
# The answer is the gcd of all elements
#
# Note: this is purely based on intuition and I don't have proof on why this is true

from math import gcd

n = int(input())
arr = list(map(lambda x: abs(int(x)), input().split()))

cur = arr[0]
for i in range(1, n):
    cur = gcd(cur, arr[i])

print(cur)
