total = soma = 0
while True:
    num = int(input('Digite um numero[999 para parar]: '))
    if num == 999:
        break
    total += 1
    soma += num
if total > 1:
    print(f'A soma de {total} numeros foi {soma}')
elif total <=1:
    print(f'A soma de {total} numero é {soma}')
