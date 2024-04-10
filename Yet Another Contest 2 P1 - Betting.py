# Induction/guessing:
# It looks like we can just set Y=1 since if we set it to 2, we would need to put twice
# as much money into X or else the money won't be enough to cover a failed bet with Y
#
# Then just rearrange equation (where A and B are constants)

from fractions import Fraction

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    A = Fraction(b, a)
    B = Fraction(d, c)

    if B - 1 > Fraction(1, A - 1):
        print("YES")
    else:
        print("NO")
