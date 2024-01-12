# name = "User"
# print("hi", name)
# age = 20
# print(age)
# print(type(age))
# age = "hello"
# print(age)
# a = 4
# print("a =", id(a))
# b = 5
# print("b =", id(b))
# a = b
# print(a)
# print("a =", id(a))
# import os.path
# import re
# import csv
# import json
#
# import requests
# a = b = c = 1
# print(a, b, c)
# import csv
# import json
# import tkinter

# a, b, c = 5, "hi", 9.21
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# name = "Игорь"
# age = 36
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
#
# temp = a
# a = b
# b = temp
# print("a:", a)
# print("b:", b)

# print("\tстрока \nсимволов")
# print('C:\\\\folder\\file.txt')

# функция явного преобразования типов
# s1 = "2"
# s2 = 5
# print(int(s1) + s2)
# print(s1 + str(s2))

# print(3453455555555555555555553)
# print(34.53455555555555555555553)

# a = 5
# b = 7
# c = 3
#
# print(a + b + c)
# print(a * b * c)
# print((a + b + c)/3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# num = 10
# num += 5
# print(num)
# num -= 3
# print(num)

# num = 4321
# res = num % 10 * 1000
# num = num // 10
# res += num % 10 * 100
# num = num // 10
# res += num % 10 * 10
# num = num // 10
# res += num % 10
# print(res)

# print(round(3.345345345, 4))

# a = 1
# b = 2
# a = a + b
# b = a - b
# a = a - b
# print(a, b)

# vod = int(input("Введите значение "))
# if 1 <= vod <= 99:
#     print(str(vod), end="")
#     if (11 <= vod <= 14) or (5 <= vod % 10 <= 9) or (vod % 10 == 0):
#         print(" копеек")
#     elif vod % 10 == 1:
#         print(" копейка")
#     elif 2 <= vod % 10 <= 4:
#         print(" копейки")
# else:
#     print("Неверное значение")

# try:
#     n = int(input("Введите цеое число: "))
#     print(n * 2)
# except ValueError:
#     print("что то пошло не так")

# try:
#     n = int(input("Ведите делимое: "))
#     m = int(input("ведите делитель: "))
#     print(n / m)
# except ValueError:
#     print("не льзя вводить строки")
# except ZeroDivisionError:
#     print("на ноль делить не льзя")

# try: # попытатся
#     n = int(input("Ведите делимое: "))
#     m = int(input("ведите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError): # исключение
#     print("не льзя вводить строки или на ноль делить не льзя")
# else:
#     print("Все нормально")
# finally:
#     print("конец программы")

# a = input("первое значение ")
# b = input("второе значение ")
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 0
# while i < 20:
#     i += 1
#     if i % 2 == 0 :
#         print("i =", i)

# a = int(input("кол символов "))
# i = 0
# while i < a:
#     print("*", end="")
#     i += 1

# a = int(input("кол символов "))
# while a > 0:
#     print("*", end="")
#     a -= 1

# a = int(input("кол символов "))
# print('*' * a)

# a = int(input("Ведите начало диапозаона "))
# b = int(input("Ведите конец диапозаона "))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a
#     a += 1
# print(res)

# n = input("Ведите число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("не коректные данные")
#         n = input("введите чесло ")
# if n % 2 == 0:
#     print("четное")
# else:
#     print("не четное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен", i)

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n == 0:
#         n = 1
#         break
#     res = n * n
# print(res)

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\t Внутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j +=1
#     print()
#     i += 1

# for i in 'Hello':
#     print(i)

# for color in 'red', 'blue', 'green':
#     print(color)

# print(range(8))
# range(start, stop, step)

# for i in range(2, 8, 2):
#     print(i, end=" ")
# print()
# j = 0
# while j < 8:
#     print(j, end=" ")
#     j += 1
# i = 11
# for i in range(100, i):
#     print(i, end=" ")

# первый вариант:
# i = 0
# while i < 100:
#     if i % 11 == 0:
#         if i == 0:
#             print(str(i) + "0", end=" ")
#         else:
#             print(i, end=" ")
#     i += 1

# второй вариант:

# for i in range(0, 100, 11):
#     if i == 0:
#         print(str(i) + "0", end=" ")
#     else:
#         print(i, end=" ")

# третий вариант
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# a = int(input("Введиет целое число "))
# i = 1
# while i < a:
#     if a % i == 0:
#         print(i)
#     i += 1

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---")
#         for y in range(4):
#             print("000")
# a = int(input("Введиет ширину прямоугольника: "))
# b = int(input("Введиет длинну прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         if i == 0 or i == b - 1 or j == 0 or j == a - 1:
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print()

# a = int(input('Ширина '))
# b = int(input('Высота '))
# for i in range(b):
#     if i == 0 or i == b - 1:
#         print('*' * a)
#     else:
#         print('*' + (' ' * (a - 2))+'*')

# a = [b * 2 for b in "Banana"]
# print(a)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# список (list)
# nums = [8, 3, 9, 4, 1]
# # print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[-1])
# # print(nums[-3])
# # nums[3] = 255
# # print(nums)
# # nums[1] += 100
# print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))

# n = list(range(2, 10, 2))
# print(n)
# n = 5
# a = [i ** 2 for i in range(1, n + 1)] # [0 0 0 0 0}
# print(a)
#
# d = [v * 3 for v in "list"]
# print(d)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Ввод "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)

# a = [4 ,8, 9, 5, 3]
# for i in range(len(a)): # 0 1 2 3 4
#     print(a[i], end=" ") # 4 8 9 5 3
# print()
# for i in a: # 4 8 9 5 3
#     print(i, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# res = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print(res)

# n = list(range(21, 41))
# print(n)
# count = 0
# nechet = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         nechet += n[i]
# print(count, nechet)

# a = [7, 9, 2, 1, 17]
# a[0], a[1] = a[1], a[0]
# print(a)

# Срезы

# s = [5 , 9, 3, 7, 1, 8]
# # список[start:stop:step]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[::-1])
# print(s[6:13])
# print(s[5:1])
# print(s[5:1:-1])

# a = list(range(1,8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1:6:2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:8])
# print(a[-3:1:-1])
# print(a[2:5])

# s = list(range(1,8))
# print(s)
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[15:16] = [30]
# print(s)

# Методы списков
# s = [1, 20, 0, 0, 0, 4, 5, 6, 7, 30]
# s.append(99) #добовляет один елемент в конец списка
# s.append([99, 0])
# print(s)
# s.extend([4,6,7]) # добовляет колекцию елементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 1000) # добовляет елемент(второй параметр) списка в указаный индекс(второй параметр)
# print(s)
# s.insert(-1, 200)
# print(s)

# первая задача
# n = [float(input("Слогаемое ")) for i in range(int(input("Количестов слогаемых ")))]
# res = 0.0
# kol = len(n)
# for i in range(len(n)):
#     res += n[i]
#     if n[i] == 0:
#         kol -= 1
# res = res / kol
# print(res)

# вторая задача
# size = int(input("Введиет размер поля: "))
# sim = int(input("Введиет колличество символов: "))
# for g in range(size):
#     for r in range(sim):
#         for i in range(size):
#             for p in range(sim):
#                 if (g + i) % 2 == 0:
#                     print(" * ", end="")
#                 else:
#                     print("   ", end="")
#         print()

# или так
# for g in range(5):
#     for r in range(3):
#         for i in range(5):
#             if (g + i) % 2 == 0:
#                 print(" *  *  * ", end="")
#             else:
#                 print("         ", end="")
#         print()

# вторая задача
# size = int(input("Введиет размер поля: "))
# sim = int(input("Введиет колличество символов: "))
# for g in range(size):
#     for r in range(sim):
#         for i in range(size):
#             for p in range(sim):
#                 if (g + i) % 2 == 0:
#                     print(" * ", end="")
#                 else:
#                     print("   ", end="")
#         print()

# 28.08.2023 Понедельник

# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("Ведите число: "))
#     if x % 3 == 0:
#         s.insert(0, x)
#     else:
#         print("число не кратно 3")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append((i))
#             break
# print(c)

# a = [1, 2, 3,4, 5]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append((a[i]))
#         c.append((b[i]))
#     for i in range(len(a), len(b)):
#         c.append((b[i]))
# else:
#     for i in range(len(b)):
#         c.append((a[i]))
#         c.append((b[i]))
#     for i in range(len(b), len(a)):
#         c.append((a[i]))
# print(c)

# s = [5, 9, 2, 1, 4, 3, 2, 4]
# s[3:5] = []
# del s[2:4]
# print((s))
# n = 3
# if n in s:
# s.remove((3)) # удоляет елемент из списка по значению
# last = s.pop(3) # удаление по индексу заданого в круглых скобках если индекс не передан то последний елемент удоляет
# print(last)
# s.clear() # очещает список
# print((s))

# n =[int(input("кол: ")) for i in range(int(input("число ")))]
# k = int(input("введите индекс для удалиения"))
# if k >= len(n):
#     k = len(n)
# n.pop(k)
# print(n)


# s = [5, 9, 2, 1, 4, 3, 2, 4,8,5]
# # num = s.count(4)
# print(s)
# ind = s.index(3, 4, 7) # возврозает индекс первого елемента,можно передать параметры страт и стоп
# print(num)
# print(ind)

# s = [5, 9, 2]
# b = s.copy()
# print("s =", s)
# print("b =", b)
# b.append(120)
# s.append(30)
# print("s =", s)
# print("b =", b)

# s = [5, 9, 2, 1, 4, 3, 2, 4,8,5]
# s.reverse() # перестраивает елементы в обратном порядке
# s.sort(reverse=True) # сортировка по возрастанию, rever=true сортировка по убываению
# print(s)
# n = sorted(s)
# print(s)
# print(n)

# s = ['виталий', 'сергей']
# s.sort(key=len, reverse=True)
# print(s)

# генирация случайных данных

# import random
# print(random.random())
# print(random.randint(1, 9))
# print(random.randrange(2,9, 2))

# from random import randint, randrange
#
# print(randint(1, 9))
# print(randrange(2,9, 2))

# from random import *
#
# print(randint(1, 9))
# print(randrange(2,9, 2))

# import  random as r
# print(r.randint(1, 9))
# print(r.randrange(2,9, 2))
# print(round(r.uniform(10.5, 25.5), 2))
#
# city = ['москва' ,'екатеринбург', 'воронеж']
# print(r.choice(city))
#
# city = ['москва' ,'екатеринбург', 'воронеж']
# print(r.choices(city, k=2))
#
# r.shuffle(city)
# print(city)

# from random import randint
#
# print([randint(20, 50) for i in range(10)])

# s = [5, 9, 2, 1, 4, 3, 2, 4, 8, 5]
# print(sum(s))
# print(len(s))
# print(min(s))
# print(max(s))

# r = ([randint(1, 100) for i in range(10)])
# s = max(r)
# r.remove(s)
# r.insert(0, s)
# print(r)

# lst = []
# # if len(lst) == 0:
# if not lst:
#     print("спсок пустой")
# print(bool(lst))

# from random import randint
#
# n1 = int(input("Значение для первого списка: "))
# n2 = int(input("Значение для вторго списка: "))
# while n1 < 1 or n2 < 1:
#     print("Введите значение больше ноля")
#     n1 = int(input("Значение для первого списка: "))
#     n2 = int(input("Значение для вторго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# if len(a) < len(b):
#     a, b = b, a
# c = a + b
# print("Первый список", a)
# print("Второй список", b)
# print("Третий список", c)
# c = []
# r = []
# m = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
#     if a[i] in b and a[i] not in r:
#         r.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# if len(r) == 0:
#     r = "Совпадений не найдено"
# m.append(min(a))
# m.append(min(b))
# m.append((max(a)))
# m.append((max(b)))
# print("Без повторов", c)
# print("Общие для двух списков: ", r)
# print("Мин и макс в каждом списке", m)

# МАТРИЦЫ
# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for i in m:
#     for j in i:
#         print(j**2, end="\t")
#     print()

# w, h = 5, 3
# m = [[0 for x in range(w)] for y in range(h)]
# m = []
# for i in range(h):
#     new_row = []
#     for j in range(w):
#         new_row.append(0)
#     m.append(new_row)
# print(m)

# m = [[0 for x in range(w)] for y in range(h)]

# print(m)

# for x, y in [[1, 2], [3 ,4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# from random import  randint
# w, h = 5, 4
# m = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# count = 0
# for i in m:
#     for j in i:
#         if j < 0:
#             count += 1
#         print(j,end='\t\t')
#     print()
# print(count)

# import math

# num1 = math.sqrt(4)
# # num2 = round(5.92324, 2) # округление по законам математики
# num2 = math.ceil(3.2) # округление в вехнюю сторону
# num3 = math.floor(3.2) # округление в нижнюю строану
# print(num1)
# print(num2)
# print(num3)
# print((math.pi))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")

# sec = time.time()
# print(sec)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
# print( res.tm_mday,"0" + str(res.tm_mon), res.tm_year)
#
# print(time.strftime("Today is %B %d %Y"))
#
# pause = 5
# print("Програма запущщена")
# time.sleep(pause)
# print(pause, "sec")

# text = input("НАзвание напоминаня: ")
# locale_time = float(input("через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(round(res))
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(round(res))

#  Функции

# def hello(name):
#     print("Hello", name)
#
#
# hello("Irina")
# hello("Ivan")


# def get_sum(a, b, r):
#     for i in range(r):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
#
# get_sum("+", "-", 5)
# get_sum("X", "0", 8)


# def get_sum(a, b):
#     return a + b
#
#
# a1 = 2
# b1 = 5
# res = get_sum(a1, b1)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 19), end='\t')

# res = 0
# def r(y, u):
#     if y > u:
#         return y - u
#     else:
#         return y + u
#
#
# a = 9
# b = 5
# res = r(a, b)
# print(res)


