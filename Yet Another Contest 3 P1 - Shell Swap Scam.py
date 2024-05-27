import sys

input = sys.stdin.readline
N, M, start, end = map(int, input().split())
moves = [list(map(int, input().split())) for _ in range(M)]

loc = start
dest = end

for ei in reversed(range(M)):
    if len(moves[ei]) == 1:
        break
    elif end in moves[ei]:
        end = moves[ei][0] if moves[ei][0] != end else moves[ei][1]

for i in range(M):
    if len(moves[i]) == 2:  # forced move
        if loc in moves[i]:
            loc = moves[i][0] if moves[i][0] != loc else moves[i][1]
        print(*moves[i])
    else:
        if loc != end:  # keep on moving it to the end
            print(loc, end)
            loc = end
        else:
            if loc == 1:  # do a useless move
                print(2, 3)
            elif loc == 2:
                print(1, 3)
            else:
                print(1, 2)
