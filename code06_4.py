from code06_1 import my_graph


def depth_first_search(start, W):
    """
    各頂点で探索できるnodeをリスト(stack)に保存し、先に探索するnodeを優先的に探索する。
    """
    work_stack = []
    visited = set()

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
    return visited


print(depth_first_search(1, my_graph))

print(depth_first_search(10, my_graph))