# def cub(a):
#     return a ** 3
#
# for i in range(1, 11):
#     print(i, "в кубу =", cub(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return  lst
#
#
#
# print(change([1,2,3]))
# print(change([1,12,33,54,105]))
# print(change(["с", "л", "о", "н"]))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# if func(10,15):
#     print("первое число боле")
# else:
#     print("второе число больше")


# def check_pass(pss):
#     has_up = False
#     has_low = False
#     num = False
#
#     for ch in pss:
#         if "A" <= ch <= "Z":
#             has_up = True
#         elif "a" <= ch <= "z":
#             has_low = True
#         elif "0" <= ch <= "9":
#             num = True
#
#     if len(pss) >= 8 and has_up and num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_pass(p):
#     print("надежный")
# else:
#     print("не надежный")


# def get_sum(a, b, c=0, d=0):
#     return a + b + c + d
#
#
#
# print(get_sum(1, 2, 3, 4))
# print(get_sum(2, 3, 4))
# print((get_sum(1, 5, d=2)))


# def rt_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_d = n % 10
#         if even and cur_d % 2 == 0:
#             s += cur_d
#         elif not even and cur_d % 2 != 0:
#             s += cur_d
#         n //= 10
#     return s
#
#
# print("Сумма четных чисел: ")
# print(rt_sum(9874023))
# print(rt_sum(38271))
# print(rt_sum(123456789))
# print("Сумма нечетных чисел: ")
# print(rt_sum(9874023, even=False))
# print(rt_sum(38271, even=False))
# print(rt_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")
# # display_info("Igor", age=23, name="Ira")
# print()
# print("Выберите фигуру:")
# a = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# res = 0
#
# def calc_area(h, w):
#     vis = int(input(h +  ": "))
#     if a < 3:
#         shir = int(input(w + ": "))
#     if a == 1:
#         res = vis * shir
#     if a == 2:
#         res = (vis * shir) / 2
#     if a == 3:
#         res = (vis ** 2) * w
#     return print("Площадь фигуры =", res)
#
#
# if a == 1:
#     calc_area("Высота", "Ширина")
# elif a == 2:
#     calc_area("Высота", "Основание")
# elif a == 3:
#     calc_area("Радиус", w=3.14)
# else:
#     print("Некоректное значение")



# 02.09.23

# lt1 = [1,2,3]
# print(lt1, id(lt1))
# lt1.append((4))
# print(lt1,id(lt1))
# print(lt1[0], id(lt1[0]))


# картеж (tuple)

# lst = [10,20,30]
# tpl = (10,20,30)
# print(lst[0])
# print(tpl[0])
#
# lst[0] = 25
# print(lst)
# tpl[0] = 25
# print(tpl)

# lst = [10,20,30]
# tpl = (10,20,30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5, 6
# a = tuple("Hello")
# print(a)
# print(type(a))

# a = tuple([1,2,3,4,5,6])
# print(a)
# print(a[1])

# from random import  randint

# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# t4 = t1 * 3
# print(t4)
# print(t3.count('l'))
# print(t3.index('l', 4))

# for i in t3:
#     print(i, end=' ')




# def slicer(t):
#     for i in t[0]:
#         if i == t[1]:
#             return print(t)
#         else:
#             return  print(tuple())
#
#
# print(slicer(((2,3,4), randint(0, 9))))

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1,2,3), 8))
# print(slicer((1,8,3,4,8,8,9,2), 8))


# def ter(a, b):
#     t = a + b
#     return print(t)
#
# s = tuple(randint(0, 5)
# p = tuple(randint(-5, 0)
#
# ter(s, p)

# t = (10, 11,[1,2,3],[4,5,6], ["hello", "world"])
#
# print(t[4][0])
# t[4][0] = "new"
# t[4].append("hi")
# print(t)

# t = (1,2,3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x,y,z = t
# print(x,y,z)

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return  name, age , is_married
# first_name, year, married  = get_user()
#
# print(first_name, year, married)

# t = (1,2,3)
# del t
# print()

# lst = [1,2,3,4,5,6]
# tpl = tuple(lst)
# print(lst)
# lt = list(tpl)
# print(lt)

# countries = (
#     ("германия", 80.2, (("берлин", 3.326), ("гамбург", 1.7))),("франция", 66, (("париж", 2.2), ("марсель", 1.6)),
#                                                                    )
# for contry in countries:
#     contry_name, contry_popul, cities = contry
#     print(contry_name, contry_popul, cities)

# множество (set)

# s = {"banana", "aple", "orange"}
# print(list(s))
# print(type(s))
#
# a = set("")
# print(type(a))

# s = ["banana", "aple", "orange"]
# print(s)
# s1= set(s)
# print(s1)
# s2 = list(s1)
# print(s2)
# s3 = tuple(s2)
# print(s3)

# s= {x * x for x in range(10)}
# print(s)

# def to_set(el):
#     el1 = set(el)
#     return el1, len(el1)
#
# print(to_set('я обыная строка'))
# print(to_set([4,5,4,6,2,9,11,3,4,2]))


# r = ['ab_1', 'ac_2', "bc_1", "bc_2"]
# # a = {i for i in r if 'a' in i}
# # a = ["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r]
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r if i[1] == "c"}
# print(a)

# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a.union(b)
# c = a | b
# print(c)
# a |= b
# print(a)
# c = a & b
# a &= b
# print(c)
# print(a)
# c = a - b
# a -= b
# print(a)
# a ^= b
# print(a)

# s1 = {1,2}
# s2 = {3}
# s3 = {4,5}
# s4 = [3,2,6]
# s5 = {6}
# s6 = {7,8}
# s7 = {9,8}
# # s = s1.union(s2,s3,s4,s5,s6,s7)
#
# print(s)
# print(len(s))

# s1 = "Hello"
# s2 = "How are you"
# s1 = set(s1)
# s2 = set(s2)
# s1 &= s2
# print(s1)

# a = {0,1,2,3,4}
# b = {3,2,1}
# print(a >= b)

# drawing = {"марина","женя","света"}
# music = {"костя","женя","илья"}
# only_one = drawing ^ music
# both = drawing & music
# print(only_one)
# print(both)
# drawing -= both
# print(drawing)

# mat = "Матвей", "Евгений", "Михаил", "Максим", "Наталья"
# fiz = "Максим", "Матвей", "Александр"
# priz_all = set(mat) | set(fiz)
# print("Все призеры: " , list(priz_all))
# priz_all = set(fiz) & set(mat)
# print('Призеры обеих олимпиад', priz_all)
# mat = priz_all
# print('Обнвленый список призеров по математике', mat)

# 06.09.23

# s = frozenset([1,2,3,4,5,6])
# print(s)

# 06.09.23

# Словарь (dict)

# s = ['s', 'b', 'c']
# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
# print(s)
# print(d)
# print(s[0])
# print(d['one'])

# d = {}
# d = dict()
# print(d)
# print(type(d))

# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
# key = 'one'
# try:
#     del d[key]
# except KeyError:
#     print("Елемента с ключом " + key + " нет в словаре")
# print(d)

# d = {'x1': 3,'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for i in d:
#     res *= d[i]
# print(res)

# d = dict()
# d[1] = input("=> ")
# d[2] = input("=> ")
# d[3] = input("=> ")
# d[4] = input("=> ")
# d = {i: input('=>') for i in range(1, 5)}
# print(d)
# dist = input("исключить: ")
# del d[int(dist)]
# print(d)

# d = {'x1': 3,'x2': 7, 'x3': 5, 'x4': -1}
# print(len(d))

# Методы словарей

#'clear', 'copy', 'fromkeys', 'get',
# 'items', 'keys', 'pop', 'popitem', 'setdefault',
# 'update', 'values'
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d.keys())
# print(d.values())
# print(d.items())

# for i,j in d.items():
#     print(i, "->", j)

# s = list(d.items())
# print(s)



# value = d['x1']
# value = d.get('x1', 'токого ключа нет')
# print(value)

# d2 = d
# print("D =", d)
# print('D2 =', d2)
#
# d2['four'] = 'd'
# print("D = ", d)
# print("D2=", d2)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# item = d.pop('x1', 'токого ключа не существует')


# item = d.popitem() # удоляет последний ключ
# print(item)
# print(d)

# d.clear()

# a = {'four': 'd'}
# d.update([('four', 'd')])
#
#
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'sity': 'New York'}
#
# # d = dict()
# # d['name'] = a.pop('name')
# # d['salary'] = a.pop('salary')
# # print(a)
# # print(d)
# a['location'] = a.pop('sity')
# print(a)

# d = {'одни': 1,'два': 2,'три': 3,'четыри': 4}
# d2 = {k: v for k, v in d.items() if v <= 2}
# print(d2)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'tree'
#     },
#     'second':{
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# a = ["one", 1,2,3,"two", 10,20, "three", 15,36,60,"four",-20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# a = {
#     'John': {'N': 3856, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4882, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3984, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# b = a.copy()
#
#
# def rec():
#     for i in b:
#         print(i)
#         for j in b[i]:
#             print(j, ':', b[i][j])
#
#
# def func():
#     name = input('Имя: ')
#     reg = input("Регион: ")
#     zna_sum = int(input("Сумма: "))
#     b[name][reg] = zna_sum
#     print("Новое значение: ", b[name])
#
#
#
# def clon():
#     proc = int(input("1- продолить работу, 2- выход: "))
#     while proc == 1:
#         print("ОБновленный список: ")
#         rec()
#         func()
#         proc = int(input("1- продолить работу, 2- выход: "))
#     rec()
#     print("ОБновленный список: ")
#
#
# try:
#     rec()
#     func()
#     clon()
# except (ValueError ,KeyError):
#     print("Ошибка данных")

# 12.09.2023

# d = dict(zip([1,2,3], ['one', 'two', 'tree']))
# print(d)

# one = {'name': 'Igor', 'surname': 'Doe', 'Job': 'Consoltabt' }
# two = {'name': 'Irina', 'surname': 'Smith', 'Job': 'Consoltabt' }
# for (k1,v1),(k2,v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->",v2)

#
# pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#
# data = list(zip(a, b))
# print(data)
#
# data.sort()
# print(data)
#
# # data.reverse()
# # print(data)
#
# data = dict(data)
# f = {k: v for k, v in data.items()}
# print(f)
# f = list(f.items())
# print(f)

# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.25, 'onion': 0.55}
# print({**one, **two})
#
# for k,v in {**one, **two}.items():
#     print(k, '->', v)

# colors = ['red','blue','green']
# for i in range(len(colors)):
#     print(i+1, ') ', colors[i], sep="")
# j = 1
# print()
# for color in colors:
#     print(j,") ", color, sep="")
#     j += 1
# print()
# for v, color in enumerate(colors, 1):
#     print(v, ") ", color, sep="")

# a = [1,2,3]
# b = [*a,4,5,6]
# print(b)

# def func(*args):
#     return args
#
# print(func(1))
# print(*func(1,2,3,'abc'))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
# print(summa(1,2,3,4,5,6,7,8,9))


# def to_dict(*reg):
#     for i in reg:
#         i = reg
#     return (dict(zip(i,i)))
#
# print(to_dict(1,2,3,4))
# print(to_dict('grey', (2,17), 3.11, -4))

# def reg(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
# print(reg(1,2,3,4,5,6,7,8,9))

# def func(a, *args):
#     return a, args
# print(func(2))
# print(func(2,5,9,7))

# def print_scores(stud, *scores):
#     print("Students Name: ", stud)
#     for score in scores:
#         print(score)
#
# print_scores("Jonathan", 10,2,5,7,8)
# print_scores("Rick", 5,5)

# def func(**kwargs):
#     print(kwargs)
#     return kwargs
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

# def info(**data):
#     for k,v in data.items():
#         print(k, "->",v)
#
# info(surname="Sharma", name="Irina",age=22, phone=12345)
# info(surname="Shak", name="Ira",age=25, phone=12345, country="Russia")

# my_dict = {'one': 'first'}
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
# db(k1=22,k2=31,k3=11,k4=91)
# db(name='Bob', age=31, weighr=61, eyes_color='grey')
# print(my_dict)

# name = "Tom"
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
# def bye():
#     print("Good bye", name)
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
# i = 6
# func()

# def add(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return a + x
#
#     return add_some()
#
#
# print(add(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# sum = 5
# print(sum)
#
# lst = [5,9,7,1,6,4,8]
# print(sum(lst))

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумм: ", a + b)
#
#     print("a: ", a)
#     fun2(1)
#
# fun1()

# x = 25


# def fn():
#     global t
#     a =30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
# fn()
# c = x + t
# print(c)

# quan_stud = int(input("Количество студенов: "))
# stud = []
# ball = []
# slovar =dict()



# def proc():
#     for i in range(quan_stud):
#         print(i+1, end="")
#         name_stud = input("-й Студент: ")
#         st_ball = int(input("Балл: "))
#         stud.append(name_stud)
#         ball.append(st_ball)
#     slovar.update(zip(stud, ball))
#
# def clut():
#     sum_ball = 0
#     sr_ball = 0
#     for k,v in slovar.items():
#         sum_ball += int(v)
#     sr_ball = sum_ball / quan_stud
#     print("Средний балл:",round(sr_ball),".","Студенты с баллом выше среднего:")
#     for k,v in slovar.items():
#         pet = int(v)
#         if pet > sr_ball:
#             print(k)
#
# proc()
# clut()


# quan_stud = int(input("Количество студенов: "))
# stud = []
# ball = []
# slovar = dict()
#
#
#
# def chet(a,b):
#     r = input(b)
#     a.append(r)
#
#
# def ter():
#     for i in range(quan_stud):
#         print(i + 1, end="")
#         chet(stud, "-й Студент: ")
#         chet(ball, "Балл: ")
#     slovar.update(zip(stud,ball))
#
#
# def clut():
#     sum_ball = 0
#     sr_ball = 0
#     for k,v in slovar.items():
#         sum_ball += int(v)
#     sr_ball = sum_ball / quan_stud
#     print("Средний балл:",round(sr_ball),".","Студенты с баллом выше среднего:")
#     for k,v in slovar.items():
#         pet = int(v)
#         if pet > sr_ball:
#             print(k)
#
#
#
# ter()
# clut()

