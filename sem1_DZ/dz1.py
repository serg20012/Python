# Задача 2: Найдите сумму цифр трехзначного числа. программа считает сумму любого числа
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# программа считает сумму любого числа
# n = int(input("Введите трехзначное число: "))
# temp = n
# sum = 0
# while (temp > 0) :
#     digit = temp % 10
#     sum = digit + sum
#     temp = temp // 10
# print (sum)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S
# журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и
# Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
# журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# n = int(input("Введите кол-во журавликов: "))
# pyty = n/6
# if pyty %1 != 0 :
#     print ('неверный ввод')
# else : print(pyty, pyty, (pyty+pyty)*2)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# или любое четное
# n = int(input("Введите номер билета 6 знаков: "))
# temp = n
# len = 0
# # в цикле определяем число знаков в номере билета
# while temp > 0:
#     temp = temp // 10
#     len = len + 1
# if len % 2 > 0:
#     print("нечетное сило знаков")

# temp = n
# sum1 = 0
# sum2 = 0
# for i in range(1, len+1, 1):
#     if i <= len/2:
#         digit = temp % 10
#         temp = temp // 10
#         sum1 = sum1 + digit
#     else:
#         digit = temp % 10
#         temp = temp // 10
#         sum2 = sum2 + digit
# print(sum1, sum2)

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
x = int(input("Введите кол-во долек по х: "))
y = int(input("Введите кол-во долек по y: "))
delitel = int(
    input("Введите сколько долек отломить: "))
if delitel % x == 0 or delitel % y == 0:
    print("можно")
else:
    print('нет')
