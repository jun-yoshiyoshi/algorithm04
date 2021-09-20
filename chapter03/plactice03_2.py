import math


def func(n):
    sum = 1
    for i in range(1, n + 1):
        sum = sum*i
    return sum


n = int(input())

print(func(n))

print(math.factorial(n))
