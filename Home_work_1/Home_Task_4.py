""" 4. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,  in       out     in       out 
если разрешается сделать один разлом по прямой между дольками                              3 2 4    yes     3 2 1    no
то есть разломить шоколадку на два прямоугольника). """
sizeOfChocM = int(
    input("Какого размера шоколадку вы купили?\nВведите размера в плитках MxN\n")
)
sizeOfChocN = int(
    input()
)
sizeOfPiece = int(
    input("Сколько плиток вы хотите отломить за раз?\n")
)
if ((sizeOfPiece % sizeOfChocN == 0)
    or
    (sizeOfPiece % sizeOfChocM == 0)):
    print("yes")
else:
    print("No")
