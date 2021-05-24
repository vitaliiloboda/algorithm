'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

В данном файле 1-й вариант решения в следующих двух еще по одному варианту.

Исходя из данных анализа через модуль timeit все три варианта решения имеют линейную сложность - O(n).
Согласно cProfile время их выполнения практически одинаковое.

Все три варианта приблизительно одинаково хороши для решения данной задачи.
Как лучший можно выбрать 1-й вариант, на больших объемах данных он показывает немного меньшеее время через cProfile
чем остальные.

'''

##############################################__Вариант_1__#############################################################

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

    index_max = array.index(max_el)
    index_min = array.index(min_el)

    array[index_max] = min_el
    array[index_min] = max_el

    return None


print(timeit.timeit('change(10)', number=1000, globals=globals()))  # 0.008215499999999997
print(timeit.timeit('change(100)', number=1000, globals=globals()))  # 0.0762581
print(timeit.timeit('change(1_000)', number=1000, globals=globals()))  # 0.7788558999999999
print(timeit.timeit('change(10_000)', number=1000, globals=globals()))  # 9.7218978
print(timeit.timeit('change(20_000)', number=1000, globals=globals()))  # 21.9464267
print(timeit.timeit('change(40_000)', number=1000, globals=globals()))  # 47.452063499999994

cProfile.run('change(1_000_000)')

#        5273308 function calls in 1.853 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.011    0.011    1.853    1.853 <string>:1(<module>)
# 1000000    0.460    0.000    0.661    0.000 random.py:238(_randbelow_with_getrandbits)
# 1000000    0.562    0.000    1.223    0.000 random.py:291(randrange)
# 1000000    0.309    0.000    1.532    0.000 random.py:335(randint)
#       1    0.036    0.036    1.843    1.843 task_1_1.py:11(change)
#       1    0.274    0.274    1.806    1.806 task_1_1.py:15(<listcomp>)
#       1    0.000    0.000    1.853    1.853 {built-in method builtins.exec}
# 1000000    0.086    0.000    0.086    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1273301    0.116    0.000    0.116    0.000 {method 'getrandbits' of '_random.Random' objects}
#       2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
