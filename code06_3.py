from collections import deque
from code06_1 import my_graph


def breadth_first_search(start, W):
    """
    隣接行列Wのグラフで、startから到達できるnodeの一覧を返す
    """
    work_queue = deque([])
    visited = set()

    work_queue.append(start)
    visited.add(start)
    while work_queue:
        here = work_queue.popleft()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                work_queue.append(i)
                visited.add(i)
    return visited


print(breadth_first_search(1, my_graph))

print(breadth_first_search(10, my_graph))
