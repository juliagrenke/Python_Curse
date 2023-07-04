#Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)


# n = int(input("Введите число: "))
# print(fib(n))

# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


from random import randint as rd

k = int(input("Введите количество оценок: "))

estimates = []
for i in range(k):
    estimates.append(rd(1, 5))
print(estimates)
x1 = max(estimates)
x2 = min(estimates)
print(x1, x2)
for i in range (k):
    if estimates[i]==x1:
        estimates[i]=x2

print(estimates)


# Задача №35. 
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

n = int(input("Введите число: "))
f = 1
for i in range(2, n // 2 + 1):
    if n % i == 0:
        f = 0

if f == 0:
    print("NO")
else:
    print("YES")


# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def reverse_numbers(n):
    if n == 0:
        return ""
    chislo = input()
    return reverse_numbers(n - 1) + f" {chislo}"


n - int(input("Введите число: "))
print(reverse_numbers(n))




