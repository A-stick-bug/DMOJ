def last_3(n):
    n = str(n)
    if len(n) > 3 and n[-1] == "8" and n[-2] == "8" and n[-3] == "8":
        return True
    return False


for _ in range(int(input())):
    num = int(input()) + 1
    while not last_3(num**3):
        num += 1
    print(num)