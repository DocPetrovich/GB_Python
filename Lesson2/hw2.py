# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# n = int(input("Введите количество монет: "))
# k = 0
#
# for i in range(n):
#     v = int(input("Введите 1 если она лежит вверх решкой , введите 0 если она лежит вверх гербом: "))
#     if(v>=0 and v<2):
#         if v == 1:
#             k += 1
#     else:
#         print("Вводите только 0 или 1")
#         break
# print("Количество монет которые нужно перевернуть :", k if k < n / 2 else n - k)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# a, b = map(int, input("Введите сумму чисел и их произведение: ").split())
# c = 0
# for i in range(a + b):
#     if c:
#         break
#     for j in range(a + b):
#         if i + j == a and i * j == b:
#             c = 1
#             print("Эти числа загадал Петя: ",*sorted([i, j]))
#             break

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k
# ), не превосходящие числа N.

# n=int(input("Введите число: "))
# p=1
# while p<=n:
#     print(p,end=' ')
#     p=p*2