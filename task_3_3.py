'''
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

'''
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_minus = [i for i in array if i < 0]

max_min = array_minus[0]

for j in array_minus:
    if j > max_min:
        max_min = j

max_min_idx = array.index(max_min)

print(f'Максимальный минимальный элемент {max_min}, его позиция в массиве {max_min_idx}')
