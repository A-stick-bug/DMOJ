# https://dmoj.ca/problem/egoi21p1
# make observation and avoid floats

a, b = map(int, input().split())

floor_div = lambda a, b: a // b  # accurate division, floats are bad
ceil_div = lambda a, b: (a + b - 1) // b

for p in range(61):  # check if there is a number with 2^p and 5^p as a factor inside [a,b]
    if floor_div(b, 2 ** p) >= ceil_div(a, 2 ** p) and floor_div(b, 5 ** p) >= ceil_div(a, 5 ** p):
        continue
    else:
        break

print(p - 1)
