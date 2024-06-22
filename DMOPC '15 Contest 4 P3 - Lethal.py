# https://dmoj.ca/problem/dmopc15c4p3
# simple brute force, iterate over all attack combinations

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    hp2, hp1 = map(int, input().split())  # first kill hp1, then hp2

    for mask in range(1 << n):  # bitmask to get all subsets
        atk1 = sum(bool(mask & (1 << i)) * arr[i] for i in range(n))
        atk2 = sum(arr) - atk1
        if atk1 >= hp1 and atk2 >= hp2:
            print("LETHAL")
            return

    print("NOT LETHAL")


for _ in range(int(input())):
    solve()
