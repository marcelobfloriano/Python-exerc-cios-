print('Calculo de FATORIAL')
numero = int(input("Escolha o numero : "))
c = 1
fatorial = numero + 1
resultado = 1
print('Calculando {}! = '.format(numero), end='')
while fatorial > c:
    fatorial = fatorial - c
    resultado = resultado * fatorial
    print('{}'.format(fatorial), end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
print(' {} '.format(resultado))