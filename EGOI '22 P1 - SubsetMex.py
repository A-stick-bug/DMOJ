"""
https://dmoj.ca/problem/egoi22p1

The way the question is present is very weird, lets simplify it:
- we have a bunch of numbers from 0 to N-1, our goal is to create a number N
- in one move, we can turn (0,...,X-1) into X or create a number 0
- what is the minimum number of moves to create a number N

This is like a math question, note that in order to insert N, we need at least 1 of N-1
Lets say we are missing a N-1, now we need at least TWO N-2, one for getting N-1 and one for N
Just loop the numbers in reverse and keep track of the numbers we are missing.

"""


def solve():
    n = int(input())
    freq = list(map(int, input().split()))
    needed = 1
    for i in reversed(range(n)):
        if freq[i] < needed:
            needed += needed - freq[i]
    print(needed)


T = int(input())
for _ in range(T):
    solve()
