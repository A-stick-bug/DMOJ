# https://dmoj.ca/problem/gfssoc3s1
# simple bitwise logic
# when you OR the numbers from 1-N, every bit after the first 1 is going to be 1

n = int(input())
b = len(bin(n)[2:])

print("1" * b)
