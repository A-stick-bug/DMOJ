n = int(input())
s = input()
overlap = [0] * n

for _ in range(int(input())):
    match = input()
    for i in range(n - len(match) + 1):
        if s[i:].startswith(match):
            for j in range(i, i + len(match)):
                overlap[j] += 1

print(sum(i >= 2 for i in overlap))
