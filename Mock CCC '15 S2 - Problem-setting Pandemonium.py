# get highest frequency

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

freq = Counter(arr)

print(max(freq.values()))
