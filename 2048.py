from collections import deque


def move(arr, r):
    for _ in range(r):  # rotate clockwise
        arr = list(map(list, list(zip(*arr[::-1]))))

    for _ in range(4):  # repeat 4 times because a number can be shifted up to 4 times
        for i in range(4):
            row = arr[i]  # alias to make code cleaner
            for j in range(3):
                if row[j] == 0:  # empty cell, don't do anything
                    continue
                if row[j] == row[j + 1]:  # combine equal numbers
                    row[j + 1] *= 2
                    row[j] = 0
                elif row[j + 1] == 0:  # push number to the right
                    row[j + 1] = row[j]
                    row[j] = 0

    for _ in range(4 - r):  # rotate back to original state
        arr = list(map(list, list(zip(*arr[::-1]))))
    return arr


def to_hash(state):  # turn board into immutable tuple, so we can store it in vis
    return tuple(map(tuple, state))


for _ in range(5):  # 5 test cases
    grid = [list(map(int, input().split())) for _ in range(4)]

    res = 0
    vis = set()
    vis.add(to_hash(grid))
    q = deque()
    q.append(grid)

    while q:
        state = q.popleft()
        res = max(res, max(max(row) for row in state))  # check if we have a new record

        for rotation in range(4):  # try moving cells in all 4 directions
            new_state = [row.copy() for row in state]
            new_state = move(new_state, rotation)

            hashable = to_hash(new_state)
            if hashable not in vis:
                vis.add(hashable)
                q.append(new_state)

    print(res)
