'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

# my_text = 'Напишите абв абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, абв содерабващие содержащие "абв"'
#
# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)
#
# my_text = del_some_words(my_text)
# print(my_text, 'абв')

'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 202 конфеты. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты 
оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

данную задачу частично смогла решить сама.'''

# import random
#
# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
#             'Основные правила игры: '
#             'Нам будет дано некоторое количество конфет, '
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы с вами договоримся.'
#             'Итак, начнём!')
#
# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']
#
#
# def play_game(n, m, players, messages):
#     count = 0
#     if n % 10 == 1 and 9 > n > 10:
#         letter = 'а'
#     elif 1 < n % 10 < 5 and 9 > n > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while n > 0:
#         print(f'{players[count % 2]}, {random.choice(messages)}')
#         move = int(input())
#         if move > n or move > m:
#             print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
#             attempt = 3
#             while attempt > 0:
#                 if n >= move <= m:
#                     break
#                 print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                 move = int(input())
#                 attempt -= 1
#             else:
#                 return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         n = n - move
#         if n > 0:
#             print(f'Осталось {n} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]

#
# print(greeting)
#
# player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
# player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
# players = [player1, player2]
#
# n = 200
# m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#
# winer = play_game(n, m, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

# # man vs smart bot
#
# from random import randint, choice
#
# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
#             'Основные правила игры: '
#             'Нам будет дано некоторое количество конфет, '
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы с вами договоримся. '
#             'Итак, начнём!')
#
# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']
#
#
# def introduce_players():
#     player1 = input('Давайте познакомися. Как Вас зовут?\n')
#     player2 = 'Робик'
#     print(f'Очень приятно, меня зовут {player2}')
#     return [player1, player2]
#
#
# def get_rules(players):
#     n = 200
#     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#     first = int(input(
#         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [n, m, int(first)]
#
#
# def play_game(rules, players, messages):
#     count = rules[2]
#     print(count)
#     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
#         letter = 'а'
#     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while rules[0] > 0:
#         if not count % 2:
#             move = rules[0] % rules[1] + 1
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > rules[0] or move > rules[1]:
#                 print(
#                     f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
#                 attempt = 3
#                 while attempt > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         rules[0] = rules[0] - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]
#
#
# print(greeting)
#
# players = introduce_players()
# rules = get_rules(players)
#
# winer = play_game(rules, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


'''Создайте программу для игры в ""Крестики-нолики"".'''
# данную задачу я написла не самостоятельно. решение понятно, но сама бы, на данном этапе, не написала бы

# board = list(range(1,10)) #задаем поле
#
# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)
#
# def take_input(player_token): #задаем возможность вводить данные
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
#
# def check_win(board): # функция проверки игрового поля
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
# def main(board): # проверка вышеуказанных функций
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)
#
# main(board)

'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''
#
# with open('my_file.txt', 'w', encoding='utf-8') as f:
#     f.write('Белеет парус одинокой В тумане моря голубом!.. Что ищет он в стране далекой? Что кинул он в краю родном?.')
# def encode(s):
#     encoding = ""
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
#         encoding += str(count) + s[i]
#         i = i + 1
#     return encoding
#
# if __name__ == '__main__':
#     with open('my_file.txt', 'r', encoding='utf-8') as f:
#         s = f.read().split()
#     with open('my_file_1.txt', 'w', encoding='utf-8') as f:
#         f.write(encode(s))
#
# import os
# stat_my_file=os.stat("my_file.txt")
# stat_my_file_1=os.stat("my_file_1.txt")
#
# print(f'Размер исходного файла {stat_my_file.st_size} бит\nРазмер сжатого файла {stat_my_file_1.st_size} бит')