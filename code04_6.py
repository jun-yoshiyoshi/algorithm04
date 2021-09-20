import time
import random
from code04_4 import merge_sort
from code04_5 import quick_sort
from code04_7 import quick2_sort


def performance_check(method, data, num=3):
    s = time.time()
    for i in range(num):
        for v in data:
            method(v)
    e = time.time()
    return e - s


sample_data = [[random.randint(0, 100) for i in range(100)] for _ in range(100)]

print(performance_check(merge_sort, sample_data))
print(performance_check(quick_sort, sample_data))
print(performance_check(quick2_sort, sample_data))
