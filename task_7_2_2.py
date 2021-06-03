'''
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.

'''

#############################################_________Вариант_2__________###############################################

import random

size = 10
max_num = 50

my_array = [round(random.random() * 100 % max_num, 2) for _ in range(size)]
print(my_array)


def merger(array):
    if len(array) == 1:
        return array

    middle = round(len(array) / 2)

    array_1 = array[:middle]
    array_2 = array[middle:]

    a = merger(array_1)
    b = merger(array_2)

    c = []

    while True:
        if min(a) < min(b):
            c.append(min(a))
            a.remove(min(a))
        else:
            c.append(min(b))
            b.remove(min(b))

        if len(a) == 0:
            c.extend(b)
            break
        if len(b) == 0:
            c.extend(a)
            break

    return c


print(merger(my_array))
