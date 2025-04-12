double = ["FIREGRASS", "WATERFIRE", "GRASSWATER"]
half = ["FIREWATER", "WATERGRASS", "GRASSFIRE"]

best = 0
enemy = input()
n = int(input())
for _ in range(n):
    dmg, t = input().split()
    dmg = int(dmg)

    atk = t + enemy
    if atk in double:
        dmg *= 2
    if atk in half:
        dmg //= 2

    best = max(best, dmg)
print(best)
