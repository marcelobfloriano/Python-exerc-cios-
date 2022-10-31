lado1 = float(input("Digite o tamanho do primeiro lado:"))
lado2 = float(input("Digite o tamanho do segundo lado:"))
lado3 = float(input("Digite o tamanho do terceiro lado:"))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Pode formar triangulo com esses segmentos!!!")
    if lado1 == lado2 and lado2 == lado3:
        print("Esse é um triangulo EQUILATERO")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Esse é um triangulo ISOCELES")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Esse é um triangulo ESCALENO")
else:
    print('Nao pode se formar um triangulo com esses segmentos')

