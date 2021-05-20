'''
6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

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

sum_el = 0

array_new = []

if array.index(min_el) < array.index(max_el):
    array_new = array[(array.index(min_el) + 1): array.index(max_el)]
else:
    array_new = array[(array.index(max_el) + 1): array.index(min_el)]

for i in array_new:
    sum_el += i

# print(array_new)
# print(max_el)
# print(min_el)

print(f'Сумма = {sum_el}')