# # первый вариант
#
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = 0
#
# def cub_area(k1, k2, k3):
#     global res
#     p1, p2, p3 = 0, 0, 0
#     def rect_area():
#         nonlocal p1,p2,p3
#         p1 = k1 * k2
#         p2 = k1 * k3
#         p3 = k2 * k3
#     rect_area()
#     res = (p1 + p2 + p3) * 2
# cub_area(a,b,c)
# print(res)
#
#
# # второй вариант
#
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = 0
#
# def cub_area(k1, k2, k3):
#     p1, p2, p3 = 0, 0, 0
#     def rect_area():
#         global res
#         nonlocal p1,p2,p3
#         p1 = k1 * k2
#         p2 = k1 * k3
#         p3 = k2 * k3
#         res = (p1 + p2 + p3) * 2
#     return rect_area
#
# g = cub_area(a,b,c)
# g()
# print(res)


# третий вариант
# def cub_area():
#     global a,b,c
#     a = int(input("a = "))
#     b = int(input("b = "))
#     c = int(input("c = "))
#     res = 0
#     def rect_area(k1, k2, k3):
#         nonlocal res
#         res = (((k1 * k2) + (k1 * k3) +(k2 * k3)) * 2)
#         print(res)
#     return rect_area
#
# g = cub_area()
# g(a,b,c)

# 19.09.2023

# st = ['a','b','c','d','e']
# st = [1,2,3,4,5]
# num = [1,2,3,4,5]
# print(list(map(lambda x,y: (x+y),st,num)))

# t = ('abcd','abc','sdss','sdf','eee')
# # t2 = tuple(filter(lambda s: len(s) == 3,t))
# t2 = tuple(filter(lambda s: s,t))
# print(t2)

# b = [66,98,68,33,66,55,57,38]
# c = [66,98,67,33,66,55,57,38]
# res = list(filter(lambda s:s>75,b))
# print(res)
# from random import randint
# t = list()
# for i in range(10):
#     s = randint(1,50)
#     t.append(s)
# print(t)
# res = list(filter(lambda s: 10<=s<=20,t))
# print(res)

# Декораторы

# def hello():
#     return "Hello, i am func 'hello'"
#
# def super_func(func):
#     print("Hello, i m func 'super func'")
#     print(func())
#
# super_func(hello)

# def hello():
#     return "Hello, i am func 'hello'"
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
# def func_test():
#     print("Hello, i am func 'hello'")
#
# test = my_decorator(func_test)
# test()

# def args_decor(fn):
#     def wrap(args1,args2):
#         fn(args1,args2)
#
#     return wrap
#
# @args_decor
# def print_full_name(first,last):
#     print("Меня зовут", first,last)
#
# print_full_name("ИРИНА","Лазарева")

# def args_decor(fn):
#     def wrap(*args,**kwargs):
#         print("args:",args)
#         print("kwargs:",kwargs)
#         fn(*args,**kwargs)
#
#     return wrap
#
# @args_decor
# def print_full_name(*names, study='Python'):
#     print(*names,"изучают",study,"\n")
#
# print_full_name("ИРИНА","Елизавета","Светлана", study='JavaScript')
# print_full_name("Владимир","Екатерина","Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x,y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x,y)
#
#         return wrap
#     return args_dec
#
# @decor("Сумма", "+")
# def summa(a,b):
#     print(a + b)
#
#
# @decor("Разнасть", "-")
# def sub(a,b):
#     print(a - b)
#
# summa(5,2)
# sub(5,2)

# def fist_func(arg1):
#     def second_func(func):
#         def three_func(arg3):
#             print(func(arg3) * arg1)
#         return three_func
#     return second_func
#
# @fist_func(3)
# def fn(r):
#     print("Результат:",end=" ")
#     return r
#
# fn(5)


# def typed_fn(x,y,z):
#     return x*y*z
#
# print(typed_fn(3,4,"sdf"))

# def typed(*args,**kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("не коректный тип данных", f_args[i])
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("не коректный т", f_kwargs[i])
#             return fn(*f_args,**f_kwargs)
#
#         return wrap
#     return wrapper
#
# @typed(int,int,int)
# def typed_fn(x,y,z):
#     return x * y * z
#
# @typed(str,str,str)
# def typed_fn2(x,y,z):
#     return x+y+z
#
# @typed(str,str,z=int)
# def typed_fn3(x,y,z="hello"):
#     return (x + y) * z
#
# print(typed_fn(3,4,5))
# # print(typed_fn(3,4,"sdf"))
# print(typed_fn2("as","asda","!"))
# print(typed_fn3("sdfsd","sdfsdf",z="sdf"))
# res = 0
#
# def sum_all(*arg,res):
#     print(list(map(lambda arg,res: (res + arg[i]),arg)))



# def decor(txt):
#     def vlozh_func(func):
#         def suma(texter,*args):
#             a = ", ".join(list(map(str,args)))
#             print(texter,a,"=",sum(args))
#             print(txt, a,"=",func(sum(args),len(args)) )
#         return suma
#     return vlozh_func
#
# @decor("Среднее арефметическое чисел")
# def pr(a,b):
#     return a/b
# pr("Сумма чисел ",2,3,3,4)

# 26.09.2023

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print(q in e)
# print(e[0])
# print(e[::-1])
# print(e[:3]+'t'+e[4:])

# def chngeCharToStr(s, c_old, c_new):
#     s2 = ""
#
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#             continue
#         s2 += i
#     return s2
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень нравится язык програмирования"
# str2 = chngeCharToStr(str1,"N","P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")

# name = 'Dmitriy'
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет")
#
# print(f"{round(3.353536,2)}")
# print(f"{3.353536:.2f}")


# x = 10
# y = 5
# print("x =", x)
# print(f"{x + y }")
# print(f"{x} * {y} / 2 = {x * y / 2}")

# num = 74
# print(f"{{ {{ {num} }} }}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")

# s = """<div>
# <a href="#">content</a>
# </div>"""
# print(s)

# def square(n):
#     """"Принемает число n, возврощает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


# import math
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основания заданой высаты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r +h)
#
#
# print(cylinder(2,4))

# print(ord('a'))
# print(ord('а'))

# s = 'Test string for me'
#
# arr = [ord(x) for x in s]
# print("ASCII коды", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("среднее арефметическое", arr)
# arr += [ord(x) for x in (input("->"))[:3] if ord(x) not in arr]
# print(arr)
# arr.sort()
# print(arr)
# print(arr.sort(reverse=True))

# print(chr(97))

# a,b = 122, 97
# if a > b:
#     arr = [chr(i) for i in range(b,a +1)]
#     print(' '.join(arr))
# else:
#     arr = [chr(i) for i in range(a,b +1)]
#     print(' '.join(arr))

# from random import randint
#
# SHORTTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     rand_len = randint(SHORTTEST, LONGEST)
#     res = ''
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += rand_char
#     return res
#
# print("Случайный пароль: ", random_password())


# s = "hello, WORLD! I am learning Python"
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())


# def dvoich():
#     t = int(input("Введиет число: "))
#     o = ''
#     if t == 0:
#         o = "0"
#     for i in range(t):
#         if t >= 1:
#             if int(t) % 2 == 0:
#                  o += "0"
#             else:
#                 o += '1'
#             t = t / 2
#     print((str(o)[::-1]))
#
#
# dvoich()

# from tkinter import *
# from speedtest import Speedtest
#
# def test():
#     download = Speedtest().download()
#     upload = Speedtest().upload()
#     download_speed = int(download / (10**6))
#     upload_speed = int(upload / (10**6))
#
#     download_lable.config(text="Загрузка:\n" + str(download_speed) + "Mb/cek")
#     upload_lable.config(text="Раздача:\n" + str(upload_speed) + "Mb/cek")
#
#
# root = Tk()
#
# root.title("SpeedTes")
# root.geometry("300x400")
#
# builtins = Button(root, text="Нажать", font=100, command=test)
# builtins.pack(side=BOTTOM, pady=40)
#
#
# download_lable = Label(root,text="Загрузка:\n", font=50)
# download_lable.pack(pady=(50,20))
# upload_lable = Label(root, text="отдача\n",font=50)
# upload_lable.pack(pady=(50,30))
#
# root.mainloop()


# 28.09.2023
# s = "hello, WORLD! I am learning Python"
# print(s.count("h",0,-1))
# print(s.find("Python")) # '-1' - нет совпадений
# print(s.index("Python"))
# print(s.find("l"))
# print(s.rfind("l"))
# print(s.index("Python"))
# print(s.rindex("Python"))

# strok = "один два"
# new_text = strok[strok.find(' ') + 1:] + " "+strok[:strok.find(' ')]
# print(new_text)

# s = "hello, WORLD! I am learning Python"
# print((s.startswith("hello")))
# print(s.endswith("Python"))

# a = "456"
# print(int(a))

# print('abc123'.isalnum()) # цифры и буквы
# print('ABcabc'.isalpha()) # буквы
# print('123'.isdigit()) # цифры

# print('abc123'.islower()) # проверяет на наличие нижнего регистра
# print('ABC'.isupper()) # проверяет на наличие верхнего регистра

# print('py'.center(10))
# print('py'.center(10,'-'))

# print('               py ff'.lstrip())
# print('py ff               '.rstrip())
# print('           py ff               '.strip())
#
# print('   https://www.python.org'.lstrip('/:pths '))

# s = "Я изучаю Nython. Мне нравится Nython. Nython очень нравится язык програмирования"
#
# print(s.replace('Nython','Python',2))

# s = "-"
# seq = ('a','b','c')
# print(s.join(seq))
#
# print("..".join(['1','2']))
#
# print(":".join("hello"))
# print('123.456.789'.split('.',1))
# print('123.456.789'.rsplit('.',1))
# print('123...456...789'.rsplit('...'))

# s = input("ФИО:").split()
# print(F"{s[0]}.{s[1][0]}.{s[2][0]}.")

# import re
#
# s = "Я ищу совпадения в 2023 году. И я их гайду в 2 счета"
# reg = '[ ]'

# print(re.findall(reg,s)) # список, содержащий все совпадения
# print(re.search(reg, s)) # месторасполажения первого совпадения
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# reg = 'Я ищу'
# print(re.match(reg, s)) # поиск по заданному шаблону в начале строки

# print(re.split(reg, s, 3)) # возвращает список строк, разбитых по шаблону разделителю

# print(re.sub(reg, '!', s,3)) # поиск и замена

# import re

# s = "Я ищу совпадения - в 2023 году. И я их гайду в 2 счета. [3689]"
# reg = '[12][0-9][0-9][0-9]'
# reg = '[А-яЁё]'
# reg = r'\.'
# reg = '[.\-\[\]]'
# reg = r'[^0-9]'
# print(re.findall(reg, s))
# print(ord('ё'))

# t = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диопазоне от 00 до 59. 2021-06-15T01:09.'
# p = r'[0-2][0-9][:][0-6][0-9]'
# print(re.findall(p,t))

# s = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диопазоне от 00 до 59. 2021-06-15T01:09.'
#
# reg = r'\d'
#
# print(re.findall(reg,s))

# from tkinter import *
# from tkinter import ttk
# import re
# def test():
#     ll = tt.get()
#     reg = '[Ее][а-я-]+'
#     rl = re.findall(reg,ll)
#     label["text"] = rl
#
# root = Tk()
# tt = ttk.Entry(width=30)
# tt.pack()
#
# root.geometry("500x200")
# root.title("Regulyar")
#
# btn = ttk.Button(text="Click", command=test)
# btn.pack(anchor=NW, padx=6, pady=6)
#
# label = ttk.Label()
# label.pack(anchor=NW, padx=6, pady=6)
#
#
# root.mainloop()

# import re


# d = 'Цифры: 7, +17 , -42, 0013, 0.3'
# print(re.findall(r'[+-]?\d+\.?\d*', d))

# s = '05-03-1987 # Дата рождения'
#
# print('Дата рождения: '+(re.sub("-",".",re.sub("#.+", "", s))))

# s = "12 сентября 2023 года"
# reg = r'\d{2,4}'
# print(re.findall(reg,s))

# s = '+ 7 499 456-45-78 , +74994564578 , 7 (499) 456 45 78 , 74994564578 '
# reg = '\+?7\d{10}'
# print(re.findall(reg, s))

# s = "Я ищу совпадения - в 2023 году. И я их гайду в 2 сче-та. [3689]"
# reg = r'\w+\.$'
# print(re.findall(reg, s))


# def validate_login(name):
#     return  re.findall('^[A-Za-z_-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Python_master!'))

# print(re.findall(r'\w+', '12+ й'))
# print(re.findall(r'\w+', '12+ й', flags=re.ASCII))
#
# s = "Я ищу совпадения - в 2023 году. И я их гайду в 2 сче-та. [3689]"
# reg = r'я'
# print(re.findall(reg, s, re.I))

# text = """
# one # коментарий
# two
# """

# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one$', text, re.MULTILINE))
# print(re.findall(r'one$', text, re.M))

# print(re.findall("""
# [a-z.-]+
# @
# [a-z.-]+
# """, 'text@mail.ru', re.VERBOSE))

# text = """Python
# python
# PYTHON"""
# reg = '(?im)^python'
# print((re.findall(reg,text)))

# text = "<body>Пример жадного соответсвие рег вырожения</body>"
# print(re.findall("<.*?>", text))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# s = "<p>Изображение <img alt =''картинка src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]*>'
# print(re.findall(reg, s))

