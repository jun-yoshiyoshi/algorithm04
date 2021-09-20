from code06_1 import my_graph
import pprint
from code06_6 import all_pairs_shortest_paths


def select_pairs(matrix, l):
    n = len(matrix)
    res = []

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] <= l:
                res.append((i, j))
    return res


matrix = all_pairs_shortest_paths(my_graph)

pprint.pprint(select_pairs(matrix, 3))
