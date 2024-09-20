# https://dmoj.ca/problem/scb24p1
# use numbers to represent rock, paper, and scissors to check who wins more easily

import sys

table = {"paper": 0, "scissors": 1, "rock": 2}

n = int(input())
win = False
opponent = [table[input()] for _ in range(n)]

for move in range(3):
    wins = sum(move == (o + 1) % 3 for o in opponent)
    lose = sum((move + 1) % 3 == o for o in opponent)
    if wins > lose:
        print("yes")
        sys.exit()
print("no")
