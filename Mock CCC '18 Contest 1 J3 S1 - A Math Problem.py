# math problem: using derivative to find min

from math import sqrt, floor

K, P, X = map(int, input().split())
KP = K * P  # consider KP to be one value

min1 = floor(sqrt(KP / X))  # find the derivative to get 2 potential the minimums since M must be an integer
if min1 == 0:
    min1 += 1
min2 = min1 + 1

# plug it back in the equation to find f(M)
f = lambda m: round(X * m + KP / m, 3)

m = float(min(f(min1), f(min2)))
dec = str(m).split(".")

dec[1] += "0" * (3 - len(dec[1]))
print(*dec, sep=".")