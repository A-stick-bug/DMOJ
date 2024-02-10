# https://dmoj.ca/problem/sac22cc5jp5
# fairly simple DP, key is to know that only the last previous letter matters
# let a pair be two consecutive characters that are the same

import sys

input = sys.stdin.readline
n = int(input())
dp = [-1] * 26  # dp[i]: best score obtainable if the previous last character is i

for _ in range(n):
    word = list(map(lambda x: ord(x) - 97, input().strip()))  # turn characters to numbers so we can index them

    pairs = 0
    for i in range(1, len(word)):  # pairs inside the word are added no matter what
        pairs += word[i] == word[i - 1]

    # we get an extra pair if the first letter of the current matches the last better of the previous
    first = word[0]
    best = max(max(dp), dp[first] + 1) + pairs
    dp[word[-1]] = best  # take best answer, store at the current word's last character

print(max(dp))
