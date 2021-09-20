import heapq
import random


def merge2_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return heapq.merge(merge2_sort(left), merge2_sort(right))


l = [random.randint(1, 100) for _ in range(50)]

print(list(merge2_sort(l)))
