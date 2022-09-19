'''Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
*Сохранить словарь в файл users_hobby.txt. Фрагмент файла с данными о пользователях (users.txt):
Иванов Иван Иванович Петров Петр Петрович Фрагмент файла с данными о хобби (hobby.txt): скалолазание, охота горные лыжи'''

# users = []
# hobby = []
# my_dict = {}
# with open('users.txt', 'w', encoding='utf-8') as f:
#     f.write("Иванов Иван Иванович\n")
#     f.write("Сергеев Сергей Сергеевич\n")
#     f.write("Владимиров Владимир Владимирович\n")
#     f.write("Петров Петр Петрович\n")
#     f.write("Романов Роман Романович\n")
# with open('hobby.txt', 'w', encoding='utf-8') as f:
#     f.write("Скалолазанье\n")
#     f.write("Охота\n")
#     f.write("Горные лыжи\n")
#     f.write("Шашки\n")
#     f.write("Шахматы\n")
# with open('users.txt', 'r', encoding='utf-8') as f:
#     users = f.read().splitlines()
# with open('hobby.txt', 'r', encoding='utf-8') as f:
#     hobby = f.read().splitlines()
# for i in range(len(users)):
#     my_dict[users[i]] = hobby[i]
# with open('users_hobby.txt', 'w', encoding='utf-8') as f:
#     for k, v in my_dict.items():
#         f.write('{}: {}\n'.format(k, v))
# print(my_dict)


'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''

# import math
#
# def prime_factors(num):
#     while num % 2 == 0:
#         print(2, )
#         num = num / 2
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         while num % i == 0:
#             print(i, )
#             num = num / i
#     if num > 2:
#         print(num)
#
# num = 35
# prime_factors(num)

'''Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности'''

'1 вариант'
# numbers = [1, 2, 2, 3, 3, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)

'2 вариант'
# numbers = [20, 20, 30, 30, 40]
#
# def get_unique_numbers(numbers):
#     unique = []
#
#     for number in numbers:
#         if number in unique:
#             continue
#         else:
#             unique.append(number)
#     return unique
#
# print(get_unique_numbers(numbers))

'''*Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
 Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0'''


# from random import randint
#
# k = randint(2, 7)
# print(f'к равно = {k}')
# koef_list= []
# polynomial = []
# for i in range(k + 1):
#     koef_list.append(randint(0, 100))
# print("Коэффициенты для многочлена: ", koef_list)
# for i in range(len(koef_list)):
#     polynomial.append(f"{koef_list[i]} * x ^ {k} + y")
#     k != 0
# polynomial = str(polynomial)
# print(polynomial)
#
# with open('hw4.txt', 'w', encoding='utf-8') as f:
#     f.write(polynomial)