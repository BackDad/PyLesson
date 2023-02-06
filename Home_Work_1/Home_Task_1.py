""" Урок 1. Ввод-Вывод, операторы ветвления  in  out    in    out
Найдите сумму цифр трехзначного числа.       123  6     100   1
"""
NUmber = int(input("Введите число для нахождения суммы цифр\n"))
Summ = 0
while (NUmber >= 1):
    Summ += NUmber % 10
    NUmber //= 10
print(Summ)
