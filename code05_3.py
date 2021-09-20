class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        left = f"[{self.left.value}]" if self.left else "[]"
        right = f"[{self.right.value}]" if self.right else "[]"
        return f"{left}<-{self.value}->{right}"


class Binary_search_tree:
    def __init__(self):
        self.root = []

    def add_node(self, value):
        node = Node(value)
        if self.root:
            parent, direction = self.find_parent(value)
            if direction == "left":
                parent.left = node
            else:
                parent.right = node
        self.root.append(node)

    def find_parent(self, value):
        node = self.root[0]
        while node:
            p = node
            if p.value == value:
                raise ValueError("すでにある値と同じ値を格納することはできません")
            if p.value > value:
                direction = "left"
                node = p.left
            else:
                direction = "right"
                node = p.right
        return p, direction
