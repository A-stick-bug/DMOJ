# https://dmoj.ca/problem/bts18p2
# using prefix sum and a frequency array to access frequency of a letter in a range with O(1) time
# binary search solution below (memory efficient)

# time complexity of prefix sum: O(26*S + Q)  # constant factor makes it slower
# of binary search: O(S + Q*log(S))

import sys

input = sys.stdin.readline

s = input().strip("\n")
q = int(input())
a = "abcdefghijklmnopqrstuvwxyz"
alphabet = {a: i for i, a in enumerate(a)}

base = [0] * 26
freq = [base]

for i in s:
    letters = freq[-1].copy()
    if i == " ":
        freq.append(letters)
        continue

    letters[alphabet[i]] += 1
    freq.append(letters)

for _ in range(q):
    start, end, letter = input().split()
    start = int(start)
    end = int(end)
    l = alphabet[letter]
    print(freq[end][l] - freq[start - 1][l])


# # using binary search (saves memory)
# import sys
# from collections import defaultdict
# from bisect import bisect_left, bisect_right
#
# input = sys.stdin.readline
#
# s = input().strip("\n")
# freq = defaultdict(list)  # keeps track of the indices at which a letter appears
#
# for i, char in enumerate(s):
#     freq[char].append(i)
#
# q = int(input())
# for _ in range(q):
#     start, end, letter = input().split()
#     first = bisect_left(freq[letter], int(start) - 1)  # find the index of the first appearance of a letter
#     last = bisect_right(freq[letter], int(end) - 1)  # index of last appearance
#     print(last - first)  # the difference is how many times it appears in the range
