n = int(input())
arr = list(map(int, input().split()))

o = sum(i % 2 == 1 for i in arr)
e = sum(i % 2 == 0 for i in arr)

if n % 2 == 0:
    if e >= n // 2:
        print("Steven")
    else:
        print("Todd")
else:
    print("Steven")
