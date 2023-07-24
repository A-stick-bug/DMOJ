# simple dict/hashmap usage

n_order = int(input())
order_map = {input(): i for i in range(1, n_order + 1)}  # give each type a number so we can sort

n_problems = int(input())
problems = []
for i in range(1, n_problems + 1):
    p = input()
    order = order_map[p]
    problems.append((order, i))  # (priority number, problem number)

problems.sort()  # sort by priority to complete
for _, i in problems:
    print(i)
