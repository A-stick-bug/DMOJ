# https://dmoj.ca/problem/scb24p3
# 2 questions in 1
# use greedy for both

def rev_num(num):
    return int(str(num)[::-1])


N, K = map(int, input().split())
arr = list(map(int, input().split()))

reduces = [i - rev_num(i) for i in arr if i > rev_num(i)]  # possible reduction amounts
neither = [0 for i in arr if i == rev_num(i)]
increases = [rev_num(i) - i for i in arr if i < rev_num(i)]  # possible increase amounts

# print(sum(arr))
# print(reduces, neither, increases)

# solve min
total_min = sum(arr)
reduces.sort(reverse=True)
total_min -= sum(reduces[:K])

if K > len(reduces):
    extras = K - len(reduces)
    # we can't waste coupons, find a way to spend them with minimal consequences
    if not (neither or extras % 2 == 0):
        total_min += min(min(reduces) if reduces else float('inf'), min(increases) if increases else float("inf"))

# solve max
total_max = sum(arr)
increases.sort(reverse=True)
total_max += sum(increases[:K])

if K > len(increases):  # deal with extra coupons
    extras = K - len(increases)
    # we can't waste coupons, find a way to spend them with minimal consequences
    if not (neither or extras % 2 == 0):
        total_max -= min(min(reduces) if reduces else float('inf'), min(increases) if increases else float("inf"))

print(total_min, total_max)

"""
5 7
12 23 34 54 65
"""
