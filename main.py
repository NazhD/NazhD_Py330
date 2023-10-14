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
import os.path
import re

# a = b = c = 1
# print(a, b, c)

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

class Car:


    def __init__(self, style, year_manu,manufacturer, eng_power, color, price):
        self.style = style
        self.year_manu = year_manu
        self.manufacturer = manufacturer
        self.eng_power = eng_power
        self.color = color
        self.price = price


    def set_year(self, year_manu):
        self.year_manu = year_manu


    def set_color(self,color):
        self.color = color

    def set_price(self,price):
        self.price = price

    def get_year(self):
        return self.year_manu

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


    def print_info(self):
        print("Данные автомобиля".center(40,"*"))
        print(f"Название модели: {self.style}\nГод выпуска: {self.year_manu}\n"
              f"Производитель: {self.manufacturer}\nМощность двиготеля: {self.eng_power} л.с.\n"
              f"Цвет машины: {self.color}\nЦена: {self.price} у.е")
        print("=" * 40)



car = Car("X7 M50I"," ","BMW","530"," "," ")
car.set_color("Red")
car.set_year("2023")
car.set_price("5 000 000 000")
car.print_info()
print(car.get_year())
print(car.get_color())
print(car.get_price())