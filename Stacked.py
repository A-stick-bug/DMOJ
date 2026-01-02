# https://dmoj.ca/problem/stackeasy
# similar to selection sort

n = int(input())

moves = []

st1 = list(map(int, input().split()))
st2 = []
for i in range(1, n + 1):
    if i in st1:
        idx = st1.index(i)
        moves.extend([(1, 2)] * (len(st1) - idx - 1))
        moves.append((1, 3))
        st2.extend(st1[idx + 1:][::-1])
        del st1[idx:]
    else:
        idx = st2.index(i)
        moves.extend([(2, 1)] * (len(st2) - idx - 1))
        moves.append((2, 3))
        st1.extend(st2[idx + 1:][::-1])
        del st2[idx:]

print(len(moves))
moves = list(map(lambda x: str(x[0]) + " " + str(x[1]), moves))
print("\n".join(moves))
