First_element = int(input("Введиет 1-й элемент последовательности \n"))
d = int(input("Введите число d\n"))
n = int(input("Введите номер n последовательности \n"))
for i in range(n):
    print(First_element + i * d)