# s = "Петр, Ольга и Виталий отлично учатся"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# reg = r'((int|double)\s*=\s*\d[.\w+]*)'
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = "28-08-2021"
# reg = r''
# print(re.findall(reg, a))

# s = "Я ищу совпадения - в 2023 году. И я их гайду в 2 сче-та. [3689]"
# reg = r'(\d+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s))
# m = re.search(reg, s)
# print(m[1])
# print(re.search(reg, s).group(2))

# text = """
# Самара
# Масква
# Уфа
# Казянь
# """
# count = 0
# def repl_find(m):
#     global count
#     count += 1
#     return f'<option value="{count}">{m.group(1)}<option>\n'
#
# print(re.sub(r"\s*(\w+)\s*", repl_find, text))

# s = "<p>Изображение <img alt ='картинка' src='bg.jpg'> - фон страницы</p>"
#
# # reg = r'<img.*?>'
# # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+?)\1'
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+?)\(?P=q)>'
# print(re.findall(reg, s))

# (?P<name>)  (?P=name)

# s = "Самолет прилетает 10/23/2023. Будет рады вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print((re.sub(reg,r'\2.\1.\3',s)))

# s = "yandex.com and yandex.ru"
# reg = '(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg,r"http://\1",s))



# # Первая задача
# import re
#
# pas = input("Придумайте пароль: ")
# reg = r'(^[a-zA-Z][\w\d_@-]{5,15}$)'
# print(re.findall(reg,pas))
#
# # Вторая задача
#
#
# def regu():
#        pas = input("Ведиет телефон: ")
#        reg = (r'(^'
#               r'[+]*[7][ ][(][0-9]{3}[)][ ][0-9]{3}[ ][0-9]{2}[ ][0-9]{2}|'
#               r'[+]*[7][ ][(][0-9]{3}[)][ ][0-9]{3}[-][0-9]{2}[-][0-9]{2}|'
#               r'[+]*[7][ ][0-9]{3}[ ][0-9]{3}[ ][0-9]{2}[ ][0-9]{2}|'
#               r'[+]*[7][ ][0-9]{3}[ ][0-9]{3}[-][0-9]{2}[-][0-9]{2}|'
#               r'[+]*[7][0-9]{10}$)')
#
#        reg2 = (r'(([+]*[7])'
#                r'(([0-9]{10})|'
#                r'([ ][(][0-9]{3}[)][ ]|'
#                r'[ ][0-9]{3}[ ])'
#                r'[0-9]{3}'
#                r'(([ ]|[-])[0-9]{2}([ ]|[-])[0-9]{2}|)))')
#        print(re.findall(reg,pas))
#        mat = re.search(reg2,pas)
#        print(mat[1])
#
# try:
#        regu()
# except (TypeError, ValueError):
#     print("Не верный формат")


# 05.10.2023
# Файлы

# f = open("text.txt", 'r')
# print(f)
# print(*f)
# print(f.closed)
# f.close()
# print(f.closed)

# f = open(r"C:\piton\text.txt")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open(r"C:\piton\one.txt")
# print(f.readline())
# print(f.readline())
# f.close()
#
# f = open(r"C:\piton\one.txt")
# print(f.readlines(16))
# f.close()

# f = open(r"C:\piton\one.txt")
# # print(f.readlines())
# # print(len(f.readlines()))
# count = 0
# for line in f:
#     print(line, end="")
#     count += 1
# print(count)
#
# f.close()

# f = open("xyz.txt", 'w')
# f.write(("Hello \nWorld"))
# f.close()
#
# f = open("xyz.txt", 'a')
# f.write(("\nНовый текст \nWorld"))
# f.close()


# f = open("xyz.txt", 'a')
# line = ['\nThis is line 1''\nThis is line 2','\nThis is line 3']
# f.writelines(line)
# f.close()
#
# f = open("xyz.txt", 'w')
# lst = [str(i) for i in range(1,20)]
#
# # lst = "\t".join(map(str,lst))
# # print(lst)
# f.write(str((lst)))
# for index in lst:
#     f.write(index + '\t')
#
# print(lst)
# f.close()


# f = open("text2.txt", 'w')
# f.write("Замены строки с текстом файле;\nизменить строку в списке;\nзаписать список в фаил")
# f.close()
# f = open("text2.txt", 'r')
# read_file = f.readlines()
# read_file[1] = "Hello world\n"
# print(read_file)
# f.close()
# f = open("text2.txt", 'w')
# f.writelines(read_file)
# f.close()

# f = open("text2.txt", 'w')
# f.write("Замены строки с текстом файле;\nизменить строку в списке;\nзаписать список в фаил")
# f.close()
# f = open("text2.txt", 'r')
# in_put = int(input("Числл: "))
# read_file = f.readlines()
# if 0 <= in_put < len(read_file):
#     del read_file[in_put]
# else:
#     print("инедкс введен не коректно")
# print(read_file)
# f.close()
# f = open("text2.txt", 'w')
# f.writelines(read_file)
# f.close()


# f = open("text.txt")
# print(f.read(3))
# print(f.tell())  # позиция условного курсора
# print(f.seek(1))
# print(f.read())
# f.close()

# f = open("text.txt", 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:3])

# file = "res_1.txt"
# lst = [4.5,2.8,3.9,1.0,0.3,4.33,7.777]
# def get_line(lt):
#     return " ".join(map(str,lt))
#
#
# with open(file, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")
#
# with open(file, 'r') as f:
#     nums = f.read()
# print(nums)
#
# nums_list = list(map(float, nums.split()))
# print((nums_list))
# print(sum(nums_list))

# def longest_words(file):
#     with open(file, 'r',encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w,key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
# print(longest_words("text.txt"))

# read_file = "one.txt"
# write_file = "two.txt"
# third = "three.txt"
# with open(read_file,'r') as f1, open(write_file, 'r') as f2,open(third,'w') as f3:
#     file_1 = f1.readlines()
#     file_2 = f2.readlines()
#     f4 = file_1 + file_2
#     f3.writelines(f4)



# test = "Строка №1\Строка №2\nСтрока №3\nСтрока №4\nСтрока №5"
# with open(read_file,'w') as f:
#     f.write(text)

# with open(read_file,'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write((line))

# dz_text = "Замены строки с текстом файле;\nизменить строку в списке;\nзаписать список в фаил"
# dz_file = 'dz.txt'
# input1 = int(input("1: ")) -1
# input2 = int(input("2: ")) -1
# with open(dz_file,'w') as f:
#     f.write(dz_text)
#
# with open(dz_file,'r') as fr:
#     read_line = fr.readlines()
#     fr1 = read_line[input1]
#     fr2 = read_line[input2]
#     fr3 = fr1.replace(fr1,fr2)
#
# print(read_line)

# Модули OS И OS.PATH

# import os
# import os.path

# print(os.getcwd()) #  возврщает путь к текущей рабочей деректории
# print(os.listdir()) # список файлов и деректорий
# print(os.listdir("..")) # выход на уровень выше
# os.mkdir("333") # создание директории
# os.makedirs("22/33/44") # слздаст промежуточные дериктории и конечную

# os.rmdir("22") # удоление папок
# os.rename("2", 'new') # переименовывает файли
# os.rename('new','3/new') # перемещение файла
# os.rename() # премещает фаил и создает в папку
# os.remove('text.txt') # удоление файла


# for root, dirs, files in os.walk("3"):
#     print("Root:", root)
#     print("Subdirs", dirs)
#     print("Files", files)
#     print()


# def remove_empty_rirs(root_tree):
#     print(f"Удаление пустых дурикторий в ветви {root_tree}")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалиена')
#     print('-' * 50)
#
#
# remove_empty_rirs("3")



# import os

# print(os.path.split(r'C:\piton\3\text1.txt'))
#
# print(os.path.dirname(r'C:\piton\3\text1.txt'))
# print(os.path.basename(r'C:\piton\3\text1.txt'))
#
# print(os.path.join('C:\piton','3','text1.txt'))

# import os

# dirs = [r'Work\F1',r'Work\F2\F21',]
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt','f12.txt','f13.txt'],
#     r'Work\F2\F21': ['f211.txt','f212.txt']
# }
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d,f)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt',r'Work\F1\f11.txt',r'Work\F1\f12.txt',r'Work\F1\f13.txt',r'Work\F2\F21\f211.txt',r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file,'w') as f:
#         f.write(f'same sample text for {file} file')
#
#
# def print_tree(root, topdown):
#     print(f"обход {root} {'сверху в низ'if topdown else'снизу в верх'}")
#     for root, dirs, fls in os.walk(root,topdown):
#         print(root)
#         print(dirs)
#         print(fls)
#     print("-" * 50)
#
# print_tree("Work", False)
# print_tree("Work", True)




# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# import os
# import time
#
# # print(os.path.exists(r'C:\piton\Work\F2\F21\f212.txt')) # возврощает True , елси path указывает
# # # на сущесвтует путь в файловой системы
# # print(os.path.isfile(r'C:\piton\Work\F2\F21\f212.txt')) # проверка на наличие по задонному пути файла
# # print(os.path.isdir(r'C:\piton\Work\F2\F21\f212.txt')) # проверка по задоному пути папки
#
# path = 'main.py'
# print(os.path.getsize(path) / 1024) # в кбайтах
# print(os.path.getmtime(path)) # время последнего изменения
# print(os.path.getatime(path)) # последнее доступ к файлу
# print(os.path.getctime(path)) # время созданиея файла
#
# c = os.path.getctime(path)
# print('последнее изменения ',time.strftime("%d.%m.%Y, %H.%M.%S", time.localtime(os.path.getmtime(path))))
# print('доступ ',time.strftime("%d.%m.%Y, %H.%M.%S", time.localtime(os.path.getatime(path))))
# print('создание ',time.strftime("%d.%m.%Y, %H.%M.%S", time.localtime(os.path.getctime(path))))

# file_path = r'C:\piton\3\text1.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getmtime((file_path))
#     print(f'{name} ({dirs}) время последнего доступа к файлу {atime}')
# else:
#     print(f'Фаил {file_path} не существует')

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("на каком вы етаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1,2,3,4,5]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
# print(to_str(105,16))


# s = '\n Ежевику для ежат \n Принесли два ежа. \n Ежевику еле-еле \n Ежата возле ели сьели'
# s1 = s.split(" ")
# count = 0
# for i in s1:
#     if i[0] == 'Е' or i[0] == 'е':
#         count += 1
# print('Тестовый пример: ', s,'('+ str(count),' слова)')
# print('Количество слов: ',count)





# def to_str(n, base):  # 255
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base] # to_str(25, 10) # convert[255%10] =>5
#
# print(to_str(255,10))

# names = ['Adam',['Bob',['Cht','Cat'],'Bard','Bert'],'Alex',['Bea','Bill'],'Ann']
# print(names)
# print(len(names))
# print(names[1])
# print(isinstance(names[1], list))
# print(isinstance(names[1][1], list))
# print(isinstance(names[1][1][0], list))

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
# print(count_items(names))



# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld  "))


# ООП

# Class Имя:
# свойства (переменные)
# методы (функции)

# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# p2 = Point()
# # print(type(p1))
# print(p1.x)
# print(p2.x)

#
# class Point:
#     x = 1
#     y = 2
#
#     def set_cord(self,x,y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p2 = Point()
# p1.set_cord(3,7)



# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     adress = 'street, house'
#
#
#     def print_info(self):
#         print(" Персональные данные ".center(40,"*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nphone: {self.phone}\nГород: {self.city}\n"
#               f"Страна: {self.country}\nАдрес: {self.adress}")
#         print("=" * 40)
#
#     def input_info(self, first_name,birthday,phone,country):
#         self.name = first_name
#         self.country = country
#         self.phone = phone
#         self.birthday = birthday
#
#     def set_phone(self,phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_name(self,name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
#
# h1 = Human()
# # h1.print_info()
# h1.input_info("Юля","21.05.1986","Баку","Грузия")
# h1.set_phone("55-99-33")
# h1.print_info()
# print(h1.get_phone())
# h1.set_name("Valya")
# print(h1.get_name())

#
# class Person:
#     skill = 10
#
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника: ", self.name, self.surname)
#
#     def add_skill(self,k):
#         self.skill += k
#         print("Квалификация сотрудника: ", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Викторов")
# p1.print_info()
# p1.add_skill(2)
#
# p2 = Person("Анна","Долгих")
# p2.print_info()
# p2.add_skill(3)

# dz_text = ("Замены строки с текстом файле;\n"
#            "изменить строку в списке;\n"
#            "записать список в фаил;\n")
# dz_file = 'dz.txt'
#
# with open(dz_file,'w') as f:
#     f.write(dz_text)
#
# dz_text2 = dz_text
#
# with open(dz_file,'r') as fr:
#     print("Изнанчальный текс:")
#     print(dz_text2)
#     dz_text2 = str()
#     dz_text_clon = []
#     dz_text_clon = fr.readlines()
#
#
# print(dz_text2)
# print("Заменить строки: ")
# input1 = int(input("1: "))-1
# input2 = int(input("2: "))-1
#
# while input1 >= len(dz_text_clon) or input1 < 0 or input1 == input2:
#     input1 = int(input("Вторым значением выбрана "+str(input2+1)+" строка,"+" повторите 1-е значение: "))-1
# while input2 >= len(dz_text_clon) or input2 < 0 or input1 == input2 :
#     input2 = int(input("Первым значением выбрана "+str(input1+1)+" строка,"+" повторите 2-е значение: "))-1
#
# dz_text_clon[input1], dz_text_clon[input2] = dz_text_clon[input2],dz_text_clon[input1]
# for i in dz_text_clon:
#     dz_text2 += i
#
# with open(dz_file, 'w') as f2:
#     f2.write(dz_text2)
# print('После замены:')
# print(dz_text2)

# dz_class_car

