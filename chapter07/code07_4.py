from code07_1 import item_list
from code07_2 import Knapsack
import itertools


def brute_force(items, size_limit):

    candidate = None

    for pattern in itertools.product((0, 1), repeat=len(items)):
        my_box = []
        for i, val in enumerate(pattern):
            if val:
                my_box.append(item_list[i])
            w = sum([item.weight for item in my_box])

            if w > size_limit:
                continue

            value = sum([item.price for item in my_box])

            if candidate is None or value > candidate.value:
                knapsack = Knapsack(size_limit)

                for v in my_box:
                    knapsack.append(v)
                candidate = knapsack

    return candidate


knap_bf = brute_force(item_list, 40)
print(knap_bf)
