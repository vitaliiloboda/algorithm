'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_el = array[0]
min_el = array[0]

for i in array:
    if i > max_el:
        max_el = i
    if i < min_el:
        min_el = i

index_max = array.index(max_el)
index_min = array.index(min_el)

array[index_max] = min_el
array[index_min] = max_el

print(array)
