# https://dmoj.ca/problem/dmopc21c1p2
# Sort array using at most 2N moves (doesn't need to be optimal)
# Insertion sort based idea
# - Let pile2 be the sorted pile
# - in 2 moves, we can insert the topmost element of pile1 into pile2
# - this strategy uses at most 2N moves every time
#   - note: the first element uses 1 less move, but 1 more is used at the end to move everything back
#
# Note: a better algorithm is to construct the sorted array starting from the max

from bisect import insort

n = int(input())
arr = list(map(int, input().split()))

pile1 = arr[::-1]
pile2 = []

moves = []

# move first element to pile2
moves.append(1)
pile2.append(pile1.pop())

# like insertion sort, starting from top of pile1, insert into pile2
for _ in range(n - 1):
    takes = 0
    while takes < len(pile2) and pile2[-1 - takes] < pile1[-1]:
        takes += 1
    if takes != 0:
        moves.append(-takes)
    moves.append(takes + 1)
    insort(pile2, pile1.pop(), key=lambda x: -x)  # insert into reverse sorted list

# move everything back
moves.append(-n)

# print(pile1, pile2)

print(len(moves))
print("\n".join(map(str, moves)))
