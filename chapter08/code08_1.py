import math


def prime_test(n):
    """
    素数判定
    但し、pow関数はflort型を返すため、nが大きくなるとmの正確性は失われる。
    """
    m = int(pow(n, 0.5))
    for d in range(2, m + 1):
        if n % d == 0:
            return False
    return True


def prime_test2(n):
    """素数判定改良版"""
    m = math.isqrt(n)
    for d in range(2, m + 1):
        if n % d == 0:
            return False
    return True
