def move_heads():
    """move all heads down by 1 cell"""
    for j in range(C):  # clear bottom heads
        if grid[-1][j] == "X":
            grid[-1][j] = "."
    for i in reversed(range(R - 1)):  # move down
        for j in range(C):
            if grid[i][j] == "X":
                grid[i][j] = "."
                grid[i + 1][j] = "X"


def move_blood():
    """move blood until resting state, optimize by breaking early"""
    for i in range(999 * (R + C)):
        m = shift_left()
        m |= step_down()
        if not m:
            break


def shift_left():
    """simultaneously shift all heads left as much as possible"""
    moved = False
    for i in range(R):
        cnt = 0
        right = C
        for j in reversed(range(-1, C)):
            cnt += grid[i][j] == "W" and j != -1
            if (j == -1 or grid[i][j] == "X") and cnt != 0:  # stopped by a head or left bounds
                moved = len(set(grid[i][j + 1:j + 1 + cnt])) != 1
                grid[i][j + 1:j + 1 + cnt] = ["W"] * cnt
                grid[i][j + 1 + cnt:right] = ["."] * (right - (j + 1 + cnt))
                cnt = 0
            if grid[i][j] == "X":
                right = j
    return moved


def step_down():
    """simultaneously move blood down by 1 if possible"""
    moved = False
    for j in range(C):
        prev = -10
        for i in range(R - 1):
            if grid[i + 1][j] == "." and grid[i][j] == "W" and prev != i - 1:
                grid[i + 1][j], grid[i][j] = grid[i][j], grid[i + 1][j]
                moved = True
                prev = i
    return moved


R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]  # add padding

Q = int(input())
for _ in range(Q):
    t = int(input())
    if t == 1:
        move_heads()
        move_blood()
    else:
        for i in grid:
            print("".join(i))
