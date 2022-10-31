num = c = soma = 0
while num != 999:
    num = int(input("Digite um numero[999 para parar]:"))
    soma += num
    c += 1
print('Voce digitou {} numeros e a soma entre eles {}'.format(c - 1, soma - 999))