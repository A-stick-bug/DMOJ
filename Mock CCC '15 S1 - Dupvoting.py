p, u, r1, r2 = [int(input()) for _ in range(4)]

total = 0
for a in range(1,u):
    for b in range(1,u):
        c = u - a - b
        if c < 0:
            continue
        if a + a + b - c != p:
            continue
        if a * r1 == b * r2 or b * r1 == c * r2 or a * r1 == c * r2:
            total += 1
            continue
        r1, r2 = r2, r1
        if a * r1 == b * r2 or b * r1 == c * r2 or a * r1 == c * r2:
            total += 1
        r1, r2 = r2, r1

print(total)
