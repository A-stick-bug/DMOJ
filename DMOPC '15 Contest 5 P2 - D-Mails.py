def is_subseq(s, t):
    """check if s is a subsequence of t"""
    ls = 0
    for letter in t:
        if ls < len(s) and letter == s[ls]:
            ls += 1
    return ls == len(s)


people = ["Okabe", "Mayuri", "Daru", "Kurisu"]
tags = ["elpsycongroo", "tuturu", "superhacker", "myfork"]

n = int(input())
for _ in range(n):
    msg = input()
    possible_senders = []
    for person, tag in zip(people, tags):
        if is_subseq(tag, msg):
            possible_senders.append(person)

    if not possible_senders:
        print("SERN spy!")
    else:
        print(*possible_senders, sep=" or ")