# https://dmoj.ca/problem/btoi03p5
# cellular automaton rule 102: A, B, C --> A^B, B^C, C^A, where ^ is bitwise XOR
# use binary lifting to jump by powers of 2
# O(N*log(M))
# uses many optimizations due to strict time limit

import sys

input = sys.stdin.readline  # fast input
log2 = lambda x: x.bit_length() - 1  # fast log2 on integers

N, iterations = map(int, input().split())
state = [int(input()) for _ in range(N)]

while iterations > 0:
    l2 = 2 ** log2(iterations)

    # update state directly using list comprehension (faster than creating a temporary state)
    state = [state[i] ^ state[(i + l2) % N] for i in range(N)]
    iterations -= l2

# print each element on separate line, slightly faster than for loop
print(*state, sep="\n")