# class Car:
#
#
#     def __init__(self, style, year_manu,manufacturer, eng_power, color, price):
#         self.style = style
#         self.year_manu = year_manu
#         self.manufacturer = manufacturer
#         self.eng_power = eng_power
#         self.color = color
#         self.price = price
#
#
#     def set_year(self, year_manu):
#         self.year_manu = year_manu
#
#
#     def set_color(self,color):
#         self.color = color
#
#     def set_price(self,price):
#         self.price = price
#
#     def get_year(self):
#         return self.year_manu
#
#     def get_color(self):
#         return self.color
#
#     def get_price(self):
#         return self.price
#
#
#     def print_info(self):
#         print("Данные автомобиля".center(40,"*"))
#         print(f"Название модели: {self.style}\nГод выпуска: {self.year_manu}\n"
#               f"Производитель: {self.manufacturer}\nМощность двиготеля: {self.eng_power} л.с.\n"
#               f"Цвет машины: {self.color}\nЦена: {self.price} у.е")
#         print("=" * 40)
#
#
#
# car = Car("X7 M50I"," ","BMW","530"," "," ")
# car.set_color("Red")
# car.set_year("2023")
# car.set_price("5 000 000 000")
# car.print_info()
# print(car.get_year())
# print(car.get_color())
# print(car.get_price())

# import os
# dir_name = "" # имя папки
# obj = os.listdit(dir_name)
# print(obj)
#
# for ob in obj:
#     p = os.path.join(dir_name, ob)
#     if os.path.isfile(p):
#         print(f"{ob} - file - {os.path.getsize(p)}")
#     elif os.path.isdir(p):
#         print(f"{ob} - dir")


# class Point:
#     count = 0
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(2 , 8)
# p3 = Point(7,12)
# print(p3.count)
# print(Point.count)
# print(p1.x)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.nane = name
#         print(f"Инициализация робота: {self.nane}")
#         Robot.k += 1
#
#     def __del__(self):
#         print(f"{self.nane} выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(f"{self.nane} был последним")
#         else:
#             print(f"Роботоющих роботов осталось: {Robot.k}")
#
#
#     def say_hi(self):
#         print(f"Приветсвую! Меня зовут {self.nane}")
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print(f"Численность роботов: {Robot.k}")
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# droid3 = Robot("C-O")
# droid3.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# print(f"\nЗдесь роботы могут проделать какуюто работу\n")
#
# print(f"Роботы закончили свою работу.Давайте их выключим.")
# del droid1
# del droid2
# del droid3
# print(f"Численность роботов: {Robot.k}")



# class Point:
#     __slots__ = ("__x","__y")
#
#     def __init__(self,x,y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(s):
#         if isinstance(s,int) or isinstance(s,float):
#             return True
#         return False
#     def set_y(self,y):  # устонавливаем координаты
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_y(self):    # получаем координаты
#         return self.__y
#
#     def set_x(self,x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#
# p1 = Point(5, 10)
# # print(p1.__dict__)
# # # p1.set_coord(10,50)
# # print(p1.__dict__)
# # print(p1.get_coord())
# # # print(Point.__dict__)
# # p1.set_x("fd")
# # print(p1.get_x())
# # print(p1._Point__x)
# # print(p1.__dict__)
# # p1.set_x(55)
# print(p1.get_y())


# class Point:
#     def __init__(self,x,y):
#             self.__x = x
#             self.__y = y
#
#     def __set_x(self,x):
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_x(self):
#         return self.__x
#
#     def __del_x(self):
#         print(f"Удаление свойства {self.x}")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
# p1 = Point(5,10)
# p1.x = 70
# print(p1.x)
# del  p1.x
# print(p1.__dict__)

#
# class Point:
#     def __init__(self,x,y):
#             self.__x = x
#             self.__y = y
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self,x):
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#
#     @x.deleter
#     def x(self):
#         print(f"Удаление свойства {self.x}")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
# p1 = Point(5,10)
# p1.x = 70
# print(p1.x)
# del  p1.x
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.kg = 0
#         if isinstance(kg, (int, float)):
#             self.__kg = kg
#         else:
#             self.kg = 0
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self,new_kg):
#         if isinstance(new_kg, (int,float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(f"{weight.kg} кг => {weight.to_pounds()} фунтов")
# weight.kg = 41
# print(f"{weight.kg} кг => {weight.to_pounds()} фунтов")
# weight.kg = "десять"
# print(f"{weight.kg} кг => {weight.to_pounds()} фунтов")
#
# class Pound:
#     def __init__(self,kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#     @kg.setter
#     def kg(self,n_kg):
#         try:
#             self.__kg = int(n_kg)
#             print(f"{self.__kg} kg => {round(self.__kg * 2.2,2)} pounds")
#         except ValueError:
#             print("Введите число")
#
#
# vod = input("=> ")
# p = Pound(0)
# p.kg = vod

# 24.10.2023

# import re
#
# class UserData:
#     def __init__(self, fio,old,ps,weight):
#         self.verify_old(old)
#         self.verify_ps(ps)
#
#         self.fio = fio
#         self.__old = old
#         self.__ps = ps
#         self.__weight = weight
#
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         print(f)
#         if len(f) != 3:
#             raise TypeError("Неверный формат")
#         letters = "".join(re.findall("[a-zа-яё-]",fio,re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("в фио можно использовать только буквы и дифис")
#         print(letters)
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("СТрока")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("числа")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#
# p1 = UserData("Волков Игорь Николаевич",26,"1234 567890",808)
# p1.fio = ("Рыцарев Игорь Николаевич")
# print(p1.fio)


# Наследование
# Базовый класс(родителький, супрекласс)
#      Дочерний (класс-наследник,подкласс)

# class Point:
#     """
#     Точка в двумерном пространстве
#     """
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
# print(issubclass(Point, object))
# print(Point.__dict__)
#
#
# class Point:
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x,self.y})"
#
#
# class Prop:
#     def __init__(self,sp: Point,ep: Point,color: str="red", width: int=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width

#
#         def get_width(self):
#             return self._width
#
#
# class Line(Prop):
#     def __init__(self,*args):
#         super().__init__(*args)
#
#
#     def draw_line(self):
#         print(f"рисование лини: {self._sp},{self._ep},{self._color},{self._width}")
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"рисование прямоуголника: {self._sp},{self._ep},{self._color},{self._width}")
#
#
#
# line = Line(Point(1,2), Point(10,20), "grey", 33)
# line.draw_line()
# print(Line._color)

# class Figure:
#     def __init__(self, color: str="цвет"):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#
# class Fig_s(Figure):
#     def __init__(self, s: int="число", t: int="число или 0", fig: str="прямоуголник,круг", *args: Figure):
#         super().__init__(*args)
#         self.verify_s(s)
#         self.verify_t(t)
#         self.verify_error(s)
#         self.verify_error(t)
#
#         self.s = s
#         self.t = t
#         self.fig = fig
#
#     @staticmethod
#     def verify_s(s):
#         if not isinstance(s,(int,float)):
#             raise TypeError("Ведите число")
#
#     @staticmethod
#     def verify_t(t):
#         if not isinstance(t,(int,float)):
#             raise TypeError("Ведите число")
#
#     @staticmethod
#     def verify_error(arg):
#         if arg < 0:
#             raise TypeError("введите число больше нуля")
#
#     @staticmethod
#     def plozh(fig,s,t):
#         if fig == "прямоуголник":
#             return s * t
#         elif fig == "круг":
#             return s**2 * 3.14
#         else:
#             raise TypeError("нет такой фигуры")
#
#     def print_info(self):
#         print(f"Площадь {self.fig}а равна:  {self.plozh(self.fig,self.s,self.t)} у.е. и имеет {self.color} цвет")
#
#
# l = Fig_s(5,4,"прямоуголник","серый")
# l2 = Fig_s(5,0,"круг","серый")
# l.print_info()
# l2.print_info()

#
# class Point:
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
#     def __str__(self):
#         return f"({self.x,self.y})"
#
#
#     def is_digit(self):
#         if isinstance(self._x, (int,float)) and isinstance(self._y,(int,float)):
#             return True
#         return False
#
#     def is_int(self,sp,ep):
#         if isinstance(self.__x, (int)) and isinstance(self.__y,(int)):
#             return True
#         return False
#
# class Prop:
#     def __init__(self,sp: Point,ep: Point,color: str="red", width: int=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_cord(self,sp,ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Коорджинаты должыны быть чилсами")
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         super().__init__(*args)
#
#
#     def draw_line(self):
#         print(f"рисование лини: {self._sp},{self._ep},{self._color},{self._width}")
#
#     def set_cord(self,sp,ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Коорджинаты должыны быть чилсами")
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"рисование прямоуголника: {self._sp},{self._ep},{self._color},{self._width}")
#
# l = Line(Point(1,2),Point(10,20),"grey",5)
# l.draw_line()
# l.set_cord(Point(20, 30),Point(100,200))
# l.draw_line()


# class Rect:
#     def __init__(self,w,h):
#         self.w = w
#         self.h = h
#
#     def show_rect(self):
#         print(f"Прямоуголник:\nШирина: {self.w}\nВысота: {self.h}")
#
# class ReFon(Rect):
#     def __int__(self, w, h, back):
#         super().__init__(w,h)
#         self.fon = back
#
#     def show_rect(self):
#         super().show_rect()
#         print("фон:", self.fon)
#
#
# shape1 = ReFon(100, 200,"red")
# shape1.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str,self))
#
#
# v = Vector([1,2,3])
# print(v)
# print(type(v))


# прегрузка методов

# def func(a,b=None,c=None):
#     ...
#
# func(1,2,3)
# func(1,2)
# func(1)
#
#
# class Point:
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
#     def __str__(self):
#         return f"({self.x,self.y})"
#
#
#     def is_digit(self):
#         if isinstance(self._x, (int,float)) and isinstance(self._y,(int,float)):
#             return True
#         return False
#
#     def is_int(self,sp,ep):
#         if isinstance(self.__x, (int)) and isinstance(self.__y,(int)):
#             return True
#         return False
#
# class Prop:
#     def __init__(self,sp: Point,ep: Point,color: str="red", width: int=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_cord(self,sp,ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Коорджинаты должыны быть чилсами")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"рисование лини: {self._sp},{self._ep},{self._color},{self._width}")




# l = Line(Point(1,2),Point(10,20),"grey",5)
# l.set_cord(Point(20, 30),Point(100,200))
# l.draw_line()
# l.set_cord(уз=Point)



# class Point:
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x,self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int,float)) and isinstance(self.__y,(int,float)):
#             return True
#         return False
#
#     def is_int(self,sp,ep):
#         if isinstance(self.__x, int) and isinstance(self.__y,int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self,sp: Point,ep: Point,color: str="red", width: int=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def drow(self): # абстракный метод
#         raise NotImplementedError("В дочернем классе должен быть определен метод drow()")
#
#     def set_cord(self,sp,ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Коорджинаты должыны быть чилсами")
#
# class Line(Prop):
#     def draw(self):
#         print(f"рисование лини: {self._sp},{self._ep},{self._color},{self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"рисование прямоуголник: {self._sp},{self._ep},{self._color},{self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0,0),Point(10,10)))
# figs.append(Line(Point(10,10),Point(20,10)))
# figs.append(Rect(Point(50,50),Point(30,30)))
#
# for f in figs:
#     f.draw()
#
# from math import pi
# class Table:
#     def __init__(self,w=None,h=None,r=None):
#         if r is None:
#             if h is None:
#                 self._w = self._h = w
#             else:
#                 self._w = w
#                 self._h = h
#         else:
#             self._r = r
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должно быть определиен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._w * self._h
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._r ** 2,2)
#
#
# t = SqTable(20,10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t3 = RoundTable(r=20)
# print(t3.calc_area())

#
# from abc import ABC, abstractmethod
#
# class Chess(ABC):
#     def draw(self):
#         print("Фигура")
#
#     @abstractmethod
#     def move(self):
#         pass
#
# class Quean(Chess):
#     def move(self):
#         print("Ferz peremechen")
#
# q = Quean()
# q.move()

# from abc import ABC, abstractmethod
#
# class Currency(ABC):
#     def __init__(self,value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EURO"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#
#         print(f"{Euro.suffix} = {self.convert_to_rub():2f} RUB")
#
#
#
#
# class Dollar(Currency):
#     rete_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rete_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
#
# d = [Dollar(5),Dollar(10),Dollar(50),Dollar(100),]
# e = [Euro(5),Euro(50),Euro(500),Euro(5000)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")
# print("*" * 50)
# for elem in e:
#     elem.print_value()

#
# class Arifmetika:
#     def __init__(self,arg1=None,arg2=None):
#         self.kat1 = arg1
#         self.kat2 = arg2
#
#     @property
#     def kat1(self):
#         return self.__arg1
#     @kat1.setter
#     def kat1(self,arg1):
#         self.args_error(arg1)
#         self.__arg1 = arg1
#
#     @property
#     def kat2(self):
#         return self.__arg2
#     @kat2.setter
#     def kat2(self,arg2):
#         self.args_error(arg2)
#         self.__arg2 = arg2
#
#
#     @staticmethod
#     def args_error(er):
#         if er == None:
#             raise ValueError("Необходимо 2 аргумента")
#         if not isinstance(er,(int,float)):
#             raise TypeError("Необходимо ввести число")
#         if er <= 0:
#             raise ValueError("Введите число больше нуля")
#
#
#     def mnozh_args(self):
#         return self.kat1 * self.kat2
#
#     def sum_args(self):
#         return self.kat1 + self.kat2
#
#     def print_sum(self):
#         return (f"Сумма катетов = {self.sum_args()}\n")
#
#     def print_mnozh(self):
#         return (f"Множество катетов = {self.mnozh_args()}\n")
#
#
# class Geometry(Arifmetika):
#     def __init__(selfs,arg1=None,arg2=None):
#         super().__init__(arg1,arg2)
#
#     def s_args(self):
#         return  f"Площадь треугольника = {self.mnozh_args() / 2}\n"
#
#     def gipotenuza(self):
#         return f"Гипотенуза треугольника = {round((self.kat1 ** 2 + self.kat2 ** 2) ** 0.5,2)}\n"
#
#     def print_info(self):
#         print(f"{self.print_sum()}{self.print_mnozh()}{self.gipotenuza()}{self.s_args()}")
#
# g = Geometry(1,1)
# g.print_info()
# g.kat1 = 5
# g.kat2 = 8
# g.print_info()


