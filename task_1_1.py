'''
https://drive.google.com/file/d/1ntjVNBs3uYfSy5l-eiAArc38etiCSUar/view?usp=sharing

9. Вводятся три разных числа.
Найти, какое из них является средним
(больше одного, но меньше другого).

'''

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if b > c:
        print(f'{b}')
    else:
        if a > c:
            print(f'{c}')
        else:
            print(f'{a}')
else:
    if a > c:
        print(f'{a}')
    else:
        if b > c:
            print(f'{c}')
        else:
            print(f'{b}')
