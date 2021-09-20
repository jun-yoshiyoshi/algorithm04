
import random
MAX = 10 << 26


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


def merge2_arryas(left, right=[]):
    res, j = [], 0
    for i in left:
        if i <= right[j]:
            res.append(i)
        else:
            for _ in right[j:]:
                if _ < i:
                    res.append(_)
                    j += 1
                    if len(right) < j:
                        right[j] = MAX
            res.append(i)
    return res


left = [i for i in range(1, 100, 2)]
right = [i for i in range(2, 100, 3)]

array = merge_arrays(left, right)
array2 = merge2_arryas(left, right)

print(array)
print(array2)
