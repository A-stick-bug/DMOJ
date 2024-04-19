import sys

N,H = map(int, input().split())
a = [input().split() for _ in range(N)]
b = [input().split() for _ in range(N)]

A = B = H
for i in range(N):
    if a[i][0] == "A":
        B -= int(a[i][1])
        if B <= 0:
            print("VICTORY")
            sys.exit()
    else:
        if b[i][0] == "A":
            A += int(b[i][1])  # cancel out damage
        else:
            A -= int(a[i][1])
            if A <= 0:
                print("DEFEAT")
                sys.exit()

    if b[i][0] == "A":
        A -= int(b[i][1])
        if A <= 0:
            print("DEFEAT")
            sys.exit()
    else:
        if i == N-1 or a[i+1][0] == "D":
            B -= int(b[i][1])
            if B <= 0:
                print("VICTORY")
                sys.exit()
        else:
            B += int(a[i+1][1])

print('TIE')
