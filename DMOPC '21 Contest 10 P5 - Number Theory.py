# 75/100
# credit to yujhtheyujh
print(12618316580415)


def num_of_divisors(m):
    count = 0
    for i in range(1, int(math.sqrt(m)) + 1):
        if m % i == 0:
            # If divisors are equal, count only one
            if m / i == i:
                count += 1
            else:  # Otherwise count both
                count += 2
    return count


from collections import Counter


def div2_factors(prime_factors):
    num_divisors = 1
    factor_counts = Counter(prime_factors)
    for exponent in factor_counts.values():
        num_divisors *= (exponent + 1)
    return num_divisors


import math


def coprimes(m):
    count = 0
    for i in range(1, m + 1):
        if math.gcd(i, m) == 1:
            count += 1
    return count


def coprime_with_factors(n, prime_factors):
    result = n
    for p in prime_factors:
        result *= (1 - 1 / p)
    return int(result)


import random

first = [3, 5, 7, 13, 17, 19, 37, 73, 97, 109, 163, 193, 257, 433, 487, 577, 769, 1153, 1297]
second = [27, 5, 7, 13, 17, 19, 37, 73, 97, 109, 163, 193, 257, 433, 487, 577, 769, 1153, 1297]


def solve(arr):
    from itertools import combinations
    all_comb = list(combinations(arr, 6))

    for numbers in all_comb:
        product = 1
        for num in numbers:
            product *= num

        divphi = num_of_divisors(coprime_with_factors(product, numbers))
        phidiv = coprimes(div2_factors(numbers))
        if divphi == phidiv:
            print(product)
            return
        else:
            print("fail")



# solve(second)


# product = 12618316580415
# numbers = [3, 5, 7, 13, 17, 19, 193, 257, 577]
#
# divphi = num_of_divisors(coprime_with_factors(product, numbers))
# phidiv = coprimes(div2_factors(numbers))
# if divphi == phidiv:
#     print(product)
# else:
#     print("fail")
