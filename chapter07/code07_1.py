from collections import namedtuple
import random
import pprint

Item = namedtuple("Item", ("name", "weight", "price"))

num = 20
max_weight = 5
max_price = 50

#price_list = list(range(1, max_price + 1))
# random.shuffle(price_list)


item_list = [Item(i, random.randint(1, max_weight), random.randint(1, max_price))
             for i in range(num)]

# pprint.pprint(item_list)
