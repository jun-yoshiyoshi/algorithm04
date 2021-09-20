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


def step(array):
    res = []
    for i in range(0, len(array), 2):
        # 長さ2もしくは1の配列がスライスの結果として返る。
        res.append(merge_arrays(*array[i:i+2]))
    return res


def step_(array):
    res = [merge_arrays(*array[i: i + 2]) for i in range(0, len(array), 2)]
    return res


random.seed(4)

my_array = [random.randint(0, 100) for i in range(15)]
my_array = [[v] for v in my_array]
step1 = step(my_array)
print(step1)

step2 = step(step1)
print(step2)
