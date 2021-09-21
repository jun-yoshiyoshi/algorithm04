import random
import time
import sys


def mk_list(k):
    s = time.time()
    n = random.randint(1, 10 ** k)
    l = [random.random() for _ in range(n)]
    e = time.time()
    return e-s, sys.getsizeof(l)


for i in range(1, 9):
    t, s = mk_list(i)
    s = s / 1024 / 1024
    # メモリーサイズを MBに変換
    print(i, ":", t, ":", s)
