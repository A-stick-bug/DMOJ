# using the grouping technique
# [a, a, a, b, a] -> [(a, 3), (b, 1), (a, 1)]

def solve():
    n = int(input())
    s = input()

    blocks = []  # letter, count
    prev = "!"
    for i, char in enumerate(s):
        if char == prev:
            blocks[-1][1] += 1
        else:
            blocks.append([char, 1])
            prev = char

    best = 0
    for i in range(1, len(blocks) - 1):  # join 2 together
        if blocks[i][1] != 1:
            continue
        if blocks[i - 1][0] == blocks[i + 1][0] and blocks[i][1] == 1:
            best = max(best, blocks[i - 1][1] + blocks[i + 1][1] + 1)

    # add extra
    if len(blocks) > 1:
        best = max(best, 1 + max(blocks, key=lambda x: x[1])[1])
    elif len(blocks) == 1:
        best = max(best, max(blocks, key=lambda x: x[1])[1])
    print(best)


for _ in range(int(input())):
    solve()
