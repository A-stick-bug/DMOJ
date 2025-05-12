# https://dmoj.ca/problem/dmopc18c4p3
# Similar idea to https://dmoj.ca/problem/othscc1p4 with extra greedy observation
# Note that we first do all single electrons, then we remove everything else double
# It is always optimal to use the double removal on the ones with largest A-B value

n = int(input())
arr = list(zip(list(map(int, input().split())), list(map(int, input().split()))))

arr.sort(key=lambda x: x[0] - x[1], reverse=True)  # sort by best savings

left = 0
right = sum(a for a, b in arr)
best = right
for i in range(1, n, 2):
    left += arr[i - 1][1] + arr[i][1]
    right -= arr[i - 1][0] + arr[i][0]
    best = min(best, left + right)

# print(arr)
print(best)
