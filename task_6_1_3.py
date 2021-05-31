'''
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

##########################################_______Вариант 3______########################################################

'''
import sys
from collections import Counter


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

numbers = [i for i in map(int, list(str(num)))]

count = Counter({'even': 0, 'odd': 0})

for i in numbers:
    if i % 2:
        count['even'] += 1
    else:
        count['odd'] += 1

print(f'Четных чисел - {count["even"]}, нечетных - {count["odd"]}')

elements = [num, numbers, count, i]

sum_m = 0
for j in elements:
    sum_m += memory(j)

print(f'\nПод переменные было выделено {sum_m} байт')  # 1101 byte, 64-разрядная ОС, Python 3.9
