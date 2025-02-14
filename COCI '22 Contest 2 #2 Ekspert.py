# https://dmoj.ca/problem/coci22c2p2
# Take the larger number as X and use a method equivalent to
# binary exponentiation (but multiplication instead)
#
# Each register has a task
# A: stores the current 'base'
# B: not used in this implementation
# C: stores the accumulated sum (answer)
# D: not used in this implementation

x, y = map(int, input().split())

moves = []

# ensure X is the larger one
if x > y:
    s = "ABCD"
else:
    s = "BACD"
    x, y = y, x
registers = [x, y, 0, 1]


def perform_addition(s1, s2, target):
    global moves
    moves.append(" ".join([s[s1], s[s2], s[target]]))
    registers[target] = registers[s1] + registers[s2]


rem = y  # number of multiplications to do still
while rem > 0:
    # even, doubling the base halves the number of operations
    if rem % 2 == 0:
        perform_addition(0, 0, 0)
        rem //= 2
    # odd, do 1 operation to make it even
    else:
        perform_addition(0, 2, 2)
        rem -= 1

print(len(moves))
print("\n".join(moves))
print("C")
