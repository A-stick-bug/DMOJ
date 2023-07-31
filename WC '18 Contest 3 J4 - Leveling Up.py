# O(P) where p is the number of locations on the trail

n = int(input())
left, level = map(int, input().split())
right = left  # both pointers start at same location

pokemons = {}
for _ in range(n):
    loc, lvl, gain = map(int, input().split())
    pokemons[loc] = (lvl, gain)

while left >= 0 or right <= 100000:
    pl, pr = left, right

    if left >= 0:  # try increasing level by moving left
        if left in pokemons:
            if level >= pokemons[left][0]:
                level += pokemons[left][1]
                left -= 1  # won battle
        else:
            left -= 1  # nothing here, move on

    if right <= 100000:  # try increasing level by moving right
        if right in pokemons:
            if level >= pokemons[right][0]:
                level += pokemons[right][1]
                right += 1
        else:
            right += 1

    if pl == left and pr == right:  # we are stuck and can't beat anything
        break

print(level)
