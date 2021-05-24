'''
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».

'''

##########################################_____Без использования Решена_____#############################################

import timeit
import cProfile


def simple(num):
    len_num = len(str(num))
    k = (3 + ((2.45 * (len_num - 1)) * (1 + len_num / 6)))

    n = int(num * k)

    b = [2]

    a = [0] * n

    for i in range(n):
        a[i] = i

    for i in a:
        if i in b or i == 1:
            continue

        for j in b:
            if i % j == 0:
                break
            else:
                continue
        else:
            b.append(i)

    return b[num - 1]


# print(simple(100))
# print(simple(1000))

print(timeit.timeit('simple(50)', number=1000, globals=globals()))  # 0.2796612
print(timeit.timeit('simple(100)', number=1000, globals=globals()))  # 1.8134625
print(timeit.timeit('simple(200)', number=1000, globals=globals()))  # 9.1762732
print(timeit.timeit('simple(400)', number=1000, globals=globals()))  # 33.648258999999996

cProfile.run('simple(4000)')

#       6149 function calls in 3.368 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    3.368    3.368 <string>:1(<module>)
#      1    3.367    3.367    3.368    3.368 task_1_6.py:20(simple)
#      1    0.000    0.000    3.368    3.368 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   6144    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
