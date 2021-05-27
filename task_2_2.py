'''
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция,
элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

'''

from collections import Counter, deque
from task_2_1 import plus

numbers = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
a = deque(['A', '2'])
b = deque(['C', '4', 'F'])

a.reverse()
b.reverse()

n = len(a) if len(a) < len(b) else len(b)

c = deque([0])
d = deque([])

for i in range(len(a)):

    for j in range(len(b)):
        k = numbers.get(a[i]) * numbers.get(b[j])
        w = k // 16
        r = k % 16
        c[j] += r

        if c[j] > 15:
            c[j] -= 16
            c.append(w + 1)
        else:
            c.append(w)

    else:
        d.append(c)
        c = deque([0])

for i, j in enumerate(d):
    if i == 0:
        continue
    else:
        j.extendleft([0] * i)

e = deque([])

for i in d:
    i.reverse()
    f = deque([])
    for j in i:
        f.append(list(numbers.keys())[j])
    e.append(f)

result = plus(e[0], e[1])

print(f'Произведение чисел {a} и {b} равно {result}')
