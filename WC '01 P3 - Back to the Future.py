for _ in range(int(input())):
    b = bin(int(input()))[2:]
    b = str(b)[::-1]
    print(int(b, 2))
