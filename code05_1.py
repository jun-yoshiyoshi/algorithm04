import random


def linear_search(array, target):
    for v in array:
        if target == v:
            return True
    return False


array = [random.randint(1, 10) for _ in range(10)]
print(linear_search(array, 10))
