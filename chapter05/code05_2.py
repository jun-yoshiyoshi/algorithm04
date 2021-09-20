import random
import bisect


array = [random.randint(1, 10) for _ in range(10)]
array.sort()

print(bisect.bisect(array, 7))


def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo muxt be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo
