from code05_3 import Node
from code05_3 import Binary_search_tree

btree = Binary_search_tree()

for v in [10, 20, 12, 4, 3, 9, 30]:
    btree.add_node(v)

print(btree)

for node in btree.root:
    print(node)
