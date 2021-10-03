import math


def is_carmichael(n):
    for a in range(1, n):
        if math.gcd(n, a) == 1 and pow(a, n-1, n) != 1:
            return False
    return True
