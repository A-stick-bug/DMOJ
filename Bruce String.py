# https://dmoj.ca/problem/brucestring
# Smart brute force, the current code probably has some redundant loops but fits in the time limit
#
# Observations
# - In our answer, there will be 1 character that hasn't moved (always optimal to center around median)
#
# Strategy:
# - First pick an index `i` and assume we make the substring centered around it
#   - For the other characters, take the closest ones on the left or right
#   - We try both since we don't know which side is better
# - Once we have the location of the 5 characters, compute cost with inversions + distance to other chars
#   assuming that index `i` doesn't move
#
# TC: O(n * 2^k * k^2), k=5

from bisect import bisect_left, bisect_right


def count_inversions(arr):  # i.e. number of swaps to sort arr
    total = 0
    for i in range(len(arr)):
        total += sum(arr[j] > arr[i] for j in range(i))
    return total


def get_all_choices(choices):
    res = [[]]
    for cur in choices:
        if len(cur) == 0:
            return []
        elif len(cur) == 1:
            res = [i + [cur[0]] for i in res]
        else:
            res = [i + [cur[0]] for i in res] + [i + [cur[1]] for i in res]
    return res


def cost_to_center(arr, mid):
    center = arr[mid]
    left = right = 1
    cost = 0
    for i in arr:
        if i == center:
            continue
        elif i < center:
            cost += center - i - left
            left += 1
        else:
            cost += i - center - right
            right += 1
    return cost


def solve():
    s = input()
    n = len(s)

    loc = [[] for _ in range(5)]
    matching = "bruce"
    for i, char in enumerate(s):
        if char not in matching:
            continue
        loc[matching.index(char)].append(i)

    best = float("inf")
    for mid in range(5):  # outer 2 loops goes through each index `i` that remains fixed
        for center in loc[mid]:
            choices = [[] for _ in range(5)]
            choices[mid].append(center)
            for c in range(5):  # get choices for other 4 characters
                if c == mid:
                    continue
                if loc[c] and loc[c][0] < center:
                    left = bisect_left(loc[c], center) - 1
                    choices[c].append(loc[c][left])
                if loc[c] and loc[c][-1] > center:
                    right = bisect_right(loc[c], center)
                    choices[c].append(loc[c][right])

            # go through all choices
            for perm in get_all_choices(choices):
                # cost to reshuffle + cost to move stuff around the center `i`
                cost = count_inversions(perm) + cost_to_center(perm, mid)
                best = min(best, cost)
    print(best)


t = int(input())
for _ in range(t):
    solve()
