import random
import string


def rand_str(n):
    char = ""
    s = [random.choice(string.ascii_lowercase) for i in range(n)]
    for _ in s:
        char += _
    return char


rand_str_list = [rand_str(random.randint(1, 10)) for _ in range(20)]

print(rand_str_list)

print(sorted(rand_str_list))

print(sorted(rand_str_list, key=lambda x: len(x)))
