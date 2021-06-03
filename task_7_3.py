'''
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
'''

import random

m = 5
min_num = 0
max_num = 100

array = [random.randint(min_num, max_num) for _ in range(2 * m + 1)]
print(array)

num = None

for i in array:
    big_num = 0
    less_num = 0
    same = 0

    for j in range(len(array)):

        if j == array.index(i):
            continue

        if i < array[j]:
            big_num += 1
        elif i > array[j]:
            less_num += 1
        else:
            same += 1

    if same >= abs(big_num - less_num):
        num = i
        break

    if big_num == less_num:
        num = i
        break

    big_num = 0
    less_num = 0

print(f'Медиана - {num}')
