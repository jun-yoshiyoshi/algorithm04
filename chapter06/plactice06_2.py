from collections import deque
from code06_1 import my_graph
import pprint


def breadth_first_search(start, W):
    """
    隣接行列Wのグラフで、startから到達できるnodeの一覧を返す
    """
    work_queue = deque([])
    visited = set()
    paths = []
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
                paths.append([here, i])
    return visited, paths


_, bfs_paths = breadth_first_search(2, my_graph)

pprint.pprint(bfs_paths)


def depth_first_search(start, W):
    """
    各頂点で探索できるnodeをリスト(stack)に保存し、先に探索するnodeを優先的に探索する。
    """
    work_stack = []
    visited = set()
    paths = []
    work_stack.append(start)
    visited.add(start)
    while work_stack:
        here = work_stack.pop()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                work_stack.append(i)
                visited.add(i)
                paths.append([here, i])
    return visited, paths


_, dfs_paths = depth_first_search(2, my_graph)

pprint.pprint(dfs_paths)
