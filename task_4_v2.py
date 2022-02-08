"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

import random
import string
import secrets


##############################################################################
def app_1(lst, login, password):
    """
    Функция работает с:
        - lst - хранилище данных (список)
        - login - логин, введенный пользователем
        - password - пароль, введенный пользователем
    Функция возвращает True - если пользователь может быть допущен к
    ресурсу, False - иначе
    Алгоритм 1:
    Предполагается, что логины в рамках хранилища уникальны.
    - Шаг 1. По логину ОБЫЧНЫМ ПЕРЕБОРОМ находится соответствующая УЗ. Если
    УЗ не найдена, то возвращается значение False, иначе - переход к Шагу 2.
    - Шаг 2. Для найденной УЗ проверяется корректность пароля, введенного
    пользователем. Если пароль некорректен, то возвращается False, иначе -
    переход к Шагу 3.
    - Шаг 3. Для найденной УЗ проверяется, активна ли она. Если УЗ не активна,
    то пользователю предлагается активировать ее. Если пользователь не хочет
    ее активировать, то возвращается значение False, иначе - возвращается True.
    соответствие пароля
    Сложность: O(n)
    """
    # Поиск УЗ пользователя
    idx = -1                                                            # O(1)
    for i in range(len(lst)):                                           # O(n)
        if lst[i][0] == login:                                          # O(1)
            idx = i                                                     # O(1)
    if idx == -1:                                                       # O(1)
        print('Пользователь с указанным логином не найден.')            # O(1)
        return False                                                    # O(1)
    # Проверка корректности пароля УЗ
    if lst[idx][1] != password:                                         # O(1)
        print('Указан неверный пароль.')                                # O(1)
        return False                                                    # O(1)
    # Проверка, что УЗ активна
    if lst[idx][2] == 0:                                                # O(1)
        active = input('\tУЗ не активна. Активировать? (yes/no): ')     # O(1)
        if active == 'no':                                              # O(1)
            return False                                                # O(1)
        else:
            lst[idx][2] = 1                                             # O(1)
            return True                                                 # O(1)
    else:
        return True                                                     # O(1)


##############################################################################
def app_2(lst, login, password):
    """
    Функция работает с:
        - lst - хранилище данных (список)
        - login - логин, введенный пользователем
        - password - пароль, введенный пользователем
    Функция возвращает True - если пользователь может быть допущен к
    ресурсу, False - иначе
    Алгоритм 1:
    Предполагается, что логины в рамках хранилища уникальны и размещены в
    алфавитном порядке.
    - Шаг 1. По логину БИНАРНЫМ ПОИСКОМ находится соответствующая УЗ. Если
    УЗ не найдена, то возвращается значение False, иначе - переход к Шагу 2.
    - Шаг 2. Для найденной УЗ проверяется корректность пароля, введенного
    пользователем. Если пароль некорректен, то возвращается False, иначе -
    переход к Шагу 3.
    - Шаг 3. Для найденной УЗ проверяется, активна ли она. Если УЗ не активна,
    то пользователю предлагается активировать ее. Если пользователь не хочет
    ее активировать, то возвращается значение False, иначе - возвращается True.
    соответствие пароля
    Сложность: O(log_n)
    """
    # Поиск УЗ пользователя
    idx = binarySearch(lst, login, 0, len(lst))                         # O(log_n)
    if idx == -1:                                                       # O(1)
        print('Пользователь с указанным логином не найден.')            # O(1)
        return False                                                    # O(1)
    # Проверка корректности пароля УЗ
    if lst[idx][1] != password:                                         # O(1)
        print('Указан неверный пароль.')                                # O(1)
        return False                                                    # O(1)
    # Проверка, что УЗ активна
    if lst[idx][2] == 0:                                                # O(1)
        active = input('\tУЗ не активна. Активировать? (yes/no): ')     # O(1)
        if active == 'no':                                              # O(1)
            return False                                                # O(1)
        else:
            lst[idx][2] = 1                                             # O(1)
            return True                                                 # O(1)
    else:
        return True                                                     # O(1)

