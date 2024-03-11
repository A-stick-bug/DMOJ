import sys

x, y, z = map(int, input().split())
l = int(input())


def check_win():
    if a >= l:
        print(1)
        sys.exit()
    if b >= l:
        print(2)
        sys.exit()


a = b = 0
while True:
    check_win()
    if a < b:
        a += x
        check_win()
    else:
        b += y
        check_win()
        a += z
        check_win()
