# https://dmoj.ca/problem/dmopc21c4p3
# Observation based question
# Brute force smaller cases and observe patterns
#
# Note that the middle 3 digits can be brute forced if you are having trouble figuring out the optimal arrangement

ans = """0
10001
10101
10201
10301
11011
11111
11211
12021
13031"""

print(ans)

# # Observe patterns for smaller numbers
# def works(x):
#     return str(x) == str(x)[::-1]
#
# # https://oeis.org/A002113 palindromic integers
# p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
#      202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424,
#      434, 444, 454, 464, 474, 484, 494, 505, 515]
# n = len(p)
#
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             for l in range(k + 1, n):
#                 for m in range(l + 1, n):
#                     for o in range(m+1, n):
#                         stuff = [p[x] for x in [i, j, k, l, m, o]]
#                         work = True
#                         for mask in range(1 << len(stuff)):
#                             res = []
#                             for b in range(len(stuff)):
#                                 if mask & (1 << b):
#                                     res.append(stuff[b])
#                             if not works(sum(res)):
#                                 work = False
#                                 break
#                         if work:
#                             print(stuff)
