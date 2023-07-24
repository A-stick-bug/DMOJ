from collections import defaultdict

for _ in range(int(input())):  # test cases
    stores = int(input())
    costs = defaultdict(list)
    for _ in range(stores):  # go through all stores
        n = int(input())
        for _ in range(n):  # get item price from this store
            item, price, quantity = input().split()
            costs[item].append([int(price), int(quantity)])

    # sort by price to get cheapest, also add number to keep track of store that still has stock
    costs = {k: sorted(v)+[0] for k, v in costs.items()}

    total = 0  # total cost of items
    for _ in range(int(input())):  # find cost for each item
        item, amt = input().split()
        amt = int(amt)
        cost = costs[item]
        for i in range(cost[-1], len(cost)-1):  # -1 because last value is reserved for index
            if cost[i][1] > amt:
                total += amt*cost[i][0]
                cost[i][1] -= amt
                break
            else:
                amt -= cost[i][1]
                total += cost[i][0] * cost[i][1]
                cost[-1] += 1

    print(total)
