# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#  m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

print(sorted(
            set([int(input(f"Введите {i}-й элемент первого множества \n"))
            for i in range(int(input("Введите количество элементов 1 множества \n")))]) 
            & 
            set([int(input(f"Введите {i}-й элемент второго множества \n"))
            for i in range(int(input("Введите количество элементов 2 множества \n")))])))

