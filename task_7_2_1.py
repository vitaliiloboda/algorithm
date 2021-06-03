'''
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.

'''

#############################################_________Вариант_1__________###############################################

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

    i = 0
    j = 0
    while True:

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

        if i > len(a) - 1:
            for k in range(j, len(b)):
                c.append(b[k])
            break
        if j > len(b) - 1:
            for k in range(i, len(a)):
                c.append(a[k])
            break

    return c


print(merger(my_array))
