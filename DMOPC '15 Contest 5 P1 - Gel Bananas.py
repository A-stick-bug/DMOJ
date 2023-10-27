from math import lcm, ceil

a = int(input())
b = int(input())
x = int(input())

l = lcm(a, b)
print(ceil(x / l))
