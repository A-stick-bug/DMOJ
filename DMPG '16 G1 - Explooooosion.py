# # https://dmoj.ca/problem/dmpg16g1
#
# from collections import Counter
#
# MOD = 10**9 + 7
# n = int(input())
# nums = list(map(int, input().split()))
# count = Counter(nums)
#
# if count[1] == n:
#     print(1)
# else:
#     smallest = 0
#     for i in nums:
#         if i != 1:
#             smallest += i
#             smallest %= MOD
#     print(smallest)
#
# # use 3 for maximal multiplication value
# if count[1] == 2 and count[2] == 1:
#     count[1] = 0
#     count[2] += 1
#
# else:
#     m = min(count[1], count[2])
#     count[3] += m
#     count[1] -= m
#     count[2] -= m
#
# if count[1] >= 3:
#     rem = count[1] % 3
#     if rem == 0:  # all 3
#         count[3] += count[1]//3
#     elif rem == 2:  # (3,2)
#         count[3] += count[1]//3
#         count[2] += 1
#     else:  # if there's 1 leftover, (2,2) us better than (3,1)
#         count[3] += (count[1]-3)//3
#         count[2] += 2
#     count[1] = 0
#
# elif count[1] == 2:  # 2 leftovers, turn into 2
#     count[1] = 0
#     count[2] += 1
#
# elif count[1] == 1:  # add to smallest
#     smallest = float('inf')
#     for k in count.keys():
#         smallest = min(smallest, k)
#     count[smallest] += 1
#
# highest = 1
# for k in count.keys():
#     for i in range(count[k]):
#         highest *= k
#         highest %= MOD
#
# print(highest)


import heapq

MOD = 10 ** 9 + 7
N = int(input())
nums = list(map(int, input().split()))
one = nums.count(1)

smallest = 0
pq = []

for num in nums:  # smallest is just sum without the ones
    if num != 1:
        smallest += num
        pq.append(num)

if smallest == 0:  # corner case: all 1
    smallest = 1
print(smallest)

heapq.heapify(pq)

while one:
    if len(pq) < 2:
        if one > 1:
            heapq.heappush(pq, 2)
            one -= 2

        elif one == 1:
            if pq:
                temp1 = heapq.heappop(pq)
                heapq.heappush(pq, temp1 + 1)
                one -= 1
            else:
                heapq.heappush(pq, 1)
                break

    else:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        if one > 1 and a == 2 and b == 2:
            heapq.heappush(pq, 3)
            heapq.heappush(pq, 3)
            one -= 2

        elif one == 1:
            heapq.heappush(pq, a + 1)
            heapq.heappush(pq, b)
            one -= 1

        elif one > 1:
            heapq.heappush(pq, 2)
            heapq.heappush(pq, a)
            heapq.heappush(pq, b)
            one -= 2


while len(pq) > 1:  # could be optimized
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    heapq.heappush(pq, (a * b) % MOD)

print(pq[0])
