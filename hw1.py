"""6.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным."""

# week_list = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']

# day_week = int(input('Введите порядковый номеp дня недели: '))

# if day_week <1 or day_week >7:
#     print(f'{[day_week-1]}-не существует')
# elif day_week <=5 :
#     print(f'{week_list[day_week-1]}- будний день')
# else:
#     print(f'{week_list[day_week-1]}-  выходной день')

""" 7.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат """""
def input_Numbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_Predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = input_Numbers(z)

if check_Predicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")




"""8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
"""

# x = int(input("x="))
# y = int(input("y="))
# if x>0 and y>0:
#     print('I')
# elif x<0 and y>0:
#     print('II')
# elif x<0 and y<0:
#     print('III')
# elif x>0 and y<0:
#     print('IV')

"""9.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)"""


# num =int(input('введите номер четверти плоскости(от 1 до 4): '))
# if num == 1:
#  print('диапозон возможных координат X и Y больше 0')
# elif num ==2:
#   print('диапозон возможных координат X меньше 0 и Y больше 0')
# elif num ==3:
#   print('диапозон возможных координат X  и Y меньше 0')
# else:
#     print('диапозон возможных координат X больше 0 и Y меньше 0')

"""10.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21"""


# print("Введите координаты точки А")
# xa = int(input("координата по оси x= "))
# ya = int(input("координата по оси y= "))
# print("Введите координаты точки B")
# xb = int(input("координата по оси x= "))
# yb = int(input("координата по оси y= "))
# result = (((xb-xa)**2 +(yb-ya)**2)**0.5)
# print ('расстояние между точками =', round(result,2))