from code07_1 import item_list
from code07_2 import Knapsack
import pprint


def greedy(items, size_limit):
    sorted_item_list = sorted(items, key=lambda x: x.price / x.weight, reverse=True)
    my_knapsack = Knapsack(size_limit)
    for v in sorted_item_list:
        try:
            my_knapsack.append(v)
        except ValueError:
            continue
        """
        appendメソッドがナップサックに入らない品物を引数にとると例外を発生することがわかっているので、try-except構文を使っている
        """
    return my_knapsack


knap_g = greedy(item_list, 40)

print(knap_g)

pprint.pprint(knap_g.items)
