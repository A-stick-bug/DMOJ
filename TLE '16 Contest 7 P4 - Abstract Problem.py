# https://dmoj.ca/problem/tle16c7p4
# O(T*log(n))
# bitwise operators and math

ctz = lambda n: ((n & -n) - 1).bit_length()  # count trailing 0 in binary


def search(end):
    cnt = 0
    while end > 0:
        if end == 3:  # corner case
            end -= 1
        elif end & 1:  # go to nearest integer with more powers of 2 since dividing is faster than minus
            if ctz(end + 1) > ctz(end - 1):
                end += 1
            else:
                end -= 1
        else:
            end //= 2
        cnt += 1
    return cnt


for _ in range(int(input())):
    n = int(input())
    print(search(n))
