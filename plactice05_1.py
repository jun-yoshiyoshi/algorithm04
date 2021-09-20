import random
from code05_3 import Node
from code05_3 import Binary_search_tree

btree = Binary_search_tree()

n = int(input())

# array = []
# while len(array) < n:
#     _ = random.randint(0, 100)
#     if _ not in array:
#         array.append(_)

array = random.sample(range(0, 100), n)

for v in array:
    btree.add_node(v)

print(btree)

for node in btree.root:
    print(node)
