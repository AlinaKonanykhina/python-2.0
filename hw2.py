'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.'''

'''сумма целых чисел '''
# n = int(input('Введите  число'))
# summa = 0
#
# while n > 0:
#     digit = n % 10
#     summa = summa + digit
#     n = n // 10
# print("Сумма:", summa)
#
# num = input("Введите  число: ")
# summa = 0
# for i in num:
#     if i != '.':
#         summa = summa + int(i)
# print('сумма числа равна: ', summa)


'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

# n = int(input('Введите число'))
# total = 1
# my_list =[]
# for i in range(1, n + 1):
#     my_list.append(total * i)
#     total = i * total
#     print(my_list)

'''Задайте список из n чисел последовательности (1+\n)^n и выведите на экран их сумму'''

# n = int(input("Введите n: "))
# dict_n = {}
# for i in range(1, n + 1):
#     dict_n[i]= round((1 + 1 / i) ** i, 2)
# print(dict_n)

# n = int(input("Введите n: "))
# my_list = []
# for i in range(1, n + 1):
#     i = round((1 + 1 / i) ** i, 2)
#     my_list.append(i)
#     print(my_list)

'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число'''

# n = int(input("Введите число N: "))
# elem1=int(input("Введите позицию элемента 1 : "))
# elem2=int(input("Введите позицию элемента 2 : "))
# my_list=[]
# for i in range(-n,n+1):
#     my_list.append(i)
# print("Последовательность элементов: ", my_list)
# print(f'Произведение элементов {elem1} и {elem2}: {my_list[elem1]} * {my_list[elem2]} = {my_list[elem1]*my_list[elem2]}')
