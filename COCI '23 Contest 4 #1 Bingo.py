# just implementation

n = int(input())
names = []
boards = []
for _ in range(n):
    names.append(input())
    boards.append([list(map(int, input().split())) for _ in range(5)])

m = int(input())
nums = list(map(int, input().split()))


def win(board):
    pos = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if board[i][j] in nums:
                pos[i][j] = True

    return (any(sum(r) == 5 for r in pos) or
            any(sum(c) == 5 for c in zip(*pos[::-1])) or
            sum(pos[i][i] for i in range(5)) == 5 or
            sum(pos[i][5 - i - 1] for i in range(5)) == 5)


winners = []
for name, board in zip(names, boards):
    if win(board):
        winners.append(name)

print(len(winners))
print("\n".join(winners))
