import random
import heapq


def heap_sort(array):
    heap = []
    for _ in array:
        heapq.heappush(heap, _)
    return [heapq.heappop(heap) for i in range(len(heap))]


array = [random.randint(0, 100) for i in range(15)]

print(array)

print(heap_sort(array))
