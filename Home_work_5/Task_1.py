def recurs_pow(a,b):
    if b == 0:
        return 1
    if b<0:
        return recurs_pow(a , b+1)*1/a
    return recurs_pow(a,b - 1)*a
list = ['\u2070','\u00B9','\u00B2','\u00B3','\u2074','\u2076','\u2077','\u2078','\u2079','\u207B']
print()
a = int(input("Введите число а \n"))
b = int(input("Введите степень b \n"))
if b>0:
    print(f"{a}{list[9]} = {recurs_pow(a,b)}")
else:
    print(f"{a}{list[9]}{list[abs(b)]} = {recurs_pow(a,b)}")

# print('a = 2\u00B2')