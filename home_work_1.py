# Task_1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно 
# входит в нужный диапазон

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number


# def checkNumber(num):
#     if 6 <= num <= 7:
#         print("Yes")
#     elif 0 < num < 6:
#         print("No")
#     else:
#         print("число вне пределов 7 дней")


# num = InputNumbers("Введите число: ")
# checkNumber(num)

# Task_2- Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

# Task_3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def inputKoord(x):
#     a = [0] * x
#     for i in range(x):
#         is_OK = False
#         while not is_OK:
#             try:
#                 number = float(input(f"Введите {i+1} координату: "))
#                 a[i] = number
#                 is_OK = True
#                 if a[i] == 0:
#                     is_OK = False
#                     print("Координата не должно быть равна 0 ")
#             except ValueError:
#                 print("Ты ошибся. Вводить надо числа!")
#     return a


# def checkCoordinates(xy):
#     text = 4
#     if xy[0] > 0 and xy[1] > 0:
#         text = 1
#     elif xy[0] < 0 and xy[1] > 0:
#         text = 2
#     elif xy[0] < 0 and xy[1] < 0:
#         text = 3
#     print(f"Точка находится в {text} четверти плоскости")


# koordinate = inputKoord(2)
# checkCoordinates(koordinate)

# Task_4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

# numb_quarter = int(input('Введите номер четверти : '))
# if numb_quarter not in range(1,5):
#     print('You wrong')
# elif numb_quarter == 1:
#     print('x∈(0, ∞) U y∈(0,∞)')
# elif numb_quarter == 2:
#     print('x∈(-∞, 0) U y∈(0,∞)')
# elif numb_quarter == 3:
#     print('x∈(-∞, 0) U y∈(-∞, 0)')
# else:
#     print('x∈(0, ∞) U y∈(-∞, 0)')

    
# Task_5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

# def inputNumbers(x):
#     xy = ["X", "Y"]
#     a = []
#     for i in range(x):
#         is_OK = False
#         while not is_OK:
#             try:
#                 number = int(input(f"Введите координату по {xy[i]}: "))
#                 a.append(number)
#                 is_OK = True
#             except ValueError:
#                 print("Ты ошибся. Вводить надо целые числа!")
#     return a


# def calculateLengthSegment(a, b):
#     lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
#     return lengthSegment


# print("Введите координаты точки А")
# pointA = inputNumbers(2)
# print("Введите координаты точки В")
# pointB = inputNumbers(2)

# print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")