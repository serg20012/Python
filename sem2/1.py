# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120
# n = int(input("Введите число: "))
# result = 1
# i = 1
# while i <= n:
#     result *= i
#     i = i + 1
# print(result)

# a = int(input('введите a: '))
# f1 = 0
# f2 = 1
# fn = 0
# x = 0
# n = 3
# while fn <= a:
#     fn = f1 + f2
#     x = f2
#     f1 = x
#     f2 = fn
#     if fn == a:
#         print(n)
#         break
#     n += 1
# else:
#     print(-1)

# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в 
# свою очередь, занялись исследованиями статистики за 
# прошлые годы. Их интересует, сколько дней длилась самая 
# длинная оттепель. Оттепелью они называют период, в 
# который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе.
# Пользователь вводит число N – общее количество 
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках 
# располагается N целых чисел. 
# Каждое число – среднесуточная температура в 
# соответствующий день. Температуры – целые числа и лежат в 
# диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2