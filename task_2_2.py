'''
3. Сформировать из введенного числа обратное
по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.

'''


def reverse(num):
    if num // 10 == 0:
        return num

    else:
        result = reverse(num // 10)
        full_result = f'{num % 10}{result}'
        return full_result


if __name__ == '__main__':
    num = int(input('Введите число: '))
    res = int(reverse(num))
    print(res)
