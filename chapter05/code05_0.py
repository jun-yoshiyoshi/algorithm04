import random

array = [random.randint(0, 100) for i in range(10)]
n = int(input())

if n in array:
    print(True)
else:
    print(False)

print(array.index(n))
