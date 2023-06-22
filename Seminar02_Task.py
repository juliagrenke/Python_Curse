# Задача 9
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input:       5
# Output:    120

# n = int(input("Введите число: "))
# i = 2
# result = 1
# while i <= n:
#     result = result * i
#     i += 1
# print(f'Факториал {n} = {result}')

# Задача 11
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input:     5
# Output:  6

# fibn = int(input("Введите число: "))
# fib0 = 0
# fib1 = 0
# fib2 = 1
# i = 2
# while fib0 < fibn:
#     print (fib0, end=' ')
#     fib0 = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib0
#     i +=1
#     if fib0 > fibn:
#         i = 0
# print()
# if i != 0:
#     print(i-1)
# else:
#     print(-1)

# Задача 15
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

# n = int(input("Введите количество арбузов: "))
# x = int(input("Введите массу арбуза: "))
# min_massa, max_massa = x, x
# for i in range (n-1):
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     elif min_massa > x:
#         min_massa = x
# print(min_massa, max_massa)


# Задача 13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная 
# температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

n = int(input("Введите количество дней (от 1 до 100): "))
count = 0
max_count = 0
for i in range (n):
    temp = int(input("Введите температуру (от -50 до 50): "))
    if temp > 0:
        count +=1
    else:
        count = 0

    if count > max_count:
        max_count = count
            

print(max_count)