def binarySearch(arr, x, left, right):                                  # O(log_n) - глубина рекурсии
    if right <= left:  # промежуток пуст                                # O(1)
        return -1                                                       # O(1)
    # промежуток не пуст
    mid = (left + right) // 2                                           # O(1)
    # если центральный элемент - искомый
    if arr[mid][0] == x:                                                # O(1)
        return mid                                                      # O(1)
    # иначе если искомый элемент лежит в правой половине
    elif arr[mid][0] < x <= arr[right - 1][0] or \
            arr[mid][0] >= arr[left][0] > x or \
            x > arr[mid][0] >= arr[right - 1][0]:                       # O(1)
        return binarySearch(arr, x, mid + 1, right)                     # O(1)
    else:  # иначе следует искать в левой половине
        return binarySearch(arr, x, left, mid)                          # O(1)


##############################################################################
def app_3(dct, login, password):
    """
    Функция работает с:
        - lst - хранилище данных (словарь)
        - login - логин, введенный пользователем
        - password - пароль, введенный пользователем
    Функция возвращает True - если пользователь может быть допущен к
    ресурсу, False - иначе
    Алгоритм 1:
    - Шаг 1. По логину в словаре находится соответствующая УЗ. Если
    УЗ не найдена, то возвращается значение False, иначе - переход к Шагу 2.
    - Шаг 2. Для найденной УЗ проверяется корректность пароля, введенного
    пользователем. Если пароль некорректен, то возвращается False, иначе -
    переход к Шагу 3.
    - Шаг 3. Для найденной УЗ проверяется, активна ли она. Если УЗ не активна,
    то пользователю предлагается активировать ее. Если пользователь не хочет
    ее активировать, то возвращается значение False, иначе - возвращается True.
    соответствие пароля
    Сложность: O(1)
    """
    # Поиск УЗ пользователя
    account = dct.get(login)                                            # O(1)
    if account is None:                                                 # O(1)
        print('Пользователь с указанным логином не найден.')            # O(1)
        return False                                                    # O(1)
    # Проверка корректности пароля УЗ
    if account[0] != password:                                          # O(1)
        print('Указан неверный пароль.')                                # O(1)
        return False                                                    # O(1)
    # Проверка, что УЗ активна
    if account[1] == 0:                                                 # O(1)
        active = input('\tУЗ не активна. Активировать? (yes/no): ')     # O(1)
        if active == 'no':                                              # O(1)
            return False                                                # O(1)
        else:
            account[1] = 1                                              # O(1)
            return True                                                 # O(1)
    else:
        return True                                                     # O(1)


##############################################################################
"""Тестирование"""

# Генерация имени пользователя
def generate_name(length):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(length))
    return name.capitalize()

# Генерация пароля
def generate_password(length):
    letters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(letters) for i in range(length))
    return password

# Генерация тестового массива
# через список
# lst = []
# for i in range(10):
#     lst.append(
#         [
#             generate_name(random.randint(4, 10)),
#             generate_password(8),
#             random.randint(0, 1)])

# через словарь
dct = {}
for i in range(10):
    dct[generate_name(random.randint(4, 10))] = [generate_password(8), random.randint(0, 1)]

# Данные в хранилище
# print('=========== ХРАНИЛИЩЕ ===========')
# for i in range(len(lst)):
#     if lst[i][2] == 1:
#         print(f'{i+1}. Учетная запись АКТИВНА')
#     else:
#         print(f'{i + 1}. Учетная запись НЕ активна')
#     print(f'\tЛогин: {lst[i][0]}\n\tПароль: {lst[i][1]}')
# print('=================================')

# Запуск процедуры аутентификации для тестирования app_1 и app_2
# i = 0
# while True:
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     if i % 2 == 0 and app_1(lst, login, password) \
#         or i % 2 == 1 and app_2(sorted(lst, key=lambda x: x[0]), login, password):
#         print('Пользователь допущен к ресурсу!')
#     else:
#         print('Пользователь НЕ допущен к ресурсу!')
#     print('-------------------------------')

# Данные в хранилище
print('=========== ХРАНИЛИЩЕ ===========')
for key, item in dct.items():
    if item[1] == 1:
        print(f'{i+1}. Учетная запись АКТИВНА')
    else:
        print(f'{i + 1}. Учетная запись НЕ активна')
    print(f'\tЛогин: {key}\n\tПароль: {item[0]}')
print('=================================')

# Запуск процедуры аутентификации для тестирования app_3
i = 0
while True:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if app_3(dct, login, password):
        print('Пользователь допущен к ресурсу!')
    else:
        print('Пользователь НЕ допущен к ресурсу!')
    print('-------------------------------')