# https://dmoj.ca/problem/coci19c4p5
# First consideration for string problems:
# - how can we use the fact that there are only 26 letters?
#
# Since the score is calculated as (number of elements)/(number of unique),
# there are only 26 possible number of unique, so we can just try all of them

def solve(mx):
    """longest substring not exceeding mx unique characters"""
    freq = [0] * 26
    unique = 0
    i = 0
    l = 0
    r = -1
    for j in range(n):
        if freq[arr[j]] == 0:
            unique += 1
        freq[arr[j]] += 1
        while unique > mx:
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                unique -= 1
            i += 1
        if j - i > r - l:
            l = i
            r = j
    return l, r, (r - l + 1) / mx


n = int(input())
arr = list(map(lambda x: ord(x) - ord('a'), input()))

best = 0
l = r = -1
for i in range(1, 27):
    l_temp, r_temp, val = solve(i)
    if val > best:
        best = val
        l, r = l_temp, r_temp

print(l + 1, r + 1)
