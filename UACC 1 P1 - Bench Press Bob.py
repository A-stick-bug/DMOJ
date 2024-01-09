n = int(input())
if n < 45:
    print("Rip Bob!")
else:
    n -= 45
    if n % 90 == 0:
        print("Let's go Bob!")
    else:
        print("Rip Bob!")
