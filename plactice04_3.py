import random


def func(array):
    if len(array) == 0:
        return True
    i = -1
    for _ in array:
        if i < _:
            i = _
        else:
            return False
    return True


array = [random.randint(1, 100) for _ in range(10)]
print(func(array))
