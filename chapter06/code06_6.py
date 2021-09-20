from code06_1 import my_graph
import math
import pprint


def all_pairs_shortest_paths(W):
    n = len(W)

    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                val = 0
            elif W[i][j]:
                val = W[i][j]
            else:
                val = math.inf
            res[i][j] = res[j][i] = val

    for k in range(n):
        for u in range(n):
            for v in range(n):
                res[u][v] = min(res[u][v], res[u][k] + res[k][v])
    return res


pprint.pprint(all_pairs_shortest_paths(my_graph))
