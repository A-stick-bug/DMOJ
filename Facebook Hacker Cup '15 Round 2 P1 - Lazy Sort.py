# greedy algorithm using deque and 'while: else:' very pythonic 🐍

from collections import deque

for i_case in range(int(input())):  # for each test case
    n = int(input())
    start = deque(map(int, input().split()))
    start2 = start.copy()

    end = deque([start.popleft()])
    end2 = deque([start2.pop()])  # check starting from both the start and end

    while start:
        if start[0] == end[0] + 1:
            end.appendleft(start.popleft())
        elif start[0] == end[-1] - 1:
            end.append(start.popleft())
        elif start[-1] == end[0] + 1:
            end.appendleft(start.pop())
        elif start[-1] == end[-1] - 1:
            end.append(start.pop())
        else:
            break  # this prevents the below else statement from executing

    else:  # this means the while loop ended 'normally', without the break
        print(f"Case #{i_case + 1}: yes")
        continue

    # this code is only reached if we haven't found a solution in the first part
    while start2:
        if start2[0] == end2[0] + 1:
            end2.appendleft(start2.popleft())
        elif start2[0] == end2[-1] - 1:
            end2.append(start2.popleft())
        elif start2[-1] == end2[0] + 1:
            end2.appendleft(start2.pop())
        elif start2[-1] == end2[-1] - 1:
            end2.append(start2.pop())
        else:
            print(f"Case #{i_case + 1}: no")
            break  # this prevents the below else statement from executing

    else:  # this means the while loop ended 'normally', without the break
        print(f"Case #{i_case + 1}: yes")
