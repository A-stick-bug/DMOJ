n = int(input())
if n % 4 == 0:  # 4, 8, 12 etc.
    for i in range(1, n // 4 + 1):
        print(n // 2, end=' ')
    for i in range(1, n // 4 + 1):
        print(0, end=' ')
    for i in range(1, n // 2 + 1):
        print(-1, end=' ')

elif n % 4 == 2:  # even case 2: 2, 6, 10, etc
    for i in range(1, n // 4 + 1):
        print(n // 2, end=' ')
    print(n // 4, end=' ')
    for i in range(1, n // 4 + 1):
        print(0, end=' ')
    for i in range(1, n // 2 + 1):
        print(-1, end=' ')

else:  # odd case
    if n % 4 == 1:  # 5, 9, 13, etc
        sign = -1
    else:  # 7, 11, 15, etc
        sign = 1
    for i in range(1, n + 1, 2):
        print(i * sign, end=' ')
        sign = -sign
    sign = 1
    for i in range(n - 1, 0, -2):
        print(i * sign, end=' ')
        sign = -sign

# for testing purposes
# def x_y(arr):
#     pos = 0
#     neg = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr) + 1):
#             total = sum(arr[i:j])
#             if total >= 0:
#                 pos += 1
#             else:
#                 neg += 1
#     # print(f"Positive: {pos}")
#     # print(f"Negative: {neg}")
#     # print(f"Difference: {abs(pos - neg)}")
#     return abs(pos - neg)


# finding the pattern
# from random import randint
#
# n=4
# test=[1,-2,-3,4]
# used = set()
# for i in range(100000):
#     a = randint(0, n-1)
#     b = randint(0, n-1)
#     test[a], test[b] = test[b], test[a]
#
#     d = x_y(test)
#     if d == 1 or d == 0:
#         t = tuple(test)
#         used.add(t)
#         # print(test)
#         # print(x_y(test))
#
# for i in used:
#     print(i)
