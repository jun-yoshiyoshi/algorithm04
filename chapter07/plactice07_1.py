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
            break
    """
    ループの中でcontinueが実行されると、最も内側のループの次のステップへ進む。
    break文が実行されると、そのループを抜ける。
    ナップサックに順々に品物を詰めていき、入らない品物が初めて見つかったとき、breakでは探索がそこで終わる。
    ナップサックの余った容量には、別の品物が入る可能性は残っているので、結果は貪欲法が正しく実行された時よりも悪いものとなる。
    """
    return my_knapsack


knap_g = greedy(item_list, 40)

print(knap_g)

pprint.pprint(knap_g.items)
