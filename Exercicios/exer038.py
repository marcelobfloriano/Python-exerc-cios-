num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite outro numero inteiro:"))
if num1 > num2:
    print('O primeiro numero {} é maior que o segundo {}'.format(num1, num2))
elif num2 > num1:
    print('O segundo numero {} é maior que o primeiro {}'.format(num2, num1))
else:
    print("Os dois numeros sao iguai")