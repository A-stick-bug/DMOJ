# https://dmoj.ca/problem/othscc2p2
# Implementation with loops and conditionals

K = int(input())
N = int(input())
arr = [int(input()) for _ in range(N)]

if max(arr) >= K:
    print("fight")
else:
    print("run away")