# class Acaunt:
#     def __init__(self,name,pas,phon):
#         self.__name = name
#         self.__pas = pas
#         self.__phon = phon
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name):
#         self.__name = name
#
#     @property
#     def pas(self):
#         return self.__pas
#
#     @pas.setter
#     def pas(self,pas):
#         self.__pas = pas
#
#     @property
#     def phon(self):
#         return self.__phon
#
#     @phon.setter
#     def phon(self,phon):
#         self.__phon = phon
#
#     def print_info(self):
#         print(f"Вариант с property: \n{self.name}\n{self.pas}\n{self.phon}")
#
#
#
# a = Acaunt("Vitya","12345","+7 *** *** ** **")
# a.name = "Vika"
# a.ps = "54321"
# a.phon = "+7 903 333 33 33"
# a.print_info()
#
#
# class Acaunt2:
#     def __init__(self,name,pas,phon):
#         self.__name = name
#         self.__pas = pas
#         self.__phon = phon
#
#     def set_name(self,name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_ps(self,ps):
#         self.__ps = ps
#
#     def get_ps(self):
#         return self.__ps
#
#     def set_phon(self,phon):
#         self.__phon = phon
#
#     def get_phon(self):
#         return self.__phon
#
#     def print_info(self):
#         print(f"Вариант через set и get: \n{self.__name}\n{self.__pas}\n{self.__phon}")
#
# a2 = Acaunt2("Vitya","12345","+7 *** *** ** **")
# a2.set_name("Vika")
# a2.set_ps("54321")
# a2.set_phon("+7 903 333 33 33")
# a2.print_info()






# 02.11.2023
# Миксины
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
# class LoggerMixin:
#             def log(self,message, filename="logfile.txt"):
#                 with open(filename,"a") as fh:
#                     fh.write(message)
#
#             def display(self,message):
#                 Displayer.display(message)
#                 self.log(message)
#
#
# class MySubClass(LoggerMixin,Displayer):
#     def log(self,mssage,filename = ""):
#         super().log(mssage,filename="subclass.txt")
#
# subclass = MySubClass()
# subclass.display("1111111111122222222223333333")


# class Goods:
#     def __init__(self,name,weight, price):
#         super().__init__()
#         print("INIT GOODS")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name},{self.weight},{self.price}")
#
# class Mixinlog:
#     ID = 0
#
#     def __init__(self):
#         print("INIT MIXINLOG")
#         Mixinlog.ID += 1
#         self.id = Mixinlog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
# class NoteBook(Goods,Mixinlog):
#     ...
#
#
# n = NoteBook("HP",1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2 = NoteBook("HP",1.5, 35000)
# n.save_sell_log()

# class Point:
#     def __init__(self,*args):
#         self.__cords = args
#
#     def __len__(self):
#         return len(self.__cords)
#
# p = Point(5,7)
# print(len(p))
# p2 = Point(2,4,9)
# print(len(p2))

# Перегрузка

# Число секунд в одном дне 24*60*60 = 86400



# c2 = Clock(100)
# # c4 = Clock(300)

# print(c2.get_format_time())
# # c3 = c1 + c2 + c4
# # c1 += c2
# # print(c1.get_format_time())
# # print(c3.get_format_time())
# if c1 == c2:
#     print("время одиниково")
# else:
#     print("время разное")
# if c1 != c2:
#     print("время разное")
# else:
#     print("время одинаково")

# from random import choice, randint
# class Cat:
#     def __init__(self,name,age,pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy"
#         elif self.pol == "F":
#             return f"{self.name} is good girl"
#         else:
#             return f"{self.name} is good Kitty"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}'"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return  [Cat("No name",0,choice(["M","F"])) for _ in range(randint(1,5))]
#         else:
#             raise TypeError("Типы не совместимы")
#
#
# cat1 = Cat("Tom",4,"M")
# cat2 = Cat("Elsa",5,'F')
# cat3 = Cat("Murzik",5,"M")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)

# class Student:
#     def __init__(self,name,*marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             return IndexError("неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Не корекное занчение")
#         if key >= len(self.marks):
#             off = key +1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Srgey",5,5,3,4,5)
# # print(s1.marks[5])
#
# s1[3] = 4
# del s1[2]
# print(s1[3])

# class Student:
#
#     def __init__(self, name, Par):
#         self.name = name
#         self.Par = Par
#         self.print_info()
#
#     def print_info(self):
#         print(f"{self.name} => {self.Par}")
#
#     class Parametr:
#         def __init__(self, model, proc, ram):
#             self.model = model
#             self.proc = proc
#             self.ram = ram
#
#         def __str__(self):
#             return f"{self.model}, {self.proc}, {self.ram}"
#
#
# stud1 = Student("Roman", Student.Parametr("HP","i7",32))
# stud2 = Student("Vladimir", Student.Parametr("HP","i5",16))

# class Clock:
#     __DAY = 86400
#     def __init__(self,sec):
#         if not isinstance(sec, int):
#             raise ValueError("секунджы должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 60
#         return f"{Clock.__get_form(h):}:{Clock.__get_form(m):}:{Clock.__get_form(s):}"
#
#     @staticmethod
#     def __get_form(x):
#         return x if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return self.sec >= other.sec
#
#     def __it__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый оеперант должен быть типом данных Clock")
#         return self.sec <= other.sec
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("ключ должен быть строкой")
#
#         if item == "hour":
#             h = (self.sec // 3600) % 24
#             return Clock.__get_form(h)
#         elif item == "min":
#             m = (self.sec // 60) % 60
#             return Clock.__get_form(m)
#         elif item == "sec":
#             s = self.sec % 60
#             return Clock.__get_form(s)
#         return "не верный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("должно быть целым числом")
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 60
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
#
#
# c1 = Clock(600)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(f"c1: {c1['hour']}:{c1['min']}:{c1['sec']}")
# c3 = c1 - c2
# print(f"c1 - c2: {c3['hour']}:{c3['min']}:{c3['sec']}")
# c3 = c1 * c2
# print(f"c1 * c2: {c3['hour']}:{c3['min']}:{c3['sec']}")
# c3 = c1 // c2
# print(f"c1 // c2: {c3['hour']}:{c3['min']}:{c3['sec']}")
# c3 = c1 % c2
# print(f"c1 % c2: {c3['hour']}:{c3['min']}:{c3['sec']}")
# c1 -= c2
# print(f"c1 -= c2: {c1['hour']}:{c1['min']}:{c1['sec']}")
# c1 *= c2
# print(f"c1 *= c2: {c1['hour']}:{c1['min']}:{c1['sec']}")
# c1 //= c2
# print(f"c1 //= c2: {c1['hour']}:{c1['min']}:{c1['sec']}")
# c1 %= c2
# print(f"c1 % c2: {c1['hour']}:{c1['min']}:{c1['sec']}")
# if c3 > c1:
#     print(f"c3 > c1 {True}")
# else:
#     print(f"c3 > c1 {False}")
# if c3 >= c1:
#     print(f"c3 >= c1 {True}")
# else:
#     print(f"c3 >= c1 {False}")
# if c3 < c1:
#     print(f"c3 < c1 {True}")
# else:
#     print(f"c3 < c1 {False}")
# if c3 <= c1:
#     print(f"c3 <= c1 {True}")
# else:
#     print(f"c3 <= c1 {False}")
# if c3 == c1:
#     print(f"c3 == c1 {True}")
# else:
#     print(f"c3 == c1 {False}")

#
#
# import os,os.path
#
# # Создание файлов
# dz_os_file1 = 'project.txt'
# dz_os_file2 = 'test.txt'
# test1 = "test1"
# test2 = "test2"
# os.mkdir(test1)
# os.mkdir(test2)
# with open(dz_os_file1, "w") as file:
#     file.write("7777777775555555555555")
# with open(dz_os_file2, "w") as file:
#     file.write("7")
#
# # проверка фалйлов
# ls = [dz_os_file1,dz_os_file2,test1,test2]
# for i in ls:
#     if os.path.isfile(i) == True:
#         print(f"{i} - file - {os.path.getsize(i)} bites")
#     else:
#         print(f"{i} - dir")
#
# # Удаление файлов
# os.remove('project.txt')
# os.remove('test.txt')
# os.rmdir("test1")
# os.rmdir("test2")

# 07.11.2023

# class Rectangle:
#     def __init__(self, w,h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return self.a * 4
#
# class Triangle:
#     def __init__(self, a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b +self.c
#
#
# r1 = Rectangle(1,2)
# r2 = Rectangle(3,4)
# # print(r1.get_perimetr(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_perimetr(), s2.get_per_sq())
#
# t1 = Triangle(1,2,3)
# t2 = Triangle(4,5,6)
# # print(t1.get_perimetr(), t2.get_per_tr())
#
# shape = [r1,r2,s1,s2,t1,t2]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self,a):
#         return self.value +int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self,a):
#         return len(self.value + str(a))
#
# t1 = Number(10)
# t2 = Text("Python")
#
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}.Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}.Мой возраст{self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает")
#
# cat = Cat("Пушок",2.5)
# dog = Dog("Мухтар",4)
#
# animal = [cat,dog]
#
# for i in animal:
#     i.info()
#     i.make_sound()
#
#
# class Human:
#     def __init__(self,name,surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         print(f"{self.name} {self.surname} {self.age}",end="")
#
#
# class Studend(Human):
#     def __init__(self,name,surname,age,spec,group,ball):
#         super().__init__(surname,name,age)
#         self.spec = spec
#         self.group = group
#         self.ball = ball
#
#     def info(self):
#         super().info()
#         print(f"{self.spec} {self.group} {self.ball}")
#
#
#
# class Teacher(Human):
#     ...
#
#
# class Graduate(Studend):
#     ...
#
#
# group = [
#     Studend("Vika","Vetosheva",15,"Гк","web_011",5),
#     Studend("Vika", "Vetosheva", 15, "Гк", "web_011", 5)
# ]
#
# for i in group:
#     i.info()

# Функторы
# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self,*args,**kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()

# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("должен быть строкой")
#         return string.strip(chars)
#     return wrap
#
# s1 = string_strip("?:!.; ")
# print(s1(" ?Heloo, World! "))
#
# class Stringstrip:
#     def __init__(self,chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
#
# s2 = Stringstrip("?:!.; ")
# print(s2(" ?Heloo, World! "))
#
# class MyDecorator:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __call__(self,x, y):
#         print("Per vizovom func")
#         res = self.fn(x,y)
#         print("posle vizova func")
#         return res
#
# @MyDecorator
# def func(a,b):
#     return a * b
#
# print(func(2,5))

# class Power:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __call__(self,x, y):
#         return self.fn(x,y)**2
#
# @Power
# def func(a,b):
#     return a * b
#
# print(func(2,5))

# class MyDecorator:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __call__(self,*args,**kwargs):
#         res = self.fn(*args,**kwargs)
#         return res
#
# @MyDecorator
# def func(a,b):
#     return a * b
# @MyDecorator
# def func1(a,b,c):
#     return a * b * c
#
# @MyDecorator
# def func2(a,b,c):
#     return a + b + c
#
# print(func(2,5))
# print(func1(2,5,2))
# print(func2(2,c=5,b=2))


# class MyDecorator:
#     def __init__(self,arg):
#         self.arg = arg
#
#     def __call__(self,fn):
#         def wrap (*args,**kwargs):
#             res = fn(*args,**kwargs)
#             return self.arg ** res
#         return wrap
#
# @MyDecorator(2)
# def func(a,b):
#     return a * b
#
#
# print(func(2,5))


# def dec(fn):
#     def wrap(*args,**kwargs):
#         print("*"*20)
#         fn(*args,**kwargs)
#         print("*"*20)
#     return wrap
#
# class Person:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
# p1 = Person("Vika", "Sokolova")
# p1.info()


# def decorator(cls):
#     class Wraper(cls):
#         def double(self,value):
#             return value * 2
#     return Wraper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print(f"Iniciolizator")
#
#     def quad(self,value):
#         return value*4
#
# obj = ActualClass()
# print(obj.quad(4))
#

# д искрипторы
# __get__()
# __set__()
# __delite()
# __set_name__()

# class String:
#     def __init__(self,value=None):
#         if value:
#             self.set(value)
#
#     def set(self,value):
#
#         if not isinstance(value,str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
#
#
# class Person:
#     def __init__(self,name,surname):
#         self.name = String(name)
#         self.surname = String(surname)

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self,value):
    #     if not isinstance(value,str):
    #         raise TypeError(f"{value} должно быть строкой")
    #     self.__surname = value



