n = int(input())
grid = [input() for _ in range(n)]
cols = [col.count("S") for col in zip(*grid)]

for i in range(n):
    row = ["."] * n
    for j in range(n):
        if n - i <= cols[j]:
            row[j] = "S"
    print("".join(row))
