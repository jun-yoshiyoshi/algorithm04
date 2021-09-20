import string
import random
from code05_6 import Hash_table


def get_random_str(num):
    dat = string.ascii_lowercase
    return ''.join([random.choice(dat) for i in range(num)])


table = Hash_table()

#array = [[get_random_str(5), random.randint(0, 1000)] for _ in range(10)]


count = 0

while count < 300:
    table.set(get_random_str(5), random.randint(0, 1000))
    count += 1

print(table.data)
