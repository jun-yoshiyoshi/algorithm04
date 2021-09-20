import random


def merge_arrays(left, right=[]):
    res = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]


def step(array):
    res = [merge_arrays(*array[i: i + 2]) for i in range(0, len(array), 2)]
    return res


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge_arrays(merge_sort(left), merge_sort(right))
# エラーを修正。再帰を用いたコード


#my_array = [random.randint(0, 100) for _ in range(15)]

# print(merge_sort(my_array))
