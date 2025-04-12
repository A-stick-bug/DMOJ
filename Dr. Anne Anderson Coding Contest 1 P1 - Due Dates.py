n = int(input())
m = int(input())
if m in [n, n + 1]:
    print("stressed")
elif m < n:
    print("relaxed")
else:
    print("okay")
