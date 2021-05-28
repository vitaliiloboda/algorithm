'''
2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция,
элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

'''

from collections import Counter, deque


def plus(a, b):
    numbers = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                       '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})

    a.reverse()
    b.reverse()

    n = len(a) if len(a) > len(b) else len(b)
    m = len(a) if len(a) < len(b) else len(b)

    c = deque([0])

    for i in range(n):

        if i > len(a) - 1:
            c[i] += numbers.get(b[i])
            break
        elif i > len(b) - 1:
            c[i] += numbers.get(a[i])
            break

        k = numbers.get(a[i]) + numbers.get(b[i])

        if i < m:
            c.append(0)

        if k > 15:
            k = k - 16
            c[i] += k
            c[i + 1] = 1
        else:
            c[i] += k
            if c[i] > 15:
                k = c[i] - 16
                c[i] = k
                c[i + 1] = 1

    c.reverse()

    d = deque([])
    for i in c:
        d.append(list(numbers.keys())[i])

    if d[0] == '0':
        d.popleft()

    return d


if __name__ == '__main__':
    num_1 = deque(['A', '2'])
    num_2 = deque(['C', '4', 'F'])

    print(f'Сумма чисел {num_1} и {num_2} равна {plus(num_1, num_2)}')
