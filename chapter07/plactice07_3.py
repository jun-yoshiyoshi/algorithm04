import random
import pprint

from code07_1 import item_list, Item
from code07_2 import Knapsack


random.seed(7)

# 品物の数
num = 10

# 品物を生成するための数を保持するリスト
val_list = []

# 最初の品物の重さ。重さの10％の標準偏差で正規分布に従う乱数を生成
w = random.gauss(2, 2*0.1)
val_list.append(w)

for i in range(num):
    total_w = sum(val_list)
    w = total_w + abs(random.gauss(total_w * 0.1, 1))
    val_list.append(w)

tender_list = []
for i, v in enumerate(val_list):
    tender_list.append(Item(i, v, v))

pprint.pprint(tender_list)


def greedy_for_tender(items, size_limit):
    #　重さ（または値段）で品物を並び替える。
    sorted_item_list = sorted(items, key=lambda x: x.weight, reverse=True)
    my_knapsack = Knapsack(size_limit)
    for v in sorted_item_list:
        # 入る余地があるなら品物を入れる。
        try:
            my_knapsack.append(v)
        except ValueError:
            continue
    return my_knapsack


answer_knapsack = greedy_for_tender(tender_list, 3000)

print(answer_knapsack)

pprint.pprint(answer_knapsack.items)
