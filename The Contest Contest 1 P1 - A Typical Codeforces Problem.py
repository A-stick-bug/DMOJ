n = int(input())
s = list(input())

left = -1
for i, char in enumerate(s):
    if char == "Y":
        left = i

if left + 1 > n // 2:
    print("YES")
else:
    print("NO")
