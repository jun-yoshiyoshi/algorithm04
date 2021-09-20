from code06_1 import my_graph
import pprint


def degree(W):
    # キーが頂点、値が次数になる辞書を用意
    res = {}
    for i in range(len(W)):
        res[i] = sum(W[i])
    return res


pprint.pprint(degree(my_graph))
