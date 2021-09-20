import random


def quick_sort(array):
    if array == []:
        return array
    p = array[-1]
    l, r, pivots = [], [], []

    for _ in array:
        if _ < p:
            l.append(_)
        elif _ == p:
            pivots.append(_)
        else:
            r.append(_)
    return quick_sort(l) + pivots + quick_sort(r)

#array = [random.randint(1, 100) for _ in range(100)]

# quick_sort(array)
