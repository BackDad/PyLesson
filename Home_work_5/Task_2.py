def Summ(a,b):
    if b==0:
        return a
    return Summ(a+1,b-1)
a = int(input("Введите число а \n"))
b = int(input("Введите число b \n"))
print(Summ(a,b))