# bfs with modifications
# try all possible states and keep track of visited ones
# no need to worry about time complexity

n = 8
grid = [list(input()) for _ in range(n)]

deepcopy = lambda x: [i.copy() for i in x]
store = lambda x: tuple(tuple(i) for i in x)
dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def get_best(r, c):
    """get the best move using current checker"""
    best = 0
    stack = [(r, c, deepcopy(grid), 0)]  # row, col, visited in current path
    vis = {(r, c, store(grid), 0)}

    while stack:

        r, c, state, catch = stack.pop()

        for dr, dc in dir:
            hr, hc = r + dr, c + dc
            nr, nc = hr + dr, hc + dc
            if not (0 <= nr < n and 0 <= nc < n):  # outside
                continue
            if state[hr][hc] == "A" and state[nr][nc] == ".":  # hop over own cell
                new_state = deepcopy(state)
                new_state[r][c] = "."
                new_state[nr][nc] = "A"
                if (nr, nc, store(new_state), catch) in vis:
                    continue
                stack.append((nr, nc, new_state, catch))
                vis.add((nr, nc, store(new_state), catch))

            elif state[hr][hc] == "B" and state[nr][nc] == ".":  # hop over enemy cell
                new_state = deepcopy(state)
                new_state[hr][hc] = "."
                new_state[r][c] = "."
                new_state[nr][nc] = "A"
                if (nr, nc, store(new_state), catch + 1) in vis:
                    continue
                stack.append((nr, nc, new_state, catch + 1))
                best = max(best, catch + 1)
                vis.add((nr, nc, store(new_state), catch + 1))

    return best


res = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "A":
            res = max(res, get_best(i, j))

print(res)
