# 28/40, code is still too long
# strategy: first write a working code, then improve from there

# # base code
# n = int(input())
# prime = [True for i in range(n + 1)]
# p = 2
# for p in range(2, int(n**0.5)+1):
#     if prime[p]:
#         for i in range(p * p, n + 1, p):
#             prime[i] = False
#     p += 1
#
# for p in range(2, n + 1):
#     if prime[p]:
#         if prime[p-2] or prime[p+2]:
#             print(p,"*",sep="")
#         else:
#             print(p)

# # checkpoint 1
# for p in range(2,int((n:=len(t:=[0]+[1for i in range(1, int(input()) + 1)]))**.5)+1):
#     if t[p]:
#         t.__setitem__(slice(p * p, n, p),[0 for _ in range(p * p, n, p)])
#
# [print(str(p) + "*" if t[p - 2] or t[p + 2] else p) for p in range(2, n) if t[p]]

# checkpoint 2 (removed some spaces and stuff)
#                                                                 ceil trick to get length
#[n:=len(t:=[0]+[1]*int(input()))],[t.__setitem__(slice(p*p,n,p),[0]*((n-p*p+p-1)//p))for p in range(2,int(n**.5)+1)if t[p]],[print(str(p)+"*"*(t[p-2]|t[p+2]))for p in range(2,n)if t[p]]

# checkpoint 3 (small optimizations)
#[t:=[0]+[1]*(n:=int(input()))],[t.__setitem__(slice(p+p,n,p),[0]*((n-p-1)//p))for p in range(2,n)if t[p]],[print(str(p)+"*"*(t[p-2]|t[p+2]))for p in range(2,n)if t[p]]

[t:=[0]+[1]*(n:=int(input())),r:=range],[t.__setitem__(i,0)for p in r(2,n)if t[p]for i in r(p*p,n,p)],[print(str(p)+"*"*(t[p-2]|t[p+2]))for p in r(2,n)if t[p]]
