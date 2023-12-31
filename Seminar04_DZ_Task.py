# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите кол-во элементов 1-го множества: "))
nabor_1 = list()
for i in range(n):
    nabor_1.append(int(input()))
print(nabor_1)

m = int(input("Введите кол-во элементов 2-го множества: "))
nabor_2 = list()
for i in range(m):
    nabor_2.append(int(input()))
print(nabor_2)

# nabor_1_set = set(nabor_1)
# nabor_2_set = set(nabor_2)

# result = set(nabor_1).intersection (set(nabor_2))
result = sorted(set(nabor_1).intersection (set(nabor_2)))
print(result)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


from random import randint as rd

n = int(input("Введите кол-во кустов N: "))
harvest = list()
for i in range(n):
    harvest.append(rd(1, 100))
print(harvest)

max_harvest = harvest[0]

for i in range(n):
    x = harvest[i] + harvest[i + 1 - n] + harvest[i + 2 - n]
    print(x)
    if x < max_harvest:
        i += 1
    else:
        max_harvest = x
print(f"Максимальный урожай = {max_harvest}")
