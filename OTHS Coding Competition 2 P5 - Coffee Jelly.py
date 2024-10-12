# https://dmoj.ca/problem/othscc2p5
# Explanation found here: https://dmoj.ca/problem/othscc2p5/editorial
# Graph theory, flood fill, DFS
# Fill every open space containing people with walls
# Then count how many open spaces there are

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]


def fill_with_wall(row, col):
    """Fill an entire open area with walls"""
    stack = [(row, col)]
    grid[row][col] = 'X'  # turn into wall
    while stack:
        r, c = stack.pop()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + dr
            new_c = c + dc

            # out of bounds, skip
            if not (0 <= new_r < N and 0 <= new_c < M):
                continue
            # already a wall, skip
            if grid[new_r][new_c] == 'X':
                continue
            grid[new_r][new_c] = 'X'
            stack.append((new_r, new_c))


for i in range(N):
    for j in range(M):
        # turn open spaces with people into walls
        if grid[i][j] == '*':
            fill_with_wall(i, j)

total = 0
for i in range(N):
    for j in range(M):
        # found open space
        if grid[i][j] == '.':
            total += 1
            fill_with_wall(i, j)  # fill with wall to prevent overcounting

print(total)
