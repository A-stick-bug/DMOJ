# https://dmoj.ca/problem/dmopc21c9p2
# Simple usage of stacks
# - if the letter does not match, keep on merging it in the stack until it does
# - note that the stack must only have 1 element when matching since you can only merge adjacent elements
# - the strings are matched if we matched every character in t and there is no leftover in s

import sys

input = sys.stdin.readline
letters = "abcdefghijklmnopqrstuvwxyz"


def solve():
    s, t = input().split()
    t += "!"  # prevent index error
    stack = []
    j = 0  # we are currently trying to match t[j]
    for char in s:
        stack.append(char)
        if len(stack) == 1 and stack[0] == t[j]:  # matched characters
            stack.pop()
            j += 1
            continue

        while len(stack) >= 2 and stack[-1] == stack[-2] and stack[-1] != "z":  # keep merging
            stack.pop()
            stack.append(letters[letters.index(stack.pop()) + 1])  # "a" + "a" -> "b"
            if len(stack) == 1 and stack[0] == t[j]:  # matched characters
                stack.pop()
                j += 1
                break

    if j == len(t) - 1 and not stack:  # check if everything matched and there is no leftover
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()
