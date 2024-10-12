# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
# https://dmoj.ca/problem/coci06c5p6
# Hashing

from itertools import accumulate

N = int(input())
str1 = list(map(lambda x: ord(x) - 97, input()))  # lower case alphabet

# - hash start -
# MOD = 177635683940025046467781066894531
MOD = 2147483647  # 2^31 - 1
MOD2 = 2147483629  # double hashing
p = 29

power = [0] * N  # precompute powers of `p`, with MOD
power[0] = 1
for i in range(1, N):
    power[i] = (power[i - 1] * p) % MOD

power2 = [0] * N  # precompute powers of `p`, with MOD2
power2[0] = 1
for i in range(1, N):
    power2[i] = (power2[i - 1] * p) % MOD2

hash1 = [0] * N  # precompute hashes of each character in `str1`
for i in range(N):
    hash1[i] = (str1[i] * power[N - i - 1]) % MOD
psa1 = [0] + list(accumulate(hash1))  # psa for range hash query

hash2 = [0] * N  # double hash
for i in range(N):
    hash2[i] = (str1[i] * power2[N - i - 1]) % MOD2
psa2 = [0] + list(accumulate(hash2))


# - hash end -


def works(le):
    seen = set()
    for i in range(N - le + 1):
        # get both hashes
        hash_single = (psa1[i + le] - psa1[i]) * power[i] % MOD  # shift up
        hash_double = (psa2[i + le] - psa2[i]) * power2[i] % MOD2  # shift up
        p = (hash_single, hash_double)
        if p in seen:
            return True
        seen.add(p)
    return False


low = 0
high = N
while low <= high:
    mid = low + (high - low) // 2
    if works(mid):
        low = mid + 1
    else:
        high = mid - 1

print(low - 1)
