# https://dmoj.ca/problem/bdep
# binary search + returning early optimization


def works(n) -> bool:
    """check if depositing n each year is enough"""
    total = 0
    for i in range(Y):
        total += n
        total += total * P // 100  # use integers to prevent float overflow
        if total >= T:  # return early to save time (or else TLE)
            return True
    return False


P, Y, T = map(int, input().split())  # P% increase each year, Y years, T is the goal

# template binary search
low = 1
high = 10 ** 16
while low <= high:
    mid = low + (high - low) // 2
    if works(mid):
        high = mid - 1
    else:
        low = mid + 1

print(low)