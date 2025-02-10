# https://dmoj.ca/problem/strategicarrays
# Observation based question
# Answer for n is just fib(n + 2) - 1 (assuming sequence starts with 1 1)
#
# Using Binet's formula, fib(n) = 1/sqrt5 * ((1 + sqrt5)^n - (1 - sqrt5)^n)/(2^n)
# This formula always gives an integer solution since the integer terms in the numerator cancels out
# while the leftover sqrt5 terms in the numerator cancel out with the 1/sqrt5
#
# Reference: https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula

MOD = 10 ** 9 + 7
mod_div = lambda p, r: (p * pow(r, MOD - 2, MOD)) % MOD


def fib(n):
    """Generate the n-th fibonacci number where f(1) = 1, f(2) = 1"""

    def multiply(t1, t2):
        a, b = t1
        c, d = t2
        return [(a * c + 5 * b * d) % MOD, (b * c + a * d) % MOD]

    term1 = [1, 1]
    term2 = [1, -1]
    res1 = [1, 0]
    res2 = [1, 0]
    power = n
    while power > 0:
        if power % 2 == 1:  # odd, multiply by a term
            res1 = multiply(res1, term1)
            res2 = multiply(res2, term2)
            power -= 1
        else:  # even, square the base
            term1 = multiply(term1, term1)
            term2 = multiply(term2, term2)
            power //= 2
    assert res1[0] == res2[0]

    sqrt5_term = (res1[1] - res2[1]) % MOD
    res = mod_div(sqrt5_term, pow(2, n, MOD))
    return res


n = int(input())
print((fib(n + 2) - 1) % MOD)

# # bash out first few terms and observe
# for n in range(1, 16):
#     arr = list(range(1, n + 1))
#     total = 0
#     for mask in range(1 << n):
#         res = []
#         for bit in range(n):
#             if mask & (1 << bit):
#                 res.append(arr[bit])
#
#         if all((i + 1) % 2 == res[i] % 2 for i in range(len(res))):
#             # print(res)
#             total += 1
#
#     print(total, fib(n+2))
