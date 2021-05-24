'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

'''

##############################################__Вариант_3__#############################################################

import random
import timeit
import cProfile


def change(size):
    min_item = -100
    max_item = 100

    array = [random.randint(min_item, max_item) for _ in range(size)]

    max_el = array[0]
    min_el = array[0]

    for i in array:
        if i > max_el:
            max_el = i
        if i < min_el:
            min_el = i

    index_max = None
    index_min = None

    for i, item in enumerate(array):
        if item == max_el:
            index_max = i
        elif item == min_el:
            index_min = i

    array[index_max] = min_el
    array[index_min] = max_el

    return None


print(timeit.timeit('change(10)', number=1000, globals=globals()))  # 0.010277500000000002
print(timeit.timeit('change(100)', number=1000, globals=globals()))  # 0.08285779999999998
print(timeit.timeit('change(1000)', number=1000, globals=globals()))  # 0.8127427
print(timeit.timeit('change(10000)', number=1000, globals=globals()))  # 8.4455798
print(timeit.timeit('change(20000)', number=1000, globals=globals()))  # 20.839213299999997
print(timeit.timeit('change(40000)', number=1000, globals=globals()))  # 45.512368099999996

cProfile.run('change(1_000_000)')

# 5273506 function calls in 1.903 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.010    0.010    1.903    1.903 <string>:1(<module>)
#   1000000    0.461    0.000    0.660    0.000 random.py:238(_randbelow_with_getrandbits)
#   1000000    0.558    0.000    1.218    0.000 random.py:291(randrange)
#   1000000    0.302    0.000    1.520    0.000 random.py:335(randint)
#         1    0.098    0.098    1.892    1.892 task_1_3.py:10(change)
#         1    0.275    0.275    1.795    1.795 task_1_3.py:14(<listcomp>)
#         1    0.000    0.000    1.903    1.903 {built-in method builtins.exec}
#   1000000    0.084    0.000    0.084    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1273501    0.115    0.000    0.115    0.000 {method 'getrandbits' of '_random.Random' objects}
