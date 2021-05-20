'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num = array[0]

first_min = array[0]
second_min = array[0]

for i in array:
    if i < first_min:
        first_min = i
    elif i < second_min:
        second_min = i

print(f'{first_min = }')
print(f'{second_min = }')
