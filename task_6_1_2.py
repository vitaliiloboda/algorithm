'''
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

##########################################_______Вариант 2______########################################################

'''

import sys


def memory(x):
    mem_size = 0
    mem_size += sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                mem_size += memory(key)
                mem_size += memory(value)
        elif not isinstance(x, str):
            for item in x:
                mem_size += memory(item)
    return mem_size


# num = int(input('Введите натуральное число: '))
num = 2354786514456574

numbers = [int(i) for i in list(str(num))]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f'Четных чисел - {len(even)}, нечетных - {len(odd)}')

elements = [num, numbers, even, odd, i]

sum_m = 0
for j in elements:
    sum_m += memory(j)

print(f'\nПод переменные было выделено {sum_m} байт')  # 1380 byte, 64-разрядная ОС, Python 3.9
