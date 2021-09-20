from code07_1 import item_list
from code07_2 import Knapsack


def dp(items, size_limit):
    n = len(items)

    table = [[0] * (size_limit + 1) for _ in range(n + 1)]

    flag = [[False] * (size_limit + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        target = items[i - 1]
        w = target.weight
        for j in range(1, size_limit + 1):
            yellow = table[i - 1][j]
            table[i][j] = yellow

            if w > j:
                continue
            pink = table[i - 1][j - w]
            include_this = target.price + pink
            table[i][j] = max(yellow, include_this)
            flag[i][j] = include_this > yellow

    i = n
    j = size_limit
    my_knapsack = Knapsack(size_limit)
    while i > 0 and j > 0:
        if flag[i][j]:
            my_knapsack.append(items[i - 1])
            j -= items[i - 1].weight
        i -= 1

    return my_knapsack


knap_dp = dp(item_list, 40)
print(knap_dp)
