'''
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

'''

from collections import namedtuple, Counter, deque

Company = namedtuple('Company', 'name, profit_1q, profit_2q, profit_3q, profit_4q, profit_y')

n = int(input('Введите количество предприятий: '))

companies = deque()
profit_sum = 0

for i in range(n):
    name = input('Название предприятия: ')
    profit_1q = int(input('Прибыль за 1-й квартал: '))
    profit_2q = int(input('Прибыль за 2-й квартал: '))
    profit_3q = int(input('Прибыль за 3-й квартал: '))
    profit_4q = int(input('Прибыль за 4-й квартал: '))
    profit_y = profit_1q + profit_2q + profit_3q + profit_4q
    profit_sum += profit_y
    companies.append(Company(name, profit_1q, profit_2q, profit_3q, profit_4q, profit_y))

average_profit = profit_sum / n

above_average = Counter()
below_average = Counter()

for i in companies:
    if i.profit_y > average_profit:
        above_average[i.name] = i.profit_y
    elif i.profit_y < average_profit:
        below_average[i.name] = i.profit_y

print()
print(f'Средняя прибыль по всем предприятиям за год - {average_profit}')
print()
print(f'Предприятия, чья прибыль выше среднего: ')
print(*above_average.keys(), sep='\n')
print()
print(f'Предприятия, чья прибыль ниже среднего: ')
print(*below_average.keys(), sep='\n')
