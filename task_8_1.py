'''
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9

'''

import hashlib


def substring(string):
    if string == '':
        return 0

    hash_list = []
    string_len = len(string)
    i = 0

    while i < string_len:
        j = i
        while j < string_len:
            j += 1
            subs = string[i:j]
            hash_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
            if hash_subs not in hash_list:
                hash_list.append(hash_subs)
        i += 1

    return f'В строке {len(hash_list) - 1} различных подстрок'  # отнимаю 1 так как в сумму не включается строка целиком


my_string = 'sova'
print(substring(my_string))
