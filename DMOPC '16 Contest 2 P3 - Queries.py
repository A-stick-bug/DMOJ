# tip: ignore sample case: it is there to throw you off

def solve():
    N, M = map(int, input().split())
    ma = mb = 0
    for _ in range(M):
        a, b = map(int, input().split())
        ma = max(a, ma)
        mb = max(b, mb)

    if ma + mb > N:
        print(-1)
    print(ma * "a" + (N - ma) * "b")


for _ in range(int(input())):
    solve()
