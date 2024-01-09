# boring casework

n = int(input())

if n % 4 == 2:
    print(n + n // 2 - 2)
elif n % 4 == 3:
    print(n + n // 2)
else:
    print(n + n // 2 - 1)