# class ValidSckript:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value,str):
#             raise TypeError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidSckript()
#     surname = ValidSckript()
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#
# p = Person("Ivan","IVANOV")
# print(p.name)
# print(p.surname)
# #
# from abc import ABC,abstractmethod
# import math
# class Shape(ABC):
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwrgs = kwargs
#     @abstractmethod
#     def perimeter(self):
#         print(" ")
#
#     @abstractmethod
#     def area(self):
#         print(" ")
#
#     @abstractmethod
#     def paint_figure(self):
#         print(" ")
#
# class Square(Shape):
#     def __init__(self, arg, color):
#         self.arg = arg
#         self.color = color
#
#     def area(self):
#         return self.arg * self.arg
#
#     def perimeter(self):
#         return self.arg * 4
#
#     def paint_figure(self):
#         print((f"{self.color * self.arg}\n")* self.arg)
#
#
#     def print_info(self):
#         print("===Квадрат===")
#         print(f"Сторона: {self.arg}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area()}")
#         print(f"Периметр: {self.perimeter()}")
#         self.paint_figure()
#
#
#
# class Rectengle(Shape):
#     def __init__(self, width,height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return (self.height + self.width) * 2
#
#     def paint_figure(self):
#         print((f"{self.color * self.width}\n")* self.height)
#
#     def print_info(self):
#         print("===Прямоуголник===")
#         print(f"Длинна : {self.height}")
#         print(f"Ширина: {self.width}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area()}")
#         print(f"Периметр: {self.perimeter()}")
#         self.paint_figure()
#
#
#
# class Triangle(Shape):
#     def __init__(self, arg_a,arg_b,arg_c, color):
#         self.arg_a = arg_a
#         self.arg_b = arg_b
#         self.arg_c = arg_c
#         self.color = color
#
#     def area(self):
#         p = (self.arg_a + self.arg_b + self.arg_c) * 0.5
#         return round((p * (p - self.arg_a) * (p - self.arg_b) * (p - self.arg_c)) ** 0.5,2)
#
#     def perimeter(self):
#         return self.arg_a + self.arg_b + self.arg_c
#
#     def paint_figure(self):
#         r = 0
#         for i in range(self.arg_b):
#             r += 1
#             print((self.color * (i + r)).center(self.arg_a," "))
#
#     def print_info(self):
#         print("===Треуголник===")
#         print(f"Сторона 1 : {self.arg_a}")
#         print(f"Сторона 2: {self.arg_b}")
#         print(f"Сторона 3: {self.arg_c}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area()}")
#         print(f"Периметр: {self.perimeter()}")
#         self.paint_figure()
#
#
# ls = [
#     Square(3," + "),
#     Rectengle(7,3," * "),
#     Triangle(11,6,6,"#")
# ]
#
# for cl in ls:
#     cl.print_info()

# class Integer(Shape):
#     @staticmethod
#     def verify_cord(cord):
#         if not isinstance(cord, int):
#             raise TypeError(f"Координата {cord} должна быть числом.")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance,self.name)
#
#     def __set__(self, instance, value):
#         Integer.verify_cord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1,2,3)
# print(p1.__dict__)
# print(p1.x,p1.y,p1.z)

#
# import json
#
# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': 1,
#     'hobbies': ('running', 'siniging'),
#     'children': [
#         {
#             'first_name' : 'Alis',
#             'age': 6
#         }
#     ]
#
# }
#
# # with open("data_file.json", "w") as fw:
# #     json.dump(data, fw)
#
# with open("data_file.json", "r") as fw:
#     data1 = json.load(fw)
#     print(data1)
#     d = json.dumps(data, sort_keys=True)
#     print(d)
#     d2 = json.loads(d)
#     print(d2)
#     print(type(d2))


# x = {
#     "name": 'Виктор'
# }
#
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))

# from random import choice
# def gen_person():
#     name = ''
#     tel = ''
#     letters = ['a','b','c','d','e','f','g','h']
#     nums = ['1','2','3','4','5','6','7','8','9','0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     # print(nums)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
#
# def wtite_json(person_dict):
#     try:
#         data = json.load(open('persons_json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open("persons_json", 'w') as fr:
#         json.dump(data, fr, indent=2)
#
# for i in range(5):
#     wtite_json(gen_person())


# class Studend:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __str__(self):
#         # a = ", ".join(map(str, self.marks))
#         # a = ""
#         # for i in self.marks:
#         #     a += str(i) + ", "
#         # return f"Студунт : {self.name}: {a[:-2]}"
#         # return f"Студунт : {self.name}: {a}"
#         return  f"Студен: {self.name}: {', '.join(map(str, self.marks))}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delite_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks),2)
#
# class Group:
#     def __init__(self, students, gr):
#         self.group = gr
#         self.students = students
#
#     def __str__(self):
#         a = ""
#         for i in self.students:
#             a += str(i) + "\n"
#         return f"Группа {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_to_json(self, file_name):
#         data = {"name": self.students, "marks": "self.mark"}
#         with open(file_name, 'w') as f:
#             json.dump(file_name, f)
#
#     def load_from_json(self, file_name):
#         with open(file_name, 'r') as f:
#             json.load(f)
#
#     def dump_group(self, file_name):
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f, indent=5,)
#
#     def upload_group(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
#
# st1 = Studend("Bodnya", 5,4,3,4,5,3)
# st2 = Studend("Nikolaenko", 2,3,5,4,2)
# st3 = Studend("Brukov", 3,5,3,2,5,4)
#
# sts = [st1,st2]
# my_group = Group(sts, "Гк Python")
# my_group.add_student(st3)
# my_group.remove_student(1)
# # print(my_group)
#
# gruop22 = [st2]
# my_group2 = Group(gruop22, "Гк Web")
# # print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
#
# # st1.add_mark(4)
# # print(st1)
# # st1.delite_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # print(st1)
# # print(st1.aerage_mark())
# file2 = "group1.json"
# my_group.dump_to_json(file2)
# my_group.load_from_json(file2)
# file = "group2.json"
# my_group2.dump_group(file)
# my_group2.upload_group(file)
# c ={
#     "5": 7,
#     "6": 8
# }
# a = {
#     "1": 1,
#     "2": 2
#      }
# b = {
#     "3": 1,
#     "4": 2
#      }
# r = [a,b,c]
# s = ['1','2','3']
# y = {}
# y["key"] = a
# y["key1"] = b
# for i in y.keys():
#     print(i)


# print(y)
#
# from random import choice
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a','b','c','d','e','f','g','h']
#     nums = ['1','2','3','4','5','6','7','8','9','0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
#
# def wtite_json(person_dict, count):
#
#     try:
#         data = json.load(open('persons_json'))
#         pers = json.load(open('persons_json'))
#
#     except FileNotFoundError:
#         data = {}
#
#     data.update({(str(count+1) +'_'+ str(len(data)+1)) + str(len(data)):person_dict})
#
#
#     with open("persons_json", 'w') as fr:
#         json.dump(data, fr, indent=2)
#
# for i in range(7):
#     wtite_json(gen_person(),i)

#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todes = json.loads(response.text)
#
# todos_by_user = {}
#
# for todo in todes:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complate = top_users[0][1]
# print(max_complate)
#
# users = []
# for user, num_compale in top_users:
#     if num_compale < max_complate:
#         break
#     users.append(str(user))
# print(users)
#
#
# max_users = " and ".join(users)
# print(max_users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complate} TODOs")
#
#
# def keep(td):
#     is_comp = td["completed"]
#     has_max_count = str(td["userId"]) in users
#     return is_comp and has_max_count
#
# with open("filter_max_comp.json", "w") as f:
#     filter_todos = list(filter(keep, todes))
#     json.dump(filter_todos, f, indent=2)


# CSV (Comma Separated Values)

# import requests
# import json
# import csv
#
# with open("data.csv",encoding="UTF8") as r_file:
#     filds = ['Имя','Профессия','Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         print(row)
#         if count == 0:
#             print(f"Фаил содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row['Имя'] - row['Профессия']}.Родился в {row['Год рождения']} году.")
#         count += 1
#
#     print(f"Всего в файде {count} строки.")


# with open("student.scv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя","Класс","Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:
#     wrter = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     wrter.writerow(row)
#     wrter.writerows(data)
#
# with open("sw_data.csv") as f:
#     print(f.read())

# import requests
# import json
# import csv

# with open("student1.csv","w") as f:
#     names = ['Имя','Возраст',]
#     file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Женя","Возраст": "22"})
#     file_writer.writerow({"Имя": "Лиля", "Возраст": "12"})
#     file_writer.writerow({"Имя": "Коля", "Возраст": "52"})

# data =[
#     {"1": "2",
#     "2": "3",
#     "3": "4",
#      },
#     {"1": "2",
#      "2": "3",
#      "3": "4",
#      },
#     {"1": "2",
#      "2": "3",
#      "3": "4",
#      }
# ]
#
#
# with open('dict.csv' , 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r",fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# # print(response.text)
#
# todos = json.loads(response.text)
# # for i in todos:
# #     print(i)
#
# with open('ff.csv', 'w') as f:
#     writer = csv.DictWriter(f, todos[0].keys(), delimiter=';', lineterminator='\r', )
#     writer.writeheader()
#     for i in todos:
#         writer.writerow(i)



# import requests
# import csv
# import json
# import os
# from tkinter import *
#
# def filtr(a):
#     if int(a) == 0:
#         return True
#
#
# class Albom:
#     def __init__(self,ur, func, file):
#         self.ur = ur
#         self.func = func
#         self.file = file
#
#
#     def convert_to_object(self):
#         response = requests.get(self.ur)
#         tod = json.loads(response.text)
#         return tod
#
#
#     def convert_to_csv(self):
#         tod = a.convert_to_object()
#         with open(self.file, "w") as f:
#             writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=list(tod[0].keys()))
#             writer.writeheader()
#             for i in  tod:
#                 if self.func(i["albumId"]) == True:
#                     writer.writerow(i)
#
#
#     def print_info(self):
#         tod = a.convert_to_object()
#         count = 0
#         for i in tod:
#             if self.func(i["albumId"]) == True:
#                 count += 1
#                 for h , j in i.items():
#                     print(f"{h} = {j}")
#                 print(f"Совпадений: {count}")
#                 print()
#
#     def ue(self):
#         tod = a.convert_to_object()
#         p = []
#         for i in tod:
#             for g, h in i.items():
#                 p.append((str(g),str(h)))
#         return p
#
#     def del_file(self):
#         os.remove(self.file)
#
#
# a = Albom("https://jsonplaceholder.typicode.com/photos", filtr, "convert.csv")
# a.convert_to_object()
# a.convert_to_csv()
# a.print_info()
# a.del_file()


#
# root = Tk()
# root.title("json convert to csv")
# root.geometry("500x500")
# fr = []
# for i in a.ue():
#     fr.append(str(i[0]))
# for i in range(30):
#     fr[i] = Label(text=fr"{fr[i]} = {a.ue()[i][1]}")
#     fr[i].pack()
#
# root.mainloop()



# Парсинг
# from bs4 import BeautifulSoup
#
# f = open("index.html",encoding="utf8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find("div", id = "whois").text
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id = "whois3").find_next_sibling()
# row = soup.find("div", id = "whois3").find_previous_sibling()



# from bs4 import BeautifulSoup

# def get_copyriter(teg):
#     whois = teg.find("div", class_="whois").text
#     if "Copywriter" in whois:
#         return teg
#     return None
#
# f = open("index.html",encoding="utf8").read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copyriter(i)
#     if cw:
#         copywriter.append(cw)
#
#
# print(copywriter)

# from bs4 import BeautifulSoup
# import re

# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern,s)[0]
#     res = re.search(pattern, s).group()
#     return res
#
# f = open("index.html",encoding="utf8").read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
#
# for i in salary:
#     print(get_salary(i.text))



# from bs4 import BeautifulSoup
# import re
#
# r = requests.get("https://ru.wordpress.org/")
# print(r.status_code)
# # print(r.headers)
# print(r.headers['Content-Type'])
# print(r.content)
# print(r.text)

# import requests
# from bs4 import BeautifulSoup
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
# if __name__ == '__main__':
#     main()

