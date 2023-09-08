"""
https://dmoj.ca/problem/bf2
THIS IS THE EASY VERSION: Simple brute force
Python lets you directly compare 2 string lexicographically (works on min() as well)

The answer will have a length of EXACTLY K even though the question says it could be greater
because adding anything to a string with make it lexicographically greater
"""

s = input()
k = int(input())

res = "z" * 99  # represents infinity as a string

for i in range(len(s) - k + 1):  # total substring to check
    substr = s[i:i + k]
    res = min(res, substr)

print(res)
