# https://dmoj.ca/problem/joi05fp3
# Generate and print all partitions of a number, large to small

def generate(cur, seq):
    if cur == 0:
        print(" ".join(map(str, seq)))

    mx = min(seq[-1], cur) if seq else cur
    for rem in reversed(range(1, mx + 1)):
        generate(cur - rem, seq + [rem])


n = int(input())
generate(n, [])
