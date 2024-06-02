import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    if bin(n)[2:].count("1") == 1:
        print("T")
    else:
        print("F")
