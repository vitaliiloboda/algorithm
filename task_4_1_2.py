'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

'''

##############################################__Вариант_2__#############################################################

import random
import timeit
import cProfile


def change(size):
    min_item = -100
    max_item = 100

    array = [random.randint(min_item, max_item) for _ in range(size)]

    array_sorted = sorted(array)

    max_item = array_sorted[-1]
    min_item = array_sorted[0]

    max_idx = array.index(max_item)
    min_idx = array.index(min_item)

    array[max_idx], array[min_idx] = array[min_idx], array[max_idx]

    return None


print(timeit.timeit('change(10)', number=1000, globals=globals()))  # 0.010133899999999998
print(timeit.timeit('change(100)', number=1000, globals=globals()))  # 0.0765106
print(timeit.timeit('change(1_000)', number=1000, globals=globals()))  # 0.8260689
print(timeit.timeit('change(10_000)', number=1000, globals=globals()))  # 8.4331818
print(timeit.timeit('change(20_000)', number=1000, globals=globals()))  # 21.4369342
print(timeit.timeit('change(40_000)', number=1000, globals=globals()))  # 44.9176643

cProfile.run('change(1_000_000)')

#        5272962 function calls in 1.961 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.028    0.028    1.961    1.961 <string>:1(<module>)
# 1000000    0.464    0.000    0.666    0.000 random.py:238(_randbelow_with_getrandbits)
# 1000000    0.562    0.000    1.227    0.000 random.py:291(randrange)
# 1000000    0.301    0.000    1.529    0.000 random.py:335(randint)
#       1    0.000    0.000    1.932    1.932 task_1_2.py:10(change)
#       1    0.270    0.270    1.799    1.799 task_1_2.py:14(<listcomp>)
#       1    0.000    0.000    1.961    1.961 {built-in method builtins.exec}
#       1    0.134    0.134    0.134    0.134 {built-in method builtins.sorted}
# 1000000    0.087    0.000    0.087    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1272954    0.115    0.000    0.115    0.000 {method 'getrandbits' of '_random.Random' objects}
#       2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
