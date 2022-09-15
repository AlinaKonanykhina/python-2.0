'''Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции'''

# my_list = [3, 5, 9, 2, 9]
# odd = []
# summa = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         summa = summa + my_list[i]
#         odd.append(my_list[i])
# print(f'Список: {my_list}  Элементы списка на нечетных позициях: {odd}  Сумма элементов списка на нечетных позициях: {summa}')



'''Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

# import random
#
# num = int(input("Введите длинну списка: "))
# my_list = []
# mult_list = []
# for i in range(0, num):  #задаем список
#     my_list.append(random.randint(1, 100))
# print(my_list)
# for i in range(num // 2):
#     mult_list.append(my_list[i] * my_list[-i - 1])
#     print(f'{i + 1} : {my_list[i]}*{my_list[-i - 1]}')
# print(f'произведение пар чисел: {mult_list}')



'''Задайте список из вещественных чисел.
 Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.'''

# import random
#
# num = int(input("Введите длинну списка: "))
# my_list = []
#
# for i in range(0, num):  # задаем список
#     my_list.append(round(random.uniform(1, 10), 2))
# print(my_list)
# min_num = my_list[0]
# max_num = my_list[0]
# for i in range(1, len(my_list)):
#     if my_list[i] > max_num:
#         max_num = my_list[i]
#     elif my_list[i] < min_num:
#         min_num = my_list[i]
# print(f'Максимум списка - {max_num}, Минимум списка - {min_num}')
#
# digit_1 = min_num * 10 % 10
# digit_2 = max_num * 10 % 10
# difference = (round(digit_1, 2) - round(digit_2, 2))
# print(f'разница между максимальным и минимальным значением дробной части элементов {difference}')



'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.'''
# n = int(input('Введите число: '))
#
# b = ''
#
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
#
# print(f'двоичное число - {b}')

'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.'''

# k = int(input("Введите число: "))
# my_list = [1, 1]
# negativ_my_list = [-1, -1]
# negativ = []
# feb_list = []
# for i in range(2, k):
#     my_list.append(my_list[i - 1] + my_list[i - 2])
#     negativ_my_list.append(negativ_my_list[i - 1] + negativ_my_list[i - 2])
# for i in range(len(negativ_my_list) - 1, -1, -1):
#     negativ.append(negativ_my_list[i])
# feb_list = [*negativ, 0, *my_list]
# print(f'список Фибонначи для числа {k} -> {feb_list}')


'''Напишите программу, которая будет преобразовывать десятичное число в двоичное'''

'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов'''