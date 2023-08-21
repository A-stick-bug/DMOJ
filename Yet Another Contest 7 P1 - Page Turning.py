# bad problem, not recommended

n = int(input())
pages = list(map(int, input().split()))

# put the even ones together and then the odd ones
odd = []
even = []
for i in range(1, n + 1):
    if pages[i - 1] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if odd:
    total = [odd[0]] + even + odd[1:]
else:
    total = even

inconv = 0
for i in even:
    if odd:
        inconv += max(0, pages[i - 1] // 2 - 1)
    else:
        inconv += max(0, (pages[i - 1]) // 2)

start = 0
for i in odd:
    inconv += max(0, (pages[i - 1]) // 2)

print(inconv)
print(*total)