# import re
# import requests
# from bs4 import BeautifulSoup
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open("plugin.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     s = soup.find(id="main").find_all("section", class_="plugin-section")[-1]
#     plugins = s.find_all("article", class_="plugin-card")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#
#
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
# if __name__ == '__main__':
#     main()

#
# import requests
# import re
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def name_id(s):
#     math = re.search(r"\d+", s)
#     return math[0]
#
#
# def server_id(s_id):
#     adr = "https://wargm.ru/user" +"/" + str(s_id)
#     r = requests.get(adr)
#     soup = BeautifulSoup(r.text, "lxml").find(id="content").find(class_="row")
#     name = soup.find(class_="of-h").find(class_="trim").text
#     id = soup.find(class_="of-h").find(class_="f-r ml-5").text
#     steamId = soup.find(class_="of-h").find(target="_blank").text
#     return name , id , steamId
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     s = soup.find(id="main").find_all(class_="row")[2]
#     s1 = s.find_all(class_="cl-12 cl-s-3")[3]
#     s2 = s1.find_all(class_="card-body pt-5 pb-5")
#
#     with open("user_steam.csv", "w") as f:
#         writer = csv.writer(f,delimiter=";",lineterminator="\r")
#         writer.writerow(("User", "ID", "SteamID"))
#
#     for i in s2:
#         name = i.find(class_="trim")
#         User_info = server_id(name_id(str(name)))
#         with open("user_steam.csv", "a") as f:
#             writer = csv.writer(f, delimiter=";", lineterminator="\r")
#             writer.writerow((User_info[0], User_info[1], User_info[2]))
#
#
# def main():
#     url = "https://wargm.ru/server/66235/votes"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refind_cy(s):
#     return s.split()
#
# def wtite_csv(data):
#     with open("plugin1.csv", "a", encoding="utf-8-sig") as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=":")
#         writer.writerow((data['name'],data['snippet'], data['active'],data['test_cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("article", class_="plugin-card")
#     for el in p1:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ''
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except ValueError:
#             snippet = ''
#
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#
#         try:
#             test = el.find("span", class_="tested-with").text.strip()
#             test_cy = refind_cy(test)[2]
#         except AttributeError:
#             test = ""
#
#         data = {
#             'name': name,
#             'snippet': snippet,
#             'active': active,
#             'test_cy': test_cy
#         }
#
#         wtite_csv(data)
#
# def main():
#     for i in range(26,50):
#         url = f"https://ru.wordpress.org/plugins/browse/popular/page/{i}"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
#

# from parsers import Parser
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
# if __name__ == '__main__':
#     main()


# MVC
# model
# view
# controller


# from tkinter import*
#
# root = Tk()
# root['bg'] = 'black'
# root.geometry('500x1000')
#
# convas = Canvas(root)
# convas['bg'] = 'grey'
# convas.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.95)
#
# frame = Frame(root, bg = 'red')
# frame.place(relx=0.1, rely=0.05, relwidth=0.80,relheight=0.2)
#
#
# title = Label(frame, text='11111', bg='red', font=40)
# title.pack()
# bth = Button(frame, text='Knopka', bg='grey')
# bth.pack()

# root.mainloop()

# Сокет
#
# import socket
# from view import index, blog
#
# URLS={
#     '/':index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Mthod Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 405 Mthod Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK',200
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     if code == 405:
#         return '<h1>405</h1><h3>Page Not Allowed!</h3>'
#     return URLS[url]()
#
# def generate_response(request):
#     method, url = parse_request(request)
#     heders, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (heders + body).encode()
#
#
# def run():
#     server_socet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socet.bind(('127.0.0.1', 5000))
#     server_socet.listen()
#
#     while True:
#         clien_socet, addr = server_socet.accept()
#         request = clien_socet.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         clien_socet.sendall(response)
#         clien_socet.close()
#
#
#
# if __name__ == "__main__":
#     run()


# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
# cur.execute("""
# """)
#
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()

    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # summa REAL,
    # date TEXT)
    # """)
    # cur.execute("DROP TABLE users")






# class DispleyTk:


    # def lable1_to_win(self):
    #     label1 = tk.Label(text="Путь к файлу", bg="#504739", fg="white", font=("arial", 15, "bold"),
    #                     padx=20, bd=3)
    #     label1.place(rely=0.1, relx=0.1)
    #
    # def buton_convert_to_json(self):
    #     buton = tk.Button(text="Convert", bg="black", fg="white",
    #                     font=("arial", 15, "bold"), relief=tk.RAISED, padx=20, bd=3,
    #                     command=self.get_entri_values,activebackground="red")
    #     buton.place(rely=0.6, relx=0.6)
    #
    # def get_entri_values(self):
    #     r = entri1.get()

# t = DispleyTk()




# import tkinter as tk
# import json
# import os

# class Decoder:
#     def __init__(self, adres, data_key, key1, key2):
#         self.adres = adres
#         self.data_key = data_key
#         self.key1 = int(key1)-1
#         self.key2 = int(key2)-1
#
#     def csv_convert_to_json(self):
#         s = []
#         r = {}
#         with open(self.adres, "r") as f:
#             for i in f:
#                 t = i.split(";")
#                 s.append({t[self.key1]:t[self.key2]})
#         print(s)
#         r[self.data_key] = s
#         with open("text_json.json", "w") as f:
#             try:
#                 tt = f.write(json.dumps(r, indent=2))
#             except FileNotFoundError:
#                 print("1111")
#
#     def get_adres_file(self):
#         return os.path.abspath("text_json.json")
#
#
# def get_entri_values():
#     values = vol.get()
#     key1 = key1_one.get()
#     key2 = key2_one.get()
#     d = Decoder(values,1,key1,key2)
#     label3 = tk.Label(text=d.get_adres_file(),bg="#504739", fg="white").pack()
#     d.csv_convert_to_json()
#


# import sqlite3
#
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()

    # cur.execute("""
    # DROP TABLE person_table
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN andress
    #
    # """)


    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN andress TEXT
    #
    # """)

    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB DEFAULT +79024416084,
    # age INTEGER CHECK(age > 0 AND age <100),
    # email TEXT UNIQUE
    # )""")
#
# import sqlite3
# cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB DEFAULT +79024416084,
#     age INTEGER CHECK(age > 0 AND age <100),
#     email TEXT UNIQUE
#     )""")


# import sqlite3
#
# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS student(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT NOT NULL,
#     name TEXT NOT NULL,
#     patronymic TEXT,
#     age INTEGER NOT NULL CHECK (age >= 16 AND age <= 45),
#     group TEXTNOT NULL,
#     FOREIGN KEY (group) REFERENCES groups (id) ON DELETE RESTRICT
#     )
#     """)
#     cur.execute("""CREATE TABLE IF NOT EXISTS groups(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     group_name TEXT NOT NULL
#     )
#     """)
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS association(
#       lesson_id INTEGER NOT NULL,
#       group_id INTEGER NOT NULL,
#       FOREIGN KEY (group_id) REFERENCES  lessons(id)
#       FOREIGN KEY (lesson_id) REFERENCES groups (id)
#       )
#       """)
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS lessons(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     lesson_title TEXT NOT NULL
#     )
#     """)

#
#
# import sqlite3
#
# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS car(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT,tr-in INTEGER,buy INTEGER
#     )
#     """)
#     cur.execute("INSERT INTO car VALUES(NULL,'запорожец','1000')")
#     last_row_id = cur.lastrowid
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья',?,?)",(last_row_id, buy_car_id))


# import sqlite3

# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)


# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


# a = {'/user/25929': {'NikName': 'SADAM0N', 'Steam_id': '76561198047567526', 'Дата регистрации': '12 янв. 2021'}, '/user/43442': {'NikName': 'Andrayd', 'Steam_id': '76561198029501508', 'Дата регистрации': '21 июн. 2021'}, '/user/97016': {'NikName': 'MarIvana', 'Steam_id': '76561198033870666', 'Дата регистрации': '3 июл. 2022'}, '/user/185373': {'NikName': 'Grenka Vyborgsky', 'Steam_id': '76561198170197811', 'Дата регистрации': '29 авг.'}, '/user/52785': {'NikName': 'ЭЛАЙВ', 'Steam_id': '76561198247587154', 'Дата регистрации': '13 сен. 2021'}, '/user/158970': {'NikName': 'CRYSIS', 'Steam_id': '76561199484662981', 'Дата регистрации': '24 апр.'}, '/user/39267': {'NikName': 'Susler', 'Steam_id': '76561198008237517', 'Дата регистрации': '14 май 2021'}, '/user/147773': {'NikName': 'NeroN', 'Steam_id': '76561198338172770', 'Дата регистрации': '13 мар.'}, '/user/11624': {'NikName': 'uz_on', 'Steam_id': '76561198063388458', 'Дата регистрации': '17 май 2020'}, '/user/21741': {'NikName': 'konoval011', 'Steam_id': '76561198448594611', 'Дата регистрации': '23 ноя. 2020'}, '/user/104966': {'NikName': 'Obnimaxa', 'Steam_id': '76561198175407053', 'Дата регистрации': '26 авг. 2022'}, '/user/27736': {'NikName': 'CAHU4_OXOTHUK', 'Steam_id': '76561198283638264', 'Дата регистрации': '26 янв. 2021'}, '/user/40175': {'NikName': 'tishka6379', 'Steam_id': '76561198384498352', 'Дата регистрации': '24 май 2021'}, '/user/90979': {'NikName': 'Alexsungod', 'Steam_id': '76561198971303501', 'Дата регистрации': '27 май 2022'}, '/user/105237': {'NikName': 'cTpaxoLud', 'Steam_id': '76561198112169185', 'Дата регистрации': '28 авг. 2022'}, '/user/122603': {'NikName': 'andreyka_filipov_1978', 'Steam_id': '76561199109362051', 'Дата регистрации': '5 дек. 2022'}, '/user/194248': {'NikName': 'ricochet', 'Steam_id': '76561199052194935', 'Дата регистрации': '23 окт.'}, '/user/184696': {'NikName': 'kirykus', 'Steam_id': '76561199247978258', 'Дата регистрации': '26 авг.'}, '/user/34081': {'NikName': 'XapoH_116rus', 'Steam_id': '76561198203265681', 'Дата регистрации': '23 мар. 2021'}, '/user/137769': {'NikName': 'dyadya_SaSHa', 'Steam_id': '76561198313568375', 'Дата регистрации': '3 фев.'}, '/user/90052': {'NikName': 'TANKvanDO', 'Steam_id': '76561198874440209', 'Дата регистрации': '21 май 2022'}, '/user/14937': {'NikName': 'Halk', 'Steam_id': '76561198980735441', 'Дата регистрации': '24 июл. 2020'}, '/user/139894': {'NikName': 'aidis307', 'Steam_id': '76561199043071130', 'Дата регистрации': '10 фев.'}, '/user/7288': {'NikName': 'Zloy', 'Steam_id': '76561198850422932', 'Дата регистрации': '12 янв. 2020'}, '/user/106902': {'NikName': 'kosmach1985', 'Steam_id': '76561199005827731', 'Дата регистрации': '9 сен. 2022'}, '/user/198869': {'NikName': 'czapaevaleksei', 'Steam_id': '76561199570565468', 'Дата регистрации': '17 ноя.'}, '/user/185795': {'NikName': 'StellShevv', 'Steam_id': '76561199382873502', 'Дата регистрации': '1 сен.'}, '/user/120316': {'NikName': '[R-ZONE]', 'Steam_id': '76561198073821942', 'Дата регистрации': '24 ноя. 2022'}, '/user/93001': {'NikName': 'Носок судьбы', 'Steam_id': '76561198414644339', 'Дата регистрации': '9 июн. 2022'}, '/user/56313': {'NikName': 'Troy', 'Steam_id': '76561198862033380', 'Дата регистрации': '16 окт. 2021'}, '/user/126402': {'NikName': 'XxX[ozery]', 'Steam_id': '76561198118213793', 'Дата регистрации': '26 дек. 2022'}, '/user/29499': {'NikName': 'San_Sanych', 'Steam_id': '76561198166354648', 'Дата регистрации': '11 фев. 2021'}, '/user/186042': {'NikName': 'Liar', 'Steam_id': '76561198076237865', 'Дата регистрации': '2 сен.'}, '/user/101751': {'NikName': 'melkeeej', 'Steam_id': '76561197967210721', 'Дата регистрации': '3 авг. 2022'}, '/user/132247': {'NikName': 'koreec525', 'Steam_id': '76561198138064717', 'Дата регистрации': '17 янв.'}, '/user/61994': {'NikName': 'Rokki_Black', 'Steam_id': '76561199163810113', 'Дата регистрации': '30 ноя. 2021'}, '/user/115036': {'NikName': 'Still_aLive', 'Steam_id': '76561198081366198', 'Дата регистрации': '26 окт. 2022'}, '/user/75331': {'NikName': 'igoryok_simba', 'Steam_id': '76561198044148733', 'Дата регистрации': '19 фев. 2022'}, '/user/123836': {'NikName': 'Baton', 'Steam_id': '76561198932628170', 'Дата регистрации': '11 дек. 2022'}}
# count1 = 0
# for key in a.keys():
#     count1 += 1
#     co = []
#     for i in a[key].keys():
#         co.append(a[key][i])
#     print(count1,"=",co)




# name = "Игорь"
# age = 28

# per = {'name': 'Igor', 'age': 28}
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}") # или {{ n | upper() }}
# msg = tm.render(p=per)
#
# print(msg)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
# per = Person("Igor",28)
#
# tm = Template(f"Мне {{ p['age'] }} лет. Меня зовут {{ p.get_name() }}") # или {{ n | upper() }}
# msg = tm.render(p=per)
#
# print(msg)


#
# cities = [
#     {'id': '/index', 'city': 'Главная'},
#     {'id':'/new', 'city': 'Новасти'},
#     {'id': '/about', 'city': 'О компании'},
#     {'id': '/shop', 'city': 'Магазин'},
#     {'id': '/contacts', 'city': 'Контакты'}
# ]
# link = """
# <ul>
# {% for c in cities %}
# <li href="{{ c.id }}" class="active">{{ c.city }}</li>
# {% endfor %}
# </ul>
# """


# from jinja2 import Template
#
#
# cars = [
# 	{'model': 'Audi', 'price': 23000},
# 	{'model': 'Skoda', 'price': 17300},
# 	{'model': 'Renault', 'price': 44300},
# 	{'model': 'Wolksvagen', 'price': 21300}
# ]
#
# tpl = "{{ cs | replace('model', 'brend') }}"
#
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)


# Макроопредеиения

# from jinja2 import Template
#
#
# html = """
# {% macro set_input(name, values='',type='text',size=20) %}
# <input type="{{ type }}" name="{{ name }}" values="{{values}}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ set_input('username') }}</p>
# <p>{{ set_input('email') }}</p>
# <p>{{ set_input('password') }}</p>
#
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# from jinja2 import Template
#
# persons = [
# 	{"name": "Алексей", "year": 18, "weight": 78.5},
# 	{"name": "Никита", "year": 28, "weight": 82.3},
# 	{"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# html = """
# {%  macro list_users(list_of_user) %}
# <ul>
# {% for u in list_of_user %}
#     <li>{{ u.name }}</li>
# {% endfor %}
# </ul>
# {% endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#     <li>age: {{ user.year }}</li>
#     <li>weigth: {{ user.weigth}}</li>
#     </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)


# from jinja2 import Template
#
# persons = [
# 	{"name": "firstname", "placeholder": "Имя", "type": "text"},
# 	{"name": "lastname", "placeholder": "Фамилия", "type": "text"},
# 	{"name": "address", "placeholder": "Адрес", "type": "text"},
#     {"name": "phone", "placeholder": "Телефон", "type": "tel"},
#     {"name": "email", "placeholder": "Почта", "type": "email"}
# ]
#
# html = """
# {% macro stroka(line) %}
# type="{{ line.type }}" name="{{ line.name }}" placeholder="{{ line.placeholder }}"
# {% endmacro %}
#
# {% for i in users %}
# <p><input {{ stroka(i) }}></p>
# {% endfor %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# with open("index.html" , "w") as f:
# 	for i in msg:
# 		f.write(i)
# print(msg)
