# https://dmoj.ca/problem/dwite11c3p5
# Python eval go brrr
# Brute force all true/false combinations for each letter
# Since there are only 10 letters, this won't TLE

t = 5
tt = 3
letter = "abcdefghij"
n = len(letter)

for _ in range(t):
    res = []
    for _ in range(tt):  # each test case
        statement = input()

        # map to a notation Python can understand
        statement = statement.replace("^", "&")
        statement = statement.replace("v", "|")
        statement = statement.replace("~", "1^")

        works = True
        for mask in range(1 << n):  # try all combinations
            st = statement
            for bit in range(n):
                if mask & (1 << bit):
                    st = st.replace(letter[bit], "1")
                else:
                    st = st.replace(letter[bit], "0")
            if not eval(st):
                works = False
                break
        res.append("Y" if works else "N")
    print("".join(res))
