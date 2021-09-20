from code07_1 import item_list, Item
from code07_2 import Knapsack

"""
単位重さあたりの価値が高い品物から順に追加していき、
品物が入らなくなったところで、ループを抜ける。
ナップサックに残っている容量にピッタリ収まる仮想的な品物を作り、これを追加する。
"""


def div_knapsack(items, size_limit):
    #　単位重さあたりの価値で品物を並び替える。
    sorted_item_list = sorted(items, key=lambda x: x.price/x.weight, reverse=True)
    my_knapsack = Knapsack(size_limit)
    for v in sorted_item_list:
        # 入る余地があるなら品物を入れる。
        try:
            my_knapsack.append(v)
        except ValueError:
            break
    # vの一部を入るだけ入れる。
    w = my_knapsack.size - my_knapsack.weight
    p = v.price * (w / v.weight)
    virtual_item = Item(-1, w, p)
    my_knapsack.append(virtual_item)
    return my_knapsack


print(div_knapsack(item_list, 40))
