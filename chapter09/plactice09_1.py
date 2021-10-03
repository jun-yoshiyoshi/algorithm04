import math


def cnt_coprime(m):
    res = 1
    for i in range(2, m):
        if math.gcd(m, i) == 1:
            res += 1
    return res


print(cnt_coprime(6))
print(cnt_coprime(23))
print(cnt_coprime(100))
